# ODD Protocol: Post-Labor Behavioral Sink ABM

Following the ODD (Overview, Design concepts, Details) protocol for describing agent-based models (Grimm et al., 2020).

---

## 1. Purpose

The model investigates what population-level equilibrium states emerge when large fractions of a society lack productive economic roles. It characterizes how displacement level, intervention regime, cultural context, and virtual role quality interact to determine whether a population reaches behavioral sink (withdrawal, aggression, collapse) or maintains functional states. The model is designed to explore mechanism-level dynamics, not to forecast specific technological timelines or displacement levels.

**Primary research questions:**
1. At what displacement level does the population equilibrium shift to behavioral sink, and is this threshold policy-malleable?
2. Can high-quality virtual worlds substitute for economic roles in providing meaning?
3. Does the speed of displacement affect the equilibrium reached?
4. Do collectivist vs. individualist cultural structures produce different equilibria?
5. What intervention combinations sustain favorable equilibria at extreme (≥90%) displacement?

---

## 2. Patterns

The model is designed to reproduce the following macroscopic patterns observed in or hypothesized from empirical and theoretical literature:

1. **Sink threshold at 80–90% displacement.** Under baseline (no-intervention) conditions, aggregate behavioral sink remains low at moderate displacement but rises steeply once 80–90% of the population lacks productive roles, consistent with the nonlinear social-collapse dynamics described by Calhoun (1962) and threshold models of collective behavior.

2. **Residual sink under income support alone.** Even with full UBI provision, a substantial fraction of the population exhibits elevated distress and withdrawal, reflecting Jahoda's (1982) latent-deprivation hypothesis that income replacement does not restore the psychological functions of work.

3. **Cohesion moderation.** Collectivist cultural settings (higher baseline social cohesion) are associated with lower sink severity at equivalent displacement levels, consistent with cross-cultural resilience findings (Hofstede, 2001).

4. **Role substitution vs. income support trade-off.** The relative effectiveness of role programs versus UBI depends on parameterization; neither dominates unconditionally, reflecting the multidimensional nature of work's psychological benefits (Rosso et al., 2010).

5. **Ramp-speed insensitivity at equilibrium.** Once a target displacement level is reached and held, late-run aggregate outcomes converge regardless of whether displacement was introduced rapidly or gradually, consistent with the model's equilibrium-seeking design.

---

## 3. Entities, State Variables, and Scales

### 2.1 Agents

**Entity:** PostLaborAgent (N=200 per simulation)

| State Variable | Type | Range | Description |
|---------------|------|-------|-------------|
| profile | categorical | resilient/balanced/vulnerable | Fixed at initialization; determines baseline trait values |
| resilience | float | [0, 1] | Capacity to maintain functioning under adversity |
| social_capital | float | [0, 1] | Quality and extent of social connections |
| skill_transferability | float | [0, 1] | Ability to adapt skills to new contexts |
| autonomy | float | [0, 1] | SDT core need: sense of self-direction |
| competence | float | [0, 1] | SDT core need: sense of mastery and efficacy |
| relatedness | float | [0, 1] | SDT core need: social connection and belonging |
| status | float | [0, 1] | Perceived social standing |
| meaning | float | [0, 1] | Derived composite: overall psychological well-being |
| role_access | float | [0, 1] | Access to meaning-generating productive roles |
| income_support | float | [0, 1] | Economic security provided by employment or UBI |
| economic_role | float | [0, 1] | Backward-compatible composite summary of role_access and income_support |
| is_displaced | boolean | true/false | Whether the agent is in the displaced subset for the current step |
| virtual_role | float | [0, 1] | Engagement with virtual role substitutes |
| archetype | categorical | productive/beautiful_one/aggressor/withdrawn/collapsed | Behavioral classification based on meaning and aggression |
| birth_intention | float | [0, 1] | Proxy for reproductive motivation |

**Profile distribution:** 15% resilient, 55% balanced, 30% vulnerable. Trait values are drawn from profile-specific means with Gaussian noise (σ=0.05).

### 2.2 Environment

**Network:** Watts-Strogatz small-world graph (k=6, rewiring probability p=0.1). Static throughout simulation.

**Global state variables:**

| Variable | Range | Description |
|----------|-------|-------------|
| current_post_labor | [0, 0.95] | Current fraction of population displaced |
| target_post_labor | [0, 0.95] | Target displacement level (reached via automation_speed) |
| automation_speed | [0.006, 0.20] | Displacement increase per step |
| virtual_world_quality | [0, 1] | Quality of available virtual role substitutes |
| collectivism_index | [0, 1] | Baseline cultural collectivism level |
| contagion_strength | [0, 1] | Strength of social contagion from distressed neighbors |
| ubi | [0, 1] | UBI policy intensity |
| roles_program | [0, 1] | Role substitution program intensity |
| fairness | [0, 1] | Perceived redistribution fairness (base + UBI boost) |
| inequality_index | [0, 1] | Derived: 1 − fairness |

### 2.3 Scales

- **Temporal:** 80 discrete timesteps per simulation. Each step represents an unspecified period; the model characterizes equilibrium states rather than specific time horizons. Horizon robustness verified: extending to T=160/T=240 changes outcomes by <0.01.
- **Spatial:** Network topology only (no geographic space).
- **Population:** 200 agents (fixed).
- **Replication:** 50–150 Monte Carlo runs per parameter point.

---

## 4. Process Overview and Scheduling

Each timestep proceeds in the following order:

### 3.1 Model-Level Processes (sequential)
1. **Automation advance:** `current_post_labor` increases by `automation_speed` toward `target_post_labor`.
2. **Role assignment:** `n_displaced = current_post_labor × N` agents are randomly sampled for displacement. Displaced agents receive `income_support = ubi × ubi_strength` and `role_access = roles_program × roles_strength`; non-displaced agents retain `income_support = 1.0` and `role_access = 1.0`. `economic_role` is retained only as a backward-compatible composite (`max(income_support, role_access)`). Displacement is re-randomized each step (population-level rate, not persistent individual state).

### 3.2 Agent-Level Processes (random activation order)
For each agent, in random order:
1. **Neighborhood assessment:** Compute fraction of neighbors in aggressor, collapsed, and withdrawn states; compute mean neighbor meaning.
2. **Psychological state update:** Update autonomy, competence, relatedness, and status via mean-reverting dynamics toward condition-dependent targets (see §8.1).
3. **Virtual role search:** Displaced agents incrementally increase `virtual_role` engagement; non-displaced agents decay back toward zero virtual engagement.
4. **Meaning computation:** Derive meaning from weighted combination of psychological states, contribution, contagion, and resilience (see §8.2).
5. **Archetype classification:** Classify agent based on meaning level and aggression drive (see §8.3).
6. **Birth intention update:** Compute reproductive motivation from relatedness, meaning, autonomy, and role access.

### 3.3 Data Collection (end of step)
All model-level reporters (mean meaning, sink index, archetype fractions, etc.) are recorded.

---

## 5. Design Concepts

### 4.1 Basic Principles

The model integrates three theoretical frameworks:
- **Self-Determination Theory (SDT; Deci & Ryan, 2000):** Three core psychological needs — autonomy, competence, relatedness — drive well-being. Economic roles satisfy all three; displacement threatens all three.
- **Social contagion (Centola & Macy, 2007):** Distressed behavioral states spread through social networks via linear network exposure in the implemented model.
- **Behavioral sink (Calhoun, 1962):** Populations lacking meaningful social roles exhibit withdrawal, aggression, and reproductive failure.

### 4.2 Emergence

The following are emergent (not directly programmed):
- **Phase transition:** The 80–90% displacement threshold where sink probability jumps from near-zero to near-certain emerges from the interaction of individual psychological dynamics and social contagion.
- **Archetype distribution:** The proportion of productive, withdrawn, aggressive, and collapsed agents emerges from individual meaning trajectories.
- **Intervention ordering:** The relative effectiveness of different interventions emerges from the model's parameterization, not from explicit ranking.

### 4.3 Adaptation

Agents adapt by:
- **Virtual role seeking:** Displaced agents actively seek virtual role engagement, increasing `virtual_role` at a rate proportional to `virtual_world_quality`.
- **Mean reversion:** Psychological states adjust toward equilibrium targets that depend on current conditions, representing gradual psychological adaptation.

### 4.4 Objectives

Agents do not optimize an explicit objective function. Behavioral state changes result from the interplay of psychological dynamics and environmental conditions.

### 4.5 Learning

No individual learning. Agent profiles (resilience, social_capital, skill_transferability) are fixed at initialization.

### 4.6 Prediction

Agents do not predict future states or make anticipatory decisions.

### 4.7 Sensing

Agents sense:
- Their own psychological state variables
- The behavioral archetypes and meaning levels of their network neighbors
- Global model parameters (fairness, virtual_world_quality, etc.) — representing access to societal-level information

### 4.8 Interaction

Agents interact through their network neighborhood:
- **Social contagion:** Neighbors in distressed states (aggressor, collapsed, withdrawn) reduce an agent's psychological targets.
- **Aggressor exposure:** Neighbor aggressors specifically reduce relatedness targets.
- **Mean neighbor meaning:** Used in neighborhood assessment (available but not directly used in current update rules).

### 4.9 Stochasticity

- **Initialization:** Agent traits drawn from profile-specific Gaussian distributions (σ=0.05). Psychological states initialized with Gaussian noise (σ=0.08).
- **Displacement assignment:** Which agents are displaced is re-randomized each step.
- **Psychological updates:** Gaussian noise (σ=0.08) added to each psychological state update, plus per-step agent-level shocks (σ=0.03).
- **Activation order:** Agents are stepped in random order each timestep.

### 4.10 Collectives

No explicit group formation. Agents are linked by a static small-world network.

### 4.11 Observation

Model-level reporters aggregate:
- meaning_index (population mean meaning)
- sink_index (fraction in aggressor/withdrawn/collapsed states)
- Archetype fractions (productive, beautiful_one, aggressor, withdrawn, collapsed)
- birth_intention (population mean)
- social_trust (population mean relatedness)
- post_labor_current (current displacement level)

---

## 6. Initialization

1. Generate Watts-Strogatz small-world network (N=200, k=6, p=0.1).
2. Assign agent profiles: 15% resilient, 55% balanced, 30% vulnerable (shuffled randomly).
3. Initialize agent traits from profile means + Gaussian noise (σ=0.05), clipped to [0, 1]:
   - Resilient: resilience=0.8, social_capital=0.7, skill_transferability=0.7
   - Balanced: resilience=0.5, social_capital=0.5, skill_transferability=0.5
   - Vulnerable: resilience=0.2, social_capital=0.3, skill_transferability=0.3
4. Initialize psychological states from Gaussian distributions:
   - autonomy, competence: N(0.55, 0.08)
   - relatedness, status: N(0.50, 0.08)
5. Set `role_access=1.0`, `income_support=1.0`, `economic_role=1.0`, `virtual_role=0.0`, `is_displaced=False` for all agents.
6. Compute initial meaning for all agents, then run one archetype classification pass before initial data collection.
7. Set `current_post_labor=0.0`.

---

## 7. Input Data

The model uses no external input data during simulation. All dynamics are endogenous.

Historical validation (post-hoc, not model input): Nauru phosphate boom/bust (1960s–1990s) and Gulf states oil wealth are used as qualitative calibration checks.

---

## 8. Submodels

### 7.1 Psychological State Update

Each psychological state follows mean-reverting dynamics:

```
state_{t+1} = state_t + decay × (target - state_t) + N(0, σ) + agent_shock
```

where decay=0.08, σ=0.08, agent_shock ~ N(0, 0.03).

Define `virtual_engagement = virtual_role` when `virtual_role > 0.1`, else `0.0`.

**Autonomy target:**
```
base + 0.25×role_access + 0.10×virtual_engagement + 0.10×fairness
+ 0.12×resilience − 0.06×status_gap − 0.05×contagion
```

**Competence target:**
```
base + 0.25×role_access + 0.10×virtual_engagement×virtual_world_quality
+ 0.12×skill_transferability + 0.10×roles_program − 0.05×contagion
```

**Relatedness target:**
```
base + 0.18×social_capital + 0.10×collectivism_index + 0.10×role_access
+ 0.05×virtual_engagement + 0.08×fairness − 0.12×aggressor_frac − 0.05×contagion
```

**Status target:**
```
base + 0.25×role_access + 0.10×fairness + 0.08×relatedness
− 0.12×status_concentration×(1−role_access) − 0.04×contagion
```

where base=0.32, contagion = sink_exposure × contagion_strength, status_gap = inequality_index × (1 − income_support), and sink_exposure = aggressor_frac + collapsed_frac + withdrawn_frac among neighbors.

### 7.2 Meaning Function

```
meaning = 0.25×autonomy + 0.25×competence + 0.25×relatedness + 0.10×status
          + 0.15×contribution − 0.08×contagion + 0.08×resilience
```

where contribution = economic_weight × role_access + virtual_weight × virtual_engagement (default weights: 0.8 role access, 0.1 virtual).

### 7.3 Archetype Classification

| Archetype | Condition |
|-----------|-----------|
| Productive | meaning > 0.55 |
| Aggressor | meaning < 0.40 AND aggression_drive > 0.3 |
| Beautiful One | meaning > 0.42 (not aggressive) |
| Withdrawn | meaning > 0.30 (not aggressive, not beautiful one) |
| Collapsed | meaning ≤ 0.30 |

where aggression_drive = (1 − meaning) × (1 − social_capital) × 0.5.

### 7.4 Virtual Role Search

Displaced agents seek virtual roles; non-displaced agents decay virtual engagement:
```
virtual_role_{t+1} = clip(virtual_role_t + 0.05 × virtual_world_quality, 0, virtual_world_quality)
```
when displaced, and
```
virtual_role_{t+1} = clip(virtual_role_t − 0.02, 0, 1)
```
when not displaced.

### 7.5 Birth Intention

```
birth_intention = clip(0.4×relatedness + 0.3×meaning + 0.3×autonomy − 0.2×(1−role_access), 0, 1)
```

### 7.6 Role Assignment (Model Level)

Each step, `n_displaced = current_post_labor × N` agents are randomly selected for displacement:
- Displaced: `income_support = ubi × ubi_strength`, `role_access = roles_program × roles_strength`
- Non-displaced: `income_support = 1.0`, `role_access = 1.0`
- Reporting composite: `economic_role = max(income_support, role_access)`

Default strengths: ubi_strength=0.30, roles_strength=0.35.

---

## References

Calhoun, J. B. (1962). Population density and social pathology. *Scientific American*, 206(2), 139-148.

Centola, D., & Macy, M. (2007). Complex contagions and the weakness of long ties. *American Journal of Sociology*, 113(3), 702-734.

Deci, E. L., & Ryan, R. M. (2000). The "what" and "why" of goal pursuits. *Psychological Inquiry*, 11(4), 227-268.

Grimm, V., et al. (2020). The ODD Protocol for Describing Agent-Based and Other Simulation Models. *JASSS*, 23(2), 7.
