# Future Research Spec — Addressing Remaining Major Issues

From Codex Iteration 3 review. Three issues remain that require substantive research (not just prose fixes).

---

## Issue #1: "Equilibrium" Claimed But Not Demonstrated

### The Problem
The paper now uses "equilibrium" framing, but all results are measured at step 80 with no convergence check. If the system hasn't reached a steady state by step 80, the results are finite-horizon transients, not equilibria. The speed comparison is especially vulnerable: rapid automation reaches target early, spending more time in the high-displacement regime before measurement.

### Research Spec: Horizon Robustness Study

**Experiment design:**
Run the current V4 model at 4 time horizons: T=80, T=120, T=160, T=240
Same parameter grid as Sweep 1: {baseline, UBI, full_bundle} × {PL=0.5, 0.8, 0.95}
50 runs per condition (450 total)

**Metrics:**
- Mean sink_index at each horizon
- Δ(sink) = |sink(T) - sink(T-40)| → convergence indicator
- Declare "converged" if Δ < 0.02

**Success criteria:**
- If results stable by T=80 → current paper is valid, add convergence table to appendix
- If results still shifting → must extend horizon OR reframe as "T=80 snapshot" explicitly in every results sentence

**Speed effect fix:**
Compare rapid vs gradual at equal time-after-reaching-target, not at fixed step 80.
E.g., rapid reaches PL=0.95 at step ~5; measure at step 5+N for both conditions.
This separates "speed of transition" from "time spent at high displacement."

**Output:**
- `data/simulation/horizon_robustness.csv`
- `reports/horizon_robustness_analysis.md`
- 1 convergence figure: sink_index vs timestep for key scenarios
- Paper update: either confirm stability (adds credibility) or reframe as snapshot

---

## Issue #2: Speed Effect is Exposure-Duration Artifact

### The Problem
Rapid automation reaches PL=0.95 in ~5 steps, then the model runs at full displacement for 75 more steps. Gradual automation reaches PL=0.95 only at step 80 (or not at all if target>0.80). The 100% vs 54% collapse difference is partly "more cumulative steps under full displacement" not "speed itself causes worse outcomes."

### Research Spec: Clean Speed Comparison

**Option A — Equal exposure measurement (quick, 1-2 days):**
Modify the sweep to measure outcomes at equal time-after-target:
- Rapid: measure at steps [T_target+20, T_target+40, T_target+80]
- Gradual: measure at same steps after it reaches target
- This isolates speed from duration

**Option B — Transition speed as continuous variable (thorough, 3-5 days):**
New sweep: vary automation_speed from 0.005 (very gradual) to 0.5 (near-instantaneous)
Measure: (a) time to first collapse, (b) sink at T=target+40
Plot: speed vs outcome curve
Expect: non-linear relationship with a "safe speed" threshold

**Output:**
- `data/simulation/sweep_speed_clean.csv`
- `reports/speed_analysis_clean.md`
- Key finding: does speed matter independently of duration? What's the safe speed threshold?
- Paper update: rewrite speed section with cleaner causal claim

**Note:** Option A is doable within current model. Option B requires small runner change.

---

## Issue #3: Roles vs UBI — Structural Advantage or Robust Finding?

### The Problem
In the model:
- UBI affects: `economic_role = ubi * 0.30` (only one pathway)
- Roles affect: `economic_role = roles * 0.35` (stronger) AND `competence += roles * 0.15` (extra pathway)
- Virtual role affects meaning at weight 0.1 vs economic role at 0.8

The "Roles > UBI" and "virtual worlds can't substitute" findings are partly determined by these weights. If we flipped the weights, we'd get different conclusions. This makes the finding conditional on assumptions, not a general result.

### Research Spec: Structural Sensitivity Ablation

**Experiment 1 — Weight ablation (2 days):**
Vary the economic_role vs virtual_role weight ratio:
- Conditions: [6:1, 7:1, 8:1 (current), 9:1, 10:1, 3:1, 1:1]
- Fixed: PL=0.95, all 10 scenarios
- 50 runs per condition
- Question: at what weight does virtual world start "working"? Is there a threshold?

**Experiment 2 — UBI vs Roles decoupled (3 days):**
Create a truly isolated comparison:
- UBI_pure: only restores economic_role (no competence, no fairness effect)
- Roles_pure: only restores economic_role at same level as UBI_pure
- Roles_full: current implementation (adds competence + stronger economic_role)
- Run all three at PL=0.95, 150 runs

Question: how much of Roles > UBI comes from (a) stronger economic_role restoration, vs (b) competence boost, vs (c) both together?

**Expected honest finding:**
"Roles outperform UBI primarily because they restore both economic role and competence pathways simultaneously. If interventions are equalized on economic role restoration alone, the advantage narrows significantly. The degree to which real role programs carry competence-building effects is an empirical question this model cannot resolve."

**Output:**
- `data/simulation/ablation_weights.csv`
- `data/simulation/ablation_interventions.csv`
- `reports/structural_sensitivity.md`
- Paper update: replace "Roles outperform UBI" (unconditional) → "Under current weighting assumptions, Roles outperform UBI, primarily via competence pathway. Sensitivity analysis shows this advantage is robust above a 5:1 economic-to-virtual weight ratio but narrows if the competence boost is removed."

---

## Suggested Iteration Order

1. **Iteration 4** — Issue #1 (Horizon Robustness): fastest to run, highest credibility payoff, fixes the "equilibrium" word problem definitively. ~2 days.

2. **Iteration 5** — Issue #3 Experiment 1 (Weight Ablation): shows the virtual role finding is structural but honest. ~2 days.

3. **Iteration 6** — Issue #2 Option A (Clean Speed): fixes the exposure-duration confound. ~1 day.

4. **Iteration 7** — Issue #3 Experiment 2 (Intervention Decoupling): most important for policy claims. ~3 days.

After Iteration 7: re-run Codex review. Target: Minor Revision.

---

## For Route B (V5 model — future work section in paper)

These specs also define what V5 would need:
- Persistent individual displacement (tracked across steps)
- Explicit re-employment mechanism (probability per step, affected by roles programs)
- Archetype hysteresis (history-dependent state transitions)
- Properly decoupled interventions (UBI = income only; Roles = role only)
- Extended time horizon (200+ steps)

Frame in paper as: "These limitations suggest a natural extension to a V5 model with persistent individual states, which we are developing as subsequent work."
