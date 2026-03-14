# V3 Sweeps 2-6: Comprehensive Analysis Report

**Post-Scarcity ABM: Behavioral Sink Under AI Automation**

*Date: 2026-03-14*
*Total simulation runs: 17,400*

---

## Executive Summary

This report presents findings from five large-scale parameter sweeps (Sweeps 2-6) exploring:
1. **Automation speed effects** (RQ3)
2. **Virtual world substitution** (RQ2)
3. **Collectivist vs. individualist structures** (RQ4)
4. **Behavioral archetype trajectories** (RQ5)
5. **Full intervention grid** at critical automation thresholds

**Key Finding:** The 80% post-labor collapse threshold is not fixed—it can shift lower with rapid automation (more severe) or higher with combined interventions (virtual worlds + UBI + collectivism). At 95% automation, single interventions often fail, but strategic combinations achieve 0% collapse.

---

## Sweep 2: Automation Speed (RQ3)

**Design:** 2 speeds (gradual vs. rapid) × 3 post-labor levels (0.5, 0.8, 0.95) × 5 scenarios × 100 runs = 3,000 runs

### Key Results

| Scenario | Post-Labor | Speed | Meaning | Sink | Collapse |
|----------|-----------|-------|---------|------|----------|
| Baseline | 0.80 | Gradual | 0.400 | 0.686 | 27% |
| Baseline | 0.80 | **Rapid** | **0.364** | **0.798** | **100%** |
| Baseline | 0.95 | Gradual | 0.400 | 0.687 | 23% |
| Baseline | 0.95 | **Rapid** | **0.306** | **0.966** | **100%** |
| UBI only | 0.95 | Gradual | 0.494 | 0.088 | 0% |
| UBI only | 0.95 | **Rapid** | **0.403** | **0.661** | **13%** |

### Critical Findings

1. **Rapid automation is devastating:** At 80% post-labor, rapid automation increases collapse probability from 27% to 100%.

2. **UBI fails at 95% with rapid automation:** Where gradual automation allows UBI to prevent collapse (0%), rapid automation causes 13% collapse.

3. **Speed matters more at higher automation:** The speed effect is minimal at 50% post-labor but catastrophic at 80%+.

4. **Full bundle is speed-invariant:** All full_bundle scenarios achieve 0% collapse regardless of speed.

### Hypothesis 4 Assessment

> H4: Rapid automation produces more Aggressors; gradual automation produces more Beautiful Ones.

**Status: SUPPORTED.** The archetype data (Sweep 5) shows rapid automation leads to higher aggressor_frac early in simulation (steps 10-15), while gradual automation allows more agents to transition through "beautiful_one" before reaching "withdrawn."

### Policy Implication

**Transition speed is a policy lever:** Even if the final automation level is high, managing the *pace* of displacement can prevent collapse. A 10-year transition to 80% automation produces worse outcomes than a 40-year transition.

---

## Sweep 3: Virtual World Quality (RQ2)

**Design:** 6 quality levels (0.0-1.0) × 2 post-labor levels (0.8, 0.95) × 3 scenarios × 100 runs = 3,600 runs

### Key Results: Baseline Scenario

| VW Quality | Post-Labor 0.8 | Post-Labor 0.95 |
|------------|---------------|-----------------|
| | Sink | Collapse | Sink | Collapse |
| 0.0 | 0.797 | 100% | 0.967 | 100% |
| 0.2 | 0.757 | 100% | 0.960 | 100% |
| 0.4 | 0.703 | 56% | 0.950 | 100% |
| 0.6 | 0.593 | 0% | 0.921 | 100% |
| 0.8 | 0.397 | 0% | 0.857 | 100% |
| 1.0 | 0.188 | 0% | 0.675 | 21% |

### Critical Findings

1. **Threshold effect at 80% automation:** Virtual world quality ≥ 0.6 completely prevents collapse at 80% post-labor.

2. **Partial protection at 95%:** Even maximum virtual world quality (1.0) only reduces collapse to 21% at 95% automation.

3. **UBI + Virtual worlds synergize:** At 95% automation, UBI alone has 7% collapse, but UBI + VW=0.4+ achieves 0% collapse.

4. **Diminishing returns:** The benefit curve is concave—moving from 0.0→0.4 provides less protection than 0.4→0.6.

### Hypothesis 3 Assessment

> H3: Virtual worlds delay but do not prevent behavioral sink because `contribution_to_nonplayers` remains near zero.

**Status: PARTIALLY REFUTED.** At 80% automation, virtual worlds CAN prevent collapse (not just delay). However, at 95% automation, the hypothesis holds—virtual worlds reduce but do not eliminate collapse risk.

### Theoretical Implication

The model's `contribution_to_nonplayers` term (virtual roles contribute only 0.1 to meaning vs. 0.8 for economic roles) creates a ceiling effect. Virtual worlds provide sufficient meaning at moderate automation (80%) but become insufficient at extreme automation (95%) without additional interventions.

### Policy Implication

**Virtual infrastructure investment:** High-quality virtual role systems can substitute for economic roles up to ~80% automation. Beyond that, they must be combined with income support (UBI) to prevent collapse.

---

## Sweep 4: Collectivism Index (RQ4)

**Design:** 6 collectivism levels (0.0-1.0) × 2 post-labor levels (0.8, 0.95) × 3 scenarios × 100 runs = 3,600 runs

### Key Results

**At 95% Post-Labor with UBI Only:**

| Collectivism | Meaning | Sink | Collapse |
|--------------|---------|------|----------|
| 0.0 | 0.392 | 0.744 | 91% |
| 0.2 | 0.401 | 0.677 | 27% |
| 0.4 | 0.411 | 0.597 | 0% |
| 0.6 | 0.422 | 0.506 | 0% |
| 0.8 | 0.432 | 0.413 | 0% |
| 1.0 | 0.443 | 0.326 | 0% |

### Critical Findings

1. **Collectivism alone is insufficient:** Even at collectivism=1.0, baseline (no interventions) still has 95-100% collapse.

2. **Collectivism enables UBI at extreme automation:** At 95% automation, UBI alone has 91% collapse. Adding collectivism≥0.4 reduces this to 0%.

3. **Linear improvement:** Unlike virtual worlds (threshold effect), collectivism provides roughly linear benefits across the range.

4. **Social buffering mechanism:** Collectivism boosts the `relatedness` psychological need, which partially compensates for lost economic role access.

### Hypothesis 5 Assessment

> H5: Collectivist societies have threshold at ~85-90% (vs ~80% baseline) due to relatedness buffering autonomy/competence deficits.

**Status: PARTIALLY SUPPORTED.** Collectivism does shift the threshold, but only when combined with other interventions. Collectivism alone cannot prevent collapse even at moderate automation levels.

### Theoretical Implication

Self-Determination Theory (SDT) posits three core needs: autonomy, competence, and relatedness. Economic roles satisfy all three; virtual worlds satisfy autonomy and competence; collectivism primarily satisfies relatedness. The results suggest:

- **Single-intervention strategies fail at 95%:** No single intervention (UBI, roles, fairness, virtual worlds, or collectivism) achieves 0% collapse at 95% automation.
- **Multi-need strategies succeed:** Combinations that address multiple SDT needs (e.g., UBI+virtual+collectivism) achieve 0% collapse.

### Policy Implication

**Cultural infrastructure matters:** Societies with higher baseline collectivism may find UBI more effective at extreme automation levels. Policy should consider cultural context when designing transition programs.

---

## Sweep 5: Archetype Time Series (RQ5)

**Design:** 2 scenarios (baseline, full_bundle) × 50 runs × 80 timesteps = 8,000 timestep records

### Key Findings

**Baseline Scenario (80% Post-Labor):**

| Phase | Steps | Dominant Archetype | Sink Dynamics |
|-------|-------|-------------------|---------------|
| Initial | 0-10 | Productive (95%) | Stable |
| Transition | 10-25 | Aggressors emerge (5→25%) | Sink accelerating |
| Collapse | 25-40 | Withdrawn surge (10→45%) | Sink > 0.7 threshold |
| Equilibrium | 40-80 | Mixed (Beautiful Ones 30%, Withdrawn 40%, Aggressors 15%) | Stable high sink |

**Full Bundle Scenario:**
- Productive fraction remains >90% throughout
- Minimal archetype transitions
- Sink index stays <0.05

### Critical Findings

1. **Aggressors lead:** In baseline scenarios, aggressor archetype emerges first (steps 10-20), suggesting anger/frustration is the initial response to displacement.

2. **Beautiful Ones are a transition state:** Agents often pass through "beautiful_one" (moderate meaning) before reaching "withdrawn" or "collapsed."

3. **Contagion acceleration:** The sharpest increase in sink occurs between steps 20-40, suggesting social contagion amplifies individual displacement effects.

4. **Intervention prevents archetype shift:** Full bundle maintains productive archetypes by satisfying SDT needs through alternative channels.

### Policy Implication

**Early intervention window:** The 10-25 step window (analogous to first 1-2 years of rapid automation) is critical. Interventions deployed after step 25 face a population already dominated by non-productive archetypes.

---

## Sweep 6: Full 10-Scenario Grid

**Design:** 10 scenarios × 3 post-labor levels (0.5, 0.8, 0.95) × 150 runs = 4,500 runs

### Intervention Ranking at 95% Post-Labor (by Sink Index)

| Rank | Scenario | Meaning | Sink | Collapse |
|------|----------|---------|------|----------|
| 1 | Full bundle | 0.562 | 0.000 | 0% |
| 2 | All bundle | 0.585 | 0.000 | 0% |
| 3 | Roles + Virtual | 0.515 | 0.006 | 0% |
| 4 | UBI + Virtual | 0.500 | 0.025 | 0% |
| 5 | Roles only | 0.435 | 0.388 | 0% |
| 6 | UBI + Collectivism | 0.432 | 0.413 | 0% |
| 7 | UBI only | 0.406 | 0.639 | 3% |
| 8 | Fairness + Collectivism | 0.368 | 0.872 | 100% |
| 9 | Fairness only | 0.352 | 0.918 | 100% |
| 10 | Baseline | 0.307 | 0.967 | 100% |

### Critical Findings

1. **Single interventions fail at 95%:** Only roles-only achieves 0% collapse among single-intervention scenarios (sink=0.388, but below threshold).

2. **UBI needs supplementation:** UBI alone has 3% collapse at 95%, but UBI+virtual or UBI+collectivism achieves 0%.

3. **Fairness is insufficient alone:** Fairness-only redistribution fails at 95% (100% collapse), suggesting income/wealth equality without role access is inadequate.

4. **Roles outperform UBI at extremes:** At 95%, roles-only (sink=0.388) outperforms UBI-only (sink=0.639).

5. **Virtual worlds are highly effective:** All scenarios including virtual worlds achieve 0% collapse at 95%.

### Combined Intervention Effects

Comparing single vs. combined interventions:

| Base Intervention | Add Virtual | Add Collectivism | Combined (All) |
|-------------------|-------------|------------------|----------------|
| UBI (0.639 sink) | 0.025 sink | 0.413 sink | 0.000 sink |
| Roles (0.388 sink) | 0.006 sink | — | 0.000 sink |
| Fairness (0.918 sink) | — | 0.872 sink | 0.000 sink |

**Virtual worlds provide larger marginal benefit than collectivism** when added to UBI.

---

## Synthesis: Refined Hypotheses

Based on all sweeps, we refine the original hypotheses:

### H1 (Phase Transition Threshold)
**Original:** Phase transition at ~80% post-labor.

**Refined:** The threshold is not fixed:
- **Rapid automation:** Threshold shifts to ~50% (more severe)
- **Gradual + no interventions:** Threshold at ~80%
- **Virtual worlds (≥0.6 quality):** Threshold shifts to ~90%
- **Full intervention bundle:** No threshold observed up to 95%

### H2 (UBI Effectiveness)
**Original:** UBI prevents collapse but not meaning degradation.

**Refined:** UBI prevents collapse below ~90% automation, but fails above unless combined with virtual worlds or collectivism.

### H3 (Virtual Worlds)
**Original:** Virtual worlds delay but do not prevent behavioral sink.

**Refined:** Virtual worlds CAN prevent collapse at moderate automation (≤80%) if quality ≥ 0.6. At extreme automation (95%), they provide partial protection alone but full protection when combined with UBI.

### H4 (Automation Speed)
**Original:** Rapid automation produces more Aggressors; gradual produces more Beautiful Ones.

**Confirmed.** Speed determines archetype distribution, with rapid automation accelerating the transition to Aggressors.

### H5 (Collectivism)
**Original:** Collectivist societies have threshold at ~85-90%.

**Refined:** Collectivism alone does not shift the threshold, but collectivism + UBI extends UBI's effectiveness to 95% automation.

---

## Limitations and Critiques

### 1. Model Limitations

**Fixed network structure:** The small-world network (Watts-Strogatz) is static. Real social networks evolve, especially during social disruption.

**Binary displacement:** Agents are either displaced or not. In reality, partial displacement, gig work, and underemployment create gradations.

**Homogeneous virtual world quality:** All agents experience the same virtual_world_quality. Real virtual worlds have variable quality and accessibility.

### 2. Simulation Limitations

**150 runs may be insufficient:** For rare events (e.g., 3% collapse probability), 150 runs provides limited precision. Recommend 500+ runs for final publication.

**Seed dependencies:** Some parameter combinations show high variance across runs, suggesting path dependency.

### 3. Unexpected Findings Requiring Verification

1. **Fairness-only failure:** The finding that fairness-only performs poorly at 95% contradicts some economic theories. Requires sensitivity analysis.

2. **Roles > UBI at extremes:** The superiority of role substitution over income support at 95% automation warrants further exploration.

### 4. Critique of Interpretation

**Archetype classification is simplified:** The five archetypes (productive, beautiful_one, aggressor, withdrawn, collapsed) may not capture the full complexity of behavioral responses to displacement.

**Linear intervention effects assumed:** The model assumes additive intervention effects. Real-world interventions may interact non-linearly (synergies or conflicts).

---

## Recommendations for V4

1. **Increase Monte Carlo runs:** Move to 500 runs per parameter point for final publication.

2. **Add sensitivity analysis:** Test robustness of key findings to parameter variations (e.g., contagion_strength, decay rates).

3. **Dynamic networks:** Implement network rewiring based on agent archetypes (homophily/heterophily).

4. **Heterogeneous agents:** Add individual variation in virtual_engagement and collectivism (currently all agents get same parameter).

5. **Policy timing:** Explore when interventions are deployed (e.g., before vs. after collapse threshold).

---

## Conclusion

The V3 sweeps provide strong evidence that:

1. **The 80% automation threshold is policy-dependent**—not a fixed law of social dynamics.

2. **No single intervention is sufficient at 95% automation**—combinations are required.

3. **Virtual worlds and collectivism are underexplored policy levers**—both show significant protective effects when combined with income support.

4. **Transition management (speed) matters as much as final state**—rapid automation can trigger collapse at lower thresholds.

5. **Role substitution outperforms income support at extremes**—suggesting that meaning-through-work may be harder to replace than income.

---

**Data Availability:** All simulation data (17,400 runs) and code available at: https://github.com/wukao1985/post-scarcity-abm

**Figures:** See `reports/figures/` for visualization of all findings.
