# Stage 1b pre-registration — held-out test on the GSS 2016–2020 panel

Frozen before any outcome in the 2020 wave was examined. Written 2026-11-16 by Claude (independent-researcher mandate
from Kao, 11-16). Parent study: `../PREREGISTRATION.md` (Stage 1, frozen `e4c410c`), results `../RESULTS.md`.

## Why this test

Stage 1's eight confirmatory hypotheses were null. Its useful findings were **exploratory**: unemployment (not
non-work as such) carried a large distress penalty (+14.8pp "not too happy"), and marriage (7.7→1.9pp) and weekly
religious attendance (4.7→2.3pp) shrank the distress penalty of non-work. Re-testing those on the same cumulative
file would be circular. The 2020 wave of the GSS 2016–2020 panel is **not in the cumulative file** (cumulative years
end …2016, 2018, 2021…) and was **excluded from Stage 1** (`../PREREGISTRATION.md` line 29). Its 2020 responses are
therefore held out. This is a partial, cheap replication; the HRS test (purpose-in-life scale) remains the proper one.

## What was looked at before freezing

Only: the variable list of `gss_panel20.rda` (gssr commit 769d48c, SHA-256
`8c1d59cc0a7760b2882b78048fcc0a1e22ea9457236847361d06cfab33151252`); `samptype` counts; marginal `wrkstat` counts
per wave; and the cross-tab of baseline-working, age 25–60, re-interviewed respondents by 2020 `wrkstat`
(N=879: working 738, unemployed 67, retired 18, keeping house 33, other 12, school 11). **No outcome variable
(`happy`, `life`) and no moderator was tabulated.**

## Data and sample

- Baseline wave = the respondent's original cross-section (2016 → suffix `_1a`; 2018 → `_1b`, chosen by `samptype`).
  Follow-up = 2020 (`_2`).
- Sample: working at baseline (`wrkstat` ∈ {1,2,3}), age 25–60 at baseline, re-interviewed in 2020 with non-missing
  2020 `wrkstat`; complete cases on the outcome in both waves.
- Exposure U: 2020 `wrkstat` = 4 (unemployed/laid off) vs 2020 `wrkstat` ∈ {1,2,3} (still working).
  Respondents in other 2020 statuses are excluded from the primary model.
- Secondary exposure NW: 2020 `wrkstat` ∈ {4,5,7,8} vs {1,2,3}.

## Outcomes

- **Primary O2b:** "not too happy" (`happy` = 3) — the outcome on which Stage 1's exploratory findings were made.
- Secondary O1: life "exciting" (`life` = 1). Asked on a ballot subset; expected to be underpowered; reported, no
  directional hypothesis beyond H4b.

## Model

First-difference linear probability model (two periods = person fixed effects):
`Δy_i = α + β·U_i + γ'X_i + ε_i`, X = baseline age, age², sex, race (white/black/other), degree, baseline self-rated
health (1–4), cohort dummy (2018 vs 2016). Robust (HC1) SEs. Unweighted primary (as Stage 1 panels, DEVIATION 2);
weighted (`wtssnr_2`, falling back to `wtssall_2`) as robustness. Two-sided α = 0.05.

## Hypotheses

| # | Prediction | Test |
|---|---|---|
| **H1b** (primary) | Entering unemployment raises "not too happy": β > 0 | β on O2b, p < .05 and positive |
| H2b | The rise is smaller for those married at baseline | U × married (baseline `marital`=1) < 0 |
| H3b | The rise is smaller for weekly attenders at baseline | U × (baseline `attend` ≥ 6) < 0 |
| H4b | The unemployment effect on distress exceeds its effect on engagement | β(O2b) − β(dull-or-routine) > 0, independent bootstrap of the difference (2,000 draws, seed 20261116) |
| H5b | Any non-work (NW) also raises "not too happy" | β_NW on O2b > 0 |

H2b–H5b are secondary; Holm correction across H2b–H5b. H2b/H3b are **expected to be underpowered** (≈67 exits split
by moderator); a null there is uninformative, and will be reported as such.

**Power (H1b), computed from counts only:** with 67 entrants to unemployment and an assumed baseline rate of ~12%
"not too happy", the SE of β is ≈ 0.04–0.05, so an effect of the Stage 1 size (+15pp) is detectable (~3 SE);
an effect of +5pp is not.

## Placebo / selection check

P1b: baseline level of "not too happy" among future-unemployed vs future-still-working (same controls). A large
baseline gap signals selection, not a refutation; reported alongside H1b.

## Known threats (stated now, not after)

1. **COVID.** The 2020 wave was fielded during the pandemic, mostly by web. Most 2020 job loss was pandemic layoffs —
   involuntary, which suits this test — but everyone's happiness shifted. The first-difference design nets out shocks
   common to stayers and leavers; it does not net out a COVID effect that differs by who lost jobs.
2. **Mode change** (face-to-face → web) affects levels; common to both groups.
3. **Attrition** from 2016/2018 to 2020 is large (~65%); estimates apply to stayers in the panel.
4. Small N; retirees (18) too few for any voluntary-vs-involuntary contrast — retirees reported descriptively only.

## Decision rules

- H1b supported → the Stage 1 exploratory "unemployment → distress" finding replicates on held-out data; the guidance
  line "what hurts is involuntary loss" keeps 🟢 with "replicated (GSS 2020 panel)".
- H1b null with CI excluding +10pp → the exploratory finding is downgraded; guidance edited to say so.
- H1b null with CI including +10pp → inconclusive; nothing changes but the note.
- Any analysis not listed here is labelled exploratory.
