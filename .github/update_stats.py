#!/usr/bin/env python3
"""Compute aggregate GitHub stats for the limxdynamics/limxdynamics profile README.

Two outputs:

1. Badges (existing behaviour, kept as-is):
   * badges/stars.json  -- total stars  across every repo linked in README.md
   * badges/forks.json  -- total forks  across every repo linked in README.md

2. Total-star growth chart (new):
   * data/stars_history.json -- daily cumulative total-star series
   * stars.svg               -- xkcd-style hand-drawn chart embedded by README.md

Repos are discovered dynamically by scanning README.md for ``github.com/owner/repo``
links, so the chart always stays in sync with what the README actually lists.

History: with GITHUB_TOKEN we read each repo's stargazers (Accept: star+json) to
recover every star's ``starred_at`` timestamp and rebuild the true curve. If the
stargazers endpoint fails for a repo (rate-limit, etc.), that repo falls back to
anchoring its current star count on today so the curve's end value still matches
the badge total.
"""

import json
import os
import re
import sys
import urllib.request
import urllib.error
from collections import defaultdict
from datetime import datetime, timezone

TOKEN = os.environ.get("GITHUB_TOKEN", "")


def api(url, accept=None):
    headers = {"User-Agent": "limx-gh-stats"}
    headers["Accept"] = accept or "application/vnd.github+json"
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect_repos(text):
    """Return the ordered unique list of ``owner/repo`` linked in README text."""
    seen = {}
    for m in re.finditer(r"github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)", text):
        seen.setdefault("%s/%s" % (m.group(1), m.group(2)), True)
    return list(seen.keys())


def fetch_stargazers(full):
    """Return the list of starred_at strings (one per current stargazer)."""
    out = []
    page = 1
    while True:
        data = api(
            "https://api.github.com/repos/%s/stargazers?per_page=100&page=%d" % (full, page),
            accept="application/vnd.github.star+json",
        )
        if not data:
            break
        for s in data:
            out.append(s.get("starred_at"))
        if len(data) < 100:
            break
        page += 1
    return out


def badge(label, value, color):
    return {
        "schemaVersion": 1,
        "label": label,
        "message": str(value),
        "color": color,
        "style": "flat",
        "namedLogo": "github",
    }


# --------------------------------------------------------------------------
# SVG rendering (hand-rolled, zero dependencies) -- star-history xkcd style
# --------------------------------------------------------------------------

LINE = "#dd4528"
AXIS = "#000000"
_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _load_font():
    try:
        with open("data/xkcd-font-b64.txt", encoding="utf-8") as f:
            return f.read().strip()
    except OSError:
        return ""


def _nice_step(raw):
    import math
    if raw < 1:
        return raw
    exp = math.floor(math.log10(raw))
    f = raw / (10 ** exp)
    nf = 1 if f < 1.5 else (2 if f < 3 else (5 if f < 7 else 10))
    return nf * (10 ** exp)


def _y_ticks(vmax, count=5):
    if vmax <= 0:
        return [0.0]
    step = _nice_step(vmax / count)
    out = []
    v = 0.0
    while v <= vmax + 1e-9:
        out.append(v)
        v += step
    return out


def _number_unit(n):
    if n >= 1000000:
        return 1000000
    if n >= 300:
        return 1000
    return 1


def _fmt_number(n, unit):
    n = int(round(n))
    if unit == 1:
        return str(n)
    if unit == 1000000:
        if n % 1000000 == 0:
            return "%dM" % (n // 1000000)
        return "%.1fM" % (n / 1000000.0)
    if n % 1000 == 0:
        return "%dK" % (n // 1000)
    return "%.1fK" % (n / 1000.0)


def _fmt_date(date_str):
    y, mo, d = date_str.split("-")
    return "%s %d, %s" % (_MONTHS[int(mo) - 1], int(d), y)


def _x_ticks(n, count=5):
    if n <= 1:
        return [0]
    if n <= count:
        return list(range(n))
    idxs = [round(k * (n - 1) / (count - 1)) for k in range(count)]
    out = []
    for i in idxs:
        if not out or i != out[-1]:
            out.append(i)
    return out


def monotone_path(pts):
    """Monotone cubic (Fritsch-Carlson) spline, matching D3 curveMonotoneX."""
    n = len(pts)
    if n < 2:
        return ""
    if n == 2:
        (x0, y0), (x1, y1) = pts
        return "M%.2f,%.2f L%.2f,%.2f" % (x0, y0, x1, y1)

    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    delta = []
    for i in range(n - 1):
        h = xs[i + 1] - xs[i]
        delta.append((ys[i + 1] - ys[i]) / h if h else 0.0)

    m = [0.0] * n
    m[0] = delta[0]
    m[n - 1] = delta[n - 2]
    for i in range(1, n - 1):
        m[i] = 0.0 if delta[i - 1] * delta[i] <= 0 else (delta[i - 1] + delta[i]) / 2.0

    for i in range(n - 1):
        if delta[i] == 0:
            m[i] = 0.0
            m[i + 1] = 0.0
        else:
            a = m[i] / delta[i]
            b = m[i + 1] / delta[i]
            s = a * a + b * b
            if s > 9:
                t = 3.0 / (s ** 0.5)
                m[i] = t * a * delta[i]
                m[i + 1] = t * b * delta[i]

    parts = ["M%.2f,%.2f" % (xs[0], ys[0])]
    for i in range(n - 1):
        h = xs[i + 1] - xs[i]
        c1x = xs[i] + h / 3.0
        c1y = ys[i] + m[i] * h / 3.0
        c2x = xs[i + 1] - h / 3.0
        c2y = ys[i + 1] - m[i + 1] * h / 3.0
        parts.append("C%.2f,%.2f %.2f,%.2f %.2f,%.2f" %
                     (c1x, c1y, c2x, c2y, xs[i + 1], ys[i + 1]))
    return " ".join(parts)


def render_svg(rows):
    if not rows:
        return "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 533'></svg>"

    W, H = 800, 533
    M_TOP, M_RIGHT, M_BOTTOM, M_LEFT = 50, 30, 50, 62
    plot_w = W - M_LEFT - M_RIGHT
    plot_h = H - M_TOP - M_BOTTOM

    dates = [r["date"] for r in rows]
    vals = [r["total_stars"] for r in rows]
    n = len(vals)
    vmax = max(vals)
    if vmax <= 0:
        vmax = 1

    def x(i):
        return M_LEFT + (plot_w * i / (n - 1) if n > 1 else 0.0)

    def y(v):
        return M_TOP + plot_h * (1 - v / vmax)

    font = _load_font()

    parts = []
    parts.append("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' "
                 "font-family='xkcd, Comic Sans MS, cursive' role='img'>" % (W, H))

    parts.append(
        "<defs><style>@font-face{font-family:\"xkcd\";"
        "src:url(data:application/font-woff;charset=utf-8;base64,%s)}"
        "</style></defs>" % font
    )

    parts.append(
        "<filter id='xkcdify' filterUnits='userSpaceOnUse' x='-5' y='-5' "
        "width='100%' height='100%'>"
        "<feTurbulence type='fractalNoise' baseFrequency='0.05' result='noise'/>"
        "<feDisplacementMap scale='5' xChannelSelector='R' yChannelSelector='G' "
        "in='SourceGraphic' in2='noise'/>"
        "</filter>"
    )

    baseline = M_TOP + plot_h

    yticks = _y_ticks(vmax, 5)
    yunit = _number_unit(next((v for v in yticks if v > 0), 1))
    parts.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='2' "
                 "filter='url(#xkcdify)'/>" % (M_LEFT, M_TOP, M_LEFT, baseline, AXIS))
    for v in yticks:
        yy = y(v)
        parts.append("<line x1='%d' y1='%.1f' x2='%d' y2='%.1f' stroke='%s'/>"
                     % (M_LEFT - 4, yy, M_LEFT, yy, AXIS))
        label = "" if v == 0 else _fmt_number(v, yunit)
        if label:
            parts.append("<text x='%d' y='%.1f' fill='%s' font-size='16' "
                         "text-anchor='end'>%s</text>" % (M_LEFT - 8, yy + 6, AXIS, label))

    parts.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='2' "
                 "filter='url(#xkcdify)'/>" % (M_LEFT, baseline, W - M_RIGHT, baseline, AXIS))
    for idx in _x_ticks(n, 5):
        parts.append("<text x='%.1f' y='%d' fill='%s' font-size='16' text-anchor='middle'>%s</text>"
                     % (x(idx), baseline + 24, AXIS, _fmt_date(dates[idx])))

    pts = [(x(i), y(v)) for i, v in enumerate(vals)]
    d = monotone_path(pts)
    if d:
        parts.append("<path d='%s' fill='none' stroke='%s' stroke-width='3' "
                     "stroke-linejoin='round' stroke-linecap='round' filter='url(#xkcdify)'/>"
                     % (d, LINE))

    parts.append("</svg>")
    return "".join(parts)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    with open("README.md", "r", encoding="utf-8") as f:
        text = f.read()
    repos = collect_repos(text)

    stars = 0
    forks = 0
    ok = 0
    hist_ok = 0
    errors = []
    buckets = defaultdict(int)  # date (YYYY-MM-DD) -> number of stars added
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for r in repos:
        try:
            d = api("https://api.github.com/repos/" + r)
            st = int(d.get("stargazers_count") or 0)
            fo = int(d.get("forks_count") or 0)
            created = d.get("created_at")
            stars += st
            forks += fo
            ok += 1
        except Exception as e:  # noqa: BLE001
            errors.append("%s: %s" % (r, e))
            continue

        # Rebuild this repo's star history (best-effort; badge above is authoritative).
        try:
            ats = fetch_stargazers(r)
            got = 0
            for sa in ats:
                if sa:
                    buckets[sa[:10]] += 1
                    got += 1
                elif created:
                    buckets[created[:10]] += 1
                    got += 1
            # Zero stars -> no timestamps -> nothing to add (correct).
            if got == 0 and st == 0:
                hist_ok += 1
            elif got > 0:
                hist_ok += 1
            else:
                # stargazers returned nothing but repo has stars; anchor today.
                buckets[today] += st
                hist_ok += 1
        except Exception as e:  # noqa: BLE001
            # Fallback: anchor this repo's current stars on today so the curve
            # still ends at the badge total.
            buckets[today] += st
            print("WARN history %s: %s" % (r, e))

    print("repos=%d ok=%d stars=%d forks=%d hist_ok=%d" %
          (len(repos), ok, stars, forks, hist_ok))
    for e in errors:
        print("WARN " + e)

    if ok == 0:
        print("No repo could be read; aborting without writing anything.", file=sys.stderr)
        sys.exit(1)

    # --- badges (unchanged behaviour) ---
    os.makedirs("badges", exist_ok=True)
    with open("badges/stars.json", "w", encoding="utf-8") as f:
        json.dump(badge("Stars", stars, "yellow"), f)
    with open("badges/forks.json", "w", encoding="utf-8") as f:
        json.dump(badge("Forks", forks, "blue"), f)

    # --- total-star growth history + chart ---
    if hist_ok == 0:
        buckets = {today: stars}

    dates = sorted(buckets)
    running = 0
    rows = []
    for dt in dates:
        running += buckets[dt]
        rows.append({"date": dt, "total_stars": running})

    # Idempotency: if the series is unchanged from the last run, skip rewriting
    # the chart/history so the daily Action does not create a no-op commit.
    try:
        with open("data/stars_history.json", "r", encoding="utf-8") as f:
            prev_series = json.load(f).get("series", [])
    except (OSError, ValueError):
        prev_series = None
    if prev_series == rows:
        print("series unchanged (%d points); skipping chart/history write" % len(rows))
        return

    payload = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo_count": len(repos),
        "series": rows,
    }
    os.makedirs("data", exist_ok=True)
    with open("data/stars_history.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    svg = render_svg(rows)
    with open("stars.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    print("series_points=%d total_stars=%d -> stars.svg" % (len(rows), stars))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as e:
        print("HTTP error %d: %s" % (e.code, e.read().decode()[:200]), file=sys.stderr)
        sys.exit(1)
