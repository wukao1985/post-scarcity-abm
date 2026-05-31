# Sweep 3 Analysis: Virtual World Quality Effects

## Overview

Sweep 3 tested whether high-quality virtual role substitutes (games, online communities, virtual work) can prevent behavioral sink. Variable: `virtual_world_quality` ∈ [0.0, 0.2, 0.4, 0.6, 0.8, 1.0], crossed with 2 post-labor levels (0.8, 0.95) and 3 scenarios (baseline, UBI, full_bundle). 3,600 total runs.

## Key Findings

### 1. Virtual Worlds Create a Phase Transition at PL=0.80

At post-labor = 0.80, baseline collapse rate drops from 100% (VW=0.0) through a sharp transition:
- VW=0.0: 100% collapse, sink=0.797
- VW=0.2: 100% collapse, sink=0.757
- VW=0.4: **56% collapse**, sink=0.704 (transition zone)
- VW=0.6: **0% collapse**, sink=0.593
- VW=0.8: 0% collapse, sink=0.397
- VW=1.0: 0% collapse, sink=0.188

This is a genuine phase transition in the VW=0.4-0.6 range where collapse probability drops from 56% to 0%. Virtual worlds appear to shift the effective phase transition threshold upward.

### 2. Virtual Worlds Cannot Prevent Collapse at PL=0.95 Without Policy

Even at VW=1.0 (perfect virtual worlds), baseline collapse rate at PL=0.95 is still 21%, and sink index is 0.675. This directly supports H3: virtual worlds delay but cannot fully prevent behavioral sink because `contribution_to_nonplayers` remains near zero.

The meaning gap at PL=0.95 baseline: VW=0.0 gives meaning=0.307, VW=1.0 gives meaning=0.403 — a gain of +0.096, but still below the productive threshold (0.55).

### 3. VW + UBI is Highly Effective

UBI + high virtual worlds is a powerful combination:
- PL=0.80, VW=0.8: meaning=0.539, sink=0.004, collapse=0%
- PL=0.95, VW=0.8: meaning=0.500, sink=0.026, collapse=0%

Compare with UBI alone at PL=0.95: meaning=0.406, sink=0.635, collapse=7%. Adding VW=0.8 to UBI nearly eliminates the sink at extreme displacement. This suggests virtual worlds are more effective as a complement to income support than as a standalone intervention.

### 4. Full Bundle Shows Ceiling Effect

Full bundle already prevents collapse at all VW levels. Adding VW to full_bundle increases meaning by only +0.013 (0.588→0.601 at PL=0.8). The intervention package has already addressed the needs that VW would satisfy. This ceiling effect suggests diminishing returns from adding more interventions to an already-comprehensive package.

### 5. Marginal Returns Are Non-Linear

The marginal meaning gain from each 0.2 increment of VW is not constant:
- For baseline at PL=0.8: gains are roughly constant (~0.022/increment) across the range
- For baseline at PL=0.95: gains are also roughly constant (~0.019/increment)
- For UBI at PL=0.8: gains diminish at high VW (ceiling near UBI's protective maximum)

## Critical Evaluation

### What's Surprising
The baseline phase transition at PL=0.8 (collapse drops from 100% to 0% between VW=0.4 and VW=0.6) is sharper than expected. This is likely driven by the threshold in the archetype classification: agents shifting from withdrawn (meaning 0.30-0.42) to beautiful_one (meaning 0.42-0.55) category, which removes them from the sink index. The transition is at least partly an artifact of the discrete archetype thresholds, not a smooth biological transition.

### What's Concerning
1. **VW model simplicity**: Virtual worlds only affect competence (via `virtual_role * vw_quality`) and relatedness (via flat `+0.05 * vw_quality`). There's no endogenous choice by agents between virtual and real-world engagement, no addiction/escapism dynamics, no quality heterogeneity. The model treats VW as pure positive, which biases results optimistically.

2. **No negative externalities**: Real virtual world engagement has documented negative effects (social isolation from in-person networks, sedentary health risks, parasocial relationship substitution). The model's virtual worlds have no downside, which limits policy applicability.

3. **Contribution dimension underweighted**: The meaning function weights contribution at only 0.15, and virtual contribution at 0.1×0.15 = 0.015 of total meaning. This is too small to create the meaning crisis that H3 predicts. The model structurally underestimates the importance of genuine contribution.

### Stochasticity Note
Standard deviations are slightly improved (0.002-0.004 for meaning) but still very low relative to between-condition effects. The model remains far too deterministic.

## Summary Table

| VW Quality | PL | Scenario | Meaning | Sink | Collapse |
|-----------|-----|----------|---------|------|----------|
| 0.0 | 0.80 | baseline | 0.365 | 0.797 | 100% |
| 0.4 | 0.80 | baseline | 0.396 | 0.704 | 56% |
| 0.6 | 0.80 | baseline | 0.418 | 0.593 | 0% |
| 1.0 | 0.80 | baseline | 0.479 | 0.188 | 0% |
| 0.0 | 0.95 | baseline | 0.307 | 0.967 | 100% |
| 1.0 | 0.95 | baseline | 0.403 | 0.675 | **21%** |
| 0.0 | 0.95 | ubi_only | 0.406 | 0.635 | 7% |
| 0.8 | 0.95 | ubi_only | 0.500 | 0.026 | 0% |
| 1.0 | 0.95 | ubi_only | 0.521 | 0.004 | 0% |

## Figures

1. `sweep3_vw_quality_curves.png` — VW quality effect on all metrics
2. `sweep3_vw_collapse_threshold.png` — Phase transition visualization
3. `sweep3_vw_scenario_heatmap.png` — VW × scenario interaction
4. `sweep3_vw_marginal_returns.png` — Diminishing returns analysis
