#!/usr/bin/env bash
# Install the runtime dependencies the bundled Claude Code skills need.
#
#   bash scripts/setup-skills.sh
#
# Safe to re-run. Skills that are pure prose (most of them) need nothing from
# this script; it exists for the ones that ship executable helpers.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REQ="$REPO_ROOT/.claude/skills/requirements.txt"

echo "==> Installing Python dependencies from $REQ"
PIP_FLAGS=()
# Debian-managed system Pythons refuse installs without this flag.
if python3 -c 'import sysconfig,sys; sys.exit(0 if sysconfig.get_config_var("EXT_SUFFIX") else 1)' 2>/dev/null \
   && [ -f /usr/lib/python3/dist-packages/pip/__init__.py ]; then
  PIP_FLAGS+=(--break-system-packages)
fi
# A Debian-packaged PyJWT has no RECORD file and blocks upgrades pulled in by
# anthropic; ignoring it lets pip install its own copy instead of failing.
python3 -m pip install "${PIP_FLAGS[@]}" --ignore-installed PyJWT -r "$REQ"

echo "==> Checking optional system binaries"
for bin in soffice tesseract; do
  if command -v "$bin" >/dev/null 2>&1; then
    echo "    ok       $bin"
  else
    echo "    missing  $bin (optional; some conversion/OCR paths degrade without it)"
  fi
done

echo "==> Verifying imports"
python3 - <<'PY'
import importlib.util, sys
mods = ["docx", "pptx", "openpyxl", "pypdf", "pdfplumber", "reportlab",
        "PIL", "numpy", "imageio", "playwright", "lxml", "defusedxml",
        "anthropic", "mcp", "bs4", "yaml"]
missing = [m for m in mods if importlib.util.find_spec(m) is None]
if missing:
    print("    MISSING:", ", ".join(missing))
    sys.exit(1)
print(f"    all {len(mods)} imports resolve")
PY

echo "==> Done."
