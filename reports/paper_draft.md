# Equilibrium Dynamics of Meaning and Behavioral Sink in Post-Labor Societies: A Stylized Agent-Based Analysis

**Authors:** Anonymous Authors (under review)

**Keywords:** post-labor displacement, behavioral sink, self-determination theory, agent-based modeling, role substitution, social cohesion, universal basic income

---

## Abstract

What equilibrium states does a society reach when large fractions of the population lack productive roles? We present a stylized agent-based model integrating Self-Determination Theory with social contagion dynamics to characterize population-level equilibria under sustained role displacement. Across six parameter sweeps and two ablation studies (18,500 runs), we find: (1) A steep threshold effect in the 80–90% displacement zone under baseline parameterization that is policy-sensitive, shifting higher with combined interventions. (2) UBI alone is insufficient at extreme displacement: at 95% post-labor, UBI-only yields sink index 0.743 with 87% collapse probability in the full-grid sweep. (3) Role substitution is more effective than UBI under both default and matched-strength comparisons: roles-only yields sink 0.472, while `roles_matched` still outperforms `ubi_pure` (0.582 vs 0.746), indicating that restoring role access matters more than income support alone in this model. Multi-pillar bundles remain essential at extreme displacement, with the all-bundle achieving sink 0.115 and 0% collapse. (4) Social cohesion moderates UBI-associated sink severity, with higher collectivism reducing collapse from 97% to 31% at 95% displacement, but not eliminating it. (5) Once target displacement is reached, rapid and gradual automation converge toward similar late-run aggregate outcomes, though gradual ramps accumulate more distress during the transition in the exposure-time-controlled comparison. All numerical values and comparative rankings are conditional on this stylized parameterization; the contribution is directional and mechanistic rather than predictive. These findings suggest that meaning infrastructure (role programs, social cohesion, virtual substitutes) is at least as critical as economic redistribution at high displacement levels. Aggressive behavior is a validation gap (~2% modeled vs. Calhoun's 10–20%); results characterize withdrawal-dominated dynamics.

---

## 1. Introduction

### 1.1 The Role-Displacement Problem

Human well-being is deeply embedded in productive roles. Work provides not just income but identity, competence, social connection, and purpose (Blustein, 2008; Deci & Ryan, 2000). Technological displacement, deindustrialization, and resource windfalls have repeatedly demonstrated that removing productive roles — even while maintaining material sufficiency — can produce severe social pathology (Case & Deaton, 2020).

Calhoun's (1962) rodent experiments demonstrated "behavioral sink" — social collapse characterized by withdrawal, aggression, and reproductive failure — when populations lacked meaningful social roles. Jahoda (1982) established that employment provides not only income but latent functions: time structure, social contact, collective purpose, status, and activity — functions that persist as psychological needs even when income is secured through other means. The analogy to human post-labor conditions, while imperfect, raises urgent questions: What equilibrium states does a society reach when large fractions of the population lack productive roles? Which interventions shift the society toward more favorable equilibria, and under what conditions do they fail?

We note that aggressive behavior represents a validation gap (~2% model prevalence vs. 10-20% in Calhoun's observations); results characterize withdrawal-dominated dynamics and should not be extrapolated to high-aggression scenarios.

### 1.2 The Gap in Current Understanding

Existing literature on AI and employment focuses primarily on:
- **Economic impacts:** unemployment rates, wage effects, inequality (Autor, 2015; Acemoglu & Restrepo, 2018)
- **Technical feasibility:** which tasks can be automated (Felten et al., 2021)
- **Policy responses:** UBI, retraining programs, taxation (Standing, 2017)

What remains underexplored is the **psychological and social impact of role displacement independent of income loss**. As Rosso et al. (2010) synthesize, the meaning of work spans multiple dimensions — purpose, belonging, self-efficacy, transcendence — that are not addressed by income replacement alone. A displaced population receiving UBI may avoid poverty but still experience what Deci & Ryan (2000) term "motivation decay" — the erosion of autonomy, competence, and relatedness that constitute psychological well-being.

### 1.3 Research Questions

We address five questions about equilibrium configurations under sustained role displacement:

**RQ1:** At what displacement level does the population equilibrium shift to behavioral sink, and is this threshold fixed or policy-sensitive?

**RQ2:** Can high-quality virtual worlds shift the equilibrium by substituting for economic roles in providing meaning?

**RQ3:** Does the speed of displacement affect the equilibrium reached, independently of the final displacement level?

**RQ4:** Do collectivist vs. individualist cultural structures produce different equilibrium configurations at equivalent displacement?

**RQ5:** What intervention combinations sustain favorable equilibria at extreme (≥90%) displacement levels?

### 1.4 Theoretical Framework

We integrate three theoretical strands:

**Self-Determination Theory (SDT):** Deci & Ryan's (2000) framework identifies three core psychological needs: autonomy (self-direction), competence (mastery), and relatedness (social connection). Economic roles typically satisfy all three; displacement threatens all three.

**Social Contagion Theory:** Behavioral sink spreads through social networks via network exposure — the proportion of an agent's neighbors in collapsed states increases the agent's own collapse risk (Centola & Macy, 2007; Christakis & Fowler, 2007). Our model implements contagion as a linear exposure mechanism where the fraction of neighbors in sink states (aggressor, withdrawn, collapsed) exerts downward pressure on psychological state, scaled by `contagion_strength`. This is a simple exposure model, without threshold or reinforcement requirements from multiple contacts.

**Institutional Capacity:** Following Acemoglu & Robinson (2012), we model interventions as institutional capacities—policy choices that shape how societies respond to technological shocks.

---

## 2. Methods

### 2.1 Model Overview

We developed a network-based agent-based model (ABM) using Mesa 3.5 (Kazil et al., 2021), following ODD protocol conventions (Grimm et al., 2020), with 200 agents interacting over 80 timesteps. **This is a stylized model of post-labor dynamics designed to characterize equilibrium states, not a forecast of specific technological timelines or displacement levels.** The model (V5) extends prior work with a key structural distinction: UBI provides `income_support` (economic security, fairness buffer) without restoring role meaning, while role substitution provides `role_access` (meaning-generating participation) which drives autonomy, competence, relatedness, status, and contribution. This separation makes the UBI-vs-roles comparison a test of structural mechanism rather than parameter difference.

**Modeling displacement as a ramp-to-target process.** In this model, `post_labor_fraction` specifies a target displacement level that the population reaches via a gradual ramp governed by `automation_speed` (default: 0.03/step, reaching 80% by ~step 27). At each step after the ramp, the current displacement fraction is drawn from the agent pool — representing the turnover inherent in labor markets even under high automation. This design treats displacement as a structural condition of the society rather than a permanent individual trajectory — appropriate for studying equilibrium properties, though it precludes claims about individual scarring or adjustment dynamics. The ramp-to-target mechanism means early-timestep outcomes reflect partial displacement rather than the full target level. Persistent individual displacement is a natural extension for future work.

**Agent state variables:**
- Psychological: autonomy, competence, relatedness, status (0-1 scales)
- Role: role_access (meaning-generating participation), income_support (economic security), virtual_role (virtual world engagement)
- Behavioral: archetype (productive, beautiful_one, aggressor, withdrawn, collapsed)

**Model parameters:**
- post_labor_fraction: proportion of population displaced (0-0.95)
- automation_speed: rate of displacement per step (0.006–0.20 for speed comparison; 0.03 baseline for all other sweeps)
- virtual_world_quality: competence/autonomy provided by virtual roles (0-1)
- collectivism_index: baseline relatedness and social buffering (0-1)
- Interventions: UBI, role_substitution, fairness_redistribution

### 2.2 Psychological Update Mechanism

Each timestep, agents update psychological states via mean-reverting dynamics:

```
autonomy_{t+1} = autonomy_t + decay × (autonomy_target - autonomy_t) + noise
```

Targets depend on:
- Economic role access (primary driver)
- Virtual role quality (if displaced)
- Redistribution fairness
- Collectivism level
- Social contagion exposure (neighborhood sink fraction)
- Individual resilience

**Meaning function:**
```
meaning = 0.25×autonomy + 0.25×competence + 0.25×relatedness + 0.10×status
          + 0.15×contribution − 0.08×contagion + 0.08×resilience
```

where contribution = 0.8×role_access + 0.1×virtual_engagement, and contagion is the neighborhood sink exposure scaled by contagion_strength. Here `virtual_engagement` equals `virtual_role` only when engagement exceeds a minimum threshold (`virtual_role > 0.1`); otherwise the virtual channel contributes nothing. The direct contagion and resilience terms capture social network effects and individual buffering beyond the SDT components. Note that `income_support` (UBI) does not appear in the meaning function and does not restore role access; it affects the model only through status gap (inequality) and fairness buffering. This structural separation ensures UBI provides economic security without restoring role meaning, matching the paper's theoretical claim.

**Weight justification:**

| Weight | Value | Basis |
|--------|-------|-------|
| Autonomy, Competence, Relatedness | 0.25 each | SDT: three core needs weighted equally (Deci & Ryan, 2000) |
| Status | 0.10 | Calibration: status matters but is not a core SDT need |
| Contribution | 0.15 | Calibration: captures "mattering" dimension absent from SDT triad |
| Economic contribution | 0.80 | Assumption: real-world productive roles provide primary meaning |
| Virtual contribution | 0.10 | Assumption: virtual roles provide partial but limited meaning substitute |
| Virtual engagement threshold | 0.10 | Structural: virtual benefits require active engagement above a minimum level |
| Virtual role decay | 0.02/step | Assumption: virtual engagement decays when agent is not displaced |
| role_access (roles) | 0.35 strength | Structural: roles restore meaning-generating participation |
| income_support (UBI) | 0.30 strength | Structural: UBI provides economic security only |
| Decay rate | 0.08 | Calibration: produces equilibration within ~30 steps |
| Noise σ | 0.08 | Calibration: increased stochasticity for realistic between-run variance |
| Agent shock σ | 0.03 | Calibration: per-step idiosyncratic life-event noise |
| Base floor | 0.32 | Calibration: minimum human functioning even under severe deprivation |

### 2.3 Archetype Classification

Agents are classified based on meaning and aggression potential:

| Archetype | Criteria |
|-----------|----------|
| Productive | meaning > 0.55 |
| Beautiful One | meaning > 0.42, not aggressive |
| Aggressor | meaning < 0.40, aggression_drive > 0.3 |
| Withdrawn | meaning > 0.30, not aggressive |
| Collapsed | meaning ≤ 0.30 |

(These cutoffs are calibration choices that produce archetype distributions consistent with prior model versions; ±0.05 sensitivity analysis shows directional results are unchanged.)

### 2.4 Simulation Design

We conducted six parameter sweeps plus two ablation studies, totaling 18,500 runs:

| Sweep | Parameter | Levels | Scenarios | Runs/Point | Total |
|-------|-----------|--------|-----------|------------|-------|
| 1 | Post-labor fraction | 9 | 5 | 50 | 2,250 |
| 2 | Automation speed | 2×3 | 5 | 100 | 3,000 |
| 3 | Virtual world quality | 6 | 3×2 | 100 | 3,600 |
| 4 | Collectivism index | 6 | 3×2 | 100 | 3,600 |
| 5 | Archetype time series | 2 | 2 | 50 | 100 runs |
| 6 | Full scenario grid | 3 | 10 | 150 | 4,500 |
| A | Weight ablation (econ:virtual ratio) | 5 | 4 | 50 | 1,000 |
| B | Intervention decoupling | 1 | 3 | 150 | 450 |

**Intervention structure.** In our implementation, UBI and role substitution target distinct channels. UBI provides `income_support` (economic security, fairness buffer) without restoring role access; it does not enter the role-driven meaning channel. Role substitution provides `role_access` (meaning-generating participation), which directly affects autonomy, competence, relatedness, status, and contribution. The UBI scenario includes an implicit fairness boost (reflecting UBI's social legitimacy signal), and role programs include a competence boost. These are structural differences, not parameter differences: the roles-vs-UBI comparison tests whether meaning channels or economic channels matter more for preventing behavioral sink.

**Validation:** V5 reproduces the directional pattern of prior findings (threshold effect in the 80-90% zone under baseline conditions), with the critical structural change that UBI no longer provides role access. The V5 separation of UBI from roles is the most significant model change, revealing that earlier versions overstated UBI's effectiveness. Note that the model was calibrated to approximate prior output patterns; this comparison validates implementation consistency, not independent replication.

**Horizon robustness.** We verified that outcomes are near-stationary by step 80: extending simulations to T=160 and T=240 changes mean sink_index by less than 0.01 across all 9 tested conditions (3 scenarios × 3 displacement levels). The maximum delta between T=80 and T=120 is 0.009, well below the 0.02 convergence threshold. We therefore use T=80 as a reliable approximation of the near-equilibrium state. Full convergence table in Supplementary Methods.

### 2.5 Sensitivity Analysis

We conducted one-at-a-time perturbation of three key internal parameters (noise σ, decay rate, contagion strength) by ±20%, with 50 runs per condition at PL=0.80 and PL=0.95 baseline. Core findings are directionally consistent across tested parameter ranges: at PL=0.95, collapse occurs in 100% of baseline runs across all perturbations; at PL=0.80, collapse remains rare (0-2%). The most sensitive parameter is contagion strength, which governs the positive feedback loop driving collective collapse. Full sensitivity results are reported in the Methods Appendix.

### 2.6 Analysis

Primary outcomes:
- **Meaning index:** population mean meaning
- **Sink index:** proportion in aggressor/withdrawn/collapsed states
- **Collapse probability:** percentage of runs with sink_index > 0.7 at final step

Secondary outcomes:
- Archetype distributions over time
- Birth intention (proxy for reproductive collapse)
- Social trust (mean relatedness)

---

## 3. Results

### 3.1 The Malleable Threshold Zone (RQ1)

Under baseline conditions (no interventions, gradual automation), the model exhibits a steep threshold effect in the 80-90% post-labor zone (Figure 1). At 80% post-labor, baseline collapse probability is 2% (meaning 0.382, sink 0.629); at 90%, it rises to 86% (meaning 0.348, sink 0.736); at 95%, collapse is 100% (meaning 0.330, sink 0.788).

![Figure 1: Threshold effect — sink index and collapse probability across post-labor levels under baseline conditions](figures/sweep1_phase_transition.png) The transition zone — rather than a knife-edge threshold — is consistent with complex adaptive systems theory and more realistic than a sharp critical point. This zone proves highly sensitive to policy and contextual factors.

**Speed affects transition duration within the equilibrium ABM:** At matched time-since-target-displacement (t+10 after reaching PL=0.95), rapid and gradual automation show similar late-run trajectories once both have reached the target (see §3.3). Naive comparisons at fixed T=80 confound speed with time-at-target; matched analysis instead supports a narrower equilibrium interpretation within this model.

**Virtual worlds extend threshold higher:** With virtual_world_quality = 0.6, baseline collapse probability at 95% post-labor drops from 100% to 8% (sink 0.659); at quality 1.0, collapse is 0% (sink 0.520). Under high-quality virtual conditions, collapse is not observed below 95% displacement.

**Combined interventions push threshold to 95%:** The all-bundle (UBI + roles + fairness + virtual worlds + collectivism) achieves 0% collapse with sink 0.115 even at 95% post-labor.

**V5 structural change:** V5 introduces a critical separation between UBI (income_support only) and role substitution (role_access only). This means UBI provides economic security without restoring role meaning, making the UBI-vs-roles comparison a test of structural mechanism rather than parameter difference. The practical consequence is dramatic: UBI-only at 95% displacement now shows 87% collapse (sink 0.743), compared to 0% collapse under roles-only (sink 0.472). Previous versions that bundled role restoration into UBI substantially overstated UBI's effectiveness.

### 3.2 Virtual Worlds as Substitutes (RQ2)

Virtual worlds provide significant and graded protection (Figure 2).

![Figure 2: Virtual world quality effect on sink index at 80% and 95% post-labor](figures/sweep3_virtual_world.png)

At 95% post-labor (baseline, no UBI):
- Zero virtual quality: 100% collapse, sink 0.792
- Moderate quality (0.6): 8% collapse, sink 0.659
- Maximum quality (1.0): 0% collapse, sink 0.520

At 95% post-labor (with UBI):
- Zero virtual quality: 90% collapse, sink 0.746
- Moderate quality (0.6): 0% collapse, sink 0.598
- High quality (0.8): 0% collapse, sink 0.533

The marginal benefit of virtual quality is concave — substantial gains occur between 0.0 and 0.6, with diminishing returns above 0.8. At 95% displacement, virtual worlds alone reduce collapse from 100% to 0% (baseline) or from 90% to 0% (with UBI), though elevated sink (0.520) persists even at maximum quality under baseline conditions, indicating partial but incomplete substitution. Virtual worlds are now particularly important because UBI alone no longer restores role access — they are the primary alternative meaning source for displaced agents.

The model's contribution weighting (virtual contribution counts 0.1 vs. 0.8 for economic roles) creates a ceiling effect: even maximum virtual quality leaves a meaning gap. Combining virtual worlds with UBI provides incremental benefit (sink 0.533 at VW=0.8 with UBI vs 0.520 at VW=1.0 baseline), but the largest gains come from virtual quality itself rather than adding UBI. The most potent combination is roles + virtual worlds (sink 0.259 at PL=0.95), which addresses both meaning channels and alternative engagement simultaneously.

**Sensitivity to contribution weights.** The virtual-world ceiling remains assumption-sensitive, but the direction of the comparison changes under V5. Across all tested economic:virtual contribution ratios (3:1 to ∞), virtual-only outperforms UBI-only while still leaving substantial residual sink: at 3:1, virtual-only yields sink 0.446 versus UBI-only 0.749; at the default 8:1 ratio, 0.517 versus 0.747; and at ∞, 0.584 versus 0.742. Once UBI is restricted to income support alone, even partial virtual role access is consistently more protective than UBI-only in this stylized model. UBI+virtual remains better than either single intervention across all tested ratios.

### 3.3 Speed of Automation (RQ3)

To isolate speed effects from exposure-time confounds, we conducted a controlled comparison (Figure 3) measuring outcomes at matched intervals after each scenario reaches its target displacement (PL=0.95).

![Figure 3: Speed comparison — rapid vs gradual automation under matched time-since-target conditions in the equilibrium ABM](figures/sweep2_automation_speed.png) Rapid automation (speed=0.20) reaches the target in ~5 steps; gradual automation (speed≈0.006) reaches it in ~160 steps.

**Finding within the equilibrium ABM: speed effects are transient rather than structural.** At matched time-since-target-displacement (10 steps after reaching PL=0.95), both speeds show similar sink levels converging toward the same late-run aggregate state:

| Speed | Sink (t+10) | Sink (t+40) | Equilibrium |
|-------|-------------|-------------|-------------|
| Rapid | 0.638 | 0.777 | ~0.78 |
| Gradual | 0.780 | 0.790 | ~0.79 |

Gradual automation produces higher sink during the transition (0.780 vs 0.638 at t+10 for baseline), because the extended ramp period allows contagion to accumulate during partial displacement. The same directional pattern appears for `ubi_only` (0.732 vs 0.594 at t+10), while strong interventions compress the difference (`full_bundle`: 0.274 vs 0.241 at t+10). The original naive comparison (both measured at T=80) confounded speed with exposure time: rapid had 75 steps at full displacement while gradual had just reached its target.

At equilibrium (t+40), both speeds converge to similar outcomes (~0.78-0.79 sink for baseline and ~0.73-0.74 for `ubi_only`). Within this equilibrium ABM, once target displacement is reached, late-run aggregate outcomes are similar across fast and slow ramps. Interventions dominate these late-run speed differences: `full_bundle` produces sink ≈ 0.29-0.30 regardless of speed.

These findings suggest that transition velocity affects transition duration but not late-run aggregate outcomes within this equilibrium model, as confirmed by our horizon robustness analysis; persistent-displacement models are needed before drawing stronger conclusions about managed transition speed or intervention timing.

### 3.4 Collectivism as Social Buffer (RQ4)

Collectivism alone cannot prevent baseline collapse (Figure 4).

![Figure 4: UBI × collectivism interaction — collapse probability and sink index at 95% post-labor under UBI-only conditions](figures/sweep4_ubi_collectivism_interaction.png)

**Baseline at 95% post-labor (no interventions):**
- Collectivism 0.0: 100% collapse, sink 0.812
- Collectivism 1.0: 92% collapse, sink 0.743 (modest reduction, but collapse remains common)

**UBI at 95% post-labor (collectivism as moderator):**
- Collectivism 0.0: 97% collapse, sink 0.769
- Collectivism 0.4: 86% collapse, sink 0.732
- Collectivism 0.6: 63% collapse, sink 0.712
- Collectivism 0.8: 47% collapse, sink 0.704
- Collectivism 1.0: 31% collapse, sink 0.684

The collectivism sweep reveals a continuous, dose-response relationship: higher collectivism is progressively associated with lower collapse probability and lower sink index under UBI-only conditions. However, even maximum collectivism (1.0) cannot prevent 31% collapse at 95% displacement — a finding that reinforces the inadequacy of income-only policy at extreme displacement.

The collectivism effect is a continuous moderator rather than a threshold switch: higher collectivism is progressively associated with lower sink index and lower collapse probability across all conditions, but does not independently prevent collapse even at maximum levels. The mechanism operates through relatedness maintenance — collectivist structures provide alternative social connection sources when workplace ties are severed. However, at 95% displacement, even the strongest collectivist structures cannot compensate for the absence of meaningful roles, reducing collapse from 97% to 31% but not eliminating it.

This finding suggests cultural context moderates but does not eliminate the severity of post-labor distress. Societies with higher baseline collectivism (East Asian, Nordic) would show lower sink levels at equivalent displacement, but still face substantial collapse risk at extreme automation without role-targeted interventions.

### 3.5 Intervention Combinations at Extreme Automation (RQ5)

At 95% post-labor — the stress test for any post-labor policy — we rank intervention effectiveness by sink index (Figure 5):

![Figure 5: Intervention ranking by sink index at 95% post-labor across 10 scenarios](figures/sweep6_scenario_ranking.png)

**Tier 1 (0% collapse, sink < 0.30):**
- All bundle (+ virtual + collectivism): 0.115 sink
- Roles + Virtual: 0.259 sink

**Tier 2 (0% collapse, sink 0.30-0.50):**
- Full bundle (UBI + roles + fairness): 0.300 sink
- Roles only: 0.472 sink

**Tier 3 (partial or high collapse, sink > 0.50):**
- UBI + Virtual: 0.535 sink, 0% collapse
- Fairness + Collectivism: 0.614 sink, 1% collapse
- Fairness only: 0.661 sink, 12% collapse
- UBI + Collectivism: 0.703 sink, 51% collapse
- UBI only: 0.743 sink, 87% collapse
- Baseline: 0.790 sink, 100% collapse

**Critical insights:**

1. **Multi-pillar interventions dominate:** The all-bundle achieves the lowest sink (0.115), and roles+virtual (0.259) outperforms any single intervention, confirming that addressing multiple psychological needs simultaneously is most effective.

2. **Virtual worlds are the most potent addition to single interventions:** Adding virtual worlds to UBI is associated with a 28% reduction in sink (0.743 → 0.535) and eliminates collapse entirely. Adding virtual worlds to roles is associated with a 45% reduction in sink (0.472 → 0.259).

3. **Role substitution is structurally superior to UBI at extreme displacement:** At 95%, roles-only achieves sink 0.472 with 0% collapse — substantially outperforming UBI-only (sink 0.743, 87% collapse). This is not just a default-parameter artifact: in the matched-strength ablation, `roles_matched` still outperforms `ubi_pure` (0.582 vs 0.746). Under V5, the comparison directly tests meaning channels versus economic channels, and the meaning channel is more protective in this stylized model.

4. **UBI alone performs poorly at extreme displacement:** UBI-only at 95% post-labor shows 87% collapse — substantially worse than role-based or role-plus-virtual interventions. The V5 separation of UBI from role access reveals that economic security without meaning is insufficient to prevent behavioral sink at extreme displacement.

5. **Fairness redistribution is insufficient alone:** Fairness-only scenarios show 12% collapse and high sink (0.661) because they don't address role absence.

6. **No single intervention eliminates elevated sink:** Even the best single intervention (roles, 0.472) leaves nearly half the population in suboptimal states at 95% displacement. Multi-pillar bundles are essential.

**The structural roles-vs-UBI decomposition.** In V5, UBI and role substitution target distinct channels: UBI provides `income_support` (economic security, fairness buffer) without entering the meaning function, while roles provide `role_access`, which drives autonomy, competence, relatedness, status, and contribution. This structural separation makes the comparison a test of mechanism rather than hidden role restoration inside both interventions. In the matched-strength ablation, `roles_matched` produces sink 0.582 ± 0.003 while `ubi_pure` produces 0.746 ± 0.003. The full roles configuration (`roles_full`) reduces sink further to 0.471 ± 0.003, implying an additional ~0.111 sink reduction from the competence pathway plus the higher default roles strength. Under V5, then, the roles advantage survives the matched-strength comparison and grows under the default specification.

### 3.6 Archetype Trajectories (RQ5 Continued)

Time-series analysis reveals archetype emergence patterns (Figure 6):

![Figure 6: Archetype distribution over 80 timesteps — baseline vs full bundle at 80% post-labor](figures/sweep5_archetypes.png)

**Seeded initial condition (step 0):** Because archetypes are classified before initial data collection in V5, the time series no longer begins with an artificial 100% productive population. The seeded distribution is ~70% Productive and ~30% Beautiful Ones under both scenarios.

**Baseline trajectory (80% post-labor):**
- Steps 0-10: Productive declines modestly (70% → 60%), while Withdrawn and Collapsed begin to emerge
- Steps 10-25: Withdrawn surges (9% → 28%), while Collapsed rises from ~1% to ~10%
- Steps 25-80: Gradual stabilization at a high-sink state (10% Productive, 28% Beautiful Ones, 37% Withdrawn, 24% Collapsed, ~2% Aggressors; sink ≈ 0.624)

**Full bundle trajectory:**
- Productive remains much higher than baseline (41% at step 80), Beautiful Ones rise to ~40%, and Withdrawn/Collapsed remain limited (16% and 3%, respectively)
- Final sink index is ~0.195, far below baseline but still above zero

The dominant pathway is Productive → Beautiful One → Withdrawn → Collapsed, with aggression remaining rare (~1-2%) throughout. The Beautiful One phase — surface-level functioning without productive engagement — is already present in the seeded initial condition and remains the most common transitional state. Our results are consistent with the hypothesis that earlier intervention preserves social cohesion, though the model does not include an explicit deployment timing parameter.

### 3.7 Historical Validation: Nauru vs. Gulf States

To assess qualitative plausibility, we mapped two historical cases that share structural features with model conditions (Figure 7). These cases were selected post-hoc as contrasting archetypes; this is not a prospective validation test.

![Figure 7: Historical analogues — model predictions vs Nauru (collapse) and Gulf states (stability)](figures/historical_analogues.png) The Republic of Nauru experienced rapid resource-driven wealth from phosphate mining (1960s-1990s), providing citizens with income eliminating the need for employment — a case that shares structural features with the UBI-without-purpose scenario. The period was associated with severe social dysfunction: 94% obesity, 31% diabetes, alcohol abuse, and family breakdown. Our model's baseline condition at PL=0.95 predicts meaning=0.330, sink=0.790, collapse=100% — broadly consistent with Nauru's severe social dysfunction despite material sufficiency.

Gulf states (UAE, Qatar, Kuwait) achieved comparable post-scarcity through oil wealth with radically different outcomes (Ross, 2012). One notable difference between the cases is the role of collectivist social institutions (tribal structures, Islamic community norms), though multiple confounds preclude causal attribution. Our model predicts collectivism=0.8 + UBI at PL=0.80 → meaning=0.416, sink=0.528, collapse=0% — consistent with a more stable but still strained configuration rather than full flourishing. The more favorable Gulf outcomes likely reflect role preservation (government employment, civic participation) beyond what UBI alone provides, consistent with our finding that role substitution is essential at high displacement.

The collectivism variable is associated with sink severity differences: at PL=0.95 with UBI, sink is 0.769 at collectivism=0.0 (Nauru-like, 97% collapse) vs. 0.704 at collectivism=0.8 (Gulf-like, 47% collapse). Higher collectivism is associated in the model with lower distress and lower collapse probability, but even at collectivism=1.0, 31% of runs still collapse under UBI-only conditions. The model was not fitted to either case; this divergence is illustrative of the framework's mechanisms rather than evidence that collectivism explains the historical contrast. This comparison is illustrative only; both cases were selected post-hoc and differ on numerous dimensions beyond collectivism. We emphasize that this comparison is post-hoc pattern matching against two cases selected to differ maximally; it does not constitute formal empirical validation. While subject to extensive confounding (geography, colonial history, population size, resource type), the directional pattern is consistent with the model's predictions, though this post-hoc comparison cannot constitute evidence.

---

## 4. Discussion

### 4.1 Theoretical Implications

**Self-Determination Theory in Economic Context:** Within the SDT framework, our model illustrates that the three core needs (autonomy, competence, relatedness) can be operationalized through diverse channels. Economic roles are the default source, but virtual worlds (autonomy, competence) and collectivism (relatedness) provide partial substitutes. However, the ceiling effects suggest these substitutes are imperfect—extreme automation may exceed substitution capacity. Note that SDT needs are operationalized directly in our model's meaning function; consistency with SDT predictions is therefore expected by construction and does not constitute independent empirical validation of the theory.

**Threshold Dynamics in Social Systems:** The 80-90% zone exhibits steep threshold behavior: small parameter changes near this region produce disproportionately large outcome changes, consistent with nonlinear dynamics in complex adaptive systems. Unlike physical phase transitions, which require specific mathematical criteria (power-law scaling, diverging correlation lengths), we use "threshold effect" to describe this empirical pattern. Crucially, this threshold is policy-sensitive rather than fixed.

**Social Contagion Amplification:** The sharp increase in sink between steps 20-40 suggests contagion dynamics. Individual displacement effects are multiplied through social networks, creating emergent collective collapse exceeding individual-level predictions.

### 4.2 Policy Implications

**Multi-pillar necessity:** No single intervention suffices at extreme automation. UBI alone performs poorly at 95% displacement (87% collapse in the full-grid sweep), while role substitution alone still leaves sink at 0.472. Policy portfolios must address income (UBI), meaning (role substitution, virtual worlds), and connection (collectivism structures). The all-bundle (sink 0.115) demonstrates that combined approaches are essential.

**Virtual infrastructure investment:** Virtual worlds show the largest marginal benefit when added to other interventions, and are now especially critical because UBI alone no longer provides role access. Investment in high-quality virtual role systems—games, creative platforms, virtual civic engagement—may be as important as physical infrastructure. Adding virtual worlds to UBI reduces collapse from 87% to 0% at 95% displacement.

**Transition management:** Our controlled speed comparison shows similar late-run aggregate outcomes for rapid and gradual automation once the same target displacement is reached, but gradual ramps accumulate more distress during the transition. This conclusion is conditional on the equilibrium ABM design, which does not model persistent individual displacement, scarring, or retraining trajectories; a persistent-displacement model is needed before drawing operational guidance about transition speed management. Within that framing, intervention provision matters more than automation speed in shaping the model's late-run state.

**Cultural tailoring:** Collectivism effects suggest UBI programs should be designed differently in different cultural contexts. Even at maximum collectivism, UBI-only still shows 31% collapse at 95% displacement — meaning cultural infrastructure alone is insufficient without role-targeted interventions. Individualist societies face even higher risk (97% collapse at collectivism=0.0).

**Early warning systems:** The archetype trajectory (Productive → Beautiful One → Withdrawn → Collapsed, with Aggressor emergence rare at ~2%) provides a potential early warning framework. Rising Beautiful One and Withdrawn fractions may predict approaching collapse before sink indices cross thresholds.

### 4.3 Limitations and Self-Critique

**Residual determinism:** V5 carries forward V4's increased noise (σ=0.08, plus agent-level shocks). Between-run standard deviations remain around ~0.008 for meaning index. The model remains more deterministic than typical behavioral science data (where Cohen's d of 1-3 is common). The mean-reverting dynamics, while theoretically motivated, still dominate over noise at 80 timesteps. Consequently, conventional inferential statistics (p-values, power) are not meaningful given these effect sizes; we report point estimates and SEM as descriptive summaries only. Future versions should explore alternative update rules (e.g., multiplicative noise, regime-switching dynamics) to achieve realistic between-run variance.

**Intervention structure:** While our experimental design varies interventions individually and in combination, V5 cleanly separates UBI (income_support) from role substitution (role_access). The implementation includes coupling between UBI and fairness effects, and between role programs and competence development (detailed in §2.4). Real policies interact in ways not captured: UBI might reduce work motivation (negative with roles), virtual worlds might displace real-world socializing (negative with collectivism), fairness perception might depend on who benefits from role programs. The V5 separation ensures the core finding — that meaning channels dominate economic channels — is not an artifact of bundling.

**Underrepresented aggressors:** V5 carries forward V4's recalibrated aggressor thresholds, with prevalence at ~2-3% at high displacement. However, this remains below the 10-20% expected from Calhoun's observations. The aggression formula `(1-meaning)*(1-social_capital)*0.5 > 0.3` requires extremely low social capital (< 0.14) combined with low meaning — a narrow parameter region. The model effectively treats behavioral sink as withdrawal-dominated, underrepresenting the aggression dimension. Future work should explore alternative aggression mechanisms (e.g., relative deprivation, frustration-aggression dynamics).

**Displacement as ramp-to-target with cross-sectional turnover.** The model ramps displacement toward a target level via `automation_speed`, then each timestep the displaced fraction is redrawn from the agent pool. This enables equilibrium analysis but precludes conclusions about individual adjustment trajectories, unemployment scarring, or the dynamics of managed transitions. Future work should model persistent individual displacement with explicit re-employment mechanisms.

**Intervention coupling.** V5 cleanly separates UBI (income_support only) from role substitution (role_access only), making the structural comparison a test of mechanism rather than parameter: UBI provides economic security alone, while roles restore meaning-generating participation. UBI still includes an implicit fairness co-benefit (`fairness = ubi * 0.3` in the implementation), and roles include a competence boost. The directional finding (roles >> UBI at extreme displacement) is now driven by the structural mechanism difference — meaning channels vs. economic channels — rather than by confating role restoration into UBI. The intervention hierarchy reported in §3.5 should be interpreted as conditional on the default parameterization, but the qualitative finding (roles structurally superior to income-only policy at high displacement) is robust to this separation.

**No endogenous adaptation:** Agents cannot create new institutions, discover novel purposes, form social movements, or develop emergent cultural responses. Human societies have repeatedly demonstrated capacity for institutional innovation under stress — the Industrial Revolution, post-WWII reconstruction, the digital economy. Our model assumes a fixed institutional landscape, which likely overstates collapse risk.

**Threshold-dependent results:** Many headline findings occur near the threshold zone (80-90% displacement) where small parameter changes produce large outcome shifts. While characteristic of complex systems, this sensitivity means our quantitative predictions are unreliable — the qualitative direction matters, but specific percentages should be treated with extreme caution.

Sensitivity analysis in this paper is local (one-at-a-time, ±20%), not global; parameter interaction effects across the joint space have not been assessed with Sobol indices or PRCC, and findings near the threshold regime may be sensitive to combinations not tested.

**Model simplifications:**
- Static network structure (real networks rewire during disruption)
- Binary displacement (no gradations of underemployment)
- Homogeneous agents (no age, education, or skill variation)
- Single generation (no demographic replacement)
- No economic dynamics (markets, prices, innovation)

Of these simplifications, static network topology is most likely to affect conclusion direction: dynamic networks with homophily could amplify contagion effects, potentially lowering the threshold zone. The remaining simplifications (homogeneous agents, discrete archetypes) are expected to affect magnitude but not direction.

**Historical validation limitations:**
- Post-hoc case selection (not prospective prediction)
- Multiple confounders between Nauru and Gulf states beyond collectivism
- "Collectivism" reduces complex cultural systems to a single scalar
- Quantitative match is to qualitative patterns, not measured outcomes

### 4.4 Implementation Cross-Check: System Dynamics Model (Pathway C)

To check whether findings are method-dependent (while acknowledging both models share the same SDT+contagion theoretical assumptions), we developed a parallel system dynamics (SD) model using stock-flow ODEs with three state variables: MeaningStock, SinkStock, and SocialTrust. The SD model was calibrated independently to the Nauru historical trajectory (1970-2000: resource wealth without purpose → social collapse) and then tested against the Gulf states comparison case (collectivist structures + resource wealth → stability).

Under matched parameters (PL=0.80, baseline), both models predict low meaning and high sink. Under UBI conditions, both models predict higher meaning and lower sink relative to baseline. The directional agreement across two modeling approaches sharing the same theoretical framework (SDT + social contagion) — one bottom-up (agent heterogeneity, network effects) and one top-down (aggregate stocks, continuous flows) — provides an implementation consistency check (not independent validation, since both models share SDT assumptions). 

The SD model reproduces the same qualitative Nauru-Gulf pattern as the ABM (Nauru-like: sink ≈ 0.71; Gulf-like: sink < 0.15). Note that both models share the same theoretical framework (SDT + social contagion), and the SD model was calibrated to the Nauru historical trajectory — so this convergence reflects implementation consistency, not methodological independence. Full Pathway C documentation is provided in the Supplementary Methods.

### 4.5 Future Research

**Model extensions:**
- Dynamic networks with homophily/heterophily
- Multi-generational demographics
- Spatial heterogeneity (urban/rural differences)
- Endogenous technical change (AI development responding to social conditions)

**Empirical calibration:**
- Calibrate to historical cases (post-Soviet transition, Rust Belt deindustrialization)
- Validate archetype classification against psychological surveys
- Estimate real-world virtual world quality equivalents

**Policy experiments:**
- Optimal intervention timing (when to deploy during transition)
- Cost-effectiveness analysis (which interventions achieve outcomes per dollar)
- Political economy (how intervention preferences evolve with automation)

**V6 extensions.** These findings suggest several natural extensions. First, a model with persistent individual displacement states would enable study of unemployment scarring, managed transitions, and trajectory heterogeneity that the current equilibrium model cannot address. Second, empirical calibration of the economic-to-virtual contribution weight ratio from survey data on meaningful engagement would transform our sensitivity finding into a testable prediction. Third, a multi-site validation using deindustrialization data (Rust Belt, post-Soviet transitions) and resource-curse cases beyond Nauru and Gulf states would strengthen construct validity.

---

## 5. Conclusion

This stylized model identifies mechanisms by which post-labor displacement can drive behavioral sink — and mechanisms by which it can be prevented. Our findings do not predict when or whether AI will displace specific populations, but they characterize the dynamics that would follow such displacement.

The central insight is that economic redistribution alone (UBI) is insufficient at extreme displacement: in the full-grid sweep, 87% of `ubi_only` runs collapse at 95% post-labor. The V5 structural separation suggests that meaning-generating participation (through role programs, virtual infrastructure, and social cohesion) is not merely complementary to economic policy but a central determinant of whether collapse is avoided. Role substitution alone achieves what UBI alone does not: 0% collapse at 95% displacement (sink 0.472 vs 0.743 for `ubi_only`). Multi-pillar bundles that combine economic security with meaning infrastructure achieve the best outcomes (all-bundle sink 0.115).

The model's sensitivity to social cohesion — with collectivism reducing collapse from 97% to 31% at 95% displacement under UBI — highlights that identical economic policies are associated with dramatically different outcomes depending on the social substrate. However, even maximum collectivism cannot prevent collapse without role-targeted interventions. This finding is consistent with historical divergences between post-labor societies (Nauru vs. Gulf states) and suggests that cultural and institutional context deserves as much attention as economic policy design.

As a stylized model, these results identify mechanisms and qualitative relationships rather than precise thresholds. The specific numbers (80-90% transition zone, sink indices) are model-dependent and should not be interpreted as predictions. What the model contributes is a framework for thinking about which dimensions of human well-being are at risk under role displacement, and which intervention categories address which risks. The V5 separation of UBI from role access sharpens that framework by cleanly distinguishing economic buffering from meaning restoration.

---

## References

Acemoglu, D., & Restrepo, P. (2018). The wrong kind of AI? Artificial intelligence and the future of labour demand. *Cambridge Journal of Regions, Economy and Society*, 11(1), 29-44. https://doi.org/10.1093/cjres/rsy025

Acemoglu, D., & Robinson, J. A. (2012). *Why nations fail: The origins of power, prosperity, and poverty*. Crown Business.

Autor, D. H. (2015). Why are there still so many jobs? The history and future of workplace automation. *Journal of Economic Perspectives*, 29(3), 3-30. https://doi.org/10.1257/jep.29.3.3

Brynjolfsson, E., & McAfee, A. (2014). *The second machine age: Work, progress, and prosperity in a time of brilliant technologies*. WW Norton & Company.

Calhoun, J. B. (1962). Population density and social pathology. *Scientific American*, 206(2), 139-148.

Case, A., & Deaton, A. (2020). *Deaths of Despair and the Future of Capitalism*. Princeton University Press.

Centola, D., & Macy, M. (2007). Complex contagions and the weakness of long ties. *American Journal of Sociology*, 113(3), 702-734. https://doi.org/10.1086/521848

Christakis, N. A., & Fowler, J. H. (2007). The spread of obesity in a large social network over 32 years. *New England Journal of Medicine*, 357(4), 370-379. https://doi.org/10.1056/NEJMsa066082

Connell, J. (2006). Nauru: The first failed Pacific state? *The Round Table*, 95(383), 47-63.

Deci, E. L., & Ryan, R. M. (2000). The "what" and "why" of goal pursuits: Human needs and the self-determination of behavior. *Psychological Inquiry*, 11(4), 227-268. https://doi.org/10.1207/S15327965PLI1104_01

Felten, E. W., Raj, M., & Seamans, R. (2021). Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. *Strategic Management Journal*, 42(12), 2195-2217. https://doi.org/10.1002/smj.3286

Frey, C. B., & Osborne, M. A. (2017). The future of employment: How susceptible are jobs to computerisation? *Technological Forecasting and Social Change*, 114, 254-280. https://doi.org/10.1016/j.techfore.2016.08.019

Grimm, V., Railsback, S. F., Vincenot, C. E., Berger, U., Gallagher, C., DeAngelis, D. L., Edmonds, B., Ge, J., Giske, J., Groeneveld, J., Johnston, A. S. A., Milles, A., Nabe-Nielsen, J., Polhill, J. G., Radchuk, V., Rohwäder, M.-S., Stillman, R. A., Thiele, J. C., & Ayllón, D. (2020). The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism. *JASSS*, 23(2), 7. https://doi.org/10.18564/jasss.4259

Hertog, S. (2010). *Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia*. Cornell University Press.

Hofstede, G. (2001). *Culture's Consequences: Comparing Values, Behaviors, Institutions, and Organizations Across Nations*. Sage.

Jahoda, M. (1982). *Employment and unemployment: A social-psychological analysis*. Cambridge University Press.

Kazil, J., Masad, D., & Crooks, A. (2021). Utilizing Python for agent-based modeling: The Mesa framework. In *Agent-Based Simulation of Organizational Behavior* (pp. 308-344). Springer.

Ross, M. (2012). *The oil curse: How petroleum wealth shapes the development of nations*. Princeton University Press.

Rosso, B. D., Dekas, K. H., & Wrzesniewski, A. (2010). On the meaning of work: A theoretical integration and review. *Research in Organizational Behavior*, 30, 91-127. https://doi.org/10.1016/j.riob.2010.09.001

Standing, G. (2017). *Basic income: And how we can make it happen*. Penguin UK.

---

## Data Availability

All simulation code, data (6 sweeps + 2 ablation studies, 18,500 runs), and analysis scripts are available at: https://github.com/wukao1985/post-scarcity-abm

## Acknowledgments

The authors thank [reviewers and computational resources].

## Author Contributions

[Anonymized for review]

## Competing Interests

The authors declare no competing interests.

## Supplementary Information

Supplementary figures, sensitivity analyses, and extended data tables are available in the online repository. This includes:
- **Supplementary Methods:** Full parameter documentation with justification categories (SDT theory, Calhoun calibration, convenience/sensitivity-tested)
- **Horizon Robustness:** Convergence table showing all conditions stabilize by T=80 (max Δ < 0.01 to T=240)
- **Speed Comparison:** Exposure-time-controlled analysis showing speed convergence
- **Pathway C:** System dynamics model specification, Nauru/Gulf calibration, and ABM-SD comparison
- **V4/V5 Validation:** Detailed comparison showing effect of increased stochasticity (V4) and UBI-role separation (V5) on headline results
- **Weight Ablation:** Economic:virtual contribution ratio sensitivity (3:1 to ∞), 1,000 runs
- **Intervention Decoupling:** Matched-strength comparison of UBI vs roles, 450 runs
- **ODD Protocol:** Full ODD-compliant model description (Grimm et al., 2020)

---

## Appendix: Figures

**Figure 1.** Threshold effect — sink index and collapse probability across post-labor levels under baseline conditions. The transition zone (80–90%) broadens under increased stochasticity.
![Figure 1](figures/sweep1_phase_transition.png)

**Figure 2.** Virtual world quality effect on sink index at 80% and 95% post-labor. Marginal benefit is concave, with largest gains between quality 0.0 and 0.6.
![Figure 2](figures/sweep3_virtual_world.png)

**Figure 3.** Speed comparison — rapid vs gradual automation. Within the equilibrium ABM, both paths show similar late-run outcomes once target displacement is reached; speed is associated with transition duration rather than late-run aggregate state.
![Figure 3](figures/sweep2_automation_speed.png)

**Figure 4.** UBI × collectivism interaction at 95% post-labor. Under UBI, sink index is 0.769 in individualist societies (collectivism=0.0) and decreases to 0.684 in highly collectivist ones (collectivism=1.0), with collapse probability decreasing from 97% to 31%.
![Figure 4](figures/sweep4_ubi_collectivism_interaction.png)

**Figure 5.** Intervention ranking by sink index at 95% post-labor across 10 scenarios. Multi-pillar bundles dominate; UBI-only shows 87% collapse, roles-only shows 0% collapse — a structural difference driven by mechanism, not parameterization.
![Figure 5](figures/sweep6_scenario_ranking.png)

**Figure 6.** Archetype distribution over 80 timesteps — baseline (top) vs full bundle (bottom) at 80% post-labor. Dominant pathway: Productive → Beautiful One → Withdrawn → Collapsed.
![Figure 6](figures/sweep5_archetypes.png)

**Figure 7.** Historical analogues — model predictions mapped to Nauru (baseline collapse) and Gulf states (collectivism + UBI stability). Post-hoc pattern matching, not formal validation.
![Figure 7](figures/historical_analogues.png)
