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

# Two documents. The Playbook stays short — it is what you DO. The Writing Bank
# is lookup material and would drown it.
ORDER = ["01-front.md", "02-listening-reading.md", "03-writing.md",
         "04-speaking-language.md", "05-testday.md"]

BANK_ORDER = ["03z-bank-intro.md", "03a-task1-bank.md", "03b-task2-bank.md",
              "03c-grammar-on-demand.md"]
BANK_OUT = ROOT / "exports/THE-WRITING-BANK.pdf"

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


COVER_PLAY = """
<div class="cover"><div class="bar"></div>
<h1>The<br>Playbook</h1>
<div class="sub">Every move that raises your band.<br>Nothing else.</div>
<div class="note"><b>Read this one.</b> Ninety-four moves, ranked by what they are
worth. When you need the actual words for a Writing task, open <b>The Writing
Bank</b>. The 226-page War Book is the evidence behind both — open it only if you
want to know why a move works.</div></div>"""

COVER_BANK = """
<div class="cover"><div class="bar"></div>
<h1>The<br>Writing<br>Bank</h1>
<div class="sub">The words. Organised by the job,<br>not by the chart type.</div>
<div class="note"><b>Do not read this. Look things up in it.</b> Task 1 language,
Task 2 language, and every grammar structure with the one error you personally
make in it. The index on the next page tells you where to go when you are stuck.</div></div>"""

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

/* wrong -> right, inline */
.x{ color:var(--stop); font-weight:700; }
.v{ color:var(--go); font-weight:700; }
.warn{ color:var(--pay); font-weight:700; }

/* language banks: phrase lists set tight and scannable */
.bank li{ margin:.18em 0; font-size:10.6pt; }
table td em{ color:#3a3a42; }
h2+table,h3+table{ margin-top:.6em; }

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

    # colour the wrong/right/warning marks wherever they appear
    html = html.replace("✗", '<span class="x">✗</span>')
    html = html.replace("✓", '<span class="v">✓</span>')
    html = html.replace("⚠", '<span class="warn">⚠</span>')

    # wrong -> right tables
    def mark(m):
        t = m.group(0)
        return t.replace("<table>", '<table class="wrong">', 1) if "✗" in t or "→" in t[:600] else t
    html = re.sub(r"<table>.*?</table>", mark, html, flags=re.S)
    return html


def build_html(md: str, bank=False) -> str:
    body = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    body = transform(body)
    body = body.replace("<h1>", '<h1 class="first">', 1)
    cover = COVER_BANK if bank else COVER_PLAY
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


def stamp(src, dst, label="The Playbook"):
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
            c.drawRightString(W - 51, 26, label)
        c.showPage()
    c.save()
    buf.seek(0)
    ov = pikepdf.open(buf)
    for i, page in enumerate(pdf.pages):
        page.add_overlay(ov.pages[i])
    pdf.save(str(dst), linearize=True)


def main():
    def assemble(names):
        parts = []
        for n in names:
            f = SRCDIR / n
            if f.is_file():
                parts.append(f.read_text(encoding="utf-8"))
            else:
                print(f"  missing: {n}")
        md = "\n\n".join(parts)
        md = re.sub(r"\s*`?\[src:[^\]]*\]`?", "", md)
        # Each ✗ correction on its own line: markdown joins single newlines into
        # one paragraph, which turns a scannable error list into a wall.
        md = re.sub(r"(?m)^(✗ .*?)(?<!  )$", r"\1  ", md)
        return md

    for names, out, bank, label in (
            (ORDER, OUT, False, "THE PLAYBOOK"),
            (BANK_ORDER, BANK_OUT, True, "THE WRITING BANK")):
        md = assemble(names)
        render(build_html(md, bank=bank), TMP / "raw.pdf")
        stamp(TMP / "raw.pdf", out, label.title().replace("The ", "The "))
        n = len(pikepdf.open(str(out)).pages)
        print(f"{label:20} {n:>3} pages  {out.stat().st_size/1024:>5.0f} KB  "
              f"{len(md.split()):>6,} words")
    return 0


if __name__ == "__main__":
    sys.exit(main())
