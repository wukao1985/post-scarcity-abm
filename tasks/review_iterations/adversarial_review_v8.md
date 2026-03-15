# Adversarial Review: Revision 8
**Reviewer:** Senior JASSS Reviewer
**Date:** 2026-03-15
**Verdict:** REJECT AND RESUBMIT (1 FATAL, 6 MAJOR)

---

## Detailed Findings

### FATAL Issues

**FATAL-1: Abstract characterization of aggressor underrepresentation**

**位置：** Abstract, line 23
**原文：** "*Note: the model underrepresents aggressive behavior (~2% vs. Calhoun's 10-20%); results characterize withdrawal-dominated dynamics.*"
**问题：** 根据Checklist Item 30 (aggressor偏低问题)，这是validation failure，不是简单的"underrepresentation"。Abstract将其描述为中性技术特征，但这是一个核心模型缺陷——模型无法复现Calhoun观察到的关键行为维度。这种淡化处理在Abstract中出现是致命的，读者可能误解为这是一个有意的设计选择而非模型失败。
**严重程度：** FATAL
**修改建议：** "*Note: This is a withdrawal-dominated model. Aggressor prevalence (~2%) underestimates Calhoun's observed 10-20%, a known validation failure. Results are therefore limited to withdrawal dynamics and cannot generalize to aggression-driven behavioral sink.*"

---

### MAJOR Issues

**MAJOR-1: Point estimates without confidence intervals at n=50**

**位置：** §3.1, line 185; §3.2, lines 204-212; §3.4, lines 246-253
**原文：** "At 80% post-labor, baseline collapse probability is 2%; at 90%, it rises to 86%; at 95%, 100%"
**问题：** Checklist Item 5要求所有n<100的比较必须有置信区间或SEM。Sweep 1使用50 runs/point（Table §2.4），但全文报告的点估计都没有误差范围。2%、86%、100%这些精确数字基于n=50样本具有高度不确定性（2% collapse = 1/50 runs，标准误差约±2%）。
**严重程度：** MAJOR
**修改建议：** 所有n<100的点估计必须添加±SEM或95% CI。例如："collapse probability is 2% ± 4% (SEM)"或报告为范围估计。

**MAJOR-2: Causal language in ABM results**

**位置：** §3.3, line 236; §3.4, line 259
**原文：** "speed affects transition duration, not the final equilibrium" / "collectivism lowers sink severity"
**问题：** Checklist Item 9指出ABM参数sweep只能说"associated with"或"under X conditions, Y is observed"，不能说"X causes Y"或"X affects Y"。文中多次使用因果动词（affects, lowers, produces）在单一方法ABM研究中构成因果推断越界。
**严重程度：** MAJOR
**修改建议：** 改为："speed is associated with transition duration differences but not equilibrium differences" / "higher collectivism is associated with lower sink severity"

**MAJOR-3: Confounded comparison: roles "advantage" over UBI**

**位置：** §3.5, lines 289-291
**原文：** "Under default parameterization, role substitution shows modest advantage over income transfers (sink ~0.46 vs ~0.52 at 95% displacement), though this advantage is parameter-dependent"
**问题：** Checklist Item 10指出如果两个condition同时变化了多个变量，不能说"A比B好是因为X"。根据§2.4，interventions是bundled的：UBI包含fairness boost，roles包含competence boost和更高的default strength。这是confounded comparison，但文中将其呈现为清晰的hierarchy发现。
**严重程度：** MAJOR
**修改建议：** 改为："Roles-only and UBI-only conditions differ on multiple implementation dimensions (restoration strength, fairness effects, competence pathways). Under default parameterization, roles-only shows lower sink, but this ranking reflects bundled intervention differences rather than pure mechanism comparison. See §3.5 decomposition analysis for partial isolation."

**MAJOR-4: Sweep 5 sample size inadequacy**

**位置：** §2.4, line 152; §3.6, lines 297-313
**原文：** Table shows Sweep 5: "Archetype time series | 2 | 2 | 50 | 100 runs"
**问题：** Sweep 5只有100 runs total（2 scenarios × 2 levels × 50 runs），却要支持Figure 5和整段archetype trajectory分析。每个condition只有50 runs，不足以支持time-series archetype比例的可靠估计。Checklist Item 5要求n<100必须有error bars，但§3.6完全没有报告任何不确定性。
**严重程度：** MAJOR
**修改建议：** 增加runs至150/condition（如Sweep 6标准），或在§3.6添加uncertainty估计（SEM ranges），或在Limitations中明确说明此分析的样本限制。

**MAJOR-5: "Effectively eliminates" language overstates finding**

**位置：** §3.1, line 191
**原文：** "High-quality virtual infrastructure effectively eliminates the transition zone below 90%"
**问题：** "Effectively eliminates"暗示一种确定性和完整性，但实际数据是：baseline 3% collapse → with virtual 0% collapse（at 80% PL）。在n=50/sample的背景下，0% vs 3%的差异在统计上是不确定的（0/50 vs 1.5/50）。使用"effectively eliminates"过度陈述了证据强度。
**严重程度：** MAJOR
**修改建议：** 改为："High-quality virtual infrastructure reduces collapse probability to 0% (from 3% at baseline), though this estimate is based on n=50 runs per condition."

**MAJOR-6: Cohen's d reporting lacks inferential disclaimer context**

**位置：** §4.3, line 351
**原文：** "Cohen's d between conditions dropped from 8-48 to ~9-12. While substantially improved, the model remains more deterministic than typical behavioral science data"
**问题：** Checklist Item 29指出如果Cohen's d > 5，统计显著性是trivial的，需要在全文加caveat。文中Cohen's d仍是9-12（>>5），但只在Limitations提到，没有在Results的统计比较中加disclaimer。读者可能将"significant differences"误解为有意义的效应。
**严重程度：** MAJOR
**修改建议：** 在§2.6 Analysis段落添加："*Note: Cohen's d values between conditions range from 9-12, indicating near-deterministic model behavior. Conventional inferential statistics are reported for descriptive completeness only; significance tests are not meaningful given these effect sizes.*"

---

### MINOR Issues (for completeness)

**MINOR-1:** §3.3 Table (lines 228-231) 报告了3位小数（0.645, 0.789），但模型precision不支持这种精度。

**MINOR-2:** Abstract line 17提到"~0.52" but §3.5 line 276 reports "0.518" — precision不一致。

**MINOR-3:** §3.7 line 317声明"selected post-hoc"，但Abstract line 23的caveat只提到aggressor问题，没有提historical validation的post-hoc性质。

---

## Summary Table

| 类别 | FATAL | MAJOR | MINOR |
|------|-------|-------|-------|
| Abstract vs Body | 1 | 0 | 1 |
| 统计规范 | 0 | 2 | 1 |
| 因果推断 | 0 | 1 | 0 |
| 循环论证 | 0 | 0 | 0 |
| Robustness声明 | 0 | 0 | 0 |
| 外部验证 | 0 | 0 | 1 |
| 模型内部一致性 | 0 | 2 | 0 |
| 语言规范 | 0 | 1 | 0 |
| 结构与透明度 | 0 | 0 | 0 |
| 高阶问题 | 0 | 0 | 0 |
| **合计** | **1** | **6** | **3** |

---

## Verdict Justification

**REJECT AND RESUBMIT** is required because:

1. **1 FATAL issue:** The Abstract's characterization of the aggressor validation failure as a neutral "underrepresentation" rather than a model limitation is a serious transparency problem that misleads readers about the model's validity boundaries.

2. **6 MAJOR issues:** The combination of unreported uncertainty at n=50 (MAJOR-1, MAJOR-4), causal language in an associational study (MAJOR-2), confounded comparison presented as clean hierarchy (MAJOR-3), overstatement of findings (MAJOR-5), and inadequate Cohen's d disclaimer (MAJOR-6) collectively undermine the paper's rigor.

**Required for next round:**
- Fix FATAL-1 with explicit validation failure language in Abstract
- Add SEM/CI to all n<50/100 point estimates
- Replace all causal verbs with associational language in Results
- Clarify that roles vs UBI comparison is confounded/bundled
- Add Cohen's d disclaimer to §2.6
- Tone down "effectively eliminates" claim

---

*Review conducted following ACADEMIC_REVIEW_PROMPT.md v2026-03-15 checklist.*
