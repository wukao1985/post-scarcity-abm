# Sweep 4 Analysis: Collectivism Index Effects

## Overview

Sweep 4 tested whether collectivist social structures provide resilience against behavioral sink. Variable: `collectivism_index` ∈ [0.0, 0.2, 0.4, 0.6, 0.8, 1.0], crossed with 2 post-labor levels (0.8, 0.95) and 3 scenarios (baseline, UBI, full_bundle). 3,600 total runs.

## Key Findings

### 1. Collectivism Has a Weak Direct Effect

At baseline, increasing collectivism from 0.0 to 1.0 barely moves the needle:
- PL=0.80: sink drops from 0.816 to 0.735, meaning rises from 0.356 to 0.387
- PL=0.95: sink drops from 0.971 to 0.956, meaning rises from 0.299 to 0.326
- Collapse remains at 100% for all baseline conditions at PL=0.80 (drops to 95% only at collectivism=1.0)

**This fails to support H5** (collectivist societies have threshold at ~85-90%). The phase transition threshold doesn't meaningfully shift. Collectivism adds ~3% to meaning and reduces sink by ~8% — insufficient to prevent collapse on its own.

### 2. Collectivism is a Critical Moderator of UBI Effectiveness

The most important finding: **collectivism dramatically moderates UBI's effectiveness at extreme displacement**.

At PL=0.95 with UBI_only:
| Collectivism | Collapse Rate | Sink Index | Meaning |
|-------------|---------------|------------|---------|
| 0.0 | **91%** | 0.744 | 0.392 |
| 0.2 | **27%** | 0.677 | 0.401 |
| 0.4 | 0% | 0.597 | 0.411 |
| 0.6 | 0% | 0.506 | 0.422 |
| 0.8 | 0% | 0.413 | 0.432 |
| 1.0 | 0% | 0.326 | 0.443 |

UBI goes from 91% collapse (individualist society) to 0% collapse (collectivist) at PL=0.95. This is a phase transition in the interaction of policy and social structure. The threshold appears between collectivism 0.2-0.4.

### 3. UBI + Collectivism Mimics Full Bundle

At PL=0.95, UBI + collectivism=0.8 produces sink=0.413, which is better than UBI alone (0.635) and approaches roles_only performance. Collectivism substitutes for formal role programs by providing relational meaning.

### 4. Full Bundle is Robust to Collectivism Variation

Full bundle performs well regardless of collectivism (meaning range: 0.554-0.606). This suggests the full intervention package has enough redundancy to work in both individualist and collectivist societies.

## Critical Evaluation

### What's Problematic

1. **Linear mechanism**: Collectivism enters the model as a flat additive term in the relatedness target (+0.10 × collectivism_index). This is far too simple. Real collectivism affects social norms, group identity, shame/honor dynamics, intergenerational obligation, and institutional trust. Our "collectivism" is really just "slightly higher baseline relatedness."

2. **No collectivism downsides**: Collectivist societies also exhibit conformity pressure, reduced individual agency, out-group hostility, and resistance to individual-level interventions. None of these are modeled. The results are thus biased toward showing collectivism as purely beneficial.

3. **Independence from UBI mechanism unclear**: The interaction between collectivism and UBI in the model comes solely through the relatedness channel. UBI provides economic floor → less economic distress. Collectivism provides relational floor → less social distress. They're additive because they address orthogonal needs. But in reality, UBI in a collectivist society might reduce work motivation more (if collective shame around unemployment is weaker), or reduce help-seeking behavior (if it replaces mutual aid networks). These dynamics are absent.

### The 91% → 0% UBI Collapse Rate Finding

This is the headline finding but I'm skeptical of its magnitude. The mechanism is: at collectivism=0.0, relatedness target has +0.0 collectivism bonus, so relatedness drops more, meaning drops more, more agents fall below the 0.70 sink threshold. At collectivism=1.0, the +0.10 bonus keeps relatedness ~0.10 higher, which propagates through meaning calculation.

But +0.10 in relatedness → +0.025 in meaning (0.25 × 0.10). A 2.5% shift in meaning shouldn't cause a 91-percentage-point shift in collapse. This sensitivity comes from being near the phase transition boundary — small changes in mean meaning cross the archetype threshold, causing cascading state changes via contagion. This is characteristic of phase transitions but also means the quantitative results are threshold-dependent artifacts.

## Summary Table

| Collectivism | PL | Scenario | Meaning | Sink | Collapse |
|-------------|-----|----------|---------|------|----------|
| 0.0 | 0.80 | baseline | 0.356 | 0.816 | 100% |
| 1.0 | 0.80 | baseline | 0.387 | 0.735 | 95% |
| 0.0 | 0.80 | ubi_only | 0.455 | 0.303 | 0% |
| 1.0 | 0.80 | ubi_only | 0.494 | 0.085 | 0% |
| 0.0 | 0.95 | ubi_only | 0.392 | 0.744 | **91%** |
| 0.4 | 0.95 | ubi_only | 0.411 | 0.597 | **0%** |
| 1.0 | 0.95 | ubi_only | 0.443 | 0.326 | 0% |

## Figures

1. `sweep4_collectivism_curves.png` — Collectivism effect on all metrics
2. `sweep4_ubi_collectivism_interaction.png` — UBI × collectivism interaction (key finding)
3. `sweep4_collectivism_heatmap.png` — Collectivism × scenario heatmap
4. `sweep4_baseline_vs_ubi.png` — Direct vs. moderating effects
