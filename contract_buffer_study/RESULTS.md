# RT-04B — Results (frozen analysis run 2026-05-31)

Pre-registration: `DESIGN.md` (frozen 2026-05-31, before any post-shock outcome examined).
Estimator, classes, exposure, window, placebo, and decision rules were locked in advance.
Numbers below are produced by `scripts/analyze.py` from the committed `data_cells.csv`
(`results_summary.json` holds the machine-readable version).

**Sample.** CPS basic monthly, 2021-07 … 2026-04 (53 months; 2025-10 and 2026-02 missing from
the public release and absorbed by month fixed effects). Primary contrast: private wage/salary
(salaried, `PEIO1COW=4`) vs unincorporated self-employed (no-contract, `PEIO1COW=7`), ages 18–64.
Occupation×class×month cells: 48,548 observations, 916 cells, 510 occupations (96% of CPS
occupation codes carry a Language-Modeling-AIOE exposure score). The Census fixed-width parser
reproduces NBER's harmonised weighted class-of-worker counts **exactly** on the 2023-11 overlap.

---

## Headline: H1 is not confirmed

**Primary PPML triple-difference** of weighted employment counts, occupation×class and month
fixed effects, SE clustered by occupation:

| Coefficient | Estimate | ≈ % per exposure-SD | p | 95% CI (%) |
|---|---|---|---|---|
| **β₃  Post × Exposure × NoContract** (the contract-buffer test) | **−0.0220** (SE 0.0175) | **−2.2%** | **0.208** | **[−5.5, +1.2]** |
| β₁  Post × Exposure (common to both classes) | +0.0172 | +1.7% | 0.007 | — |
| β₂  Post × NoContract | −0.0640 | — | <0.001 | — |

**β₃ is not statistically distinguishable from zero.** The contract-buffer hypothesis predicted
β₃ < 0 (no-contract workers in AI-exposed occupations losing employment faster than salaried
workers in the same occupations). The point estimate is weakly negative — directionally what H1
predicts — but the confidence interval comfortably includes zero, so **H1 fails its pre-registered
test.**

Two facts make the failure sharper, not marginal:

1. **The placebo reproduces it.** A fake shock at 2022-05 (pre-ChatGPT, AI-clean window) gives
   **β₃ = −0.0223 (p=0.368)** — essentially identical to the real estimate. Whatever weak negative
   tilt exists is present *before* ChatGPT, so it is not a ChatGPT response. (Per `DESIGN.md` §7,
   the placebo passes the identification gate precisely by being null — and here it also matches the
   real estimate, voiding any causal reading of the −2.2%.)
2. **The event study shows no shock-timed change.** β₃ by 6-month event block: pre-shock blocks are
   flat and non-significant (−18mo: +0.6%, p=0.85; −12mo: +2.5%, p=0.31 → **parallel pre-trends
   hold**), and **no** post-shock block is significantly negative (the most negative is +12mo at
   −4.3%, p=0.13). There is no emergence of a no-contract penalty after the shock.

---

## The other coefficients (context for the null)

- **β₁ > 0 (exposed occupations did not shrink).** Employment in higher-AI-exposure occupations grew
  *slightly* faster after ChatGPT (+1.7% per SD, p=0.007), for salaried workers. Through early 2026,
  CPS shows **no AI-driven employment decline at all** in exposed occupations — consistent with the
  book's own Chapter 4 ("the broad white-collar catastrophe has not shown up in the aggregate
  data"). With no visible exposure-driven decline even on the salaried side, there is little
  differential for a contract buffer to modulate — the test is, in part, **too early / under-powered**
  for an effect the book itself argues is still mostly in the future for contract-protected work.
- **β₂ < 0 (self-employment fell broadly).** Unincorporated self-employment declined after 2022
  across *all* exposure levels (−6.4%, p<0.001) — the unwinding of the 2021 pandemic self-employment
  surge, not an AI-exposure effect (it does not concentrate in exposed occupations; see fig 3).

---

## Pre-registered secondary tests — all fail to support the mechanism

| Test | Result | Verdict |
|---|---|---|
| **H1b (earlier):** β₃ in early window 2022-11…2023-12 | −0.0126 (p=0.481) | no early penalty |
| **H2 (gradient):** unincorp(7) vs salaried(4) | −0.0220 (p=0.208) | — |
| **H2 (gradient):** incorp(6) vs salaried(4) | −0.0558 (p=0.035) | **non-monotone — wrong direction** (the *more* contract-buffered incorporated self-employed move *more*, not less) |

The H2 gradient is the opposite of the contract-buffer prediction: incorporated self-employed
(a legal/organisational buffer) show a *larger* exposure-related shift than the unincorporated
(no buffer). This is incompatible with a buffer that monotonically slows AI's reach.

## Robustness — the null is uniform

β₃ (per exposure-SD), primary window unless noted:

| Specification | β₃ | p |
|---|---|---|
| Primary (Language-Modeling AIOE) | −0.0220 | 0.208 |
| Base AIOE exposure | −0.0215 | 0.198 |
| Ages 25–54 | −0.0058 | 0.749 |
| Ages 16+ | −0.0238 | 0.140 |
| Cell respondents ≥ 10 | −0.0215 | 0.310 |
| Cell respondents ≥ 5 | −0.0245 | 0.203 |
| Hours (intensive margin) | −0.0145 | 0.467 |
| **Placebo shock 2022-05** | **−0.0223** | **0.368** |

Every estimate is a small, non-significant negative whose confidence interval crosses zero, and
the placebo is indistinguishable from the real estimate (figure 2).

---

## What this means (and does not mean)

- **It does not refute the contract-buffer mechanism.** The estimate is imprecise (CI down to
  −5.5%/SD), the AI employment shock is barely visible in CPS by 2026 even for salaried workers, and
  self-employed occupation is measured with noise in thin cells. A real but small or still-emerging
  effect cannot be excluded.
- **It does fail to confirm it, where the book predicted it should already show.** The book's
  Chapter 4 argues the no-contract workforce is hit *first, fast, and unbuffered*. Broad CPS
  employment for unincorporated self-employed in AI-exposed occupations does **not** show that early,
  fast, exposure-concentrated collapse through early 2026. The Stack Overflow collapse — real and
  documented — therefore stands, on this evidence, more as a **possibly-special, perfectly-
  substitutable case** than as the leading edge of a broad no-contract employment decline. The
  substitutability objection the chapter already steelmans gains a little weight.
- **Honest bottom line:** a pre-registered, placebo-controlled **null**. The contract buffer is not
  corroborated by the broad labour data — yet — and the book's forerunner hinge keeps its honest
  "reasoned worry, not demonstrated fact" status, now citing a direct test that failed to confirm it.

## Figures
- `figures/fig1_event_study.png` — β₃ over event time: flat pre-trends, no post-shock descent.
- `figures/fig2_coef_robustness.png` — β₃ across all specifications + placebo; every CI crosses zero.
- `figures/fig3_descriptive.png` — employment change by exposure quartile and class (size-weighted):
  the no-contract drop is broad, not concentrated in exposed occupations.
