# Statistical Validity Audit Report

**Scope:** Verify effect sizes (Cohen's d), statistical tests, confidence intervals, and deterministic-ABM caveats. Flag statistical claims lacking evidence.

**Status:** PASS with observations

---

## Executive Summary

The paper demonstrates **unusual statistical self-awareness for an ABM study**. It explicitly acknowledges that the model is more deterministic than real behavioral science data, correctly avoids formal inferential statistics (p-values, power analysis), and reports results as "point estimates and SEM as descriptive summaries only." The main statistical validity concerns are properly disclosed in the Limitations section (Section 4.3).

---

## 1. Effect Sizes (Cohen's d)

### Findings

| Issue | Status | Evidence |
|-------|--------|----------|
| Cohen's d reported | YES | V4 validation report: d = 9-12 between conditions |
| Comparison to norms | YES | Paper states "where Cohen's d of 1-3 is common" |
| Acknowledgment of problem | YES | "model remains more deterministic than typical behavioral science data" |

### Assessment

**COMPLIANT.** The paper explicitly reports Cohen's d values (§4.3: "Cohen's d between conditions dropped from 8-48 to ~9-12") and correctly identifies this as a limitation. The V4 validation report shows improvement from V3, but acknowledges the target of d = 1-5 was not met.

**Evidence from paper_draft.md (line 355):**
> "Cohen's d between conditions dropped from 8-48 to ~9-12. While substantially improved, the model remains more deterministic than typical behavioral science data (where Cohen's d of 1-3 is common)."

---

## 2. Statistical Tests

### Findings

| Test Type | Used | Status |
|-----------|------|--------|
| p-values | Avoided in main paper | APPROPRIATE |
| t-tests/ANOVA | Not used | APPROPRIATE |
| Regression | Linear fit in one sensitivity report | SEE NOTE |
| Confidence intervals | Reported as SD/SEM | APPROPRIATE |

### Assessment

**COMPLIANT.** The paper correctly avoids formal inferential statistics given the excessive determinism.

**Evidence from paper_draft.md (line 355):**
> "Consequently, conventional inferential statistics (p-values, power) are not meaningful given these effect sizes; we report point estimates and SEM as descriptive summaries only."

**Note on sensitivity_decay_fullscale.md:** This supplementary file reports `r = 0.9778` and `p = 7.32e-4` for a linear fit. While technically accurate, these p-values are misleading given the model's determinism. The "37.35 pooled standard errors" claim conflates model stochasticity with meaningful statistical inference. However, this appears in a supplementary analysis rather than the main paper, and the main paper correctly avoids such claims.

---

## 3. Confidence Intervals

### Findings

| Metric | Reporting | Assessment |
|--------|-----------|------------|
| Mean values | Reported with ± SD or ± SEM | OK |
| Collapse probability | Reported as percentages | OK |
| Between-run variance | SD ~ 0.008 for meaning index | DISCLOSED |

### Assessment

**COMPLIANT.** The paper reports standard deviations and standard errors appropriately. It correctly does NOT claim these represent traditional confidence intervals, instead describing them as "descriptive summaries."

**Evidence from sweep1_summary.csv:** The narrow standard deviations (e.g., `meaning_std` = 0.008) are an artifact of the model's determinism, which is explicitly disclosed.

---

## 4. Pseudo-Replication / Deterministic ABM Caveats

### Key Concerns for ABMs

Pseudo-replication in ABMs occurs when:
1. Multiple "runs" with different seeds produce nearly identical results
2. Within-run variance is conflated with between-condition variance
3. The number of runs (N) is treated as sample size for inferential statistics

### Findings

| Caveat | Addressed | Location |
|--------|-----------|----------|
| Mean-reverting dynamics dominate | YES | §4.3, V4 validation |
| Runs are not independent samples | IMPLICIT | "descriptive summaries only" |
| Model is more deterministic than real data | YES | §4.3 |
| Noise levels increased in V4 | YES | §4.3, V4 validation |
| Effect sizes unrealistically large | YES | §4.3 |

### Assessment

**COMPLIANT WITH OBSERVATIONS.**

The paper addresses the deterministic ABM problem explicitly:

**Evidence from paper_draft.md (line 355):**
> "V4 increased noise (σ=0.08, plus agent-level shocks) to address V3's excessive determinism. Between-run standard deviations improved from ~0.002 to ~0.008 for meaning index..."

**Evidence from methods_appendix.md (line 158):**
> "50 runs per condition (not the 150 used in primary sweeps) -- adequate for directional conclusions but wider CIs"

**Observation:** The paper could more explicitly state that Monte Carlo runs in a deterministic-dominated ABM do not constitute independent samples in the inferential statistics sense. However, by avoiding p-values and treating results as "descriptive," this is implicitly handled.

---

## 5. Statistical Claims Audit

### Claims with Adequate Evidence

| Claim | Evidence |
|-------|----------|
| "Collapse probability 100% at PL=0.95 baseline" | sweep1_summary.csv: collapse_prob = 1.0 |
| "Sink index ~0.79 at PL=0.95" | sweep1_summary.csv: sink_mean = 0.788 |
| "UBI reduces collapse to 0%" | sweep1_summary.csv: ubi_only collapse_prob = 0.0 |
| "Cohen's d dropped from 8-48 to 9-12" | V4 validation report |

### Claims Requiring Caution (but disclosed)

| Claim | Issue | Disclosure |
|-------|-------|------------|
| "46 percentage point collapse difference (speed effect)" | Confounds speed with endpoint displacement | Disclosed in §3.3 and V4 validation |
| "Collectivism effect: 0.549 → 0.443 sink" | Large effect from deterministic model | Characterized as "directional" |
| "Phase transition at 80-90%" | Threshold is model-dependent | Disclosed in §4.3, §5 |

### Claims Lacking Evidence

**None identified in main paper.** The paper appropriately qualifies all numerical claims as "model-dependent" and "conditional on this stylized parameterization."

---

## 6. Supplementary File Audit

| File | Issue | Severity |
|------|-------|----------|
| sensitivity_decay_fullscale.md | Reports p-value (7.32e-4) which is misleading given determinism | LOW (supplementary only) |
| sweep2_analysis.md | Cohen's d 8-48 documented as limitation | OK (self-critical) |
| ablation_analysis.md | Reports differences as ± 0.003 implying high precision | LOW (consistent with disclosed determinism) |

---

## 7. Recommended Additions

While the paper is statistically valid as written, consider adding to §4.3:

1. **Explicit pseudo-replication statement:** "Monte Carlo runs in this ABM do not constitute independent samples; the narrow confidence intervals reflect model stochasticity, not sampling uncertainty from a population."

2. **Run count justification:** Briefly explain why 50-150 runs were chosen (sufficient for estimating mean and variance of a deterministic-dominated process, not for inferential power).

These are **suggestions for strengthening**, not requirements for statistical validity.

---

## Verdict

**PASS**

The paper demonstrates appropriate statistical humility:
- Explicitly discloses Cohen's d problem
- Avoids formal inferential statistics
- Reports results as "descriptive summaries only"
- Acknowledges model is more deterministic than real behavioral science
- Qualifies all numerical findings as model-dependent

The main limitation (excessive determinism) is disclosed rather than hidden. The paper does not overclaim statistical significance or generalizability.

---

## Audit Methodology

- Reviewed: paper_draft.md, methods_appendix.md, v4_validation.md, sweep1-6 analysis files, ablation_analysis.md, sensitivity files
- Searched for: Cohen's d, effect size, p-value, confidence interval, SEM, pseudo, replication, deterministic
- Cross-checked: Data files (sweep1_summary.csv, sensitivity_analysis.csv) against reported statistics

**Audit Date:** 2026-04-02
**Auditor:** Automated statistical validity review
