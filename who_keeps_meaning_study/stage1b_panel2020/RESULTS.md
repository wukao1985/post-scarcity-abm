# Stage 1b results — held-out test on the GSS 2016–2020 panel

Plan frozen `bb3463a` (2026-11-16 01:40 UTC); deviations in `DEVIATIONS.md`; raw output `results/output_1b.json`.
Sample: working at baseline (2016 or 2018), age 25–60, re-interviewed in 2020. First-difference LPM, HC1 SEs, unweighted.

## 中文一段话

**主假设没能确认，也没被推翻——样本太小，结论是"不确定"。** 2020 年失业的人"不太快乐"多升了 8 个百分点，方向和第一阶段一致，
但置信区间从 −11 到 +27，有效样本只有 35 个失业者（原以为 67 个，一半人缺幸福感题）。按预注册的规则，这属于"不确定，
只加注释"。婚姻缓冲的假设方向反了（已婚失业者反而升得更多），但只有 17 人，不可信。**意外的一条（次要结局，未校正）：**
失业者觉得生活"有劲"的比例掉了约 19 个百分点（p=0.04）——第一阶段横截面里没有这个代价。2020 年所有人的"不太快乐"都
从约 9% 涨到 27%（疫情），这是背景噪音。

## Confirmatory

| Hypothesis | Estimate (pp) | 95% CI | p | Verdict |
|---|---|---|---|---|
| **H1b** entering unemployment raises "not too happy" (35 exposed / 525) | +8.0 | −11.2, +27.3 | 0.41 | **inconclusive** (CI includes +10pp) |
| H1b weighted | +7.1 | −12.9, +27.1 | 0.48 | same |
| H2b marriage buffers (U × married; 17 married exposed) | +36.3 | −0.0, +72.6 | 0.050 (Holm 0.20) | not supported, wrong sign |
| H3b weekly attendance buffers (7 exposed) | +35.6 | −9.6, +80.8 | 0.12 (Holm 0.37) | not supported, uninformative |
| H4b distress effect > engagement effect | −10.9 | −37.2, +16.1 | 0.47 (Holm 0.93) | not supported |
| H5b any non-work raises "not too happy" (76 exposed) | +3.8 | −9.8, +17.5 | 0.58 (Holm 0.93) | not supported |
| P1b baseline gap (future-unemployed vs stayers) | +8.0 | −3.9, +19.9 | 0.19 | some selection likely |

Secondary outcome, no directional hypothesis: entering unemployment raised "life not exciting" by **+18.9pp**
(CI +1.0, +36.8; p=0.039; 34 exposed / 522). Uncorrected; read as a hint.

Descriptive "not too happy" rates (baseline → 2020): still working 9.3% → 26.6%; unemployed 19.4% → 46.3%;
retired (n=18) 5.6% → 22.2%; keeping house 24.2% → 27.3%.

## What this changes

1. **Per the decision rule, nothing in the guidance changes except a note:** the "unemployment → distress" finding
   is now "exploratory, direction replicated on held-out data, magnitude unconfirmed".
2. **The engagement null from Stage 1 may be a cross-section artefact.** Within the same people, losing a job in 2020
   lowered "life exciting" — the very penalty the cross-section did not find. Two readings: (a) selection in the
   cross-section (people who stay out of work long-term are those for whom it was not costly); (b) COVID-specific.
   This cannot be settled here; it is the strongest argument yet that the **HRS panel** (with a purpose scale and many
   job-loss transitions outside 2020) is needed.
3. P1b: future-unemployed were already somewhat less happy at baseline (+8pp, ns) — consistent with selection, which
   is why the within-person design matters.

## Limitations

COVID year and web-mode change (common shocks are differenced out; differential ones are not); ~65% attrition;
35 exposed in the primary model, so all moderator tests are uninformative.
