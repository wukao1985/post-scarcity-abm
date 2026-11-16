# Results — Who keeps meaning without work? (GSS 1973–2024, pre-registered)

Run 2026-11-16 on the frozen plan (`PREREGISTRATION.md`, commit `e4c410c`); deviations in `DEVIATIONS.md`.
Raw numbers: `results/output.json`. Effects are average marginal effects in **percentage points (pp)**,
prime-age adults 25–64, students excluded, weighted, health-adjusted unless stated.

## 中文一段话

**预注册的八个假设全部没有通过。** 控制健康后，不工作的人觉得"生活有劲"的比例只比在职者低 1.0 个百分点
（p=0.21），朋友、宗教、婚姻、收入都没有显著的缓冲作用；面板里个人从在职到不工作，"有劲"不降反升（+4.9pp，
p=0.11）；"中年代价最大"的猜测也被否定——代价反而出现在 25–39 岁（−3.0pp）。安慰剂干净。这是项目第三个
预注册零结果。**探索性发现（不作确认性结论）**比确认性的更有用："不工作"不是一件事：失业者"不太快乐"高
14.8pp，65 岁前退休的人反而更"有劲"（+5.4pp）、更少不快乐；婚姻（7.7→1.9pp）和每周宗教活动（4.7→2.3pp）
显著削减不工作带来的**不快乐**，但不影响"有劲"。不控制健康时，"有劲"的差距是 3.5pp 且显著——相当一部分
关联来自健康。

## Confirmatory (pre-registered)

| Hypothesis | Estimate (pp) | 95% CI | p | Verdict |
|---|---|---|---|---|
| H1 non-work penalty on "life exciting" (O1), N=31,768 | −1.0 | −2.6, +0.5 | 0.21 | **not supported** |
| H2 friends buffer (N=15,397) | +0.0 | −4.3, +4.6 | 0.99 (Holm 1.0) | not supported |
| H3 weekly religious attendance buffers | +2.3 | −1.0, +5.4 | 0.17 (Holm 0.68) | not supported |
| H4 marriage buffers | +1.1 | −2.0, +4.3 | 0.48 (Holm 1.0) | not supported |
| H5a top-income non-workers still less engaged | −0.7 | −3.8, +2.5 | 0.66 | not supported (no penalty to persist) |
| H5b income moderates distress more than engagement | std. 0.044 vs 0.024 | diff CI −0.07, +0.10 | 0.63 (Holm 1.0) | not supported |
| H6 penalty largest at 40–54 | 40–54: +0.3; 25–39: −3.0; 55–64: +0.1 | 40–54 minus 25–39: +3.3 (−0.3, +6.7) | 0.06 | **rejected — direction opposite** |
| H7 within-person exit lowers O1 (998 people, 266 exits) | +4.9 | ±5.9 | 0.11 | not supported (wrong sign) |
| H8 baseline friends buffer the exit (509 people, 141 exits) | −15.3 | ±17.2 | 0.08 | not supported (wrong sign) |
| P1 placebo: decline before exit (722 people, 112 later exiters) | −2.1 | ±11.1 | 0.71 | clean |

Reading: in 50 years of US data, once self-rated health is held fixed, **prime-age adults who are not working
are about as likely as workers to say life is exciting**, and none of the four pre-specified resources changes
that. The panel is underpowered (H7/H8 CIs are wide), so it cannot rule out moderate within-person effects; it
does not show the predicted drop, and the placebo shows no pre-exit decline.

## Robustness

- Without the health control, the H1 penalty is **−3.5pp (CI −5.1, −1.9), p<0.001**. Health is a confounder
  (ill health causes exit) but also possibly a mediator (exit harms health), so the true figure is plausibly
  between −1.0 and −3.5. Unweighted: −0.4 (ns). Linear probability: −1.0 (ns). Conclusions unchanged.
- Relatives instead of friends (S4): no buffer (−0.9, ns).

## Exploratory (not confirmatory; no multiplicity correction; for hypothesis generation only)

**"Not working" is not one thing (S1, each type vs workers):**

| Type | "Life exciting" | "Not too happy" |
|---|---|---|
| Unemployed / laid off | −2.5 (ns) | **+14.8** (CI 12.3, 17.5) |
| Retired before 65 | **+5.4** (1.9, 9.0) | **−2.4** (−4.0, −0.8) |
| Keeping house | **−2.6** (−4.6, −0.7) | +0.5 (ns) |
| Other (incl. disabled) | +1.2 (ns) | **+5.0** (2.6, 8.0) |

**Buffers work on distress, not on engagement (pooled non-work, outcome "not too happy"):**
- Married: non-work distress penalty **7.7pp unmarried vs 1.9pp married** (difference −5.7, CI −7.9, −3.6).
- Weekly religious attendance: **4.7 vs 2.3pp** (difference −2.5, CI −4.5, −0.5).
- Friends several times a month: no buffer (−0.3, ns). Income top vs bottom tercile: −1.5 (ns).
- Pooled non-workers are also slightly *more* often "very happy" (+1.7pp): non-work spreads people out to both tails.

**By decade (S2):** penalty on "exciting" bounces between −4.0 and +4.4pp with no clear trend.

## What this changes

1. **For the project's synthesis (proposal, not yet applied to SYNTHESIS.md):** Q4 ("people with money but no
   work") gains a 🟢-associational line: *in US data, what hurts is involuntary loss (unemployment → distress),
   not non-work as such; early retirees are, if anything, more engaged.* This sharpens rather than overturns Q4
   ("depends on health, voluntariness, social ties") — voluntariness and health now carry measured weight.
   Q2's "money buys relief, not meaning" is **not** tested cleanly here (no engagement penalty for money to fail
   to fix); it is neither supported nor weakened.
2. **For Paper 2 / Stage 2:** the GSS cannot calibrate the ABM's meaning channels on engagement — there is no
   engagement penalty to decompose. The usable estimates are on **distress**: marriage (≈ roles) strong, religion
   moderate, friends ≈ 0, income ≈ 0. That ordering is itself at odds with Paper 1's assumed weights (relatedness
   and roles low). A confirmatory Stage 1b on distress, pre-registered on a **held-out** data source, is the honest
   next step — re-testing the exploratory buffers on the same GSS would be circular.
3. **Measurement is the bottleneck.** One item ("exciting / routine / dull") may simply be too blunt. The HRS
   (Ryff purpose-in-life scale + retirement/job-loss panel) is the right held-out test; it needs a free account
   registration by the project owner.
4. **For the guidance series:** midlife guidance should not claim "non-work drains meaning in midlife" — this data
   says the risk concentrates in **involuntary** loss and in the **unpartnered / unconnected-to-a-community**, and
   (weakly) among **25–39** for engagement.

## Follow-up (Stage 1b, 2026-11-16)

Held-out test on the GSS 2020 panel wave (`stage1b_panel2020/RESULTS.md`): unemployment → distress **+8pp, CI −11 to +27, inconclusive** (35 exposed). Within-person, job loss in 2020 lowered "life exciting" by ~19pp (secondary, uncorrected) — the engagement penalty the cross-section did not show.

## Limitations

US only; one-item outcome; cross-section has selection (who stops working); health is both confounder and
possible mediator; panels small (≈260 exits) so within-person nulls are uninformative about moderate effects;
none of these people stopped working because of AI. Exploratory findings are on the same data that generated them.
