#!/usr/bin/env bash
# Stop hook: rebuild book PDFs if chapter files have changed in this working
# tree (uncommitted), so the committed PDFs can stay in sync with prose.
#
# Always exits 0 — never blocks session end. Silent if nothing needs doing.

set -uo pipefail

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
BUILD_DIR="$PROJECT_DIR/meaning_project/book/build"

# Skip if build infrastructure isn't here yet.
[ -x "$BUILD_DIR/build.sh" ] || exit 0

cd "$PROJECT_DIR" || exit 0

# Only act if chapter files are dirty in working tree OR were touched in the
# last commit (HEAD).
CHAPTER_GLOB='meaning_project/book/chapters(_zh)?/[0-9][0-9]_.*\.md'
DIRTY=$(git status --porcelain 2>/dev/null | awk '{print $2}' | grep -E "$CHAPTER_GLOB" || true)
LAST_COMMIT=$(git diff --name-only HEAD~1 HEAD 2>/dev/null | grep -E "$CHAPTER_GLOB" || true)

if [ -z "$DIRTY$LAST_COMMIT" ]; then
  exit 0
fi

# Make sure TeX is on PATH (BasicTeX puts it in /Library/TeX/texbin).
if [ -d /Library/TeX/texbin ]; then
  export PATH="/Library/TeX/texbin:$PATH"
fi

# Quiet skip if dependencies aren't installed yet (user may not have run the
# one-time TeX install). The README has install instructions.
for tool in pandoc xelatex biber; do
  command -v "$tool" >/dev/null 2>&1 || {
    echo "[auto-rebuild-book-pdfs] $tool not installed; skipping. See $BUILD_DIR/README.md" >&2
    exit 0
  }
done

echo "[auto-rebuild-book-pdfs] chapter files changed -> rebuilding PDFs..." >&2
if "$BUILD_DIR/build.sh" >/tmp/book-build.log 2>&1; then
  echo "[auto-rebuild-book-pdfs] OK. PDFs at meaning_project/book/dist/" >&2
else
  echo "[auto-rebuild-book-pdfs] FAILED. See /tmp/book-build.log" >&2
fi

exit 0
