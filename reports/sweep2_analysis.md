# Sweep 2 Analysis: Automation Speed Effects

## Overview

Sweep 2 tested the effect of automation speed on behavioral sink outcomes. Two speeds were compared:
- **Gradual**: 0.01/step (reaches target post-labor level over ~80 steps)
- **Rapid**: 0.08/step (reaches target by ~step 10-12)

Crossed with 3 post-labor levels (0.5, 0.8, 0.95) and 5 intervention scenarios, for 3,000 total runs (100/point).

## Key Findings

### 1. Speed Matters — But Only Above the Phase Transition

At post-labor = 0.5, automation speed has negligible effects (meaning diff = -0.003, sink diff = +0.015). Below the ~80% threshold, the system absorbs displacement regardless of speed.

At post-labor = 0.8, rapid automation dramatically worsens outcomes:
- Baseline collapse rate: 27% (gradual) → **100% (rapid)**
- Meaning drops from 0.400 to 0.364
- Sink index rises from 0.686 to 0.798

At post-labor = 0.95, the divergence is extreme:
- UBI collapse rate: 0% (gradual) → **13% (rapid)**
- Baseline meaning: 0.400 → 0.306
- Baseline sink: 0.687 → 0.966

### 2. UBI Breaks Down Under Rapid + Extreme Displacement

This is the most policy-relevant finding. UBI alone prevents collapse under gradual automation at all levels, but at rapid/0.95, 13% of runs collapse and the sink index reaches 0.661. This suggests UBI's protective effect depends on having time for adaptation.

### 3. Full Bundle Remains Universally Protective

Full bundle (UBI + roles + fairness + status deconcentration) produces 0% collapse across ALL conditions, including rapid/0.95. However, meaning still degrades (0.600 → 0.561), suggesting even comprehensive intervention cannot fully insulate against rapid displacement.

### 4. Fairness Intervention is Speed-Sensitive

Fairness_only is the most speed-sensitive single intervention:
- At rapid/0.95: collapse rate = 100%, sink = 0.922
- At gradual/0.95: collapse rate = 0%, sink = 0.307

This makes conceptual sense: fairness-based interventions require time to redistribute gains.

## Critical Methodological Issues

### ARTIFACT: Gradual Speed Cap

**The gradual condition (0.01/step × 80 steps) can only reach a maximum automation level of 0.80.** Therefore, all gradual/0.95 results are actually gradual/0.80 results. The post_labor_current at the end of simulation confirms this (0.800 for both gradual/0.80 and gradual/0.95).

This means the gradual vs. rapid comparison at 0.95 is confounded: we're comparing a system that reaches 0.80 automation against one that reaches 0.95. The speed effect and the endpoint effect are entangled.

**Implication for interpretation**: The gradual/0.95 → rapid/0.95 comparison overstates the speed effect because it also includes 15 percentage points more total displacement. A fairer comparison would use a gradual speed that actually reaches 0.95 (e.g., 0.012/step), or compare at 0.80 only.

### Excessive Determinism

Cohen's d values range from 8 to 48 across conditions. For context, d > 2 is rarely seen in behavioral science. This suggests the model's stochastic elements (noise terms, random displacement) are far too small relative to the deterministic dynamics.

The standard deviation of meaning index across 100 runs is typically 0.002 (range: 0.0015 to 0.0032). This means 100 runs of what is nominally a stochastic model produce results that vary by less than 1%. The mean-reverting dynamics with decay=0.08 and small noise (σ=0.02) dominate.

**This is a limitation**: The model gives false precision. The narrow confidence intervals are artifacts of insufficient stochasticity, not evidence of robust findings. Real social systems would show much more variance.

### Missing Aggressors

Aggressor fraction ranges from 0.0 to 0.03 across all conditions. The archetype classification makes it very difficult to become an aggressor (requires meaning < 0.40 AND aggression_drive > 0.3). In practice, collapsed and withdrawn agents dominate the sink, with "beautiful ones" as a large intermediate category. This limits our ability to test H4 (speed determines archetype distribution).

## Summary Statistics

| Speed | PL | Scenario | Meaning | Sink | Collapse |
|-------|-----|----------|---------|------|----------|
| Gradual | 0.50 | baseline | 0.499 | 0.203 | 0% |
| Rapid | 0.50 | baseline | 0.496 | 0.218 | 0% |
| Gradual | 0.80 | baseline | 0.400 | 0.686 | 27% |
| Rapid | 0.80 | baseline | 0.364 | 0.798 | **100%** |
| Gradual | 0.95 | baseline | 0.400* | 0.687* | 23%* |
| Rapid | 0.95 | baseline | 0.306 | 0.966 | **100%** |
| Gradual | 0.80 | ubi_only | 0.494 | 0.085 | 0% |
| Rapid | 0.80 | ubi_only | 0.467 | 0.228 | 0% |
| Gradual | 0.95 | ubi_only | 0.494* | 0.088* | 0%* |
| Rapid | 0.95 | ubi_only | 0.403 | 0.661 | **13%** |
| Gradual | 0.80 | full_bundle | 0.600 | 0.000 | 0% |
| Rapid | 0.80 | full_bundle | 0.588 | 0.000 | 0% |
| Gradual | 0.95 | full_bundle | 0.600* | 0.000* | 0%* |
| Rapid | 0.95 | full_bundle | 0.561 | 0.000 | 0% |

*Gradual/0.95 = gradual/0.80 due to speed cap artifact

## Figures

1. `sweep2_speed_baseline.png` — Speed effect on baseline outcomes
2. `sweep2_speed_scenario_heatmap.png` — Speed × scenario interaction heatmap
3. `sweep2_speed_effect_size.png` — Effect sizes (rapid − gradual) by scenario
4. `sweep2_archetypes_by_speed.png` — Archetype distributions by speed
5. `sweep2_intervention_robustness.png` — Intervention collapse rates under rapid vs gradual

## Conclusions

1. Automation speed is a critical moderating variable, but only at high displacement levels
2. UBI is necessary but not sufficient under rapid automation at extreme levels
3. Only comprehensive intervention packages remain robust across all speed conditions
4. **The gradual/0.95 artifact must be disclosed in any publication**
5. **Model variance is unrealistically low — consider increasing noise terms**
