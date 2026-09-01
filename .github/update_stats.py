import json
import os
import re
import sys
import urllib.request

TOKEN = os.environ.get("GITHUB_TOKEN", "")


def api(url):
    req = urllib.request.Request(
        url, headers={"Accept": "application/vnd.github+json", "User-Agent": "limx-gh-stats"}
    )
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect_repos(text):
    seen = {}
    for m in re.finditer(r"github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)", text):
        seen.setdefault("%s/%s" % (m.group(1), m.group(2)), True)
    return list(seen.keys())


def main():
    with open("README.md", "r", encoding="utf-8") as f:
        text = f.read()
    repos = collect_repos(text)

    stars = 0
    forks = 0
    ok = 0
    errors = []
    for r in repos:
        try:
            d = api("https://api.github.com/repos/" + r)
            stars += int(d.get("stargazers_count") or 0)
            forks += int(d.get("forks_count") or 0)
            ok += 1
        except Exception as e:  # noqa: BLE001
            errors.append("%s: %s" % (r, e))

    print("repos=%d ok=%d stars=%d forks=%d" % (len(repos), ok, stars, forks))
    if errors:
        for e in errors:
            print("WARN " + e)

    if ok == 0:
        print("No repo could be read; aborting without writing badges.", file=sys.stderr)
        sys.exit(1)

    def badge(label, value, color):
        return {
            "schemaVersion": 1,
            "label": label,
            "message": str(value),
            "color": color,
            "style": "flat",
            "namedLogo": "github",
        }

    os.makedirs("badges", exist_ok=True)
    with open("badges/stars.json", "w", encoding="utf-8") as f:
        json.dump(badge("Stars", stars, "yellow"), f)
    with open("badges/forks.json", "w", encoding="utf-8") as f:
        json.dump(badge("Forks", forks, "blue"), f)


if __name__ == "__main__":
    main()