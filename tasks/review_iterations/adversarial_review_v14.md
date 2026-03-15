# Adversarial Review — Revision 14 (Final Pass)
**Role:** Senior JASSS Reviewer
**Date:** 2026-03-15
**Review Type:** Final pass with explicit issue classification (A/B/C)

---

## Summary

Revision 14 has addressed 1 of 3 FATAL issues from v13 (F1-virtual worlds claim), but 2 FATAL and 3 MAJOR issues remain. All remaining issues are fixable through text edits without re-running simulations. The paper is close to acceptance but requires these final fixes.

**Recommendation:** MINOR REVISION — all remaining issues are Type-A/B text problems plus one Type-C fixable by text clarification.

---

## FATAL Issues (2 remaining)

### F2. Abstract Finding 3: Roles Advantage Claim Still Misleading

**位置：** Abstract Finding 3 (lines 17-18)
**原文：** "role substitution shows modest advantage over income transfers (sink ~0.46 ± 0.02 vs ~0.52 ± 0.02 at 95% displacement); this ranking reverses when strengths are equalized, revealing UBI's hidden fairness co-benefit dominates when parameterization is held constant (see §3.5 decomposition)."
**问题：** The Abstract still foregrounds the "modest advantage" framing as a primary finding, despite §3.5 showing this ranking is entirely parameter-dependent. When equalized on economic_role restoration strength (both at 0.30), roles_matched produces sink 0.575 — *worse* than UBI's 0.516. The net advantage comes entirely from (a) higher default strength (0.35 vs 0.30) and (b) competence boost. Presenting the raw comparison as headline finding misleads readers about the robustness of this ranking.
**严重程度：** FATAL
**修改建议：** Rewrite Finding 3 entirely: "Intervention effectiveness rankings are parameter-dependent: under default parameterization role substitution shows lower sink, but this advantage reverses when restoration strengths are equalized, revealing that the competence pathway and implementation intensity rather than mechanism superiority drive observed differences. Neither single intervention suffices at extreme displacement."
**类型：** (B) Persistent unfixed — v13 flagged this; revision 14 added the "reverses when equalized" clause but retained the misleading framing.

---

### F3. Conclusion Still Implicitly Overstates UBI Inferiority

**位置：** Conclusion paragraph 2 (line 412)
**原文：** "The central insight is that income support, while preventing outright collapse, leaves substantial residual meaning deficit (sink ~0.52 at 95% displacement even under UBI)."
**问题：** This implicitly positions UBI as inferior to the unmentioned alternative (role substitution at ~0.46). But §3.5 shows this 0.06 difference is artifactual — it reverses when strength is equalized. The Conclusion should acknowledge that both single interventions leave ~0.46-0.52 sink, and the difference between them is not robust to parameterization.
**严重程度：** FATAL
**修改建议：** Change to: "Income support and role substitution both leave substantial residual meaning deficit at extreme displacement (sink ~0.46-0.52 at 95%); their relative ranking depends on implementation intensity assumptions. Neither single intervention suffices."
**类型：** (B) Persistent unfixed — v13 flagged this; revision 14 did not address.

---

## MAJOR Issues (3 remaining)

### M1. Abstract Contains Unqualified Causal Language

**位置：** Abstract Finding 2 (line 15-16)
**原文：** "Income support (UBI) alone leaves substantial residual sink"
**问题：** "Leaves" implies causation. The model shows association (under UBI conditions, sink is observed at ~0.52), not that UBI "leaves" or "causes" this sink. The sink is a joint product of displacement level *and* intervention. Same issue affects Finding 4: "Social cohesion moderates sink severity" — "moderates" is causal language.
**严重程度：** MAJOR
**修改建议：** Finding 2: "Income support (UBI) alone is associated with substantial residual sink (~0.52 at 95% displacement)"
Finding 4: "Higher collectivism is associated with lower sink severity under UBI conditions"
**类型：** (B) Persistent unfixed — v13 flagged this; revision 14 did not address.

---

### M2. "Robust" Claim in Finding 3 Lacks Supporting Evidence

**位置：** Abstract Finding 3 (lines 17-18)
**原文：** "this ranking reverses when strengths are equalized, revealing UBI's hidden fairness co-benefit dominates when parameterization is held constant"
**问题：** The text acknowledges parameter-dependence but doesn't specify what range was tested for this reversal. §3.5 shows the ranking reverses at matched strength, but was this tested at ±20% sensitivity? The claim implies a systematic pattern without providing evidence of systematic testing.
**严重程度：** MAJOR
**修改建议：** Either (a) add explicit sensitivity range for the ranking in §3.5, or (b) soften the Abstract claim to: "this ranking reverses when restoration strengths are equalized in our decomposition analysis."
**类型：** (B) Persistent unfixed — v13 flagged this; revision 14 did not address.

---

### M3. "Triangulation" Section Header Overstates Independence

**位置：** §4.4 (lines 378-384)
**原文：** "Implementation Cross-Check: System Dynamics Model (Pathway C)" [section header changed but still uses "Triangulation" framing in opening] / "To test whether our findings are method-dependent, we developed a parallel system dynamics (SD) model... The directional agreement across two modeling approaches... provides an implementation consistency check"
**问题：** The section header was improved from "Triangulation" to "Implementation Cross-Check," but the opening still frames the SD model as testing "whether our findings are method-dependent." Both models share (a) SDT theoretical framework, (b) same core feedback loops, and (c) the SD model was calibrated to the same Nauru case. This is not method-independent triangulation — it's the same theory in different formalisms.
**严重程度：** MAJOR
**修改建议：** Revise opening to: "To test whether our ABM findings depend on ABM-specific implementation choices, we developed a parallel SD model using the same theoretical framework. Convergence demonstrates findings are robust to formalism choice, not independent of theoretical assumptions."
**类型：** (C) Inherent structural limitation — can be fixed by text clarification only; no model changes needed. The models cannot be made truly independent post-hoc; the fix is honest disclosure of shared assumptions.

---

## Issue Classification Summary

| Issue | Severity | Type | Explanation |
|-------|----------|------|-------------|
| F1 (Virtual worlds claim) | — | — | **FIXED in v14** — Abstract no longer claims virtual worlds "reduce collapse from 100% to 0%" |
| F2 (Roles advantage) | FATAL | (B) Persistent unfixed | v13 flagged; revision 14 added caveat but kept misleading framing |
| F3 (Conclusion overstatement) | FATAL | (B) Persistent unfixed | v13 flagged; revision 14 did not address |
| M1 (Causal language) | MAJOR | (B) Persistent unfixed | v13 flagged; revision 14 did not address |
| M2 ("Robust" without evidence) | MAJOR | (B) Persistent unfixed | v13 flagged; revision 14 did not address |
| M3 (Triangulation claim) | MAJOR | (C) Structural fixable by text | Requires disclosure that models share theoretical framework, not independent validation |

---

## Summary by Category

| 类别 | FATAL | MAJOR | MINOR |
|------|-------|-------|-------|
| Abstract vs Body | 1 (F2) | 1 (M1) | — |
| Causal inference | — | 1 (M1) | — |
| Robustness claims | 1 (F2) | 1 (M2) | — |
| Conclusion alignment | 1 (F3) | — | — |
| Triangulation framing | — | 1 (M3) | — |
| **合计** | **2** | **3** | **0** |

---

## Final Recommendation

**ACCEPT WITH MINOR REVISION**

All 5 remaining issues are fixable through text edits:
- **Type-B (4 issues):** F2, F3, M1, M2 — require text clarification or rewording
- **Type-C (1 issue):** M3 — requires honest disclosure of shared theoretical assumptions

No structural model changes or re-running of simulations is required.

**Required fixes:**
1. Rewrite Abstract Finding 3 to emphasize parameter-sensitivity rather than presenting conditional finding as robust (F2)
2. Acknowledge UBI/roles parity in Conclusion; remove implicit inferiority framing (F3)
3. Change causal to associational language in Abstract "leaves" → "is associated with" (M1)
4. Clarify sensitivity range or soften "dominates" claim in Finding 3 (M2)
5. Revise §4.4 opening to disclose shared SDT assumptions between ABM and SD models (M3)

Once these 5 text edits are made, the paper meets JASSS standards for publication.

---

*Review completed per JASSS methodological standards.*
