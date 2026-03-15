# Codex Review — Iteration 1
**Date:** 2026-03-14  
**Model:** gpt-5.4  
**Mode:** codex review (read-only, no code changes made)

## Raw Verdict
> "The patch introduces several reproducibility and evidence-alignment problems... material enough that the submission package should not be considered correct yet."

## Issues Found (Cloud parsed)

### P1 — Fatal (blocks submission)
**Sweeps 3–6 data is V3, paper claims V4**
- V4 model changes were applied, but only Sweep 1 + 2 were re-run
- Sweeps 3–6 CSVs (virtual_world, collectivism, archetypes, full_grid) are still V3 data
- Paper abstract says "17,050 runs" as if all are V4 — misleading to reviewers
- Fix: Re-run Sweeps 3–6 with V4 model, OR explicitly state which sweeps are V3 vs V4

### P2 — Major (breaks reproducibility)
1. **pytest missing from requirements.txt** — `make test` fails on fresh clone
   Fix: add `pytest>=7.0` to requirements.txt

2. **Pathway C crashes on headless** — sd_model.py calls plt.show() without MPLBACKEND=Agg
   Fix: add `matplotlib.use('Agg')` at top of sd_model.py

3. **Stale ABM reference values in compare_with_abm()** — hardcoded V3 values (sink=0.80)
   but V4 data shows baseline sink=0.629 at post_labor=0.8
   Fix: auto-read reference values from sweep1_results.csv instead of hardcoding

## Key Observation on Review Mode
Codex ran shell commands (read files, ran Python) but made ZERO commits or file changes.
Confirmed: `codex review` is truly read-only. ✅

## Note on Review Format
Codex gave code-quality review (technical issues), not academic peer review.
For academic paper review → need different prompt strategy (see below).

## Next Actions for Claude Code (Iteration 2)
Priority order:
1. Re-run Sweeps 3–6 with V4 model (fixes P1 — most critical)
2. Add pytest to requirements.txt
3. Fix sd_model.py matplotlib backend
4. Fix compare_with_abm() to read values from CSV dynamically
5. Update paper abstract to clarify which sweeps are V3 vs V4 (if re-run not possible)
