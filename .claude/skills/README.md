# Bundled Claude Code skills

60 skills, extracted from `claudeskills.zip` and installed as project-level
skills. Claude Code picks up everything under `.claude/skills/<name>/SKILL.md`
automatically when a session starts in this repo.

## Setup

Most skills are prose only and need nothing. The ones that ship executable
helpers need Python packages:

```bash
bash scripts/setup-skills.sh
```

Optional system binaries: `soffice` (LibreOffice — document conversion and
thumbnails) and `tesseract` (OCR for scanned PDFs). Both are already present in
the Claude Code web container; install via your package manager elsewhere.

## Verification status

All 60 skills were confirmed to load by enumerating the skills the Claude Code
runtime actually registers — the list matched the 60 directories exactly, with
none dropped.

Beyond loading, the skills carrying real executable payloads were exercised
end-to-end:

| Skill | Check |
|---|---|
| `docx` | create → `office/unpack.py` → `office/pack.py` → re-read, text preserved |
| `pptx` | create → unpack → pack round-trip; `markitdown` text extraction |
| `xlsx` | workbook create/read via openpyxl |
| `pdf` | reportlab create → pypdf + pdfplumber read; pdf2image + tesseract OCR; form-field scripts |
| `canvas-design` | 54 bundled TTFs (27 OFL licenses) load and render via Pillow |
| `webapp-testing` | `with_server.py` boots a server and drives real Chromium to a passing assertion |
| `web-artifacts-builder` | `init-artifact.sh` scaffolds, `bundle-artifact.sh` produces a 248 KB `bundle.html` that renders in Chromium |
| `mcp-builder` | `connections.py` / `evaluation.py` import cleanly |
| `slack-gif-creator` | pillow / imageio / numpy / imageio-ffmpeg present |
| `skill-creator` | entry points run as `python3 -m scripts.<name>` |

All 72 Python files compile, all 11 shell scripts parse, and no script has an
unresolved import.

## Fixes applied

Four defects were found and fixed rather than left in place:

1. **`web-artifacts-builder/scripts/bundle-artifact.sh`** — bundling failed
   outright. `init-artifact.sh` scaffolds a Vite project, and Vite serves
   `public/` from the site root, so `index.html` refers to `/favicon.svg`.
   Parcel resolves a leading `/` against the project root instead and aborted
   with `Failed to resolve '/favicon.svg'`. The script now builds from a
   temporary entry point with those references rewritten to `./public/...`.
2. **`mcp-builder/scripts/requirements.txt`** — pinned `mcp>=1.1.0,<2.0.0`. The
   unpinned range resolved to mcp 2.0, which renamed
   `streamablehttp_client` to `streamable_http_client`, so `connections.py`
   raised `ImportError` on any fresh install.
3. **`pdf/scripts/convert_pdf_to_images.py`** — added `os.makedirs(...,
   exist_ok=True)`. The script accepts an output directory but never created
   it, so it crashed with `FileNotFoundError` unless the directory already
   existed.
4. **`playwright` pin** — `requirements.txt` pins `playwright==1.56.0` to match
   the Chromium revision (1194) already installed at `PLAYWRIGHT_BROWSERS_PATH`.
   Newer Playwright expects revision 1228 and `chromium.launch()` fails with a
   "run playwright install" error.

## Known caveats

These are upstream characteristics, left as-is deliberately:

- **Two frontmatter conventions.** 31 skills (the "superpowers" set —
  `writing-plans`, `systematic-debugging`, `test-driven-development-tdd`, …)
  use `name: Title Case` plus `when_to_use:`, `version:`, and `languages:`
  keys. `skill-creator/scripts/quick_validate.py` rejects these as unexpected
  keys, but the Claude Code runtime keys skills off the **directory name** and
  ignores the extra fields — all 31 load and are invocable. Left unchanged to
  stay aligned with upstream.
- **`claude-api` description is 1068 characters**, over the 1024 limit the
  Skills API enforces. Claude Code does not enforce it, so the skill works
  here; it would need trimming before uploading via the Skills API.
- **The 10 firecrawl skills need external setup** — the `firecrawl` CLI
  (`npx -y firecrawl-cli init`) plus a Firecrawl API key. Not installed here,
  since authentication is yours to provide.
- **`pdf/scripts/check_fillable_fields.py`** raises `IndexError` instead of
  printing usage when run with no arguments. It works correctly with a file
  argument; the other pdf scripts print usage.
- **`web-artifacts-builder` demo page** references `/icons.svg` from
  `src/App.tsx`. Those icons 404 in the bundled output, but Step 2 of the skill
  has you replace `App.tsx` with your own artifact, so the scaffold's demo
  content is throwaway.
