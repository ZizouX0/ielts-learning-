#!/usr/bin/env python3
"""Render The Playbook — the short, tactical companion to the War Book.

    python3 scripts/build-playbook-pdf.py

Designed to be scanned, not read. Big type, wide spacing, every move a card with
a numbered badge and a payoff line. No source notes, no citations, no prose.
"""
import base64
import io
import pathlib
import re
import sys

import markdown
import pikepdf
from playwright.sync_api import sync_playwright
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as rl_canvas

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRCDIR = ROOT / "ielts-book/playbook"
OUT = ROOT / "exports/THE-PLAYBOOK.pdf"
FONTS = ROOT / ".claude/skills/canvas-design/canvas-fonts"
TMP = pathlib.Path("/tmp/playbook")
TMP.mkdir(exist_ok=True)

ORDER = ["01-front.md", "02-listening-reading.md", "03-writing.md",
         "04-speaking-language.md", "05-testday.md"]

FONT_FACES = [
    ("PBSerif", "IBMPlexSerif-Regular.ttf", 400, "normal"),
    ("PBSerif", "IBMPlexSerif-Italic.ttf", 400, "italic"),
    ("PBSerif", "IBMPlexSerif-Bold.ttf", 700, "normal"),
    ("PBSans", "InstrumentSans-Regular.ttf", 400, "normal"),
    ("PBSans", "InstrumentSans-Italic.ttf", 400, "italic"),
    ("PBSans", "InstrumentSans-Bold.ttf", 700, "normal"),
    ("PBMono", "JetBrainsMono-Regular.ttf", 400, "normal"),
]


def font_css():
    out = []
    for fam, f, w, s in FONT_FACES:
        b64 = base64.b64encode((FONTS / f).read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{s};"
                   f"src:url(data:font/ttf;base64,{b64}) format('truetype');}}")
    return "\n".join(out)


CSS = """
:root{ --ink:#17171a; --muted:#5e5e66; --faint:#96969e; --rule:#e0e0e5;
       --accent:#8c2f39; --go:#166b46; --stop:#a02c2c; --pay:#8a5a00; }
@page{ size:A4; margin:20mm 18mm 18mm 18mm; }
html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
body{ font-family:'PBSerif',Georgia,serif; font-size:11.2pt; line-height:1.55;
      color:var(--ink); font-variant-ligatures:none;
      font-feature-settings:"liga" 0,"clig" 0; }
p{ margin:0 0 .6em; }
strong{ font-weight:700; }
em{ font-style:italic; }

h1{ font-family:'PBSans',sans-serif; font-size:27pt; font-weight:700;
    letter-spacing:-.02em; margin:0 0 .5rem; padding-bottom:.5rem;
    border-bottom:4px solid var(--accent); page-break-before:always;
    break-before:page; }
h1.first{ page-break-before:auto; break-before:auto; }
h2{ font-family:'PBSans',sans-serif; font-size:15pt; font-weight:700;
    margin:2em 0 .7em; color:var(--accent); page-break-after:avoid; }
h3{ font-family:'PBSans',sans-serif; font-size:11.5pt; font-weight:700;
    margin:1.5em 0 .5em; page-break-after:avoid; }

/* ---- a move: numbered card ---- */
.move{ position:relative; margin:.85em 0; padding:.62em .95em .62em 3.1em;
       background:#fafafa; border:1px solid #e8e8ec; border-radius:5px;
       page-break-inside:avoid; break-inside:avoid; }
.move .n{ position:absolute; left:.72em; top:.55em;
  font-family:'PBSans',sans-serif; font-size:13pt; font-weight:700;
  color:var(--accent); line-height:1; }
.move .ttl{ font-family:'PBSans',sans-serif; font-weight:700; font-size:11.4pt;
  display:block; margin-bottom:.15em; line-height:1.3; }
.move .body{ font-size:10.6pt; color:#2e2e34; }
.pay{ display:block; margin-top:.4em; padding-top:.35em;
  border-top:1px dotted #dcdce2; font-family:'PBSans',sans-serif;
  font-size:9.3pt; color:var(--pay); font-style:normal; }
.pay::before{ content:"→ "; font-weight:700; }

/* ---- callouts ---- */
blockquote{ margin:1em 0; padding:.75em 1em; background:#f7f0f0;
  border-left:4px solid var(--accent); border-radius:0 4px 4px 0;
  font-size:11pt; page-break-inside:avoid; }
blockquote p{ margin:0; }

/* ---- tables ---- */
table{ border-collapse:collapse; width:100%; margin:1em 0; font-size:10pt;
  page-break-inside:avoid; break-inside:avoid; }
th,td{ border:1px solid #dedee4; padding:6px 9px; text-align:left; }
th{ background:#f0f0f3; font-family:'PBSans',sans-serif; font-weight:700;
    font-size:9.4pt; }
tbody tr:nth-child(even){ background:#fafafb; }
table.wrong td:first-child{ color:var(--stop); font-style:italic; }
table.wrong td:last-child{ color:var(--go); font-weight:600; }

ul,ol{ margin:.5em 0 .9em; padding-left:1.4em; }
li{ margin:.32em 0; }
code{ font-family:'PBMono',monospace; font-size:9.6pt; background:#f1f1f4;
  padding:1px 4px; border-radius:3px; }
pre{ background:#f6f6f8; border:1px solid #e6e6ea; border-left:4px solid var(--muted);
  padding:.8em 1em; border-radius:4px; font-size:9.8pt; line-height:1.5;
  page-break-inside:avoid; }
pre code{ background:none; padding:0; }
hr{ border:0; border-top:1px solid var(--rule); margin:1.7em 0; }

/* ---- cover ---- */
.cover{ page-break-after:always; break-after:page; height:245mm;
  display:flex; flex-direction:column; padding-top:44mm; }
.cover .bar{ width:70px; height:6px; background:var(--accent); margin-bottom:16mm; }
.cover h1{ font-size:52pt; border:0; padding:0; margin:0 0 6mm;
  page-break-before:auto; break-before:auto; line-height:1; }
.cover .sub{ font-family:'PBSans',sans-serif; font-size:15pt; color:var(--muted);
  line-height:1.45; max-width:110mm; margin-bottom:auto; }
.cover .note{ font-family:'PBSans',sans-serif; font-size:10pt; color:var(--muted);
  border-top:1px solid var(--rule); padding-top:5mm; }
.cover .note b{ color:var(--ink); }
"""


def transform(html: str) -> str:
    # Payoff line: "→ *italic*" (what the distillers produced) or "→ **bold**"
    # (what the hand-written pages used). Accept either, and strip a trailing
    # <br> so the payoff always starts its own line.
    html = re.sub(r"(?:<br\s*/?>\s*)?→\s*<(em|strong)>(.*?)</\1>",
                  lambda m: f'<span class="pay">{m.group(2)}</span>',
                  html, flags=re.S)

    # moves: <p><strong>N. Title</strong> body...</p>
    def as_move(m):
        num, title, body = m.group(1), m.group(2), m.group(3)
        return (f'<div class="move"><span class="n">{num}</span>'
                f'<span class="ttl">{title}</span>'
                f'<span class="body">{body}</span></div>')
    html = re.sub(r"<p><strong>(\d+)\.\s*(.*?)</strong>(.*?)</p>", as_move, html, flags=re.S)

    # wrong -> right tables
    def mark(m):
        t = m.group(0)
        return t.replace("<table>", '<table class="wrong">', 1) if "✗" in t or "→" in t[:600] else t
    html = re.sub(r"<table>.*?</table>", mark, html, flags=re.S)
    return html


def build_html(md: str) -> str:
    body = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    body = transform(body)
    body = body.replace("<h1>", '<h1 class="first">', 1)
    cover = """
<div class="cover"><div class="bar"></div>
<h1>The<br>Playbook</h1>
<div class="sub">Every move that raises your band.<br>Nothing else.</div>
<div class="note"><b>Read this one.</b> The 226-page War Book is the reference —
open it only when you want the evidence behind a move. This is what you actually do.</div></div>"""
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>The Playbook</title>"
            f"<style>{font_css()}\n{CSS}</style></head><body>{cover}{body}</body></html>")


def render(html, out):
    f = TMP / "pb.html"
    f.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(f"file://{f}", wait_until="load")
        pg.wait_for_timeout(2000)
        pg.pdf(path=str(out), format="A4", print_background=True,
               margin={"top": "20mm", "bottom": "18mm", "left": "18mm", "right": "18mm"})
        b.close()


def stamp(src, dst):
    pdf = pikepdf.open(str(src))
    W, H = A4
    buf = io.BytesIO()
    c = rl_canvas.Canvas(buf, pagesize=A4)
    for i in range(1, len(pdf.pages) + 1):
        if i > 1:
            c.setFont("Helvetica-Bold", 9)
            c.setFillColor(HexColor("#8c2f39"))
            c.drawCentredString(W / 2, 26, str(i))
            c.setFont("Helvetica", 7.5)
            c.setFillColor(HexColor("#a8a8b0"))
            c.drawRightString(W - 51, 26, "The Playbook")
        c.showPage()
    c.save()
    buf.seek(0)
    ov = pikepdf.open(buf)
    for i, page in enumerate(pdf.pages):
        page.add_overlay(ov.pages[i])
    pdf.save(str(dst), linearize=True)


def main():
    parts = []
    for name in ORDER:
        p = SRCDIR / name
        if not p.is_file():
            print(f"  missing: {name}")
            continue
        parts.append(p.read_text(encoding="utf-8"))
    md = "\n\n".join(parts)
    # strip any citation that leaked through the distillation
    md = re.sub(r"\s*\[src:[^\]]*\]", "", md)
    md = re.sub(r"`\[src:[^\]]*\]`", "", md)

    render(build_html(md), TMP / "raw.pdf")
    stamp(TMP / "raw.pdf", OUT)
    n = len(pikepdf.open(str(OUT)).pages)
    print(f"Wrote {OUT} — {n} pages, {OUT.stat().st_size/1024:.0f} KB, "
          f"{len(md.split()):,} words")
    return 0


if __name__ == "__main__":
    sys.exit(main())
