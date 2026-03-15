# Claude Code Task — Iteration 4: Horizon Robustness Study
**Source:** tasks/future_research_spec.md — Issue #1
**Goal:** Prove or disprove that step 80 results are near equilibrium. Add convergence evidence to paper.

## Background
Codex reviewer flagged: paper claims "equilibrium states" but only measures at T=80. No convergence check.
This is Major Issue #1. We need to either:
A) Show results are stable by T=80 → add convergence table, keep "equilibrium" language  
B) Show results are still drifting → replace "equilibrium" with "T=80 end-state" throughout

## Task 1 — Write and run horizon robustness sweep

Add a new runner function (to models/pathway_a_abm/runner.py or a new file) that runs:
- Horizons: T = [80, 120, 160, 240]
- Scenarios: baseline, ubi_only, full_bundle (3 scenarios)
- PL levels: 0.5, 0.80, 0.95 (3 levels)
- 50 runs per condition
- Total: 4 × 3 × 3 × 50 = 1,800 runs

For each run, record sink_index and meaning_index at EACH of the 4 horizon steps (not just the final).

Save to: data/simulation/horizon_robustness.csv
Columns: horizon, scenario, post_labor, run_id, sink_index, meaning_index

## Task 2 — Compute convergence metrics

After the sweep, compute for each (scenario, post_labor) combination:
- sink at T=80, T=120, T=160, T=240 (mean across runs)
- delta_80_120 = |sink(120) - sink(80)|
- delta_120_160 = |sink(160) - sink(120)|
- converged = True if delta_80_120 < 0.02

Write results to: data/simulation/convergence_summary.csv

## Task 3 — Speed comparison fix

Also run a clean speed comparison:
- Both rapid and gradual automation to PL=0.95
- Measure outcomes at: [T_target_reached + 10, + 20, + 40] steps after EACH scenario reaches its target
- 50 runs per condition
- Save to: data/simulation/speed_clean_comparison.csv

For rapid: automation_speed=0.20 (reaches 0.95 in ~5 steps → measure at steps 15, 25, 45)
For gradual: automation_speed=0.95/160 (reaches 0.95 in ~160 steps → measure at steps 170, 180, 200)

## Task 4 — Write analysis report

Write reports/horizon_robustness_analysis.md:
- Table: sink_index at T=80/120/160/240 for each scenario × PL combination
- Convergence verdict: which conditions have stabilized by T=80?
- Speed comparison: does rapid vs gradual difference hold when controlling for exposure time?
- Conclusion: "equilibrium" justified or not?

## Task 5 — Update paper

Based on results:

If converged (delta < 0.02 for all key scenarios):
- Add to Methods §2.4: "We verified that outcomes are near-stationary by step 80: extending to T=160 changes mean sink_index by less than 0.02 across all conditions (see Appendix Table X). We therefore use T=80 as a reliable approximation of the near-equilibrium state."
- Add Appendix Table: convergence summary

If NOT converged:
- Replace "equilibrium states" → "end-states at T=80" throughout paper_draft.md
- Add limitation: "Results represent T=80 snapshots; longer horizons may produce different equilibria in some conditions."
- Update speed section with clean comparison results

## Completion Criteria
- [ ] data/simulation/horizon_robustness.csv exists (1800 rows)
- [ ] data/simulation/convergence_summary.csv exists
- [ ] data/simulation/speed_clean_comparison.csv exists  
- [ ] reports/horizon_robustness_analysis.md written with verdict
- [ ] paper_draft.md updated with either convergence evidence OR honest snapshot language
- [ ] Commit: "Iteration 4: horizon robustness + clean speed comparison"
