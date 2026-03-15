# Adversarial Review — Revision 13
**Role:** Senior JASSS Reviewer
**Date:** 2026-03-15
**Review Type:** Final push — FATAL and MAJOR issues only

---

## Summary

Revision 13 represents substantial improvement with careful causal language, caveated claims, and transparent limitation acknowledgment. However, **3 FATAL and 3 MAJOR issues remain**, all requiring text edits (no Type-C structural limitations).

**Recommendation:** MINOR REVISION — all issues are fixable through text clarification.

---

## FATAL Issues

### F1. Abstract Finding 2: Virtual Worlds Claim Exceeds Body Evidence

**位置：** Abstract Finding 2 (lines 15-16)
**原文：** "Virtual worlds alone reduce collapse from 100% to 0%"
**问题：** The Abstract states this as a general finding, but §3.2 makes clear this only applies at 80% displacement. At 95% displacement with virtual worlds alone, "elevated sink (0.517) persists even at maximum quality, indicating partial but incomplete substitution." The Abstract omits this critical qualification, creating the false impression that virtual worlds fully prevent collapse at all displacement levels.
**严重程度：** FATAL
**修改建议：** Change to: "Virtual worlds eliminate collapse at moderate displacement levels (≤80%), though elevated sink persists at 95% displacement even with maximum virtual quality, indicating partial rather than complete substitution."
**类型：** (A) New problem — this exact wording was not present in previous versions

---

### F2. Abstract Finding 3: Roles Advantage Claim Ignores Equalization Caveat

**位置：** Abstract Finding 3 (lines 17-18)
**原文：** "role substitution shows modest advantage over income transfers (sink ~0.46 ± 0.02 vs ~0.52 ± 0.02 at 95% displacement), though this advantage is parameter-dependent and reverses when restoration strength is equalized"
**问题：** While the caveat exists, the Abstract still foregrounds the "modest advantage" framing as the primary finding. §3.5 decomposes this extensively: when equalized on economic_role restoration strength (both at 0.30), roles_matched produces sink 0.575 — *worse* than UBI's 0.516. The net advantage comes entirely from (a) higher default strength (0.35 vs 0.30) and (b) competence boost. Presenting the raw comparison as headline finding is misleading.
**严重程度：** FATAL
**修改建议：** Rewrite Finding 3 entirely: "Role substitution and UBI show comparable effectiveness when equalized on restoration strength; any observed advantage for roles depends on implementation intensity (competence pathway, higher default strength). The key finding is that neither single intervention suffices at extreme displacement."
**类型：** (B) Persistent unfixed — previous reviews flagged this comparison as problematic; revision 13 added the "reverses when equalized" clause but retained the misleading framing

---

### F3. Conclusion Overstates Finding 3 Despite Equalization Caveat

**位置：** Conclusion paragraph 2 (line 412)
**原文：** "The central insight is that income support, while preventing outright collapse, leaves substantial residual meaning deficit (sink ~0.52 at 95% displacement even under UBI)."
**问题：** This implicitly positions UBI as inferior to the unmentioned alternative (role substitution at ~0.46). But the decomposition in §3.5 shows this 0.06 difference is artifactual — it reverses when strength is equalized. The Conclusion should acknowledge that both single interventions leave ~0.46-0.52 sink, and the difference between them is not robust to parameterization.
**严重程度：** FATAL
**修改建议：** Change to: "Income support and role substitution both leave substantial residual meaning deficit at extreme displacement (sink ~0.46-0.52 at 95%); their relative ranking depends on implementation intensity assumptions. Neither single intervention suffices."
**类型：** (A) New problem — this specific overstatement was introduced or strengthened in revision 13

---

## MAJOR Issues

### M1. Abstract Contains Unqualified Causal Language

**位置：** Abstract Finding 2 (line 15-16)
**原文：** "Income support (UBI) alone leaves substantial residual sink"
**问题：** "Leaves" implies causation. The model shows association (under UBI conditions, sink is observed at ~0.52), not that UBI "leaves" or "causes" this sink. The sink is a joint product of displacement level *and* intervention. Same issue affects Finding 4: "Social cohesion moderates sink severity" — "moderates" is causal language.
**严重程度：** MAJOR
**修改建议：** Finding 2: "Income support (UBI) alone is associated with substantial residual sink (~0.52 at 95% displacement)"
Finding 4: "Higher collectivism is associated with lower sink severity under UBI conditions"
**类型：** (A) New — previous revisions were more careful with "is associated with" phrasing

---

### M2. "Robust" Used Without Sensitivity Evidence for Roles-UBI Ranking

**位置：** §3.5 paragraph 3 (lines 289)
**原文：** "the advantage is parameter-dependent and reverses when restoration strength is equalized (see §3.5)"
**问题：** The text acknowledges parameter-dependence but doesn't specify what range was tested. §3.5 shows the ranking reverses at matched strength, but was this tested at ±20% sensitivity? The robustness claim is implied but unsupported. If the ranking is truly parameter-dependent, the Abstract shouldn't present it as a finding at all.
**严重程度：** MAJOR
**修改建议：** Either (a) add explicit sensitivity range for the ranking in §3.5, or (b) remove Finding 3 entirely from Abstract and present only the "neither single intervention suffices" conclusion.
**类型：** (B) Persistent — robustness of the roles-UBI comparison has been questioned in prior reviews

---

### M3. Triangulation Claim Overstates SD Model Independence

**位置：** §4.4 (lines 378-384)
**原文：** "To test whether our findings are method-dependent, we developed a parallel system dynamics (SD) model... The directional agreement across two modeling approaches... provides an implementation consistency check"
**问题：** The text correctly notes "implementation consistency" rather than "validation" but still frames the SD model as a "triangulation" test (section header: "Triangulation"). Both models share (a) SDT theoretical framework, (b) same core feedback loops (meaning → sink → contagion), and (c) the SD model was calibrated to the same Nauru case. This is not independent triangulation — it's the same theory in different formalisms.
**严重程度：** MAJOR
**修改建议：** Change section header to "Cross-Implementation Comparison" and revise opening: "To test whether our findings depend on ABM-specific implementation choices, we developed a parallel SD model using the same theoretical framework. Convergence demonstrates findings are robust to formalism choice, not independent of theoretical assumptions."
**类型：** (C) Structural limitation — but can be fixed by text clarification; no model changes needed

---

## Summary Table

| 类别 | FATAL | MAJOR | MINOR |
|------|-------|-------|-------|
| Abstract vs Body | 2 (F1, F2) | 1 (M1) | — |
| 因果推断 | — | 1 (M1) | — |
| Robustness 声明 | — | 1 (M2) | — |
| 循环论证/Triangulation | — | 1 (M3) | — |
| **合计** | **3** | **3** | **0** |

---

## Type Classification Summary

| Issue | Type |
|-------|------|
| F1 | (A) New problem introduced by revision |
| F2 | (B) Persistent unfixed problem |
| F3 | (A) New problem introduced by revision |
| M1 | (A) New problem introduced by revision |
| M2 | (B) Persistent unfixed problem |
| M3 | (C) Structural limitation fixable by text edit |

---

## Final Recommendation

**ACCEPT WITH MINOR REVISION**

All remaining issues are Type-A or Type-B text problems, plus one Type-C that requires text clarification only. No structural model changes needed. The paper has reached the threshold for acceptance pending correction of the 6 identified issues.

Key fixes required:
1. Qualify virtual worlds claim in Abstract (F1)
2. Restate or remove Finding 3 in Abstract (F2)
3. Acknowledge UBI/roles parity in Conclusion (F3)
4. Change causal to associational language in Abstract (M1)
5. Clarify sensitivity range or remove ranking claim (M2)
6. Retitle "Triangulation" section and clarify shared assumptions (M3)
