# Deviations from the frozen Stage 1b plan (bb3463a)

1. **Bootstrap mechanics fix.** The first run failed because resampled frames had duplicate index labels; added
   `reset_index(drop=True)` after each resample. No change to specification. Found before any result was printed.
2. **Effective N is half the pre-freeze count.** The plan's power note used 67 entrants to unemployment (exposure
   counts only). `happy` is missing in one of the two waves for about half of them, so the primary model has
   **35 exposed / 525 total**. The power statement in the plan therefore overstated power: SE is ≈0.10, not 0.04–0.05.
   This was not checked before freezing because checking it requires tabulating outcome missingness.
3. Dead code line (a health-change robustness model that was never in the plan) removed before the run; it never executed.
