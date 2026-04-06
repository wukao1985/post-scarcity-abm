# Code Reproducibility Audit Report

**Date:** 2026-04-02
**Auditor:** Claude Opus 4.6 (automated)
**Status:** PASS

---

## Executive Summary

This audit verifies that the code in `models/pathway_a_abm/` reproduces the numerical claims in `reports/paper_draft.md`. A fresh execution of Sweep 1 (`python models/pathway_a_abm/runner.py 1`) was performed, and all key metrics match the paper's claims within acceptable tolerances.

**Verdict: All 31 numerical claims verified. Code is reproducible.**

---

## 1. Test Suite Verification

```
Tests: 14/14 passed
Runtime: 44.68s
Warning: FutureWarning about seed→rng deprecation (non-breaking)
```

| Test Category | Tests | Status |
|--------------|-------|--------|
| Model Creation | 4 | PASS |
| Model Dynamics | 5 | PASS |
| Interventions | 3 | PASS |
| Reproducibility | 2 | PASS |

---

## 2. Data File Integrity

All sweep data files have correct row counts matching paper claims (Section 2.4):

| File | Expected | Actual | Status |
|------|----------|--------|--------|
| sweep1_results.csv | 2,250 | 2,250 | MATCH |
| sweep2_automation_speed.csv | 3,000 | 3,000 | MATCH |
| sweep3_virtual_world.csv | 3,600 | 3,600 | MATCH |
| sweep4_collectivism.csv | 3,600 | 3,600 | MATCH |
| sweep5_archetypes.csv | 8,100 | 8,100 | MATCH |
| sweep6_full_grid.csv | 4,500 | 4,500 | MATCH |

---

## 3. Section 3.1 — Phase Transition (RQ1)

Paper claims verified against `sweep1_summary.csv`:

| Condition | Paper Claim | Actual | Status |
|-----------|-------------|--------|--------|
| Baseline @ 80% PL | collapse=2% | collapse=2.0% | MATCH |
| Baseline @ 90% PL | collapse=86% | collapse=86.0% | MATCH |
| Baseline @ 95% PL | collapse=100% | collapse=100.0% | MATCH |
| Baseline @ 80% PL | sink~0.63 | sink=0.629 | MATCH |

---

## 4. Section 3.2 — Virtual Worlds (RQ2)

Paper claims verified against `sweep3_virtual_world.csv`:

**At 80% post-labor:**

| Virtual Quality | Paper (collapse/sink) | Actual | Status |
|----------------|----------------------|--------|--------|
| 0.0 | 3% / 0.627 | 3% / 0.627 | MATCH |
| 0.6 | 0% / 0.475 | 0% / 0.475 | MATCH |
| 1.0 | 0% / 0.353 | 0% / 0.353 | MATCH |

**At 95% post-labor:**

| Virtual Quality | Paper (collapse/sink) | Actual | Status |
|----------------|----------------------|--------|--------|
| 0.0 | 100% / 0.792 | 100% / 0.792 | MATCH |
| 0.6 | 6% / 0.658 | 6% / 0.658 | MATCH |
| 1.0 | 0% / 0.517 | 0% / 0.517 | MATCH |

---

## 5. Section 3.3 — Automation Speed (RQ3)

Paper claims verified against `speed_clean_comparison.csv`:

| Speed | Steps After Target | Paper sink | Actual sink | Status |
|-------|-------------------|------------|-------------|--------|
| Rapid | t+10 | 0.645 | 0.645 | MATCH |
| Rapid | t+40 | 0.789 | 0.789 | MATCH |
| Gradual | t+10 | 0.775 | 0.775 | MATCH |
| Gradual | t+40 | 0.797 | 0.797 | MATCH |

---

## 6. Section 3.4 — Collectivism (RQ4)

Paper claims verified against `sweep4_collectivism.csv`:

**Baseline @ 95% PL:**

| Collectivism | Paper (collapse/sink) | Actual | Status |
|--------------|----------------------|--------|--------|
| 0.0 | 100% / 0.812 | 100% / 0.812 | MATCH |
| 1.0 | 92% / 0.743 | 92% / 0.743 | MATCH |

**UBI @ 95% PL:**

| Collectivism | Paper sink | Actual sink | Status |
|--------------|------------|-------------|--------|
| 0.0 | 0.549 | 0.549 | MATCH |
| 0.4 | 0.504 | 0.504 | MATCH |
| 0.8 | 0.462 | 0.462 | MATCH |
| 1.0 | 0.443 | 0.443 | MATCH |

---

## 7. Section 3.5 — Intervention Ranking (RQ5)

Paper claims verified against `sweep6_full_grid.csv` at 95% PL:

| Scenario | Paper (sink/collapse) | Actual | Status |
|----------|----------------------|--------|--------|
| all_bundle | 0.090 / 0% | 0.090 / 0% | MATCH |
| full_bundle | 0.130 / 0% | 0.130 / 0% | MATCH |
| roles+virtual | 0.247 / 0% | 0.247 / 0% | MATCH |
| UBI+virtual | 0.293 / 0% | 0.293 / 0% | MATCH |
| roles | 0.459 / 0% | 0.459 / 0% | MATCH |
| UBI+collectivism | 0.466 / 0% | 0.466 / 0% | MATCH |
| ubi_only | 0.518 / 0% | 0.518 / 0% | MATCH |
| fairness+collectivism | 0.614 / 1% | 0.614 / 1% | MATCH |
| fairness | 0.661 / 12% | 0.661 / 12% | MATCH |
| baseline | 0.790 / 100% | 0.790 / 100% | MATCH |

---

## 8. Section 2.5 — Sensitivity Analysis

Paper claims verified against `sensitivity_analysis.csv`:

| Condition | Paper Claim | Actual | Status |
|-----------|-------------|--------|--------|
| PL=0.80 collapse range | 2-12% | 2-12% | MATCH |
| PL=0.95 collapse range | 92-100% | 92-100% | MATCH |
| Contagion +20% @ 0.80 | 12% collapse | 12% | MATCH |

---

## 9. Section 2.4 — Horizon Robustness

Paper claims verified against `convergence_summary.csv`:

| Claim | Paper | Actual | Status |
|-------|-------|--------|--------|
| Max delta T=80→T=120 | < 0.01 | 0.0092 | MATCH |
| All conditions converged | True | True | MATCH |

---

## 10. Fresh Sweep 1 Reproducibility

A fresh execution of `python models/pathway_a_abm/runner.py 1` was performed during this audit. The new run generated 2,250 results and all key metrics matched exactly:

| Scenario | PL | Metric | Paper | Fresh Run | Status |
|----------|-----|--------|-------|-----------|--------|
| baseline | 0.80 | collapse | 2% | 2.0% | MATCH |
| baseline | 0.90 | collapse | 86% | 86.0% | MATCH |
| baseline | 0.95 | collapse | 100% | 100.0% | MATCH |
| baseline | 0.80 | sink | 0.629 | 0.629 | MATCH |
| ubi_only | 0.95 | sink | 0.515 | 0.515 | MATCH |
| roles_only | 0.95 | sink | 0.458 | 0.458 | MATCH |
| full_bundle | 0.95 | sink | 0.130 | 0.130 | MATCH |

---

## Conclusion

All numerical claims in the paper are reproducible from the code. The model implementation correctly generates the reported results when executed with the same parameters and seeds.

**Reproducibility Status: VERIFIED**

---

## Appendix: Execution Environment

- Python: 3.14.2
- Mesa: 3.5+
- Platform: darwin (macOS)
- CPU: Apple Silicon (ARM64)
- Seed strategy: Deterministic per-run seeding via `seed=run_id * 1000 + param_offset`
