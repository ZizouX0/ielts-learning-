#!/usr/bin/env python3
"""Render a Markdown file to PDF via Chromium's print engine.

    python3 scripts/md-to-pdf.py knowledge/revision-playbook.md exports/revision-playbook.pdf

Uses the Chromium already present in this environment (PLAYWRIGHT_BROWSERS_PATH),
so nothing is downloaded. Tables, code blocks and anchor links all render.
"""
import pathlib
import sys

import markdown
from playwright.sync_api import sync_playwright

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt;
       line-height: 1.5; color: #1a1a1a; }
h1 { font-size: 21pt; border-bottom: 2px solid #333; padding-bottom: 6px;
     margin-top: 0; }
h2 { font-size: 15pt; margin-top: 22px; border-bottom: 1px solid #bbb;
     padding-bottom: 3px; page-break-after: avoid; }
h3 { font-size: 12pt; margin-top: 16px; page-break-after: avoid; }
h4 { font-size: 11pt; margin-top: 13px; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
table { border-collapse: collapse; width: 100%; margin: 12px 0;
        font-size: 9pt; page-break-inside: avoid; }
th, td { border: 1px solid #999; padding: 5px 7px; text-align: left;
         vertical-align: top; }
th { background: #ececec; font-weight: bold; }
code { font-family: 'DejaVu Sans Mono', Consolas, monospace; font-size: 9pt;
       background: #f2f2f2; padding: 1px 3px; border-radius: 2px; }
pre { background: #f6f6f6; border: 1px solid #ddd; padding: 9px;
      border-radius: 3px; page-break-inside: avoid; }
pre code { background: none; padding: 0; }
blockquote { border-left: 3px solid #bbb; margin-left: 0; padding-left: 12px;
             color: #333; font-style: italic; page-break-inside: avoid; }
blockquote em, blockquote strong { font-style: normal; }
a { color: #14449c; text-decoration: none; }
hr { border: none; border-top: 1px solid #ccc; margin: 22px 0; }
ul, ol { padding-left: 22px; }
"""


def main():
    if len(sys.argv) != 3:
        print("Usage: md-to-pdf.py <input.md> <output.pdf>")
        return 1

    src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    if not src.is_file():
        print(f"Error: {src} not found")
        return 1
    dst.parent.mkdir(parents=True, exist_ok=True)

    html_body = markdown.markdown(
        src.read_text(encoding="utf-8"),
        extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
    )
    html = (f"<!doctype html><html><head><meta charset='utf-8'>"
            f"<title>{src.stem}</title><style>{CSS}</style></head>"
            f"<body>{html_body}</body></html>")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html, wait_until="load")
        page.pdf(path=str(dst), format="A4", print_background=True,
                 margin={"top": "18mm", "bottom": "18mm",
                         "left": "16mm", "right": "16mm"},
                 display_header_footer=True,
                 header_template="<div></div>",
                 footer_template=(
                     "<div style='font-size:8pt;color:#666;width:100%;"
                     "text-align:center;font-family:Georgia,serif;'>"
                     "<span class='pageNumber'></span> / "
                     "<span class='totalPages'></span></div>"))
        browser.close()

    print(f"Wrote {dst} ({dst.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
