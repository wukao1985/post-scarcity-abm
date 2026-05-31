# JASSS Adversarial Review v16
**Verdict:** 0 FATAL, 1 MAJOR, 4 MINOR
**Recommendation:** Major Revision

## v15 Issue Tracking
1. **Archetype threshold justification gap:** Resolved. `paper_draft.md` §2.3 now explicitly states that the cutoffs are calibration choices and reports a `±0.05` sensitivity check.
2. **Model simplification directionality assessment:** Resolved. `paper_draft.md` §4.3 now identifies which simplifications are most likely to affect conclusion direction.
3. **Figure reference order error:** Resolved. Intervention ranking is now Figure 5 and archetype trajectories Figure 6, matching the order of first reference in the text.
4. **Abstract general model-dependence caveat:** Partially resolved. The Abstract now embeds model-dependence caveats in Findings 1 and 3, but it still lacks one compact catch-all sentence that all reported magnitudes and rankings are model-conditional and directional rather than transportable.

## New Issues Found

### FATAL (must fix before submission)
None.

### MAJOR (should fix, affects scientific validity)

#### 1. RQ3 and the policy discussion still overstate what the implemented displacement process can support
The manuscript now correctly documents that `post_labor_fraction` is a **population-level share re-drawn each step**, not a persistent individual displacement state (`paper_draft.md` §2.1, §4.3; `ODD_protocol.md` §3.1). That framing is sufficient for an **aggregate equilibrium** interpretation. The problem is that the paper then goes beyond that valid interpretation in several places:

- Abstract Finding 5 says that "the displacement level and intervention regime, not the transition path, determine the final state."
- Results §3.3 states that "the displacement level, not the path taken, determines the final state."
- Discussion §4.2 converts this into a policy claim: intervention provision matters more than automation speed, "rather than managing automation speed per se."

Those stronger statements are not warranted by the implemented model, because the model does **not** represent persistent exposure, individual scarring, retraining trajectories, or managed transitions. The recent diagnostics reinforce this exact point: `calibration_diagnosis.md` identifies the per-step re-randomization as the key structural fact, and the paper itself already admits that the design "precludes conclusions about ... the dynamics of managed transitions." As written, the paper simultaneously says transition-path claims are out of scope and then makes one.

This is a major issue because RQ3 is one of the manuscript's five headline questions, and the current wording overextends the result from "cross-sectional equilibrium under repeated random reassignment" to "real transition speed is secondary." The fix can be textual rather than architectural: narrow the claim to the implemented model. For example, the authors can say that **within this equilibrium ABM, once target displacement is reached, aggregate late-run outcomes are similar across fast and slow ramps**; they should then explicitly state that persistent-displacement models are needed before drawing claims about real transition management or unemployment scarring.

### MINOR (text fixes)

#### 1. Sensitivity analysis is still local/OAT only, and that limitation should appear in the main-paper limitations
The manuscript is transparent in Methods §2.5 that sensitivity analysis is one-at-a-time (`±20%` on three parameters), and `methods_appendix.md` explicitly notes that OAT does not capture parameter interactions. But the main-paper limitations section never states plainly that the paper lacks a **global sensitivity analysis** (e.g. Sobol, PRCC, or another interaction-sensitive design). For a stylized JASSS paper this is not fatal, but the omission matters because several headline claims concern threshold location and intervention ranking near a sensitive regime. A one-sentence limitation in §4.3 would be enough: robustness evidence is local and targeted, not global across the joint parameter space.

#### 2. One number-consistency issue remains: the Abstract's roles-vs-UBI uncertainty notation is not traceable
Most spot-checked numbers are internally consistent and traceable:

- `18,500` total runs matches the design table.
- Baseline collapse at `PL=0.80/0.90/0.95` is `2% / 86% / 100%`, matching the sweep summary.
- Virtual-world results at `PL=0.95` (`0.517` virtual-only sink; `0.294` for UBI+virtual) match the simulation CSV.
- Collectivism results (`0.549` down to `0.443`) are consistent across Results, Conclusion, and Figure 4 caption.
- Scenario-ranking values (`0.090`, `0.130`, `0.459`, `0.518`, `0.790`) match the full-grid data.

The exception is Abstract Finding 3: `~0.46 ± 0.02 vs ~0.52 ± 0.02` does not match the uncertainty actually reported later in §3.5 for the 150-run matched comparison (`0.460 ± 0.003` vs `0.516 ± 0.003`), and it is not clear what the `±0.02` refers to. Either define the statistic explicitly and use the correct value, or remove the uncertainty notation from the Abstract. A smaller cleanup is also needed in §3.2, where "UBI clearly dominates virtual-only (sink 0.542 vs 0.514)" reverses the intuitive order of the numbers and invites misreading.

#### 3. Historical validation is mostly well-caveated, but a few sentences are still stronger than "illustrative only"
The manuscript does many things right here: it says the cases were selected post hoc, labels the comparison "illustrative only," denies that it is formal validation, and lists multiple confounders. That is sufficient on the whole. The remaining problem is tone in a few sentences. Calling Nauru a "natural experiment in UBI-without-purpose" and stating "The key structural difference: collectivist social institutions" is still more causal and exclusive than the later caveat permits. Those lines should be softened so the section consistently reads as post-hoc pattern matching, not quasi-identification.

#### 4. The partial fix to the Abstract's model-dependence caveat should be finished cleanly
This is the only v15 issue I consider still partly open. The Abstract now includes local caveats, but readers who stop there still do not get one clean sentence saying: all specific numerical values and comparative rankings are conditional on this stylized parameterization, and the main contribution is directional/mechanistic rather than predictive. Given how many readers only read the Abstract, this is worth fixing directly rather than relying on scattered caveats.

## Submission Readiness
Not ready to submit as-is.

The paper is close. The core manuscript is substantially improved since v15, and most of the checklist now passes: ODD coverage is complete across all 7 elements, intervention confounds are disclosed, the aggressor validation gap is prominently acknowledged, historical comparison is mostly disciplined, and most reported numbers are internally consistent. I do **not** see a new fatal flaw in the recent auxiliary reports. `calibration_diagnosis.md` and `codex_verification_decay.md` mainly reinforce the already-documented fact that displacement is re-randomized each step; `sensitivity_decay_fullscale.md` adds an outcome-specific decay result for a secondary metric but does not overturn the paper's main RQ1/RQ2/RQ4/RQ5 findings.

The blocking issue is the over-broad RQ3 interpretation. If the authors narrow the speed claim to what the implemented equilibrium model actually supports, add one explicit main-text limitation about local rather than global sensitivity, and clean the remaining Abstract / historical-comparison wording, the paper becomes submission-ready quickly.

**Estimated time to address and submit:** about 1 working day for text revision and consistency checking. If the authors want to preserve the broader "speed does not matter" claim rather than narrow it, that would require a persistent-displacement model and additional experiments, which is a materially larger revision.
