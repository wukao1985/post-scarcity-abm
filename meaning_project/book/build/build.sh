#!/usr/bin/env bash
# Build LaTeX-typeset PDFs of the book in both languages.
#
# Output: meaning_project/book/dist/post-labour-meaning-{en,zh}.pdf
#
# Dependencies: pandoc, xelatex, biber, latexmk (BasicTeX/MacTeX/TexLive).
# See README.md for install instructions.

set -euo pipefail

BUILD_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOOK_DIR="$(cd "$BUILD_DIR/.." && pwd)"
OUT_DIR="$BOOK_DIR/dist"

mkdir -p "$OUT_DIR"

# macOS BasicTeX installs into /Library/TeX/texbin, often missing from PATH in
# non-interactive shells. Prepend if present.
if [ -d /Library/TeX/texbin ] && ! command -v xelatex >/dev/null 2>&1; then
  export PATH="/Library/TeX/texbin:$PATH"
fi

for tool in pandoc xelatex biber latexmk; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "ERROR: $tool not found on PATH." >&2
    echo "See $BUILD_DIR/README.md for install instructions." >&2
    exit 1
  fi
done

build_lang() {
  local lang="$1"
  local chapters_dir="$2"
  local strip_re="$3"
  local out_name="$4"

  local tmp
  tmp="$(mktemp -d)"
  trap 'rm -rf "$tmp"' RETURN

  # references.bib must be in the same dir as the .tex for biber to find it.
  cp "$BUILD_DIR/references.bib" "$tmp/"

  local input="$tmp/book.md"
  : > "$input"

  # Concatenate ordered chapter files, stripping the parallel-language H2 line
  # that lives directly under each chapter's H1.
  local f
  for f in "$chapters_dir"/[0-9][0-9]_*.md; do
    awk -v pat="$strip_re" '
      NR <= 5 && $0 ~ pat { next }
      { print }
    ' "$f" >> "$input"
    printf "\n\n" >> "$input"
  done

  # Append references page.
  cat "$BUILD_DIR/refs-$lang.md" >> "$input"

  echo "[$lang] pandoc -> book.tex"
  pandoc \
    --from=markdown+smart+raw_tex \
    --to=latex \
    --standalone \
    --top-level-division=section \
    --metadata-file="$BUILD_DIR/metadata-$lang.yaml" \
    --resource-path="$BUILD_DIR" \
    --output="$tmp/book.tex" \
    "$input"

  echo "[$lang] latexmk -> $OUT_DIR/$out_name.pdf"
  ( cd "$tmp" && latexmk -xelatex -interaction=nonstopmode \
        -file-line-error book.tex >latexmk.log 2>&1 ) || {
    echo "[$lang] latexmk FAILED. Tail of log:" >&2
    tail -40 "$tmp/latexmk.log" >&2
    return 1
  }

  cp "$tmp/book.pdf" "$OUT_DIR/$out_name.pdf"
  echo "[$lang] done."
}

build_lang en "$BOOK_DIR/chapters"    '^## (第|序章|终章)'              "post-labour-meaning-en"
build_lang zh "$BOOK_DIR/chapters_zh" '^## (Chapter|Prologue|Epilogue)' "post-labour-meaning-zh"

echo "All builds OK. PDFs in $OUT_DIR/"
