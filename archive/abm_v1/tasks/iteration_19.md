# Task: Fix FATAL Code-Paper Inconsistencies in Post-Scarcity ABM

## Context
Codex adversarial review (v19, weighted framework) found 3 FATAL issues where code does not match paper claims. We need to fix the code so the paper's claims are honest, then re-run simulations.

## FATAL Fixes Required

### FATAL 1: UBI implementation contradicts paper claims
**Problem:** Paper says "UBI provides income without restoring role meaning" but in model.py, UBI increases `economic_role`, which drives autonomy/competence/relatedness/status/contribution. So UBI actually partially restores the channels the paper claims it doesn't address.

**Fix in code:** Separate `income_support` from `role_access` in the state equations:
- UBI should only provide `income_support` (a fairness/economic buffer)
- UBI should NOT increase `economic_role` or directly affect autonomy/competence/relatedness/status
- Role substitution should be the intervention that restores `role_access` → meaning channels
- This makes the "roles vs UBI" comparison a true structural comparison, not a parameter difference

**Fix in paper:** After re-running, update all UBI-related claims. The roles > UBI finding becomes stronger (structural difference, not parameter difference).

### FATAL 2: post_labor_fraction description mismatch
**Problem:** Paper describes displacement as "per-timestep cross-sectional rate" but code implements ramp-to-target via `automation_speed`.

**Fix:** Update paper text only — describe the model correctly as a ramp-to-target model. No code change needed. The paper_draft.md §2.1 already has a note about this but needs to be more explicit.

### FATAL 3: "Complex contagion" claim unsupported
**Problem:** Paper claims "complex contagion" but code implements simple linear exposure (no threshold, no reinforcement, no multi-contact requirement).

**Fix:** Change all "complex contagion" references in paper to "network exposure" or "social contagion via network neighbors". No code change needed.

## Additional MAJOR Fixes (while we're at it)

### MAJOR 4: virtual_role doesn't decay
- Add decay: when agent is not displaced, virtual_role should decay toward 0
- Gate virtual benefits on actual engagement (virtual_role > threshold)

### MAJOR 5: Archetype initialization artifact
- Run one classification pass before initial data collection
- Or label step 0 as seeded initial condition in paper

## Execution Plan

1. Fix model.py (FATAL 1 + MAJOR 4 + MAJOR 5)
2. Fix paper_draft.md (FATAL 2 + FATAL 3)
3. Run full simulation sweep (18,500 runs baseline, adjust if parameters changed)
4. Update paper_draft.md Results with new numbers
5. Run tests to ensure model still produces valid output
6. Git commit with clear message

## Acceptance Criteria
- [ ] UBI in code only affects income/fairness, NOT economic_role or meaning channels
- [ ] virtual_role decays when not displaced
- [ ] No "complex contagion" in paper (replaced with "network exposure")
- [ ] Displacement described as ramp-to-target in paper
- [ ] All existing tests pass
- [ ] New simulation runs complete and produce results
- [ ] Paper numbers updated to match new simulation output

## Files to modify
- `models/pathway_a_abm/model.py` — main model code
- `reports/paper_draft.md` — paper text
- `reports/methods_appendix.md` — methods details

## Working Directory
/Users/cloud/Documents/claude/post-scarcity-abm
