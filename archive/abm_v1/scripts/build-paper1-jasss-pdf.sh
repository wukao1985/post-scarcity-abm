#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if ! command -v weasyprint >/dev/null 2>&1; then
  echo "weasyprint is required but not available" >&2
  exit 1
fi

if [[ -x "$repo_root/.venv/bin/python" ]]; then
  python_bin="$repo_root/.venv/bin/python"
elif command -v /opt/homebrew/bin/python3 >/dev/null 2>&1; then
  python_bin="/opt/homebrew/bin/python3"
elif command -v python3 >/dev/null 2>&1; then
  python_bin="$(command -v python3)"
else
  echo "A Python interpreter is required but not available" >&2
  exit 1
fi

"$python_bin" scripts/render_paper1_jasss.py
weasyprint reports/paper_jasss_submission.html reports/paper_jasss_submission.pdf

if [[ ! -s reports/paper_jasss_submission.pdf ]]; then
  echo "PDF build failed: reports/paper_jasss_submission.pdf is missing or empty" >&2
  exit 1
fi

echo "Built reports/paper_jasss_submission.pdf"
