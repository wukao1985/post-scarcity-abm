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
| `automation_speed` | 0.03 default (variable in sweeps) | Convenience/sensitivity-tested |
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

**Status: Placeholder -- formal analysis pending V4 validation sweep completion.**

A formal sensitivity analysis will perturb the top candidate parameters by +/-20% and measure the effect on three outcome variables: mean meaning index, sink index, and collapse probability (fraction of runs with sink_index > 0.7 at step 80).

### Candidate parameters for sensitivity testing

| Parameter | Baseline | -20% | +20% | Expected sensitivity |
|-----------|----------|------|------|---------------------|
| `noise_sigma` | 0.08 | 0.064 | 0.096 | High -- controls between-run variance and tail risk of collapse |
| `decay` | 0.08 | 0.064 | 0.096 | Medium -- affects equilibration speed and transient dynamics |
| `contagion_strength` | 0.5 | 0.4 | 0.6 | High -- governs positive feedback loop in behavioral sink |
| `base_floor` | 0.32 | 0.256 | 0.384 | High -- sets the minimum functioning level, directly affects collapse threshold distance |

### Protocol (planned)

- 150 runs per parameter point (per CLAUDE.md Monte Carlo minimum)
- Fixed scenario: 80% post-labor, baseline (no intervention)
- One-at-a-time (OAT) perturbation with all other parameters held at baseline
- Report: tornado diagram showing delta in mean sink_index at step 80
- If resources permit, a Sobol global sensitivity analysis across all four parameters simultaneously

### Preliminary observations

From existing sweep results (Sweeps 1-6, 4500+ runs), the model shows qualitative sensitivity to:
- **contagion_strength**: Higher values produce sharper phase transitions between stable and collapsed states
- **noise_sigma**: The V4 increase from 0.02 to 0.08 substantially widened the distribution of outcomes, reducing the frequency of deterministic-looking trajectories
- **base_floor**: At 0.32, the floor is 0.38 units below the collapse threshold (meaning=0.30 for "collapsed" archetype), providing enough dynamic range for meaningful variation

---

*This appendix documents model V4 as implemented in `models/pathway_a_abm/model.py`. Parameter values are exact as coded; justification categories reflect the authors' honest assessment of theoretical grounding.*
