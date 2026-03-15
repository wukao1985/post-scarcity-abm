# Reproduction & Submission Readiness Checklist

Status of each item for journal submission (JASSS target).

## Repository Infrastructure

- [x] `requirements.txt` exists with pinned versions
- [x] `REPRODUCE.md` has exact commands for all sweeps
- [x] `Makefile` with sweep and figure targets
- [x] `.venv` excluded from git (in `.gitignore`)
- [x] Tests pass (`python -m pytest tests/ -v` — 14/14)

## README & Scope

- [x] README scope matches actual completion status
- [x] README has Quick Start block with copy-paste commands
- [x] README explicitly states "model findings" not empirical claims
- [x] README includes honest Current Status section
- [x] Pathway B/C described as planned/initial, not complete
- [x] Includes sentence: "mature ABM research prototype with planned triangulation extensions"

## Code & Data

- [x] Every sweep has a runner function in `runner.py`
- [x] Every sweep output saved to `data/simulation/sweep*.csv`
- [x] Seed-based reproducibility (`np.random.seed(seed)` per run)
- [x] Agent profiles documented (15% resilient, 55% balanced, 30% vulnerable)
- [x] Network structure documented (Watts-Strogatz k=6, p=0.1)

## Paper & Documentation

- [x] Paper draft exists (`reports/paper_draft.md`)
- [x] Abstract does not claim forecasting or prediction
- [x] Limitations section is honest and detailed
- [x] Methods appendix with parameter justification categories (`reports/methods_appendix.md`)
- [x] Paper-to-repo map exists (`docs/paper_to_repo_map.md`)
- [x] V4 validation documented (`reports/v4_validation.md`)
- [x] Historical validation protocol (`reports/historical_validation.md`)

## Figures

- [x] Every figure maps to a generation script (see `docs/paper_to_repo_map.md`)
- [x] Figures saved to `reports/figures/`
- [x] Pathway C comparison figure generated

## Statistical Rigor

- [x] Monte Carlo run counts explicitly stated (50-150 per parameter point)
- [x] Contagion parameters published (contagion_strength=0.5)
- [x] Cohen's d reported and discussed (V4: ~9-12, improved from V3: 8-48)
- [ ] Sensitivity analysis: ±20% on top parameters — placeholder in methods appendix, not yet run
- [ ] Bimodality formally checked and reported — not yet tested
- [ ] Sobol sensitivity indices computed — planned, not implemented

## Model Quality

- [x] Noise σ increased to 0.08 (V4, from 0.02)
- [x] Gradual speed artifact fixed (runner computes target/80)
- [x] Aggressor thresholds recalibrated (improved but still underrepresented at ~2-3%)
- [ ] Aggressor prevalence at target 10-20% — currently ~2-3%, documented as limitation
- [ ] Cohen's d in target range 1-5 — currently ~9-12, documented as limitation
- [ ] Non-additive intervention interactions — not yet implemented
- [ ] Endogenous adaptation mechanism — not yet implemented

## Pathway Status

- [x] Pathway A: ABM substantially complete (V4 model, 6 sweeps, 22,000+ runs)
- [x] Pathway C: Initial SD model with Nauru/Gulf calibration and ABM directional agreement
- [ ] Pathway B: LLM generative agents — not started
- [ ] Pathway C: Formal calibration to additional historical cases
- [ ] Cross-pathway triangulation analysis — requires Pathway B

## Submission Readiness Summary

**Ready for submission as single-pathway ABM paper:** Yes, with caveats noted above.
**Ready for submission as multi-pathway triangulation paper:** No — requires Pathway B and expanded Pathway C.

**Recommended target:** JASSS (Journal of Artificial Societies and Social Simulation) as a stylized ABM study with initial triangulation support from Pathway C.
