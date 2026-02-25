#!/usr/bin/env python3
"""Check all local links in index.html for existence and git tracking."""
import os
import sys
import subprocess
from html.parser import HTMLParser

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value:
                    self.links.append(value)

def is_tracked(filepath):
    try:
        subprocess.run(
            ["git", "ls-files", "--error-unmatch", filepath],
            cwd=SCRIPT_DIR, capture_output=True, check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    index_path = os.path.join(SCRIPT_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    parser = LinkExtractor()
    parser.feed(html)

    anchors, externals, ok, untracked, broken = [], [], [], [], []

    seen = set()
    for href in parser.links:
        if href in seen:
            continue
        seen.add(href)

        if href.startswith("#"):
            anchors.append(href)
        elif href.startswith("http://") or href.startswith("https://"):
            externals.append(href)
        else:
            clean = href.split("#")[0].split("?")[0]
            full = os.path.join(SCRIPT_DIR, clean.replace("/", os.sep))
            if not os.path.exists(full):
                broken.append(clean)
            elif not is_tracked(clean):
                untracked.append(clean)
            else:
                ok.append(clean)

    print("=" * 60)
    print("LINK CHECK REPORT: index.html")
    print("=" * 60)

    print(f"\n[ANCHOR] ({len(anchors)} links -- not checked)")
    print(f"\n[EXTERNAL] ({len(externals)} links -- not checked)")

    print(f"\n[LOCAL OK] ({len(ok)} links)")
    for f in sorted(ok):
        print(f"  {f}")

    print(f"\n[LOCAL UNTRACKED] ({len(untracked)} links -- exists but not in git)")
    for f in sorted(untracked):
        print(f"  {f}")

    print(f"\n[LOCAL BROKEN] ({len(broken)} links -- file not found on disk)")
    for f in sorted(broken):
        print(f"  {f}")

    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Anchors  : {len(anchors)}")
    print(f"  External : {len(externals)}")
    print(f"  Local OK : {len(ok)}")
    print(f"  Untracked: {len(untracked)}")
    print(f"  BROKEN   : {len(broken)}")

    strict = "--strict" in sys.argv
    if broken:
        print(f"\nResult: FAIL ({len(broken)} broken links)")
        sys.exit(1)
    elif strict and untracked:
        print(f"\nResult: FAIL ({len(untracked)} untracked files -- git add them before committing)")
        sys.exit(1)
    else:
        print(f"\nResult: PASS (no broken links)")
        sys.exit(0)

if __name__ == "__main__":
    main()
