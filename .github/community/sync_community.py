#!/usr/bin/env python3
"""Insert / refresh the shared "WeChat developer community" badge in every
LimX Dynamics repository README.

Single source of truth
----------------------
* The QR code lives ONLY in this repo: ``doc/wechat_qr.png``.
  Every repo's badge links to that file, so refreshing the (weekly-expiring)
  WeChat group QR code = replace ``doc/wechat_qr.png`` here. Nothing else.
* The badge markup lives in ``BLOCK_EN`` / ``BLOCK_ZH`` below. To change the
  wording or style, edit them and re-run this script over local clones.

The block is wrapped in ``<!-- limx-community:start -->`` /
``<!-- limx-community:end -->`` markers, so re-running replaces it in place.

Usage::

    python3 sync_community.py /path/to/clones/*      # edit READMEs in place
    python3 sync_community.py --check /path/to/clones/*

Repositories listed in ``EXCLUDE`` are skipped (FluxVLA repos live in the
FluxVLA org and are never touched).
"""
import argparse
import os
import re
import sys

QR_URL = "https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"

START = "<!-- limx-community:start -->"
END = "<!-- limx-community:end -->"
NOTE = "<!-- Managed by limxdynamics/limxdynamics/.github/community/sync_community.py; QR code: doc/wechat_qr.png in that repo -->"

BLOCK_EN = (
    '<p align="center"><a href="%s"><img src="https://img.shields.io/badge/'
    'Join%%20Our%%20WeChat%%20Community-All%%20Projects%%20Welcome-07C160'
    '?style=for-the-badge&logo=wechat&logoColor=white" alt="WeChat Community"></a></p>'
) % QR_URL

BLOCK_ZH = (
    '<p align="center"><a href="%s"><img src="https://img.shields.io/badge/'
    '%%E5%%BE%%AE%%E4%%BF%%A1%%E5%%BC%%80%%E5%%8F%%91%%E8%%80%%85%%E7%%BE%%A4-'
    '%%E6%%89%%AB%%E7%%A0%%81%%E5%%8A%%A0%%E5%%85%%A5%%20%%C2%%B7%%20'
    '%%E8%%A6%%86%%E7%%9B%%96%%E5%%85%%A8%%E9%%83%%A8%%E5%%BC%%80%%E6%%BA%%90%%E9%%A1%%B9%%E7%%9B%%AE-07C160'
    '?style=for-the-badge&logo=wechat&logoColor=white" alt="微信开发者社区"></a></p>'
) % QR_URL

EXCLUDE = {
    "limxdynamics",            # the profile repo itself (has its own badge)
    "troncamp-mani",
    "troncamp-web-mani",
    "troncamp-web-locomotion",
}

README_RE = re.compile(r"^README([._-](cn|zh|zh-cn|en))?\.md$", re.I)
BLOCK_RE = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
# A line in the language switcher: "English | 中文" / "中文 | English" etc.
LANG_RE = re.compile(r"(English|英文).{0,80}\|.{0,80}(中文|Chinese)|(中文|Chinese).{0,80}\|.{0,80}(English|英文)")


def is_chinese(text):
    return len(re.findall(r"[一-鿿]", text)) > 200


def is_stub(text):
    return text.count("\n") < 10 and re.search(r"kept so that old\s+links", text)


def render(text):
    body = BLOCK_ZH if is_chinese(text) else BLOCK_EN
    return "%s\n%s\n%s\n%s\n" % (START, NOTE, body, END)


def insert(text):
    block = render(text)
    if START in text:
        return BLOCK_RE.sub(lambda _: block, text, count=1)
    lines = text.splitlines(keepends=True)
    # 1) right after the paragraph that contains the language switcher
    for i, line in enumerate(lines[:40]):
        if LANG_RE.search(line):
            j = i
            if not line.rstrip().endswith("</p>") and "<p" in "".join(lines[max(0, i - 2):i + 1]):
                while j < len(lines) - 1 and "</p>" not in lines[j]:
                    j += 1
            return "".join(lines[:j + 1]) + "\n" + block + "".join(lines[j + 1:])
    # 2) otherwise right after the first top-level heading
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return "".join(lines[:i + 1]) + "\n" + block + "\n" + "".join(lines[i + 1:])
    # 3) otherwise at the very top
    return block + "\n" + text


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
            new = insert(old)
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
