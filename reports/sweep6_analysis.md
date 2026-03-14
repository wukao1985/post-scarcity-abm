# Sweep 6 Analysis: Full 10-Scenario Grid

## Overview

Sweep 6 is the definitive comparison: 10 intervention scenarios × 3 post-labor levels (0.5, 0.8, 0.95) × 150 runs = 4,500 runs. This provides the final evidence for policy recommendations.

## Results Summary

### At Post-Labor = 0.50 (Moderate Automation)

No scenario collapses. Even baseline has only 21.6% sink. All interventions work. This is below the phase transition threshold.

### At Post-Labor = 0.80 (Critical Threshold)

| Scenario | Meaning | Sink | Collapse |
|----------|---------|------|----------|
| baseline | 0.365 | 0.798 | **100%** |
| fairness | 0.418 | 0.594 | 0% |
| fairness+collectivism | 0.440 | 0.450 | 0% |
| ubi_only | 0.467 | 0.222 | 0% |
| UBI+collectivism | 0.486 | 0.122 | 0% |
| roles | 0.486 | 0.116 | 0% |
| UBI+virtual | 0.538 | 0.004 | 0% |
| roles+virtual | 0.551 | 0.001 | 0% |
| full_bundle | 0.588 | 0.000 | 0% |
| **all_bundle** | **0.611** | **0.000** | **0%** |

Key findings:
- Any single intervention prevents collapse at 0.80
- Virtual world combinations (UBI+VW, roles+VW) nearly eliminate sink entirely
- All_bundle achieves highest meaning (0.611) with zero sink

### At Post-Labor = 0.95 (Extreme Automation)

| Scenario | Meaning | Sink | Collapse |
|----------|---------|------|----------|
| baseline | 0.307 | 0.967 | **100%** |
| fairness | 0.352 | 0.918 | **100%** |
| fairness+collectivism | 0.368 | 0.872 | **100%** |
| ubi_only | 0.406 | 0.639 | **2.7%** |
| UBI+collectivism | 0.432 | 0.413 | 0% |
| roles | 0.435 | 0.388 | 0% |
| UBI+virtual | 0.500 | 0.025 | 0% |
| roles+virtual | 0.515 | 0.006 | 0% |
| full_bundle | 0.562 | 0.000 | 0% |
| **all_bundle** | **0.585** | **0.000** | **0%** |

Critical findings:
1. **Fairness alone fails at 0.95** — 100% collapse, even with collectivism added
2. **UBI is necessary but insufficient** — 2.7% collapse, high sink (0.639)
3. **Role programs outperform income support** — roles (sink=0.388) vs UBI (sink=0.639)
4. **Virtual worlds are a force multiplier** — adding VW to either UBI or roles dramatically reduces sink
5. **Only comprehensive packages achieve zero sink at 0.95**

## Policy-Relevant Findings

### 1. The Fairness Trap

Fairness-based redistribution (taxing AI gains, progressive wealth redistribution) **fails catastrophically at extreme automation**. Even with high collectivism (fairness+collectivism at PL=0.95 → 100% collapse). This is because fairness addresses inequality but not the fundamental loss of purpose, competence, and social role.

### 2. Roles > Income

Role programs consistently outperform income support:
- PL=0.95: roles (sink=0.388) vs UBI (0.639)
- PL=0.80: roles (sink=0.116) vs UBI (0.222)

This suggests that providing alternative sources of purpose, competence, and social recognition is more effective than providing economic security alone.

### 3. The Virtual World Multiplier

Adding virtual worlds to any intervention dramatically reduces sink:
- UBI+VW vs UBI alone at PL=0.95: sink drops 0.639 → 0.025
- Roles+VW vs roles alone at PL=0.95: sink drops 0.388 → 0.006

Virtual worlds appear to substitute for competence and partial relatedness needs that neither income nor traditional role programs can address.

### 4. Diminishing Returns of Comprehensiveness

All_bundle barely outperforms full_bundle:
- PL=0.95: all_bundle meaning=0.585 vs full_bundle 0.562 (+0.023)
- Both achieve zero sink and zero collapse

The marginal return of adding virtual worlds and collectivism to an already-comprehensive package is small.

## Critical Evaluation

### What's Too Clean

The results produce a perfectly ordered hierarchy at every post-labor level. No scenario outperforms expectations; no scenario shows unexpected weakness. In real policy, interventions interact in non-linear and sometimes paradoxical ways. Our model's additive structure (each intervention adds independent benefit) produces unrealistically monotonic results.

### The 100% Baseline Collapse

Baseline at PL=0.80 collapses 100% of the time (150/150 runs). This is not a finding — it's a consequence of the model sitting exactly at the phase transition with insufficient stochasticity. In reality, some societies at ~80% automation would find emergent adaptations.

### Fairness+Collectivism Still Collapses

This is the most surprising result and deserves scrutiny. Adding collectivism (from 0.3 to 0.8) to fairness at PL=0.95 does reduce sink (0.918→0.872) but not enough to prevent collapse. This is because fairness enters the model through `fairness` parameter (affecting autonomy and relatedness targets) while collectivism enters through relatedness only. Neither addresses the competence or status channels that drive the deepest sink.

### Missing Interactions

The model assumes interventions are additive. In reality:
- UBI might reduce work motivation (negative interaction with roles)
- Virtual worlds might displace real-world social connection (negative interaction with collectivism)
- Fairness perception might depend on who benefits from role programs (interaction between fairness and roles)

None of these interactions are modeled.

## Figures

1. `sweep6_grand_heatmap.png` — Complete 10×3 outcome matrix
2. `sweep6_scenario_ranking.png` — Scenario ranking at PL=0.95
3. `sweep6_intervention_decomposition.png` — Marginal intervention effects
4. `sweep6_meaning_violins.png` — Distribution of meaning at PL=0.95
