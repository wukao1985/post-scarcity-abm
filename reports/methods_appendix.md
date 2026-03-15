# Methods Appendix: Post-Scarcity ABM (V4)

## 1. Parameter Table

| Parameter | Value | Justification |
|-----------|-------|---------------|
| `n_agents` | 200 | Convenience/sensitivity-tested |
| `time_horizon` | 80 steps | Convenience/sensitivity-tested |
| `decay` | 0.08 | Calhoun calibration -- produces equilibration in ~30 steps |
| `noise_sigma` | 0.08 | Calhoun calibration -- V4 recalibration for realistic between-run variance (increased from 0.02) |
| `base_floor` | 0.32 | Calhoun calibration -- minimum human functioning floor |
| `agent_shock_sigma` | 0.03 | Convenience/sensitivity-tested -- per-step idiosyncratic life-event noise |
| Network type | Watts-Strogatz | Calhoun calibration -- small-world structure |
| Network `k` | 6 | Calhoun calibration |
| Network `p` | 0.1 | Calhoun calibration |
| `contagion_strength` | 0.5 | Calhoun calibration |
| Profile distribution | 15% resilient, 55% balanced, 30% vulnerable | Convenience/sensitivity-tested |
| Resilient profile | resilience=0.8, social_capital=0.7, skill_transfer=0.7 | Convenience/sensitivity-tested |
| Balanced profile | resilience=0.5, social_capital=0.5, skill_transfer=0.5 | Convenience/sensitivity-tested |
| Vulnerable profile | resilience=0.2, social_capital=0.3, skill_transfer=0.3 | Convenience/sensitivity-tested |
| Profile initialization noise | N(0, 0.05) per trait | Convenience/sensitivity-tested |
| Initial psychological state | autonomy/competence ~ N(0.55, 0.08); relatedness/status ~ N(0.50, 0.08) | Convenience/sensitivity-tested |
| Collapse threshold | sink_index > 0.7 | Calhoun calibration |
| Post-labor targets tested | 0.0 to 0.95 | SDT theory -- spans full automation range |
| `automation_speed` | 0.03 default; 0.006–0.20 in speed comparison sweep | Convenience/sensitivity-tested |
| `collectivism_index` | 0.3 default (variable in sweeps) | Convenience/sensitivity-tested |
| UBI economic floor | displaced role = ubi * 0.30 + roles_program * 0.35 | Convenience/sensitivity-tested |

## 2. Meaning Function Weights

The composite meaning index is computed as:

```
meaning = 0.25 * autonomy + 0.25 * competence + 0.25 * relatedness
        + 0.10 * status + 0.15 * contribution
```

where:

```
contribution = economic_role * 0.8 + virtual_role * 0.1
```

During the step update, meaning also incorporates contagion and resilience adjustments:

```
meaning_step = [weighted sum above] - contagion * 0.08 + 0.08 * resilience
```

### Theoretical grounding

| Weight | Component | Source | Rationale |
|--------|-----------|--------|-----------|
| 0.25 | Autonomy | SDT theory (Deci & Ryan, 2000) | Core psychological need; equal weighting across the three SDT needs |
| 0.25 | Competence | SDT theory (Deci & Ryan, 2000) | Core psychological need; equal weighting across the three SDT needs |
| 0.25 | Relatedness | SDT theory (Deci & Ryan, 2000) | Core psychological need; equal weighting across the three SDT needs |
| 0.10 | Status | Researcher choice | Not a core SDT need, but empirically relevant to well-being in hierarchical societies; reduced weight reflects secondary importance |
| 0.15 | Contribution | Researcher choice | Captures the "mattering" dimension -- the sense that one's actions have impact. Not part of SDT proper but supported by eudaimonic well-being literature |

### Contribution sub-weights

| Sub-weight | Component | Source | Rationale |
|------------|-----------|--------|-----------|
| 0.80 | `economic_role` | Researcher choice | Assumes that real-world productive roles provide substantially more felt contribution than virtual substitutes |
| 0.10 | `virtual_role` | Researcher choice | Virtual roles provide partial but limited meaning substitution. The 8:1 ratio with economic role is an assumption, not empirically calibrated |

### Transparency note

The three SDT weights (0.25 each, summing to 0.75) are grounded in Self-Determination Theory's claim that autonomy, competence, and relatedness are equally fundamental psychological needs. The status and contribution weights (0.10 and 0.15) are researcher choices that allocate the remaining 0.25 of the index. The 8:1 ratio between economic and virtual contribution is an assumption reflecting the hypothesis that traditional productive roles carry substantially more meaning than virtual substitutes -- this is a testable claim, not an established finding.

## 3. Archetype Transition Rules

Archetypes are reassigned every step based on current meaning and behavioral state. The classification is evaluated top-down (first match wins):

```
aggression_drive = (1 - meaning) * (1 - social_capital) * 0.5
```

| Priority | Archetype | Condition | Calhoun Analogue |
|----------|-----------|-----------|------------------|
| 1 | **productive** | `meaning > 0.55` | Normal functioning adults |
| 2 | **aggressor** | `meaning < 0.40` AND `aggression_drive > 0.3` | "Somnambulists" / aggressive males |
| 3 | **beautiful_one** | `meaning > 0.42` (and not aggressive) | "Beautiful ones" -- passive, well-groomed, socially disengaged |
| 4 | **withdrawn** | `meaning > 0.30` (and not aggressive) | Socially withdrawn individuals |
| 5 | **collapsed** | `meaning <= 0.30` | Complete behavioral breakdown |

### Notes on classification logic

- The aggression check at priority 2 means agents with low meaning but high social capital will not become aggressors (social capital buffers aggression via the `(1 - social_capital)` term).
- "Beautiful one" occupies a narrow band (0.42 < meaning <= 0.55) representing agents who maintain surface functioning but have lost productive engagement.
- The sink index counts aggressors + withdrawn + collapsed as the dysfunctional fraction.
- Archetype assignment is memoryless: agents transition freely each step based on current state, with no hysteresis or lock-in.

## 4. Network Structure

**Type:** Watts-Strogatz small-world graph
**Parameters:** n=200, k=6, p=0.1, seed-controlled

### Rationale

Watts-Strogatz graphs were chosen because they reproduce two key properties of real social networks:

1. **High clustering** -- most of your friends know each other (local triadic closure), as in neighborhood or workplace networks.
2. **Short path lengths** -- any two individuals are connected by a small number of intermediaries (the "small world" property).

The specific parameters:

- **k=6** (each node connected to 6 nearest neighbors): Produces a mean degree of 6, consistent with estimates of close social ties ("support clique" size of 5-7 in Dunbar's social brain hypothesis).
- **p=0.1** (rewiring probability): A low rewiring rate preserves local clustering while introducing enough long-range links for information/contagion to spread globally. At p=0.1, the graph retains ~80% of the clustering of a regular lattice while achieving path lengths close to a random graph.
- **Seed-controlled**: The network is generated with the model seed, ensuring identical topology across runs with the same seed for reproducibility.

### Contagion mechanism

Neighbors influence agents through `sink_exposure`, the fraction of neighbors in aggressor, collapsed, or withdrawn states. This is scaled by `contagion_strength` (0.5) and applied as a negative pressure on all four psychological dimensions plus the meaning index directly.

## 5. Sensitivity Analysis

One-at-a-time (OAT) perturbation of the top 3 internal parameters by ±20%, with 50 runs per condition at PL=0.80 and PL=0.95 baseline (no intervention). All other parameters held at defaults.

### Results

| Parameter | Level | Value | PL | Meaning (±SD) | Sink (±SD) | Collapse |
|-----------|-------|-------|----|---------------|------------|----------|
| noise_sigma | default | 0.080 | 0.80 | 0.382 ±0.008 | 0.629 ±0.036 | 2% |
| noise_sigma | -20% | 0.064 | 0.80 | 0.376 ±0.008 | 0.661 ±0.035 | 10% |
| noise_sigma | +20% | 0.096 | 0.80 | 0.391 ±0.009 | 0.600 ±0.038 | 2% |
| noise_sigma | default | 0.080 | 0.95 | 0.330 ±0.008 | 0.788 ±0.026 | 100% |
| noise_sigma | -20% | 0.064 | 0.95 | 0.321 ±0.007 | 0.828 ±0.023 | 100% |
| noise_sigma | +20% | 0.096 | 0.95 | 0.342 ±0.008 | 0.744 ±0.026 | 92% |
| decay | default | 0.080 | 0.80 | 0.382 ±0.008 | 0.629 ±0.036 | 2% |
| decay | -20% | 0.064 | 0.80 | 0.389 ±0.009 | 0.606 ±0.035 | 2% |
| decay | +20% | 0.096 | 0.80 | 0.378 ±0.007 | 0.648 ±0.034 | 6% |
| decay | default | 0.080 | 0.95 | 0.330 ±0.008 | 0.788 ±0.026 | 100% |
| decay | -20% | 0.064 | 0.95 | 0.340 ±0.009 | 0.749 ±0.028 | 94% |
| decay | +20% | 0.096 | 0.95 | 0.324 ±0.007 | 0.814 ±0.024 | 100% |
| contagion | default | 0.500 | 0.80 | 0.382 ±0.008 | 0.629 ±0.036 | 2% |
| contagion | -20% | 0.400 | 0.80 | 0.391 ±0.008 | 0.605 ±0.036 | 2% |
| contagion | +20% | 0.600 | 0.80 | 0.373 ±0.008 | 0.657 ±0.037 | 12% |
| contagion | default | 0.500 | 0.95 | 0.330 ±0.008 | 0.788 ±0.026 | 100% |
| contagion | -20% | 0.400 | 0.95 | 0.341 ±0.008 | 0.759 ±0.024 | 96% |
| contagion | +20% | 0.600 | 0.95 | 0.319 ±0.008 | 0.812 ±0.025 | 100% |

### Robustness summary

**Core finding is robust to ±20% parameter perturbation:**

- At PL=0.95, collapse occurs in 92-100% of runs across all perturbations. Minimum sink index: 0.744.
- At PL=0.80, collapse remains rare (2-12%) across all perturbations. Sink index range: 0.600-0.661.
- The phase transition zone (80-90%) is directionally stable: no perturbation moves PL=0.80 into reliable collapse territory or PL=0.95 into non-collapse territory.

**Most sensitive parameter:** `contagion_strength` produces the largest swing at PL=0.80 (2% → 12% collapse at +20%). This is expected since contagion governs the positive feedback loop that drives collective collapse.

**Least sensitive parameter:** `decay` produces the smallest effects, consistent with its role as an equilibration speed rather than a structural driver.

### Limitations

- OAT analysis does not capture parameter interactions (e.g., high noise + high contagion)
- 50 runs per condition (not the 150 used in primary sweeps) -- adequate for directional conclusions but wider CIs
- `base_floor` not tested in this round (hardcoded deeper in agent psychology; requires more invasive patching)

---

*This appendix documents model V4 as implemented in `models/pathway_a_abm/model.py`. Parameter values are exact as coded; justification categories reflect the authors' honest assessment of theoretical grounding.*
