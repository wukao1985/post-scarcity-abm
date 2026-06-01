# Build — LaTeX-typeset PDFs

Produces standard book-quality PDFs of *When the Work Is Gone* / 《当工作消失之后》
in English and Chinese from the markdown chapters in `../chapters/` and `../chapters_zh/`.

## Output

After a successful build:

- `../dist/post-labour-meaning-en.pdf`
- `../dist/post-labour-meaning-zh.pdf`

Both are committed to git so the latest PDF is always available without rebuilding.

## How it works

1. `build.sh` concatenates the nine chapter files (`00`–`08`) in order for each
   language, stripping the parallel-language H2 line under each chapter title.
2. Appends a References page (`refs-en.md` / `refs-zh.md`) that prints the full
   bibliography from `references.bib` via `biblatex` (APA style, alphabetical).
3. Runs `pandoc → xelatex → biber → xelatex` to produce the PDF.

Citations: the book's prose stays as essays, with inline source references kept
casual. The formal bibliography lives on the References page at the end —
generated from `references.bib`, which is the BibTeX form of
`meaning_project/evidence_base.md`.

## Install dependencies (one time)

### macOS

```sh
# Install BasicTeX (~100MB, recommended over the 5GB MacTeX)
brew install --cask basictex

# Add TeX binaries to PATH (open a new shell after this, or source profile)
eval "$(/usr/libexec/path_helper)"

# Install LaTeX packages we need on top of BasicTeX
sudo tlmgr update --self
sudo tlmgr install \
    collection-xetex collection-latexrecommended \
    ctex xecjk \
    biblatex biblatex-apa biber \
    titlesec microtype setspace \
    csquotes

# pandoc (if not already)
brew install pandoc
```

### Verify

```sh
pandoc --version | head -1
xelatex --version | head -1
biber --version
```

## Build

```sh
cd meaning_project/book/build
./build.sh
```

Rebuild takes ~15–30 seconds per language on a modern Mac.

## Automatic rebuild

A project-level Stop hook (`.claude/settings.json`) runs `build.sh` at the end
of every Claude Code session that touched any chapter file, so the committed
PDFs stay in sync with prose. To rebuild manually at any time, run `./build.sh`.

## Adding a new citation

1. Add a BibTeX entry to `references.bib`.
2. Either (a) leave the prose in the casual essay register (the entry will
   still appear on the References page via `\nocite{*}`), or (b) cite it
   inline with pandoc syntax `[@cite-key]` and use `--citeproc` instead of
   `--biblatex` in `build.sh`.

Current style is (a): all entries from `references.bib` print on the References
page; prose stays untouched. To change, edit the toggle in `build.sh`.

## Why these choices

- **XeLaTeX** (not pdfLaTeX) for system-font CJK without preprocessing.
- **ctexbook** for the ZH build — handles Chinese chapter headings, line
  breaking, and TOC labels correctly. `fontset=mac` selects Songti SC /
  Heiti SC bundled with macOS.
- **biblatex + biber** (not natbib) so APA formatting is built-in and the bib
  file works without pandoc-citeproc CSL fiddling.
- **6 × 9 inch** trim with conservative margins — standard trade-book size.
- **No chapter numbering in print** (`secnumdepth: 0`) — the prose treats
  chapters as essays; numbers in titles would feel academic.
