# Claude Code Task — Iteration 5 (Final): Minor Revision Fixes
**Source:** Codex Iteration 4 review — Minor Revision verdict
**Goal:** Fix all 5 remaining minor issues. No new experiments. Paper text only.

## Fix 1 — automation_speed parameter range inconsistency
Current paper says: "automation_speed ranges from 0.01–0.08" (paper_draft.md:85)
ODD_protocol.md says: [0.006, 0.20]
Horizon analysis uses: 0.20 and ~0.006

Fix: Update paper_draft.md §2 to say "automation_speed ∈ {0.006, 0.20} for the speed comparison sweep; all other sweeps use a baseline automation_speed of 0.01 per step." 
Also update methods_appendix.md to match.

## Fix 2 — Remove overclaiming about intervention timing
The model has NO intervention_timing parameter and NO deployment timing experiment.

Find and remove/soften these phrases in paper_draft.md:
- "the window for intervention deployment ... is the critical variable" → change to "these findings suggest that transition velocity, not just endpoint displacement level, may affect equilibrium outcomes; formal intervention timing analysis is left to future work"
- "early deployment preserves a larger Productive fraction" → change to "our results are consistent with the hypothesis that earlier intervention preserves social cohesion, though the model does not include an explicit deployment timing parameter"
- Any other claim that implies timing was experimentally varied

## Fix 3 — Three stale text contradictions

**Fix 3a:** Find the sentence containing "0% in V4" and "sink remains 0.565" in paper_draft.md:233 area.
This is logically garbled. Rewrite it clearly: "At collectivism=0.8 and PL=0.95, collapse probability falls to 0% by our threshold definition (sink_index > 0.7), though mean sink_index remains 0.565 — indicating meaningful improvement that does not cross the collapse threshold."

**Fix 3b:** In Discussion section, find where it says "Aggressors → Withdrawn → Collapsed as early-warning sequence" (around paper_draft.md:329). Replace with the correct V4 sequence from Results: "Productive → Beautiful One → Withdrawn → Collapsed (with Aggressor emergence rare at ~2%)"

**Fix 3c:** Find the sentence in Limitations that says interventions are treated as "independent additive effects". Replace with: "While our experimental design varies interventions individually and in combination, the implementation includes coupling between UBI and fairness effects, and between role programs and competence development (detailed in §2.4). Fully orthogonal comparisons would require further model decoupling."

## Fix 4 — Soften historical validation section
In §3.7 (Historical Validation), find the strongest causal-sounding sentences and soften:
- "The model successfully reproduces..." → "The model produces outcomes broadly consistent with..."
- "validates our framework" → "provides qualitative plausibility evidence for our framework"  
- "confirms" → "is consistent with"
- Add/strengthen the existing caveat: "We emphasize that this comparison is post-hoc pattern matching against two cases selected to differ maximally; it does not constitute formal empirical validation."

## Fix 5 — Remove CLAUDE.md reference from appendix
In methods_appendix.md:158 area, find any reference to "CLAUDE.md" and delete it. This is an internal development file that should never appear in a manuscript.

Also check paper_draft.md for any other internal file references (CLAUDE.md, tasks/, .venv, etc.) and remove them.

## Final checks before commit
Run these greps and fix any remaining issues:
1. `grep -n "CLAUDE.md\|tasks/\|\.venv" reports/paper_draft.md reports/methods_appendix.md` → should return nothing
2. `grep -n "independent additive" reports/paper_draft.md` → should return nothing or only the corrected version
3. `grep -n "automation_speed" reports/paper_draft.md reports/methods_appendix.md reports/ODD_protocol.md` → should be consistent

## Completion Criteria
- [ ] automation_speed range consistent across paper + appendix + ODD
- [ ] intervention timing overclaims removed/softened
- [ ] "0% collapse but sink=0.565" sentence fixed
- [ ] Discussion uses correct V4 archetype sequence
- [ ] Limitations no longer says "independent additive"
- [ ] Historical validation hedged further
- [ ] No CLAUDE.md or internal file references in any report
- [ ] All greps clean
- [ ] Commit: "Iteration 5 final: minor revision fixes — paper ready for JASSS submission"
