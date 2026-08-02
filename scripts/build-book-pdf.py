#!/usr/bin/env python3
"""Render the War Book as a designed study edition.

    python3 scripts/build-book-pdf.py              # the 219-page book (screen)
    python3 scripts/build-book-pdf.py --companions # appendices + cheat sheets
    python3 scripts/build-book-pdf.py --print      # print-optimised companions

The visual language is derived from the book's own label vocabulary — "The
trap.", "Technique.", "Rules.", "Band-6 mistake." and so on all recur dozens of
times — so each becomes a consistent, recognisable block. Nothing is removed from
the source markdown; this is presentation only.

Three passes: lay out, find page numbers, re-render with a real contents page.
Running headers and page numbers are stamped afterwards with reportlab, because
Chromium's header template cannot vary by chapter.
"""
import base64
import io
import pathlib
import re
import sys

import markdown
import pikepdf
import pypdf
from playwright.sync_api import sync_playwright
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as rl_canvas

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOOKDIR = ROOT / "ielts-book/book"
SRC = BOOKDIR / "IELTS-Academic-War-Book.md"
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

# What each chapter is worth — shown on its opener page.
CHAPTER_META = {
    1: ("The whole test", "Where your two missing half-bands actually are"),
    2: ("40 marks, objective", "Band 6 to 7 is seven marks. From the top of 6.5, one."),
    3: ("40 marks, objective", "Band 6.5 to 7 is three marks. Every tip here is priced in marks."),
    4: ("One third of Writing", "The overview and the grouping decide Task Achievement."),
    5: ("Two thirds of Writing", "Worth double Task 1 — and Writing is your weakest paper."),
    6: ("A quarter of your overall", "Four criteria, equally weighted, one of them free."),
    7: ("A quarter of Writing and of Speaking", "Precision beats rarity — and the scale says so."),
    8: ("A quarter of Writing and of Speaking", "Articles separate band 6 from band 7. This is your chapter."),
    9: ("Everything above, scheduled", "90 minutes a day, working backwards from your test date."),
}

# The book's own label vocabulary -> visual role.
LABEL_MAP = [
    (r"(?:The )?[Tt]raps?\.", "trap"),
    (r"(?:The )?[Bb]and-6 (?:mistake|failure mode)[.:]", "trap"),
    (r"[Bb]and-6 mistake — L1-specific\.", "trap"),
    (r"(?:The )?[Tt]echniques?\.", "do"),
    (r"Procedure:", "do"),
    (r"Do instead:", "do"),
    (r"[Rr]ules?\.", "rule"),
    (r"Order:", "rule"),
    (r"Assessed:", "rule"),
    (r"How it is scored\.", "rule"),
    (r"(?:Worked|Mini|Original)[- ]examples?\.", "eg"),
    (r"Worked skeleton\.", "eg"),
    (r"When to use\.", "when"),
    (r"When it backfires\.", "when"),
    (r"Appearance\.", "id"),
    (r"Looks like\.", "id"),
    (r"Recognise it by:", "id"),
    (r"Form\.", "id"),
    (r"What it is(?:, in plain words)?\.", "id"),
]


def font_css():
    out = []
    for family, fname, weight, style in FONT_FACES:
        b64 = base64.b64encode((FONTS / fname).read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{family}';font-weight:{weight};"
                   f"font-style:{style};src:url(data:font/ttf;base64,{b64}) "
                   f"format('truetype');}}")
    return "\n".join(out)


BASE_CSS = """
:root{
  --ink:#1c1c1e; --muted:#63636a; --faint:#9a9aa2; --rule:#dcdce1;
  --accent:#8c2f39;
  --trap:#a02c2c;  --trap-bg:#fdf1f0;
  --do:#1d6b4a;    --do-bg:#eef7f2;
  --rule2:#2c5aa0; --rule-bg:#eef3fb;
  --eg:#5b5b64;    --eg-bg:#f5f5f7;
  --when:#8a5a00;  --when-bg:#fdf6e8;
  --id:#6a3d8f;    --id-bg:#f6f1fa;
  --l1:#0f6f7a;    --l1-bg:#ecf6f7;
}
@page{ size:A4; margin:22mm 19mm 20mm 19mm; }
html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
body{
  font-family:'BookSerif',Georgia,serif;
  font-size:10.3pt; line-height:1.6; color:var(--ink); text-align:left;
  hyphens:auto; -webkit-hyphens:auto;
  font-variant-ligatures:none;
  font-feature-settings:"liga" 0,"clig" 0;
}
p{ margin:0 0 .7em; orphans:3; widows:3; }
strong{ font-weight:700; }
a{ color:var(--accent); text-decoration:none; }
a.xref{ border-bottom:.5px dotted var(--accent); }

h1,h2,h3,h4{ font-family:'BookSans',system-ui,sans-serif; line-height:1.22;
  page-break-after:avoid; break-after:avoid; }
h1{ font-size:24pt; font-weight:700; letter-spacing:-.015em; margin:0 0 1.2rem;
    padding-bottom:.6rem; border-bottom:3px solid var(--accent);
    page-break-before:always; break-before:page; }
h1.no-break{ page-break-before:auto; break-before:auto; }
h2{ font-size:14pt; font-weight:700; margin:1.9em 0 .5em; padding-bottom:.25rem;
    border-bottom:1px solid var(--rule); }
h3{ font-size:11.4pt; font-weight:700; margin:1.5em 0 .4em; color:#2c2c30; }
h4{ font-size:9.6pt; font-weight:700; margin:1.2em 0 .3em; color:var(--muted);
    text-transform:uppercase; letter-spacing:.06em; }

/* source notes: all 634 kept, but out of the reading path */
.src{ font-family:'BookSans',sans-serif; font-size:6.8pt; color:#adadb4;
      line-height:1.25; }
.src::before{ content:"\\00a0"; }

/* ---------- the visual language ---------- */
.cal{ margin:.95em 0; padding:.55em .9em .55em .85em; border-left:3px solid;
      border-radius:0 3px 3px 0; page-break-inside:avoid; break-inside:avoid; }
.cal .lbl{ font-family:'BookSans',sans-serif; font-size:7.6pt; font-weight:700;
           letter-spacing:.07em; text-transform:uppercase; display:block;
           margin-bottom:.28em; }
.cal-trap{ background:var(--trap-bg); border-color:var(--trap); }
.cal-trap .lbl{ color:var(--trap); }
.cal-do{ background:var(--do-bg); border-color:var(--do); }
.cal-do .lbl{ color:var(--do); }
.cal-rule{ background:var(--rule-bg); border-color:var(--rule2); }
.cal-rule .lbl{ color:var(--rule2); }
.cal-eg{ background:var(--eg-bg); border-color:var(--eg); }
.cal-eg .lbl{ color:var(--eg); }
.cal-when{ background:var(--when-bg); border-color:var(--when); }
.cal-when .lbl{ color:var(--when); }
.cal-id{ background:var(--id-bg); border-color:var(--id); }
.cal-id .lbl{ color:var(--id); }

/* myths keep their own identity */
p.myth{ margin:1.1em 0 .8em; padding:.55em .9em; background:var(--when-bg);
        border-left:3px solid var(--when); border-radius:0 3px 3px 0;
        page-break-inside:avoid; break-inside:avoid; }
p.lead{ margin-top:1.1em; }

/* ---------- 60-second summary as a card ---------- */
.summary{
  background:#fbfaf7; border:1px solid #e6e2d8; border-top:4px solid var(--accent);
  border-radius:4px; padding:1em 1.1em .85em; margin:0 0 1.6em;
}
.summary h2{ border:0; margin:0 0 .5em; font-size:12.5pt; padding:0; }
.summary p{ font-size:9.9pt; }
.summary p:last-child{ margin-bottom:0; }

/* ---------- L1 sections: your highest-value content ---------- */
.l1zone{ border-left:4px solid var(--l1); background:var(--l1-bg);
         padding:.15em 1em .3em; margin:1.4em 0; border-radius:0 4px 4px 0; }
.l1zone h2{ border-bottom-color:#bfe0e3; color:var(--l1); }
.l1zone::before{
  content:"YOUR L1 — ARABIC / FRENCH"; display:block;
  font-family:'BookSans',sans-serif; font-size:7.2pt; font-weight:700;
  letter-spacing:.1em; color:var(--l1); padding-top:.7em;
}

/* ---------- tables ---------- */
/* Tables break across pages rather than jumping whole — avoiding the break
   left large blank gaps at the foot of pages. The header row repeats. */
table{ border-collapse:collapse; width:100%; margin:.9em 0; font-size:8.8pt;
       line-height:1.4; page-break-inside:auto; break-inside:auto; }
thead{ display:table-header-group; }
tr{ page-break-inside:avoid; break-inside:avoid; }
th,td{ border:1px solid #dedee3; padding:5px 7px; text-align:left; vertical-align:top; }
th{ background:#eeeef1; font-family:'BookSans',sans-serif; font-weight:700; font-size:8.3pt; }
tbody tr:nth-child(even){ background:#fafafb; }
td .src,th .src{ font-size:6.4pt; }
/* band tables: make the band column unmissable */
table.bands td:first-child,table.bands th:first-child{
  font-family:'BookSans',sans-serif; font-weight:700; text-align:center;
  width:3.2em; background:#f2eef0; color:var(--accent); }

blockquote{ margin:.9em 0; padding:.6em .95em; background:#f7f0f0;
  border-left:3px solid var(--accent); border-radius:0 3px 3px 0;
  page-break-inside:avoid; break-inside:avoid; }
blockquote p{ margin:0 0 .45em; } blockquote p:last-child{ margin-bottom:0; }

ul,ol{ margin:.5em 0 .8em; padding-left:1.35em; }
li{ margin:.22em 0; }
code{ font-family:'BookMono',monospace; font-size:8.3pt; background:#f1f1f4;
      padding:.5px 3px; border-radius:2px; }
pre{ background:#f7f7f9; border:1px solid #e4e4e8; border-left:3px solid var(--muted);
     padding:.6em .8em; border-radius:3px; font-size:8.2pt; line-height:1.45;
     page-break-inside:avoid; break-inside:avoid; }
pre code{ background:none; padding:0; }
hr{ border:0; border-top:1px solid var(--rule); margin:1.5em 0; }

/* ---------- printable checklists ---------- */
.check{ list-style:none; padding-left:0; }
.check li{ margin:.42em 0; padding-left:1.7em; position:relative; line-height:1.5; }
.check li::before{ content:""; position:absolute; left:0; top:.16em;
  width:11px; height:11px; border:1.3px solid #8c8c95; border-radius:2px; }

/* ---------- chapter openers ---------- */
.opener{ page-break-before:always; break-before:page; padding-top:14mm; }
.opener .kicker{ font-family:'BookSans',sans-serif; font-size:8pt; font-weight:700;
  letter-spacing:.16em; text-transform:uppercase; color:var(--accent); }
.opener .no{ font-family:'BookSans',sans-serif; font-size:62pt; font-weight:700;
  line-height:.9; color:#eceaea; letter-spacing:-.04em; margin:.1em 0 -.32em; }
.opener h1{ page-break-before:auto; break-before:auto; border:0; padding:0;
  margin:0 0 .6rem; font-size:26pt; }
.opener .worth{ display:flex; gap:1.4em; border-top:2px solid var(--accent);
  border-bottom:1px solid var(--rule); padding:.6em 0; margin:.9em 0 1.4em;
  font-family:'BookSans',sans-serif; font-size:8.6pt; }
.opener .worth div{ flex:1; }
.opener .worth .k{ display:block; font-size:7pt; letter-spacing:.1em;
  text-transform:uppercase; color:var(--faint); margin-bottom:.25em; }
.opener .worth .v{ color:var(--ink); font-weight:700; }

/* ---------- cover / contents ---------- */
.cover{ page-break-after:always; break-after:page; height:245mm;
  display:flex; flex-direction:column; padding-top:26mm; }
.cover .rule{ width:64px; height:5px; background:var(--accent); margin-bottom:18mm; }
.cover h1{ font-size:40pt; line-height:1.06; border:0; margin:0 0 8mm; padding:0;
  page-break-before:auto; break-before:auto; letter-spacing:-.028em; }
.cover .sub{ font-family:'BookSans',sans-serif; font-size:12pt; line-height:1.5;
  color:var(--muted); max-width:112mm; margin-bottom:auto; }
.cover .key{ font-family:'BookSans',sans-serif; font-size:8.2pt; color:var(--muted);
  border-top:1px solid var(--rule); padding-top:4mm; margin-bottom:6mm;
  display:flex; flex-wrap:wrap; gap:.55em 1.1em; }
.cover .key i{ font-style:normal; display:inline-flex; align-items:center; gap:.35em; }
.cover .key b{ width:9px; height:9px; border-radius:2px; display:inline-block; }
.cover .meta{ font-family:'BookSans',sans-serif; font-size:8.6pt; color:var(--faint); }
.cover .meta strong{ color:var(--ink); }

.toc{ page-break-after:always; break-after:page; }
.toc h1{ page-break-before:auto; break-before:auto; }
.toc-row{ display:flex; align-items:baseline; gap:.5em; margin:.32em 0;
  font-size:9.9pt; break-inside:avoid; }
.toc-row .t{ font-family:'BookSans',sans-serif; }
.toc-row.ch{ margin-top:1em; font-weight:700; font-size:10.8pt; }
.toc-row.ch .num{ color:var(--accent); margin-right:.2em; }
.toc-row.sec{ padding-left:1.5em; font-size:9pt; color:#3c3c42; }
.toc-row .dots{ flex:1; border-bottom:1px dotted #c8c8ce; transform:translateY(-.22em); }
.toc-row .pg{ font-family:'BookSans',sans-serif; font-size:8.8pt; color:var(--muted);
  font-variant-numeric:tabular-nums; }
.toc-note{ font-size:8.8pt; color:var(--muted); margin-top:1.5em;
  border-top:1px solid var(--rule); padding-top:.7em; }

h2+p,h3+p{ page-break-before:avoid; }
"""

# Print edition: ink-cheap, greyscale-safe, room to write.
PRINT_CSS = """
.cal,p.myth,blockquote,.summary,.l1zone{ background:#fff !important; }
.cal,p.myth{ border-left-width:3px; border-top:1px solid #d5d5da;
  border-right:1px solid #d5d5da; border-bottom:1px solid #d5d5da; }
.summary{ border:1.5px solid #444 !important; border-top-width:4px !important; }
.l1zone{ border:1.5px dashed var(--l1) !important; border-left-width:4px !important; }
tbody tr:nth-child(even){ background:#f4f4f5; }
.check li{ padding-left:2.1em; margin:.62em 0; }
.check li::before{ width:14px; height:14px; border-width:1.6px; border-color:#333; }
body{ font-size:10.6pt; }
"""


def transform_html(html: str) -> str:
    """Apply the visual language. Removes nothing."""
    # source notes recede
    html = re.sub(r"<code>(\[src:.*?\])</code>",
                  lambda m: f'<span class="src">{m.group(1)}</span>', html, flags=re.S)
    html = re.sub(r"(?<!>)(\[src:[^\[\]]*?\])",
                  lambda m: f'<span class="src">{m.group(1)}</span>', html, flags=re.S)

    # labelled paragraphs -> callouts, using the book's own vocabulary
    for pattern, role in LABEL_MAP:
        html = re.sub(
            rf"<p><strong>({pattern})</strong>",
            lambda m, r=role: (f'<p class="cal cal-{r}">'
                               f'<span class="lbl">{re.sub(r"[.:]$", "", m.group(1))}</span>'),
            html)

    # myths: a bold quotation opening a paragraph
    html = re.sub(r'<p><strong>(&quot;|"|“)',
                  lambda m: f'<p class="myth"><strong>{m.group(1)}', html)
    # any other bold-opening paragraph gets air
    html = re.sub(r'<p><strong>(?!(&quot;|"|“))', '<p class="lead"><strong>', html)

    # band tables
    def mark_bands(m):
        tbl = m.group(0)
        head = tbl[:400]
        if re.search(r"<th[^>]*>\s*(Band|band)\s*</th>", head) or \
           re.search(r"<td[^>]*>\s*\**(9|8\+?|7|6|5)\**\s*</td>", tbl):
            return tbl.replace("<table>", '<table class="bands">', 1)
        return tbl
    html = re.sub(r"<table>.*?</table>", mark_bands, html, flags=re.S)

    # 60-second summary -> card (up to the following <hr> or <h2>)
    html = re.sub(r"(<h2>60-second summary</h2>)(.*?)(?=<h2|<hr)",
                  lambda m: f'<div class="summary">{m.group(1)}{m.group(2)}</div>',
                  html, flags=re.S)

    # L1 alert sections -> highlighted zone
    html = re.sub(r"(<h2>L1 alert[^<]*</h2>)(.*?)(?=<h2|<hr\s*/?>|<h1)",
                  lambda m: f'<div class="l1zone">{m.group(1)}{m.group(2)}</div>',
                  html, flags=re.S)

    # checkbox lists
    html = html.replace("<li>[ ] ", '<li>').replace("<li>[x] ", '<li>')
    html = re.sub(r"<ul>\s*(<li>(?:(?!</ul>).)*?)</ul>",
                  lambda m: (f'<ul class="check">{m.group(1)}</ul>'
                             if "[ ]" in m.group(0) or "☐" in m.group(0) else m.group(0)),
                  html, flags=re.S)

    # clickable cross-references
    html = re.sub(r"\b([Cc]hapter) (\d)\b(?![^<]*</a>)",
                  lambda m: f'<a class="xref" href="#chapter-{m.group(2)}">'
                            f'{m.group(1)} {m.group(2)}</a>', html)
    return html


def build_openers(md: str) -> str:
    """Turn each '# Chapter N — Title' into a designed opener."""
    def rep(m):
        n, title = int(m.group(1)), m.group(2).strip()
        worth, line = CHAPTER_META.get(n, ("", ""))
        words = 0
        seg = md.split(m.group(0), 1)
        if len(seg) > 1:
            nxt = re.search(r"^# Chapter ", seg[1], flags=re.M)
            words = len((seg[1][:nxt.start()] if nxt else seg[1]).split())
        mins = max(1, round(words / 200))
        return (
            f'<div class="opener">'
            f'<div class="kicker">Chapter {n}</div>'
            f'<div class="no">{n}</div>'
            f'<h1 class="no-break" id="chapter-{n}">{title}</h1>'
            f'<div class="worth">'
            f'<div><span class="k">What it is worth</span><span class="v">{worth}</span></div>'
            f'<div><span class="k">Why it matters</span><span class="v">{line}</span></div>'
            f'<div><span class="k">Full read</span><span class="v">~{mins} min</span></div>'
            f'</div></div>'
        )
    return re.sub(r"^# Chapter (\d+) — (.+)$", rep, md, flags=re.M)


def build_html(body_md: str, toc_html: str, print_mode=False, cover=True) -> str:
    body = markdown.markdown(
        body_md, extensions=["tables", "fenced_code", "attr_list", "sane_lists", "md_in_html"])
    body = transform_html(body)
    css = BASE_CSS + (PRINT_CSS if print_mode else "")
    cov = ""
    if cover:
        keys = [("--trap", "Trap / band-6 mistake"), ("--do", "Technique"),
                ("--rule2", "Official rule"), ("--eg", "Worked example"),
                ("--when", "Judgement / myth"), ("--id", "How to recognise it"),
                ("--l1", "Your Arabic / French")]
        chips = "".join(f'<i><b style="background:var({v})"></b>{k}</i>' for v, k in keys)
        cov = f"""
<div class="cover"><div class="rule"></div>
<h1>The IELTS<br>Academic<br>War Book</h1>
<div class="sub">A complete preparation system for band 7.0 — built for one
reader, and verified line by line against official sources.</div>
<div class="key"><span style="width:100%;font-weight:700;color:#1c1c1e">How to read the blocks</span>{chips}</div>
<div class="meta"><strong>Verified 31 July 2026.</strong> Nine research passes ·
six independent adversarial audits · every claim traced to an official source ·
nothing unverified in the text.</div></div>"""
    return (f"<!doctype html><html><head><meta charset='utf-8'>"
            f"<title>The IELTS Academic War Book</title>"
            f"<style>{font_css()}\n{css}</style></head><body>"
            f"{cov}{toc_html}{body}</body></html>")


def render(html: str, out: pathlib.Path, name="book"):
    f = TMP / f"{name}.html"
    f.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(f"file://{f}", wait_until="load")
        pg.wait_for_timeout(2500)
        pg.pdf(path=str(out), format="A4", print_background=True,
               margin={"top": "22mm", "bottom": "20mm", "left": "19mm", "right": "19mm"})
        b.close()


def norm(s): return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def find_pages(pdf_path, headings):
    """Locate each heading's page. Chapter openers print only the title, not the
    'Chapter N —' prefix, so match on the title alone for those.

    The contents page lists every heading too, so searching from page 1 matches
    them all there and collapses the map. Start after the contents instead — it
    ends with the distinctive 'Short of time?' note.
    """
    reader = pypdf.PdfReader(str(pdf_path))
    pages = [norm(p.extract_text() or "") for p in reader.pages]
    start = 0
    for i, txt in enumerate(pages[:12]):
        if "short of time" in txt:
            start = i + 1
    found, cur = {}, start
    for key, text in headings:
        m = re.match(r"Chapter \d+\s*[—-]\s*(.+)", text)
        probe = norm(m.group(1) if m else text)[:55]
        if not probe:
            continue
        for i in range(cur, len(pages)):
            if probe in pages[i]:
                found[key], cur = i + 1, i
                break
    return found, len(reader.pages)


def stamp_and_bookmark(src: pathlib.Path, dst: pathlib.Path, chapter_at: dict,
                       headings, pages, skip=2):
    """Running header + page number, then the outline.

    Uses pikepdf, not pypdf. pypdf's merge_page deep-copies the embedded font
    resources onto every page: it turned a 3.7 MB book into 82 MB. pikepdf's
    add_overlay shares them and costs 0.2 MB.
    """
    pdf = pikepdf.open(str(src))
    n_pages = len(pdf.pages)
    W, H = A4
    starts = sorted(chapter_at.items())

    buf = io.BytesIO()
    c = rl_canvas.Canvas(buf, pagesize=A4)
    for i in range(1, n_pages + 1):
        if i > skip:
            title = ""
            for pg0, name in starts:
                if i >= pg0:
                    title = name
            c.setStrokeColor(HexColor("#e4e4e8"))
            c.setLineWidth(.5)
            c.line(54, H - 42, W - 54, H - 42)
            c.setFont("Helvetica", 7.2)
            c.setFillColor(HexColor("#9a9aa2"))
            if title:
                c.drawString(54, H - 37, title[:76])
            c.drawRightString(W - 54, H - 37, "The IELTS Academic War Book")
            c.setFont("Helvetica-Bold", 8.6)
            c.setFillColor(HexColor("#63636a"))
            c.drawCentredString(W / 2, 32, str(i))
        c.showPage()
    c.save()
    buf.seek(0)

    overlay = pikepdf.open(buf)
    for i, page in enumerate(pdf.pages):
        page.add_overlay(overlay.pages[i])

    n_marks = 0
    with pdf.open_outline() as ol:
        parent = None
        for key, (lvl, text) in headings:
            pg = pages.get(key)
            if pg is None:
                continue
            item = pikepdf.OutlineItem(text, pg - 1)
            if lvl == 1:
                ol.root.append(item)
                parent = item
            elif parent is not None:
                parent.children.append(item)
            else:
                ol.root.append(item)
            n_marks += 1
    pdf.Root.PageMode = pikepdf.Name.UseOutlines
    pdf.save(str(dst), linearize=True)
    return n_marks


COMPANIONS = [
    ("CHEAT-SHEETS.md", "CHEAT-SHEETS", "Cheat Sheets"),
    ("appendix-C-error-card.md", "error-card", "Error Card"),
    ("appendix-D-pre-test-checklist.md", "pre-test-checklist", "Pre-test Checklist"),
    ("appendix-A-band-descriptors.md", "appendix-A-band-descriptors", "Band Descriptors"),
    ("appendix-B-question-type-index.md", "appendix-B-question-index", "Question-Type Index"),
    ("appendix-E-sources.md", "appendix-E-sources", "Sources Consulted"),
]
PRINT_SET = {"CHEAT-SHEETS", "error-card", "pre-test-checklist"}


def do_companions(print_mode=False):
    label = "print edition" if print_mode else "screen edition"
    print(f"companions ({label}):")
    for src, stem, title in COMPANIONS:
        if print_mode and stem not in PRINT_SET:
            continue
        md = (BOOKDIR / src).read_text(encoding="utf-8")
        html = build_html(md, "", print_mode=print_mode, cover=False)
        html = html.replace("<h1>", "<h1 class='no-break'>", 1)
        out = ROOT / "exports" / (f"{stem}-PRINT.pdf" if print_mode else f"{stem}.pdf")
        render(html, out, stem)
        print(f"  {out.name:40} {len(pypdf.PdfReader(str(out)).pages):>3} pp")


def main():
    if "--print" in sys.argv:
        return do_companions(print_mode=True)
    if "--companions" in sys.argv:
        return do_companions(print_mode=False)

    md = SRC.read_text(encoding="utf-8")
    md = re.sub(r"\n## Contents\n.*?(?=\n---\n)", "\n", md, count=1, flags=re.S)
    md = re.sub(r'<a id="chapter-\d"></a>\n?', "", md)   # openers carry the ids now

    headings = []
    for m in re.finditer(r"^(#{1,2}) (.+)$", md, flags=re.M):
        headings.append((f"{len(m.group(1))}:{m.start()}",
                         (len(m.group(1)), re.sub(r"[*`]", "", m.group(2)).strip())))
    flat = [(k, v[1]) for k, v in headings]
    md_open = build_openers(md)

    print("pass 1 — locating headings…")
    render(build_html(md_open, "<div class='toc'></div>"), TMP / "p1.pdf")
    pages, total = find_pages(TMP / "p1.pdf", flat)
    print(f"        {total} pp, {len(pages)}/{len(flat)} located")

    rows = ["<div class='toc'><h1 class='no-break'>Contents</h1>"]
    for key, (lvl, text) in headings:
        pg = pages.get(key)
        if pg is None or text.lower().startswith("contents"):
            continue
        if lvl == 1:
            m = re.match(r"Chapter (\d+)\s*[—-]\s*(.+)", text)
            lab = (f"<span class='num'>{m.group(1)}</span><span class='t'>{m.group(2)}</span>"
                   if m else f"<span class='t'>{text}</span>")
            rows.append(f"<div class='toc-row ch'>{lab}<span class='dots'></span>"
                        f"<span class='pg'>{pg}</span></div>")
        else:
            rows.append(f"<div class='toc-row sec'><span class='t'>{text}</span>"
                        f"<span class='dots'></span><span class='pg'>{pg}</span></div>")
    rows.append("<div class='toc-note'><strong>Short of time?</strong> Every chapter "
                "opens with a <em>60-second summary</em> in a cream box. On a busy day "
                "that box is the chapter — the nine of them take about fifteen minutes "
                "and carry most of what moves a band. Coloured blocks are explained on "
                "the cover.</div></div>")

    print("pass 2 — rendering with contents…")
    render(build_html(md_open, "\n".join(rows)), TMP / "p2.pdf")
    pages2, total2 = find_pages(TMP / "p2.pdf", flat)
    print(f"        {total2} pp, {len(pages2)}/{len(flat)} located")

    chapter_at = {}
    for key, (lvl, text) in headings:
        m = re.match(r"Chapter (\d+)\s*[—-]\s*(.+)", text)
        if lvl == 1 and m and key in pages2:
            chapter_at[pages2[key]] = f"{m.group(1)} · {m.group(2)}"

    if len(chapter_at) != 9:
        print(f"        WARNING: {len(chapter_at)} chapter starts mapped, expected 9")
    n_marks = stamp_and_bookmark(TMP / "p2.pdf", OUT, chapter_at, headings, pages2)
    print(f"\nWrote {OUT} — {total2} pages, "
          f"{OUT.stat().st_size / 1048576:.1f} MB, {n_marks} bookmarks, "
          f"{len(chapter_at)} chapters with running headers")


if __name__ == "__main__":
    sys.exit(main())
