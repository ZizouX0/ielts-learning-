#!/usr/bin/env python3
"""Render the War Book to a designed, navigable PDF.

    python3 scripts/build-book-pdf.py

Two passes: the first finds which page every heading lands on, the second
rebuilds the contents page with real page numbers. Afterwards, PDF bookmarks are
written so the reader's sidebar outline works.

Nothing is removed from the source markdown — this is presentation only.
"""
import base64
import pathlib
import re
import subprocess
import sys

import markdown
import pypdf
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "ielts-book/book/IELTS-Academic-War-Book.md"
OUT = ROOT / "exports/IELTS-Academic-War-Book.pdf"
FONTS = ROOT / ".claude/skills/canvas-design/canvas-fonts"
TMP = pathlib.Path("/tmp/warbook")
TMP.mkdir(exist_ok=True)

FONT_FACES = [
    ("BookSerif", "IBMPlexSerif-Regular.ttf", 400, "normal"),
    ("BookSerif", "IBMPlexSerif-Italic.ttf", 400, "italic"),
    ("BookSerif", "IBMPlexSerif-Bold.ttf", 700, "normal"),
    ("BookSerif", "IBMPlexSerif-BoldItalic.ttf", 700, "italic"),
    ("BookSans", "InstrumentSans-Regular.ttf", 400, "normal"),
    ("BookSans", "InstrumentSans-Italic.ttf", 400, "italic"),
    ("BookSans", "InstrumentSans-Bold.ttf", 700, "normal"),
    ("BookMono", "JetBrainsMono-Regular.ttf", 400, "normal"),
    ("BookMono", "JetBrainsMono-Bold.ttf", 700, "normal"),
]


def font_css():
    out = []
    for family, fname, weight, style in FONT_FACES:
        b64 = base64.b64encode((FONTS / fname).read_bytes()).decode()
        out.append(
            f"@font-face{{font-family:'{family}';font-weight:{weight};"
            f"font-style:{style};src:url(data:font/ttf;base64,{b64}) format('truetype');}}"
        )
    return "\n".join(out)


CSS = """
:root{
  --ink:#1c1c1e; --muted:#6b6b70; --faint:#96969c;
  --rule:#d8d8dc; --accent:#8c2f39; --accent-soft:#f7f0f0;
  --tip:#1f5c3d; --tip-soft:#eef5f1;
  --warn:#8a5a00; --warn-soft:#fdf6e8;
}
@page{ size:A4; margin:20mm 19mm 18mm 19mm; }
@page:first{ margin:0; }

html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
body{
  font-family:'BookSerif',Georgia,serif;
  font-size:10.4pt; line-height:1.58; color:var(--ink);
  hyphens:auto; -webkit-hyphens:auto; text-align:left;
  /* This is a reference book people search. The fi/fl ligatures are prettier,
     but they break plain-text search for "find", "first", "flow", "fluency"
     and "difficult" in most PDF readers. Searchability wins. */
  font-variant-ligatures:none; -webkit-font-feature-settings:"liga" 0,"clig" 0;
  font-feature-settings:"liga" 0,"clig" 0;
}
p{ margin:0 0 .72em; orphans:3; widows:3; }

/* ---- headings ---- */
h1,h2,h3,h4{ font-family:'BookSans',system-ui,sans-serif; line-height:1.22;
  color:var(--ink); page-break-after:avoid; break-after:avoid; }

/* chapter opener */
h1{
  font-size:25pt; font-weight:700; letter-spacing:-.015em;
  margin:0 0 1.4rem; padding:0 0 .7rem;
  border-bottom:3px solid var(--accent);
  page-break-before:always; break-before:page;
}
h1.no-break{ page-break-before:auto; break-before:auto; }

h2{ font-size:14.5pt; font-weight:700; margin:1.9em 0 .55em;
    padding-bottom:.28rem; border-bottom:1px solid var(--rule); }
h3{ font-size:11.6pt; font-weight:700; margin:1.5em 0 .4em; color:#2c2c30; }
h4{ font-size:10.6pt; font-weight:700; margin:1.2em 0 .3em; color:var(--muted);
    text-transform:uppercase; letter-spacing:.05em; }

/* ---- the 634 source notes: present, but out of the way ---- */
.src{
  font-family:'BookSans',sans-serif; font-size:6.9pt; color:#a6a6ac;
  white-space:normal; line-height:1.25; letter-spacing:-.002em;
}
.src::before{ content:"\\00a0"; }

/* ---- rhythm on dense prose pages ---- */
/* a paragraph that opens with a bold run is a labelled point: give it air */
p.lead{ margin-top:1.15em; }

/* a paragraph opening with a bold quotation is a myth: make it scannable */
p.myth{
  margin:1.15em 0 .8em; padding:.55em .85em .55em .8em;
  background:var(--warn-soft); border-left:3px solid var(--warn);
  border-radius:0 3px 3px 0;
  page-break-inside:avoid; break-inside:avoid;
}

/* checklists read better with room */
li input[type=checkbox]{ margin-right:.4em; }

/* ---- callouts (blockquotes) ---- */
blockquote{
  margin:.9em 0; padding:.62em .95em;
  background:var(--accent-soft); border-left:3px solid var(--accent);
  border-radius:0 3px 3px 0;
  page-break-inside:avoid; break-inside:avoid;
}
blockquote p{ margin:0 0 .45em; }
blockquote p:last-child{ margin-bottom:0; }
blockquote em{ font-style:italic; }

/* ---- tables ---- */
table{
  border-collapse:collapse; width:100%; margin:.95em 0;
  font-size:8.9pt; line-height:1.42;
  page-break-inside:avoid; break-inside:avoid;
}
thead{ display:table-header-group; }
th,td{ border:1px solid #dcdce0; padding:5px 7px; text-align:left; vertical-align:top; }
th{ background:#f0f0f2; font-family:'BookSans',sans-serif; font-weight:700;
    font-size:8.4pt; }
tbody tr:nth-child(even){ background:#fafafb; }
td .src,th .src{ font-size:6.6pt; }

/* ---- lists ---- */
ul,ol{ margin:.5em 0 .8em; padding-left:1.35em; }
li{ margin:.24em 0; }
li>ul,li>ol{ margin:.2em 0; }

/* ---- code ---- */
code{ font-family:'BookMono',monospace; font-size:8.4pt;
      background:#f2f2f4; padding:.5px 3px; border-radius:2px; }
pre{ background:#f7f7f9; border:1px solid #e4e4e8; border-left:3px solid var(--muted);
     padding:.65em .8em; border-radius:3px; font-size:8.3pt; line-height:1.45;
     page-break-inside:avoid; break-inside:avoid; overflow-wrap:break-word; }
pre code{ background:none; padding:0; font-size:inherit; }

hr{ border:0; border-top:1px solid var(--rule); margin:1.6em 0; }
a{ color:var(--accent); text-decoration:none; }
strong{ font-weight:700; }

/* ---- cover ---- */
.cover{
  page-break-after:always; break-after:page;
  height:257mm; padding:38mm 24mm 0; box-sizing:border-box;
  display:flex; flex-direction:column;
}
.cover .rule{ width:64px; height:5px; background:var(--accent); margin-bottom:20mm; }
.cover h1{
  font-size:41pt; line-height:1.06; font-weight:700; letter-spacing:-.028em;
  border:0; margin:0 0 9mm; padding:0; page-break-before:auto; break-before:auto;
}
.cover .sub{ font-family:'BookSans',sans-serif; font-size:12.5pt; line-height:1.5;
  color:var(--muted); max-width:118mm; margin-bottom:auto; }
.cover .meta{ font-family:'BookSans',sans-serif; font-size:9pt; color:var(--faint);
  border-top:1px solid var(--rule); padding-top:5mm; margin-bottom:22mm; }
.cover .meta strong{ color:var(--ink); }

/* ---- contents ---- */
.toc{ page-break-after:always; break-after:page; }
.toc h1{ page-break-before:auto; break-before:auto; }
.toc-row{
  display:flex; align-items:baseline; gap:.5em;
  margin:.34em 0; font-size:10pt; break-inside:avoid;
}
.toc-row .t{ font-family:'BookSans',sans-serif; }
.toc-row.ch{ margin-top:1.05em; font-weight:700; font-size:11pt; }
.toc-row.ch .num{ color:var(--accent); font-weight:700; margin-right:.15em; }
.toc-row.sec{ padding-left:1.5em; font-size:9.2pt; color:#3a3a3e; }
.toc-row .dots{ flex:1; border-bottom:1px dotted #c4c4ca; transform:translateY(-.22em); }
.toc-row .pg{ font-family:'BookSans',sans-serif; font-size:9pt; color:var(--muted);
  font-variant-numeric:tabular-nums; }
.toc-note{ font-size:9pt; color:var(--muted); margin-top:1.6em;
  border-top:1px solid var(--rule); padding-top:.8em; }

/* keep short blocks whole */
h2+p,h3+p{ page-break-before:avoid; }
"""


def transform_html(html: str) -> str:
    """Make source notes recede, without removing a single one."""
    # <code>[src: ...]</code>  ->  span
    html = re.sub(r"<code>(\[src:.*?\])</code>",
                  lambda m: f'<span class="src">{m.group(1)}</span>',
                  html, flags=re.S)
    # bare [src: ...] in text
    html = re.sub(r"(?<!>)(\[src:[^\[\]]*?\])",
                  lambda m: f'<span class="src">{m.group(1)}</span>',
                  html, flags=re.S)

    # Paragraphs opening with a bold quotation are myths — box them so the
    # Myths sections can be scanned rather than read.
    html = re.sub(r'<p><strong>(&quot;|"|“)',
                  lambda m: f'<p class="myth"><strong>{m.group(1)}',
                  html)
    # Any other paragraph opening with a bold run is a labelled point.
    html = re.sub(r'<p><strong>(?!(&quot;|"|“))',
                  '<p class="lead"><strong>', html)
    return html


def build_html(body_md: str, toc_html: str) -> str:
    body = markdown.markdown(
        body_md,
        extensions=["tables", "fenced_code", "attr_list", "sane_lists", "md_in_html"],
    )
    body = transform_html(body)

    cover = """
<div class="cover">
  <div class="rule"></div>
  <h1>The IELTS<br>Academic<br>War Book</h1>
  <div class="sub">A complete preparation system for band 7.0 — built for one
  reader, and verified line by line against official sources.</div>
  <div class="meta">
    <strong>Verified 31 July 2026.</strong><br>
    Nine research passes · six independent adversarial audits · every claim traced
    to an official source · nothing unverified in the text.
  </div>
</div>
"""
    return (f"<!doctype html><html><head><meta charset='utf-8'>"
            f"<title>The IELTS Academic War Book</title>"
            f"<style>{font_css()}\n{CSS}</style></head><body>"
            f"{cover}{toc_html}{body}</body></html>")


def render(html: str, out: pathlib.Path):
    page_file = TMP / "book.html"
    page_file.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(f"file://{page_file}", wait_until="load")
        pg.wait_for_timeout(2500)
        pg.pdf(path=str(out), format="A4", print_background=True,
               display_header_footer=True,
               header_template="<div></div>",
               footer_template=(
                   "<div style=\"width:100%;font-family:sans-serif;font-size:7.5pt;"
                   "color:#96969c;padding:0 19mm;display:flex;justify-content:space-between;\">"
                   "<span>The IELTS Academic War Book</span>"
                   "<span class='pageNumber'></span></div>"),
               margin={"top": "20mm", "bottom": "18mm",
                       "left": "19mm", "right": "19mm"})
        b.close()


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def find_pages(pdf_path: pathlib.Path, headings):
    """Map each heading to the 1-based page it first appears on."""
    reader = pypdf.PdfReader(str(pdf_path))
    pages = [norm(p.extract_text() or "") for p in reader.pages]
    found, cursor = {}, 0
    for key, text in headings:
        probe = norm(text)[:60]
        if not probe:
            continue
        for i in range(cursor, len(pages)):
            if probe in pages[i]:
                found[key] = i + 1
                cursor = i          # headings are in document order
                break
    return found, len(reader.pages)


def build_companion(md_path: pathlib.Path, out_path: pathlib.Path, title: str):
    """Render a companion document with the same typography, no cover or TOC."""
    body = markdown.markdown(
        md_path.read_text(encoding="utf-8"),
        extensions=["tables", "fenced_code", "attr_list", "sane_lists"],
    )
    body = transform_html(body)
    body = body.replace("<h1>", "<h1 class='no-break'>", 1)
    html = (f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title>"
            f"<style>{font_css()}\n{CSS}</style></head><body>{body}</body></html>")
    render(html, out_path)
    n = len(pypdf.PdfReader(str(out_path)).pages)
    print(f"  {out_path.name:38} {n:>3} pages")


COMPANIONS = [
    ("CHEAT-SHEETS.md", "CHEAT-SHEETS.pdf", "Cheat Sheets"),
    ("appendix-C-error-card.md", "error-card.pdf", "Error Card"),
    ("appendix-D-pre-test-checklist.md", "pre-test-checklist.pdf", "Pre-test Checklist"),
    ("appendix-A-band-descriptors.md", "appendix-A-band-descriptors.pdf", "Band Descriptors"),
    ("appendix-B-question-type-index.md", "appendix-B-question-index.pdf", "Question-Type Index"),
    ("appendix-E-sources.md", "appendix-E-sources.pdf", "Sources Consulted"),
]


def main():
    if "--companions" in sys.argv:
        print("companions:")
        for src, out, title in COMPANIONS:
            build_companion(ROOT / "ielts-book/book" / src,
                            ROOT / "exports" / out, title)
        return 0

    md = SRC.read_text(encoding="utf-8")

    # Strip the hand-written contents list; we generate a real one.
    md = re.sub(r"\n## Contents\n.*?(?=\n---\n)", "\n", md, count=1, flags=re.S)

    # Collect chapter (h1) and section (h2) headings in document order.
    headings = []
    for m in re.finditer(r"^(#{1,2}) (.+)$", md, flags=re.M):
        level, text = len(m.group(1)), m.group(2).strip()
        text = re.sub(r"[*`]", "", text)
        headings.append((f"{level}:{m.start()}", (level, text)))
    flat = [(k, v[1]) for k, v in headings]

    # ---- pass 1: no page numbers yet ----
    print("pass 1 — laying out to find page numbers…")
    render(build_html(md, "<div class='toc'></div>"), TMP / "pass1.pdf")
    pages, total = find_pages(TMP / "pass1.pdf", flat)
    print(f"        {total} pages, {len(pages)}/{len(flat)} headings located")

    # ---- build the contents page ----
    rows = ["<div class='toc'><h1 class='no-break'>Contents</h1>"]
    chapter_no = 0
    for key, (level, text) in headings:
        pg = pages.get(key)
        if pg is None:
            continue
        if level == 1:
            if text.lower().startswith("contents"):
                continue
            m = re.match(r"Chapter (\d+)\s*[—-]\s*(.+)", text)
            if m:
                chapter_no = int(m.group(1))
                label = (f"<span class='num'>{chapter_no}</span>"
                         f"<span class='t'>{m.group(2)}</span>")
            else:
                label = f"<span class='t'>{text}</span>"
            rows.append(f"<div class='toc-row ch'>{label}"
                        f"<span class='dots'></span><span class='pg'>{pg}</span></div>")
        else:
            if text.lower() in {"contents"}:
                continue
            rows.append(f"<div class='toc-row sec'><span class='t'>{text}</span>"
                        f"<span class='dots'></span><span class='pg'>{pg}</span></div>")
    rows.append(
        "<div class='toc-note'><strong>Short of time?</strong> Every chapter opens "
        "with a <em>60-second summary</em>. On a busy day, that summary is the "
        "chapter — the nine of them take about fifteen minutes and carry most of "
        "what moves a band. The appendices, error card and cheat sheets ship as "
        "separate files so you can print them.</div></div>")
    toc_html = "\n".join(rows)

    # ---- pass 2: with real page numbers ----
    print("pass 2 — rendering with the contents page…")
    render(build_html(md, toc_html), TMP / "pass2.pdf")
    pages2, total2 = find_pages(TMP / "pass2.pdf", flat)
    print(f"        {total2} pages, {len(pages2)}/{len(flat)} headings located")

    # ---- bookmarks ----
    reader = pypdf.PdfReader(str(TMP / "pass2.pdf"))
    writer = pypdf.PdfWriter()
    for p in reader.pages:
        writer.add_page(p)
    parent = None
    for key, (level, text) in headings:
        pg = pages2.get(key)
        if pg is None:
            continue
        if level == 1:
            parent = writer.add_outline_item(text, pg - 1)
        else:
            writer.add_outline_item(text, pg - 1, parent=parent)
    writer.page_mode = "/UseOutlines"      # open with the sidebar showing
    with open(OUT, "wb") as fh:
        writer.write(fh)

    size = OUT.stat().st_size
    print(f"\nWrote {OUT} — {total2} pages, {size:,} bytes, "
          f"{len(pages2)} bookmarks")


if __name__ == "__main__":
    sys.exit(main())


