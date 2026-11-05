#!/usr/bin/env python3
"""Keep the shared README badges in every LimX Dynamics repository in sync.

What it manages, in the badge row at the top of each README
-----------------------------------------------------------
* A small "WeChat developer community" badge. It links to ``doc/wechat_qr.png``
  in limxdynamics/limxdynamics, so refreshing the (weekly-expiring) WeChat group
  QR code = replace that one file. No other repository needs to change.
* A "fork of <upstream>" badge for repositories derived from an upstream
  project (``FORKS`` below), whether or not GitHub records them as forks.
* For READMEs that have no badge row yet, a basic row (``BASE_ROWS``).

The script is idempotent: badges it manages are found by their link and are
replaced in place on every run.

Usage::

    python3 sync_community.py /path/to/clones/*            # edit in place
    python3 sync_community.py --check /path/to/clones/*    # report only
"""
import argparse
import os
import re
import sys

QR_URL = "https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"
COLOR = "2f6feb"

WECHAT_EN = ("WeChat Community",
             "https://img.shields.io/badge/WeChat-Developer%20Community-07C160?logo=wechat&logoColor=white")
WECHAT_ZH = ("微信开发者社区",
             "https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E5%BC%80%E5%8F%91%E8%80%85%E7%A4%BE%E5%8C%BA-07C160?logo=wechat&logoColor=white")

# Repositories derived from an upstream project -> upstream owner/repo.
FORKS = {
    "GMR": "YanjieZe/GMR",
    "luna-beyondmimic": "HybridRobotics/whole_body_tracking",
    "tron1-rl-isaacgym": "leggedrobotics/legged_gym",
    "tron1-rl-isaaclab": "isaac-sim/IsaacLabExtensionTemplate",
    "tron2_openpi": "Physical-Intelligence/openpi",
    "tron2-navigation-pct-gpl": "byangw/PCT_planner",
}

# Basic badges for READMEs that had no badge row: (alt, label, message, link).
_LIC = ("License: Apache-2.0", "license", "Apache-2.0", "LICENSE")
BASE_ROWS = {
    "humanoid-rl-deploy-ros": [_LIC, ("ROS Noetic", "ROS", "Noetic", None),
                               ("Ubuntu 20.04", "Ubuntu", "20.04", None),
                               ("x86_64 / aarch64", "platform", "x86_64 | aarch64", None)],
    "limx-cli": [_LIC, ("Python 3.8+", "Python", "3.8+", None),
                 ("Node.js 22", "Node.js", "22", None)],
    "ros1-bridger": [_LIC, ("ROS Noetic", "ROS", "Noetic", None),
                     ("Ubuntu 20.04", "Ubuntu", "20.04", None),
                     ("x86_64 / aarch64", "platform", "x86_64 | aarch64", None)],
    "tron1-gazebo-ros": [_LIC, ("ROS Noetic", "ROS", "Noetic", None),
                         ("Ubuntu 20.04", "Ubuntu", "20.04", None),
                         ("Gazebo", "simulator", "Gazebo", None)],
    "tron1-gazebo-ros2": [_LIC, ("ROS 2 Iron", "ROS 2", "Iron", None),
                          ("Ubuntu 22.04", "Ubuntu", "22.04", None),
                          ("Gazebo", "simulator", "Gazebo", None)],
    "tron1-rl-deploy-arm": [_LIC, ("ROS Noetic", "ROS", "Noetic", None),
                            ("Ubuntu 20.04", "Ubuntu", "20.04", None),
                            ("Gazebo", "simulator", "Gazebo", None)],
    "tron1-rl-deploy-ros2": [_LIC, ("ROS 2 Iron", "ROS 2", "Iron", None),
                             ("Ubuntu 22.04", "Ubuntu", "22.04", None),
                             ("ONNX Runtime", "inference", "ONNX Runtime", None)],
}

EXCLUDE = {"limxdynamics", "troncamp-mani", "troncamp-web-mani", "troncamp-web-locomotion"}

README_RE = re.compile(r"^README([._-](cn|zh|zh-cn|en))?\.md$", re.I)
OLD_BLOCK_RE = re.compile(r"<!-- limx-community:start -->.*?<!-- limx-community:end -->\n\n?", re.S)
LANG_RE = re.compile(r"(English|英文).{0,80}\|.{0,80}(中文|Chinese)|(中文|简体中文|Chinese).{0,80}\|.{0,80}(English|英文)")


def esc(s):
    return s.replace("-", "--").replace("_", "__").replace(" ", "%20").replace("|", "%7C").replace("+", "%2B")


def is_chinese(text):
    return len(re.findall(r"[一-鿿]", text)) > 200


def is_stub(text):
    return text.count("\n") < 10 and re.search(r"kept so that old\s+links", text)


def html_badge(alt, img, link, close):
    tag = '<img src="%s" alt="%s"%s>' % (img, alt, close)
    return '<a href="%s">%s</a>' % (link, tag) if link else tag


def md_badge(alt, img, link):
    return "[![%s](%s)](%s)" % (alt, img, link) if link else "![%s](%s)" % (alt, img)


def managed(repo, zh):
    """(alt, img, link) badges this script owns, in order."""
    out = []
    if repo in FORKS:
        up = FORKS[repo]
        out.append(("Fork of " + up, "https://img.shields.io/badge/fork%20of-" + esc(up).replace("/", "%2F") + "-" + COLOR,
                    "https://github.com/" + up))
    alt, img = WECHAT_ZH if zh else WECHAT_EN
    out.append((alt, img, QR_URL))
    return out


def strip_managed(text, repo):
    text = OLD_BLOCK_RE.sub("", text)
    links = [re.escape(QR_URL)] + [re.escape("https://github.com/" + FORKS[repo])] if repo in FORKS else [re.escape(QR_URL)]
    for link in links:
        # whole line that only holds the badge (HTML or Markdown)
        text = re.sub(r"(?m)^[ \t]*(<a href=\"%s\">[^\n]*?</a>|\[!\[[^\]]*\]\([^)]*\)\]\(%s\))[ \t]*\n" % (link, link), "", text)
        # inline occurrence inside a single-line row
        text = re.sub(r"\s*<a href=\"%s\"><img [^>]*></a>" % link, "", text)
    return text


def top_region_end(text):
    m = re.search(r"(?m)^## ", text)
    return m.start() if m else min(len(text), 6000)


def find_html_row(text):
    end = top_region_end(text)
    for m in re.finditer(r'<p align="center">.*?</p>', text[:end], re.S):
        if "img.shields.io" in m.group() and not LANG_RE.search(m.group()):
            return m
    return None


def find_md_row(text):
    end = top_region_end(text)
    lines = text[:end].splitlines(keepends=True)
    pos, last = 0, None
    for ln in lines:
        if re.match(r"\s*\[?!\[[^\]]*\]\(https://img\.shields\.io", ln):
            last = pos + len(ln)
        elif last is not None and ln.strip():
            break
        pos += len(ln)
    return last


def insert(text, repo):
    zh = is_chinese(text)
    text = strip_managed(text, repo)
    badges = managed(repo, zh)
    # skip a fork badge the README already carries by hand
    if repo in FORKS and re.search(r"fork%20of-", text[:top_region_end(text)]):
        badges = [b for b in badges if not b[0].startswith("Fork of")]

    row = find_html_row(text)
    if row:
        body = row.group()
        close = " /" if "/>" in body else ""
        style = re.search(r"[?&](style=[\w-]+)", body)
        def img(u):
            return u + (("&" if "?" in u else "?") + style.group(1) if style and "style=" not in u else "")
        if "\n" in body.strip():
            indent = re.search(r"\n([ \t]*)<", body)
            ind = indent.group(1) if indent else "  "
            add = "".join("%s%s\n" % (ind, html_badge(a, img(i), l, close)) for a, i, l in badges)
            cut = body.rfind("</p>")
            pre = body[:cut]
            if not pre.endswith("\n"):
                pre += "\n"
            new = pre + add + body[cut:]
        else:
            cut = body.rfind("</p>")
            new = body[:cut] + "".join(" " + html_badge(a, img(i), l, close) for a, i, l in badges) + body[cut:]
        return text[:row.start()] + new + text[row.end():]

    pos = find_md_row(text)
    if pos is not None:
        add = "".join(md_badge(a, i, l) + "\n" for a, i, l in badges)
        return text[:pos] + add + text[pos:]

    # no badge row yet: build a basic one under the language switcher
    base = [(a, "https://img.shields.io/badge/%s-%s-%s" % (esc(lb), esc(ms), COLOR), lk)
            for a, lb, ms, lk in BASE_ROWS.get(repo, [_LIC])]
    items = base + badges
    block = '<p align="center">\n' + "".join("  %s\n" % html_badge(a, i, l, "") for a, i, l in items) + "</p>\n\n"
    lines = text.splitlines(keepends=True)
    for i, ln in enumerate(lines[:40]):
        if LANG_RE.search(ln):
            j = i
            while "<p" in "".join(lines[max(0, i - 2):i + 1]) and j < len(lines) - 1 and "</p>" not in lines[j]:
                j += 1
            k = j + 1
            while k < len(lines) and not lines[k].strip():
                k += 1
            return "".join(lines[:j + 1]) + "\n" + block + "".join(lines[k:])
    return block + text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repos", nargs="+", help="local clone directories")
    ap.add_argument("--check", action="store_true", help="report only, do not write")
    a = ap.parse_args()
    changed = 0
    for repo in a.repos:
        name = os.path.basename(os.path.normpath(repo))
        if name in EXCLUDE or name.lower().startswith("flux"):
            print("skip  %s" % name)
            continue
        for fn in sorted(os.listdir(repo)):
            if not README_RE.match(fn):
                continue
            path = os.path.join(repo, fn)
            with open(path, encoding="utf-8", newline="") as f:
                raw = f.read()
            crlf = "\r\n" in raw
            old = raw.replace("\r\n", "\n")
            if is_stub(old):
                continue
            new = insert(old, name)
            if crlf:
                new = new.replace("\n", "\r\n")
            if new != raw:
                changed += 1
                print("%s %s/%s" % ("would" if a.check else "edit ", name, fn))
                if not a.check:
                    with open(path, "w", encoding="utf-8", newline="") as f:
                        f.write(new)
    print("%d file(s) %s" % (changed, "need updating" if a.check else "updated"))
    return 1 if (a.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
