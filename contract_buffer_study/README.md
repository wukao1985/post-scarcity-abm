# Contract-Buffer Study (RT-04B)

A pre-registered, placebo-controlled test of the hinge argument in the book's Chapter 4:
**does the *employment contract*, not just AI *substitutability*, govern where generative AI
hits employment first?**

The book argues that Stack Overflow collapsed after ChatGPT because it had **no contract**
buffering it, while salaried white-collar work has not yet visibly cratered because contracts
are *delaying* the same force — making exposed professionals **forerunners** for everyone. A
reviewer's rival explanation: SO was simply a **perfectly substitutable special case**. This
study discriminates between the two by holding AI-exposure roughly constant (same occupation)
and varying only the contract buffer.

**Design (the test):** within the same detailed occupation, compare the post-ChatGPT employment
path of **no-contract** workers (unincorporated self-employed) vs **salaried** workers (private
wage/salary), as a function of the occupation's generative-AI exposure. A triple-difference
(Post × Exposure × NoContract) coefficient **β₃ < 0** supports the contract-buffer mechanism;
**β₃ = 0** (with a common negative exposure effect) favours the pure-substitutability rival.

- 🔒 **`DESIGN.md`** — the frozen pre-registration. Hypotheses, class/exposure definitions,
  estimator, placebo, and decision rules were locked **before any post-2022m11 outcome was
  examined**. A null is a pre-committed, publishable outcome (this repo's `so_sdt_study` is a
  pre-registered null done right).
- **`scripts/build_exposure.py`** — builds the occupation→AI-exposure table
  (CPS 2018 census occ → 2010 SOC → Language-Modeling AIOE), committed as
  `exposure_inputs/occ_exposure.csv`.
- **`scripts/build_extract.py`** — pulls CPS basic monthly microdata (NBER `.dta` ≤2023-11;
  Census public-use `.dat` after), collapses to a slim committed cell file `data_cells.csv`
  (occupation × class × age-band × month weighted employment). Validates the Census parser
  against NBER on the overlap (exact match). Raw microdata are never committed.
- **`scripts/analyze.py`** — the frozen analysis: PPML triple-difference, event study, the
  incorporated-self-employed gradient, the 2022-05 placebo, and the robustness battery →
  `RESULTS.md` + `results_summary.json`.
- **`scripts/figures.py`** — figures for `PAPER.md`.
- **`PAPER.md`** — the honest write-up (template: `so_sdt_study/PAPER.md`).

## Data sources (public, no registration)
- CPS basic monthly: NBER `data.nber.org/cps-basic2/dta/` + Census Bureau
  `www2.census.gov/programs-surveys/cps/datasets/`.
- AI exposure: AIOE (Felten, Raj & Seamans) — `AIOE-Data/AIOE`, Language-Modeling variant.
- Crosswalk: Census 2018 occupation code list with 2010↔2018 SOC crosswalk.

## Reproduce
```
python3 scripts/build_exposure.py        # -> exposure_inputs/occ_exposure.csv
python3 scripts/build_extract.py --validate   # NBER vs Census parser check (expect exact)
python3 scripts/build_extract.py         # -> data_cells.csv  (downloads ~a few GB to a cache)
python3 scripts/analyze.py               # -> RESULTS.md, results_summary.json
python3 scripts/figures.py               # -> figures/*.png
```
