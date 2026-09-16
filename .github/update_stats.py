#!/usr/bin/env python3
"""Compute aggregate GitHub stats for the limxdynamics/limxdynamics profile README.

Two outputs:

1. Badges (existing behaviour, kept as-is):
   * badges/stars.json  -- total stars  across every repo linked in README.md
   * badges/forks.json  -- total forks  across every repo linked in README.md

2. Total-star growth chart (new):
   * data/stars_history.json -- daily cumulative total-star series
   * stars.svg               -- xkcd-style hand-drawn chart embedded by README.md

The chart carries a star glyph plus the current total in its TOP-RIGHT corner,
right-aligned to the plot's right edge, so the headline number is readable without
cross-referencing the badge. The plot area itself keeps its original proportions
(433px tall): the legend lives in a strip reserved above the y-axis, which shifts
the whole plot down without rescaling it. ``CHART_VERSION`` is bumped whenever the
rendered markup changes, so the idempotency guard in ``main()`` does not mistake
a renderer-only change for "nothing to do".

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
AXIS_DARK = "#c9d1d9"
STAR = "#dd4528"       # same accent as the curve: ties the legend to the line
LEGEND_STRIP = 36      # px reserved above the y-axis for the legend
LEGEND_FONT = 20       # a touch larger than the 16px axis labels, for emphasis
LEGEND_GAP = 12        # px between the star glyph and the count
# Advance width of one digit in the embedded xkcd font, in em. Measured from the
# woff itself (every digit is 55.5px at font-size:100px, i.e. exactly additive),
# so the right-aligned label needs no font-metrics library at run time.
DIGIT_ADV = 0.555
CHART_VERSION = 3      # bump when the rendered markup changes (see main())
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


def _star_path(cx, cy, r_out, inner_ratio=0.382):
    """Return a 5-pointed star outline centred on (cx, cy).

    ``inner_ratio`` 0.382 is the regular-pentagram ratio, so the glyph reads as
    a proper star rather than a spiky blob. Rendered through the same
    ``xkcdify`` displacement filter as the axes, it picks up the hand-drawn
    wobble of the rest of the chart.
    """
    import math
    pts = []
    for k in range(10):
        ang = -math.pi / 2 + k * math.pi / 5
        rr = r_out if k % 2 == 0 else r_out * inner_ratio
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    return "M" + " L".join("%.2f,%.2f" % p for p in pts) + " Z"


def render_svg(rows, axis_color=AXIS):
    if not rows:
        return ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 %d'>"
                "</svg>" % (533 + LEGEND_STRIP))

    W = 800
    M_TOP, M_RIGHT, M_LEFT = 50 + LEGEND_STRIP, 30, 62
    M_BOTTOM = 50
    H = 533 + LEGEND_STRIP         # strip reserved at the top for the legend
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
                 "filter='url(#xkcdify)'/>" % (M_LEFT, M_TOP, M_LEFT, baseline, axis_color))
    for v in yticks:
        yy = y(v)
        parts.append("<line x1='%d' y1='%.1f' x2='%d' y2='%.1f' stroke='%s'/>"
                     % (M_LEFT - 4, yy, M_LEFT, yy, axis_color))
        label = "" if v == 0 else _fmt_number(v, yunit)
        if label:
            parts.append("<text x='%d' y='%.1f' fill='%s' font-size='16' "
                         "text-anchor='end'>%s</text>" % (M_LEFT - 8, yy + 6, axis_color, label))

    parts.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='2' "
                 "filter='url(#xkcdify)'/>" % (M_LEFT, baseline, W - M_RIGHT, baseline, axis_color))
    for idx in _x_ticks(n, 5):
        anchor = "middle"
        if idx == 0:
            anchor = "start"
        elif idx == n - 1:
            anchor = "end"
        parts.append("<text x='%.1f' y='%d' fill='%s' font-size='16' text-anchor='%s'>%s</text>"
                     % (x(idx), baseline + 24, axis_color, anchor, _fmt_date(dates[idx])))

    pts = [(x(i), y(v)) for i, v in enumerate(vals)]
    d = monotone_path(pts)
    if d:
        parts.append("<path d='%s' fill='none' stroke='%s' stroke-width='3' "
                     "stroke-linejoin='round' stroke-linecap='round' filter='url(#xkcdify)'/>"
                     % (d, LINE))

    # Top-right legend: hand-drawn star glyph + current total, right-aligned to
    # the plot's right edge. Same xkcd font as every other label, the curve's
    # accent colour for the glyph and the axis colour for the count -- i.e. the
    # chart's own palette, nothing new. The glyph sits left of the count; the pair
    # is placed from DIGIT_ADV so the label stays flush with the axis edge however
    # many digits the total grows to.
    label = str(int(vals[-1]))
    legend_y = M_TOP - 30
    star_r = 13
    text_w = len(label) * DIGIT_ADV * LEGEND_FONT
    parts.append("<path d='%s' fill='%s' stroke='%s' stroke-width='1.5' "
                 "stroke-linejoin='round' filter='url(#xkcdify)'/>"
                 % (_star_path(W - M_RIGHT - text_w - LEGEND_GAP - star_r,
                               legend_y, star_r), STAR, STAR))
    parts.append("<text x='%d' y='%.1f' fill='%s' font-size='%d' "
                 "text-anchor='end'>%s</text>"
                 % (W - M_RIGHT, legend_y + 7, axis_color, LEGEND_FONT, label))

    parts.append("</svg>")
    return "".join(parts)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def bump_readme_cache_bust(path, token):
    """Rewrite the `?v=` cache-bust on chart URLs so GitHub's image proxy
    re-fetches the freshly generated SVG. raw.githubusercontent.com itself
    ignores the query string, but the proxy keys its cache on the full URL,
    so a new `?v=` value forces a fresh fetch."""
    with open(path, "r", encoding="utf-8") as f:
        t = f.read()
    new = re.sub(r'(stars(?:-dark)?\.svg)(?:\?v=[^"\']*)?', r"\1?v=" + token, t)
    if new != t:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
    return new != t


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
            prev = json.load(f)
    except (OSError, ValueError):
        prev = {}
    if prev.get("series") == rows and prev.get("chart_version") == CHART_VERSION:
        print("series unchanged (%d points) and chart already v%d; "
              "skipping chart/history write" % (len(rows), CHART_VERSION))
        return

    payload = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo_count": len(repos),
        "chart_version": CHART_VERSION,
        "series": rows,
    }
    os.makedirs("data", exist_ok=True)
    with open("data/stars_history.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    with open("stars.svg", "w", encoding="utf-8") as f:
        f.write(render_svg(rows))

    with open("stars-dark.svg", "w", encoding="utf-8") as f:
        f.write(render_svg(rows, axis_color=AXIS_DARK))

    # Bump the cache-bust query on the README chart URLs so GitHub's image
    # proxy re-fetches the new SVG instead of serving a stale cached copy.
    ts = datetime.now(timezone.utc).strftime("%Y%m%d%H%M")
    for p in ("README.md", "README_cn.md"):
        bump_readme_cache_bust(p, ts)

    print("series_points=%d total_stars=%d -> stars.svg / stars-dark.svg" % (len(rows), stars))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as e:
        print("HTTP error %d: %s" % (e.code, e.read().decode()[:200]), file=sys.stderr)
        sys.exit(1)
