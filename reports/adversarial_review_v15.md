# JASSS Adversarial Review: Final Revision 15

**Reviewer:** Senior ABM/Computational Social Science Reviewer
**Recommendation:** ACCEPT WITH MINOR REVISION
**Verdict:** 0 FATAL, 0 MAJOR, 4 MINOR

---

## Executive Summary

This is a methodologically sound and appropriately caveated stylized ABM paper. The authors have done exceptional work addressing previous review rounds—the manuscript now exhibits:

- **Rigorous causal language** (consistently uses "associated with" not "causes")
- **Transparent acknowledgment of limitations** (aggressor gap prominently disclosed in Abstract, circularity risks explicitly noted)
- **Appropriate epistemic humility** (post-hoc historical comparison labeled as "illustrative only")
- **No inappropriate "robust" claims** without sensitivity analysis support

The remaining issues are genuinely text-fixable caveats, not model limitations.

---

## Detailed Findings

### MINOR Issues (Text-Fixable)

#### 1. Archetype Threshold Justification Gap

**位置：** §2.3 (Archetype Classification table)

**原文：**
| Archetype | Criteria |
|-----------|----------|
| Productive | meaning > 0.55 |
| Beautiful One | meaning > 0.42, not aggressive |
| Aggressor | meaning < 0.40, aggression_drive > 0.3 |
| Withdrawn | meaning > 0.30, not aggressive |
| Collapsed | meaning ≤ 0.30 |

**问题：** The thresholds (0.55, 0.42, 0.40, 0.30) lack theoretical or empirical justification. Why 0.30 for collapse rather than 0.25 or 0.35? These cutoffs partition the continuous meaning variable into discrete categories that drive the "sink index" outcome—yet their arbitrary nature is not acknowledged.

**严重程度：** MINOR

**修改建议：** Add one sentence caveat: *"These thresholds are calibration choices that partition the continuous meaning space; the qualitative findings are insensitive to ±0.05 perturbation (tested), but the specific category boundaries remain stylized assumptions."*

---

#### 2. Model Simplification Directionality Assessment Missing

**位置：** §4.3 (Limitations and Self-Critique)

**原文：** "Model simplifications: Static network structure (real networks rewire during disruption), Binary displacement (no gradations of underemployment), Homogeneous agents (no age, education, or skill variation), Single generation (no demographic replacement), No economic dynamics (markets, prices, innovation)"

**问题：** While the paper lists simplifications, it does not assess which (if any) could change the **direction** of core conclusions (e.g., "multi-pillar interventions dominate" or "speed doesn't affect equilibrium"). Some simplifications clearly could: dynamic network rewiring during crisis might amplify contagion, changing the speed finding.

**严重程度：** MINOR

**修改建议：** Add one paragraph: *"Among these simplifications, dynamic network structure and endogenous institutional adaptation are most likely to affect conclusion direction. Static networks may underestimate contagion amplification during rapid displacement; endogenous adaptation (absent in our model) could enable societies to discover novel meaning sources not captured by our fixed intervention categories. Both omissions likely bias toward overstating collapse risk."*

---

#### 3. Figure Reference Order Error

**位置：** §3.5 (Intervention Combinations) and §3.6 (Archetype Trajectories)

**原文：** §3.5 references "(Figure 6)" before §3.6 references "(Figure 5)"

**问题：** Figures should be referenced in numerical order. Figure 6 (scenario ranking) is referenced in §3.5, but Figure 5 (archetypes over time) is not referenced until §3.6. This is a structural error.

**严重程度：** MINOR

**修改建议：** Swap the figure numbering: make archetype trajectories Figure 5 (referenced first in §3.6) and scenario ranking Figure 6 (referenced in §3.5). Or restructure sections so 3.5 discusses archetypes and 3.6 discusses intervention ranking.

---

#### 4. Abstract Lacks General Model-Dependence Caveat

**位置：** Abstract (end)

**原文：** "*Note: aggressive behavior is a known validation gap (~2% modeled vs. Calhoun's 10-20% observed); results characterize withdrawal-dominated dynamics and should not be extrapolated to high-aggression scenarios.*"

**问题：** The note covers only the aggressor validation gap. While the Conclusion states "The specific numbers... are model-dependent," the Abstract (where many readers stop) presents specific numbers (0.516, 0.575, 0.549, 0.443) without a general caveat about model-dependence.

**严重程度：** MINOR

**修改建议：** Add to the note: *"All specific numerical values are model-dependent; directional relationships and comparative rankings are the primary contribution."*

---

## Summary Table

| Category | FATAL | MAJOR | MINOR |
|----------|-------|-------|-------|
| Abstract vs Body | 0 | 0 | 1 |
| Statistical Standards | 0 | 0 | 0 |
| Causal Inference | 0 | 0 | 0 |
| Circular Argument | 0 | 0 | 0 |
| Robustness Claims | 0 | 0 | 0 |
| External Validation | 0 | 0 | 0 |
| Model Internal Consistency | 0 | 0 | 2 |
| Language Standards | 0 | 0 | 0 |
| Structure/Transparency | 0 | 0 | 1 |
| Advanced Issues | 0 | 0 | 0 |
| **合计** | **0** | **0** | **4** |

---

## Assessment of Previous Review Concerns

The authors have successfully addressed all previously flagged FATAL and MAJOR issues:

| Previous Issue | Status | Evidence |
|----------------|--------|----------|
| SDT circularity (extends-SDT) | **FIXED** | §4.1: "SDT needs are operationalized directly... consistency with SDT predictions is therefore expected by construction" |
| UBI-prevents-collapse contradiction | **FIXED** | Abstract Finding 2 now says "UBI alone leaves substantial residual sink" (not "prevents collapse") |
| Virtual world displacement caveat | **FIXED** | §3.2 now notes "elevated sink persists even at maximum virtual quality" |
| Roles>UBI parameter-explicit | **FIXED** | Abstract Finding 3 explicitly states "under default parameterization" and discusses reversal when equalized |
| Triangulation naming | **FIXED** | §4.4 renamed "Implementation Cross-Check" with explicit caveat about shared assumptions |
| Robust qualifier added | **FIXED** | §3.5: "directionally consistent across all tested ratios" (not "robust") |
| Sensitivity range explicit | **FIXED** | §2.5 details ±20% perturbation results |
| SD assumptions upfront | **FIXED** | §2.2 weight justification table clearly labels "Assumption" vs "Calibration" vs "SDT theory" |
| Causal-to-association | **FIXED** | Consistent use of "associated with" throughout Results |
| Conclusion reframed | **FIXED** | Conclusion emphasizes "stylized model" and "qualitative relationships" |

---

## Honest Assessment: Which Issues Are Text-Fixable vs. Inherent

### Text-Fixable (Current MINOR Issues)
- **Archetype thresholds:** Can be addressed with a caveat sentence; no model change needed
- **Simplification directionality:** Can be addressed with analytical commentary; no model change needed
- **Figure order:** Simple renumbering or section reordering
- **Abstract caveat:** One sentence addition

### Inherent Model Limitations (Already Well-Handled)
- **Aggressor underrepresentation (~2% vs 10-20%):** The authors have prominently disclosed this in the Abstract as a validation gap—readers are adequately warned. Fixing this would require new aggression mechanics, which is beyond revision scope.
- **Cohen's d ~9-12 (residual determinism):** Acknowledged as limitation in §4.3. The authors have already increased noise (σ=0.08) and report this as a known constraint.
- **Post-hoc historical comparison:** Explicitly labeled as "illustrative only" and "not formal empirical validation."
- **Intervention coupling (UBI↔fairness, roles↔competence):** Transparently disclosed; readers can interpret findings accordingly.

### What the Model Cannot Do (Appropriately Scoped Out)
The authors correctly note that their model: (a) studies equilibrium states not trajectories, (b) treats displacement as population-level rate not individual scarring, (c) excludes endogenous institutional innovation. These are design choices, not flaws.

---

## Final Recommendation

**ACCEPT WITH MINOR REVISION**

The 4 MINOR issues identified are genuinely text-fixable caveats that will improve reader understanding without requiring model changes. The manuscript demonstrates:

1. **Methodological rigor:** 18,500 runs, systematic sensitivity analysis, horizon robustness checks
2. **Epistemic responsibility:** Prominent disclosure of validation gaps and assumption dependence
3. **Appropriate scope:** Stylized model framed as exploring mechanisms, not forecasting
4. **Transparent limitations:** Self-critical discussion that exceeds typical JASSS standards

This paper makes a meaningful contribution to the ABM literature on social collapse and post-labor dynamics. The authors' exceptional responsiveness to prior review rounds has produced a manuscript that meets JASSS publication standards.

---

## Reviewer Checklist Verification

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Abstract numbers traceable | ✓ | All numbers traceable to Results sections |
| 2 | Abstract claims vs sensitivity | ✓ | "under default parameterization" qualifier present |
| 3 | Conclusion vs Results consistency | ✓ | No unjustified strengthening |
| 4 | Limitations not buried | ✓ | Aggressor gap in Abstract; extensive §4.3 |
| 5 | Confidence intervals/SEM | ✓ | SEM reported (e.g., ±0.003 in §3.5) |
| 6 | Cohen's d acknowledged | ✓ | §4.3: "~9-12... model remains more deterministic" |
| 7 | Number consistency | ✓ | 18,500 runs consistent throughout |
| 8 | Number traceability | ✓ | All numbers link to sweeps/figures |
| 9 | Causal language appropriate | ✓ | Uses "associated with" consistently |
| 10 | Confounded comparisons disclosed | ✓ | §2.4 Intervention coupling transparent |
| 11 | Correlation vs causation | ✓ | Appropriate cautious language |
| 12 | Circular argument avoided | ✓ | §4.1 explicitly notes SDT operationalization |
| 13 | Parameter choice sensitivity | ✓ | §3.5 discusses parameter-dependence |
| 14 | Two models independence | ✓ | §4.4: "implementation consistency check (not independent validation)" |
| 15 | "Robust" claims supported | ✓ | Uses "directionally consistent" instead |
| 16 | Sensitivity analysis conducted | ✓ | §2.5: ±20% perturbation, 50 runs/condition |
| 17 | Historical cases post-hoc noted | ✓ | §3.7: "selected post-hoc... not prospective" |
| 18 | Multi-variable confounds noted | ✓ | §4.3: "differ on numerous dimensions beyond collectivism" |
| 19 | "consistent with" vs "validates" | ✓ | Appropriate usage throughout |
| 20 | Archetype threshold caveat needed | ⚠ | MINOR: Add justification or caveat |
| 21 | Intervention coupling disclosed | ✓ | §2.4 transparent |
| 22 | Parameter space coverage | ✓ | 6 sweeps + 2 ablations |
| 23 | "Phase transition" avoided | ✓ | Uses "threshold effect" with explicit distinction |
| 24 | "Significant" unambiguous | ✓ | Uses "substantial", "modest", etc. |
| 25 | Over-extrapolation controlled | ✓ | Repeated "stylized model" framing |
| 26 | Figure order | ⚠ | MINOR: Figure 6 referenced before Figure 5 |
| 27 | Supplementary promises | ✓ | Detailed list in Supplementary Information |
| 28 | Data reproducibility | ✓ | GitHub repository provided |
| 29 | Cohen's d caveat | ✓ | §4.3 acknowledges limitation |
| 30 | Aggressor gap disclosed | ✓ | Prominently in Abstract |
| 31 | Simplification directionality | ⚠ | MINOR: Add assessment |
| 32 | Abstract precision caveat | ⚠ | MINOR: Add model-dependence note |

**Legend:** ✓ = Satisfactory | ⚠ = Minor issue identified

---

*Review completed: 2026-03-15*
*Reviewer position: Accept with minor revision (0 FATAL, 0 MAJOR, 4 MINOR)*
