#!/usr/bin/env python3
"""Subset the Google Fonts request in index.html to the glyphs the page uses.

Rewrites the `text=` parameter of the fonts.googleapis.com/css2 <link> with every
character that can appear on the page (visible text, alt/aria-label/title
attributes, strings in the inline script, CSS `content:` values) plus printable
ASCII, so later edits to Latin names / digits stay covered.

Usage:
  python3 tools/subset-fonts.py          # rewrite index.html in place
  python3 tools/subset-fonts.py --check  # exit 1 if index.html needs regenerating
Run it after ANY wording change: a character missing from the list renders in
the fallback system font (PingFang / Microsoft JhengHei) instead of Noto Sans TC.
"""
import re, sys, urllib.parse
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML, CSS = ROOT / "index.html", ROOT / "styles.css"

class Collect(HTMLParser):
    def __init__(self):
        super().__init__(); self.chars = set(); self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag == "style": self.skip += 1
        for k, v in attrs:
            if k in ("alt", "aria-label", "title", "placeholder") and v: self.chars.update(v)
    def handle_endtag(self, tag):
        if tag == "style": self.skip -= 1
    def handle_data(self, data):
        if not self.skip: self.chars.update(data)   # includes inline <script> strings

def glyphs(html: str, css: str) -> str:
    c = Collect(); c.feed(html)
    chars = c.chars | set(chr(i) for i in range(0x20, 0x7F))
    for m in re.finditer(r'content:\s*"([^"]*)"', css): chars.update(m.group(1))
    # keep U+0020: spaces between Latin/CJK words must also come from Noto Sans TC
    return "".join(sorted(ch for ch in chars if ch == " " or (not ch.isspace() and ch.isprintable())))

LINK = re.compile(r'(https://fonts\.googleapis\.com/css2\?)([^"]+)')

def rewrite(html: str, text: str) -> str:
    m = LINK.search(html)
    if not m: sys.exit("fonts.googleapis.com/css2 <link> not found in index.html")
    params = [p for p in m.group(2).split("&") if not p.startswith(("text=", "display="))]
    params += ["display=swap", "text=" + urllib.parse.quote(text, safe="")]
    return html[:m.start(2)] + "&".join(params) + html[m.end(2):]

def main():
    html, css = HTML.read_text(encoding="utf-8"), CSS.read_text(encoding="utf-8")
    new = rewrite(html, glyphs(html, css))
    if "--check" in sys.argv:
        ok = new == html
        print("font subset up to date" if ok else "font subset OUT OF DATE: run python3 tools/subset-fonts.py")
        sys.exit(0 if ok else 1)
    HTML.write_text(new, encoding="utf-8")
    print(f"index.html: text= now covers {len(glyphs(html, css))} glyphs")

if __name__ == "__main__":
    main()
