# Equilibrium Dynamics of Meaning and Behavioral Sink in Post-Labor Societies: A Stylized Agent-Based Analysis

**Authors:** Anonymous Authors (under review)

**Keywords:** post-labor displacement, behavioral sink, self-determination theory, agent-based modeling, role substitution, social cohesion, universal basic income

---

## Abstract

What equilibrium states does a society reach when large fractions of the population lack productive roles? We present a stylized agent-based model integrating Self-Determination Theory with social contagion dynamics to characterize population-level equilibria under sustained role displacement. Across six parameter sweeps and two ablation studies (18,500 primary runs), we find: (1) a steep, policy-sensitive threshold zone in the 80-90% displacement range under baseline conditions, with collapse probability rising from 2% at 80% post-labor to 86% at 90% and 100% at 95%; (2) UBI alone is insufficient at extreme displacement, yielding sink index 0.743 and 87.3% collapse probability at 95% post-labor in the full-grid sweep, even though the mean collapsed agent fraction is only 0.325; (3) role substitution is more protective than UBI under both the default and matched-strength comparisons, with sink 0.472 for `roles`, 0.582 for `roles_matched`, and 0.746 for `ubi_pure`; (4) multi-pillar bundles dominate at extreme displacement, with `all_bundle` reducing sink to 0.115 and eliminating collapse at 95% post-labor; and (5) collectivism moderates UBI-associated distress, lowering collapse from 97% to 31% as collectivism rises from 0.0 to 1.0 at 95% post-labor, while a separate exposure-time-controlled speed comparison shows that rapid and gradual automation differ sharply at t+10 after target displacement but nearly converge by t+40. All numerical values are conditional on this stylized parameterization and are intended as mechanistic rather than predictive statements. Aggressive behavior remains rare in the reported high-displacement conditions (1.6-3.3%), so the reported dynamics are withdrawal-dominated rather than aggression-dominated.

---

## 1. Introduction

### 1.1 The Role-Displacement Problem

Human well-being is deeply embedded in productive roles. Work provides not just income but identity, competence, social connection, and purpose (Blustein, 2008; Deci & Ryan, 2000). Technological displacement, deindustrialization, and resource windfalls have repeatedly demonstrated that removing productive roles — even while maintaining material sufficiency — can produce severe social pathology (Case & Deaton, 2020).

Calhoun's (1962) rodent experiments demonstrated "behavioral sink" — social collapse characterized by withdrawal, aggression, and reproductive failure — when populations lacked meaningful social roles. Jahoda (1982) established that employment provides not only income but latent functions: time structure, social contact, collective purpose, status, and activity — functions that persist as psychological needs even when income is secured through other means. The analogy to human post-labor conditions, while imperfect, raises urgent questions: What equilibrium states does a society reach when large fractions of the population lack productive roles? Which interventions shift the society toward more favorable equilibria, and under what conditions do they fail?

We note that aggressive behavior remains a validation gap: in the reported high-displacement conditions, aggressor prevalence ranges from 1.6% (step 80 in the baseline PL=0.80 time-series sweep) to 3.3% (baseline PL=0.95 in the full-grid sweep), versus the 10-20% aggression prevalence often associated with Calhoun's observations. Results therefore characterize withdrawal-dominated dynamics and should not be extrapolated to high-aggression scenarios.

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
| Virtual role decay | 0.95 factor (5%/step) | Multiplicative decay when agent has real role access (model.py:195) |
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

We conducted six parameter sweeps plus two primary ablation studies, totaling 18,500 runs:

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

In addition, §3.3 draws on a separate exposure-time-controlled speed comparison comprising 300 simulations (50 runs × 3 scenarios × 2 speeds). That supplementary dataset is reported separately and is not included in the 18,500-run primary total above.

**Intervention structure.** In our implementation, UBI and role substitution target distinct channels. UBI provides `income_support` (economic security, fairness buffer) without restoring role access; it does not enter the role-driven meaning channel. Role substitution provides `role_access` (meaning-generating participation), which directly affects autonomy, competence, relatedness, status, and contribution. The UBI scenario includes an implicit fairness boost (reflecting UBI's social legitimacy signal), and role programs include a competence boost. These are structural differences, not parameter differences: the roles-vs-UBI comparison tests whether meaning channels or economic channels matter more for preventing behavioral sink.

**Validation:** V5 reproduces the directional pattern of prior findings (threshold effect in the 80-90% zone under baseline conditions), with the critical structural change that UBI no longer provides role access. The V5 separation of UBI from roles is the most significant model change, revealing that earlier versions overstated UBI's effectiveness. Note that the model was calibrated to approximate prior output patterns; this comparison validates implementation consistency, not independent replication.

**Horizon robustness.** We verified that outcomes are near-stationary by step 80: across all 9 tested scenario × displacement conditions, the absolute change in mean sink_index between T=80 and T=120 ranges from 0.0009 to 0.0092, and all 9 conditions are flagged as converged in `convergence_summary.csv`. We therefore use T=80 as a reliable approximation of the near-equilibrium state. Full convergence table in Supplementary Methods.

### 2.5 Sensitivity Analysis

We conducted one-at-a-time perturbation of three key internal parameters (noise σ, decay rate, contagion strength) by ±20%, with 50 runs per condition at PL=0.80 and PL=0.95 baseline. Core findings are directionally consistent across tested parameter ranges: at PL=0.80, collapse probability ranges from 2% to 12%; at PL=0.95, it ranges from 92% to 100%. The largest PL=0.80 sink shift occurs under contagion-strength perturbation, where mean sink_index ranges from 0.605 at -20% to 0.657 at +20%. Full sensitivity results are reported in the Methods Appendix.

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

Under baseline conditions (no interventions, gradual automation), the model exhibits a steep threshold effect in the 80-90% post-labor zone (Figure 1). In `sweep1_results.csv`, baseline collapse probability rises from 2% at 80% post-labor (meaning 0.382, sink 0.629) to 86% at 90% (meaning 0.348, sink 0.736) and 100% at 95% (meaning 0.330, sink 0.788).

![Figure 1: Threshold effect — sink index and collapse probability across post-labor levels under baseline conditions](figures/sweep1_phase_transition.png) The transition zone is therefore broad rather than knife-edged, and it is highly policy-sensitive.

**Policy sensitivity within the threshold zone.** In the same sweep, `full_bundle` remains at 0% collapse through 95% post-labor and averages sink 0.301 at PL=0.95, while `ubi_only` reaches 32% collapse at PL=0.90 and 92% at PL=0.95. The threshold is therefore not fixed; it moves with the intervention mix.

**Virtual worlds extend the threshold upward.** In `sweep3_virtual_world.csv`, baseline PL=0.95 collapse probability falls from 100% at virtual-world quality 0.0 to 59% at 0.4, 8% at 0.6, and 0% at 0.8 and 1.0; the corresponding mean sink_index declines from 0.793 to 0.715, 0.659, 0.597, and 0.520.

**Combined interventions push the threshold beyond the tested range.** In `sweep6_full_grid.csv`, `all_bundle` achieves 0% collapse with sink 0.115 at PL=0.95.

**Run-level collapse is not the same metric as `collapsed_frac`.** In the PL=0.95 full-grid conditions, `ubi_only` averages sink 0.743, `collapsed_frac` 0.325, and collapse probability 87.3% because collapse is defined in the code as final `sink_index > 0.7`. By contrast, `roles` averages sink 0.472, `collapsed_frac` 0.122, and 0% collapse probability. This distinction matters throughout the paper: mean collapsed-agent share and run-level collapse probability move together, but they are not interchangeable statistics.

### 3.2 Virtual Worlds as Substitutes (RQ2)

Virtual worlds provide significant and graded protection (Figure 2).

![Figure 2: Virtual world quality effect on sink index at 80% and 95% post-labor](figures/sweep3_virtual_world.png)

At 95% post-labor (baseline, no UBI):
- Zero virtual quality: 100% collapse, sink 0.793
- Moderate quality (0.6): 8% collapse, sink 0.659
- Maximum quality (1.0): 0% collapse, sink 0.520

At 95% post-labor (with UBI):
- Zero virtual quality: 90% collapse, sink 0.746
- Moderate quality (0.6): 0% collapse, sink 0.598
- High quality (0.8): 0% collapse, sink 0.533

The marginal benefit of virtual quality is concave. In the baseline PL=0.95 condition, the largest collapse-probability drop occurs between quality 0.2 and 0.6 (97% to 8%), and in the `ubi_only` PL=0.95 condition collapse falls from 90% at quality 0.0 to 10% at 0.4 and 0% at 0.6. Even so, maximum virtual quality leaves substantial residual sink under baseline conditions (0.520 at quality 1.0), indicating partial rather than full substitution.

The full-grid sweep shows the same ordering at PL=0.95: `UBI+virtual` averages sink 0.535 with 0% collapse, while `roles+virtual` reaches sink 0.259 with 0% collapse. Virtual worlds therefore help most when paired with an intervention that also restores meaning-generating participation.

**Sensitivity to contribution weights.** The ceiling is assumption-sensitive, but the ranking is stable in `ablation_weights.csv`. At 3:1, `virtual_only` yields sink 0.446 versus 0.749 for `ubi_only`; at the default 8:1 ratio, 0.517 versus 0.747; and at `inf`, 0.584 versus 0.742. `ubi_plus_virtual` remains better than either single intervention at every tested ratio, ranging from sink 0.381 at 3:1 to 0.520 at `inf`.

### 3.3 Speed of Automation (RQ3)

To isolate speed effects from exposure-time confounds, we conducted a controlled comparison (Figure 3) measuring outcomes at matched intervals after each scenario reaches its target displacement (PL=0.95).

![Figure 3: Speed comparison — rapid vs gradual automation under matched time-since-target conditions in the equilibrium ABM](figures/sweep2_automation_speed.png) Rapid automation (speed = 0.20) reaches the target in 5 steps; gradual automation (speed = 0.95/160 = 0.0059) reaches it in 160 steps.

**Finding within the equilibrium ABM: speed effects are transient rather than structural.** In `speed_clean_comparison.csv`, gradual automation produces substantially higher sink immediately after target displacement, but the gap narrows over time:

| Speed | Sink (t+10) | Sink (t+40) |
|-------|-------------|-------------|
| Rapid | 0.638 | 0.777 |
| Gradual | 0.780 | 0.790 |

The same directional pattern appears in the other two scenarios. For `ubi_only`, sink is 0.732 under gradual automation versus 0.594 under rapid automation at t+10, narrowing to 0.739 versus 0.727 by t+40. For `full_bundle`, the difference is smaller throughout: 0.274 versus 0.241 at t+10 and 0.291 versus 0.302 at t+40.

The original naive comparison at fixed T=80 confounds ramp speed with time spent at the target displacement. Once outcomes are aligned by time-since-target, late-run aggregate states are similar: by t+40, the rapid-gradual sink difference is 0.013 in `baseline`, 0.012 in `ubi_only`, and 0.011 in `full_bundle`.

These findings suggest that transition velocity affects transition duration but not late-run aggregate outcomes within this equilibrium model, as confirmed by our horizon robustness analysis; persistent-displacement models are needed before drawing stronger conclusions about managed transition speed or intervention timing.

### 3.4 Collectivism as Social Buffer (RQ4)

Collectivism reduces distress, but it does not independently eliminate collapse at extreme displacement (Figure 4).

![Figure 4: UBI × collectivism interaction — collapse probability and sink index at 95% post-labor under UBI-only conditions](figures/sweep4_ubi_collectivism_interaction.png)

**Baseline at 95% post-labor (no interventions):**
- At collectivism 0.0, sink is 0.812 and collapse probability is 100%
- At collectivism 1.0, sink is 0.743 and collapse probability is 92%

**UBI at 95% post-labor (collectivism as moderator):**
- Collectivism 0.0: 97% collapse, sink 0.769
- Collectivism 0.4: 86% collapse, sink 0.732
- Collectivism 0.6: 63% collapse, sink 0.713
- Collectivism 0.8: 47% collapse, sink 0.704
- Collectivism 1.0: 31% collapse, sink 0.684

The collectivism sweep therefore reveals a continuous dose-response relationship: higher collectivism is associated with lower sink and lower collapse probability under both baseline and `ubi_only` conditions.

The effect is a moderator rather than a threshold switch. In `ubi_only` at PL=0.80, the same increase from collectivism 0.0 to 1.0 lowers sink from 0.600 to 0.511 while collapse remains at 0% throughout, showing that collectivism is more effective below the extreme-displacement regime than within it.

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
- Fairness + Collectivism: 0.614 sink, 0.7% collapse
- Fairness only: 0.661 sink, 12% collapse
- UBI + Collectivism: 0.703 sink, 51% collapse
- UBI only: 0.743 sink, 87.3% collapse
- Baseline: 0.790 sink, 100% collapse

**Critical insights:**

1. **Multi-pillar interventions dominate:** The all-bundle achieves the lowest sink (0.115), and roles+virtual (0.259) outperforms any single intervention, confirming that addressing multiple psychological needs simultaneously is most effective.

2. **Virtual worlds are the most potent addition to single interventions:** Adding virtual worlds to UBI lowers sink from 0.743 to 0.535 and reduces collapse from 87.3% to 0%. Adding virtual worlds to roles lowers sink from 0.472 to 0.259.

3. **Role substitution is structurally superior to UBI at extreme displacement:** At 95%, `roles` achieves sink 0.472 and 0% collapse probability, versus 0.743 and 87.3% for `ubi_only`. The difference persists in `ablation_interventions.csv`, where `roles_matched` averages sink 0.582 versus 0.746 for `ubi_pure`.

4. **UBI alone performs poorly at extreme displacement:** At PL=0.95 in the full-grid sweep, `ubi_only` averages collapsed_frac 0.325 but crosses the run-level collapse threshold in 87.3% of runs. Economic security without restored role access is insufficient to prevent behavioral sink at extreme displacement in this model.

5. **Fairness redistribution is insufficient alone:** Fairness-only scenarios show 12% collapse and high sink (0.661) because they don't address role absence.

6. **No single intervention eliminates elevated sink:** Even the best single intervention (roles, 0.472) leaves nearly half the population in suboptimal states at 95% displacement. Multi-pillar bundles are essential.

**The structural roles-vs-UBI decomposition.** In the intervention-decoupling ablation, `ubi_pure`, `roles_matched`, and `roles_full` average sink 0.746, 0.582, and 0.471, respectively. The default roles configuration therefore improves on the matched-strength version by 0.110 sink points, but even the matched-strength roles condition substantially outperforms the income-only condition.

### 3.6 Archetype Trajectories (RQ5 Continued)

Time-series analysis reveals archetype emergence patterns (Figure 6):

![Figure 6: Archetype distribution over 80 timesteps — baseline vs full bundle at 80% post-labor](figures/sweep5_archetypes.png)

**Seeded initial condition (step 0):** Because archetypes are classified before initial data collection in V5, the time series no longer begins with an artificial 100% productive population. The seeded distribution is 70.5% Productive and 29.5% Beautiful Ones under both scenarios.

**Baseline trajectory (80% post-labor):**
- Steps 0-10: Productive declines from 70.5% to 60.5%, while Withdrawn and Collapsed emerge to 8.9% and 1.3%
- Steps 10-25: Withdrawn rises from 8.9% to 27.9%, while Collapsed rises from 1.3% to 10.2%
- Step 80: the population stabilizes at 9.6% Productive, 28.0% Beautiful Ones, 37.1% Withdrawn, 23.7% Collapsed, and 1.6% Aggressors; sink_index = 0.624

**Full bundle trajectory:**
- Step 80 ends at 40.7% Productive and 39.8% Beautiful Ones, with only 16.4% Withdrawn, 3.1% Collapsed, and 0.1% Aggressors
- Final sink index is 0.195

The dominant pathway is Productive → Beautiful One → Withdrawn → Collapsed, with aggression remaining rare throughout. The Beautiful One phase is already present in the seeded initial condition and remains the most common transitional state before collapse deepens.

### 3.7 Historical Validation: Nauru vs. Gulf States

To assess qualitative plausibility, we mapped two historical cases that share structural features with model conditions (Figure 7). These cases were selected post-hoc as contrasting archetypes; this is not a prospective validation test.

![Figure 7: Historical analogues — model predictions vs Nauru (collapse) and Gulf states (stability)](figures/historical_analogues.png) The Republic of Nauru experienced rapid resource-driven wealth from phosphate mining (1960s-1990s), providing citizens with income eliminating the need for employment — a case that shares structural features with the UBI-without-purpose scenario. The period was associated with severe social dysfunction: 94% obesity, 31% diabetes, alcohol abuse, and family breakdown. Our model's PL=0.95 baseline full-grid condition yields meaning 0.330, sink 0.790, and 100% collapse probability — broadly consistent with a severe dysfunction analogue despite material sufficiency.

Gulf states (UAE, Qatar, Kuwait) achieved comparable post-scarcity through oil wealth with radically different outcomes (Ross, 2012). One notable difference between the cases is the role of collectivist social institutions (tribal structures, Islamic community norms), though multiple confounds preclude causal attribution. Our PL=0.80 `UBI+collectivism` full-grid condition yields meaning 0.416, sink 0.526, and 0% collapse probability, which is consistent with a more stable but still strained configuration rather than full flourishing. The more favorable Gulf outcomes likely reflect role preservation (government employment, civic participation) beyond what UBI alone provides, consistent with our finding that role substitution is essential at high displacement.

The dedicated collectivism sweep shows the same directional moderation at PL=0.95 with UBI: sink falls from 0.769 at collectivism 0.0 to 0.704 at collectivism 0.8, and collapse probability falls from 97% to 47%; even at collectivism 1.0, however, 31% of runs still collapse. The model was not fitted to either case; this comparison is illustrative of the framework's mechanisms rather than evidence that collectivism explains the historical contrast.

---

## 4. Discussion

### 4.1 Theoretical Implications

**Self-Determination Theory in Economic Context:** Within the SDT framework, our model illustrates that the three core needs (autonomy, competence, relatedness) can be operationalized through diverse channels. Economic roles are the default source, but virtual worlds (autonomy, competence) and collectivism (relatedness) provide partial substitutes. However, the ceiling effects suggest these substitutes are imperfect—extreme automation may exceed substitution capacity. Note that SDT needs are operationalized directly in our model's meaning function; consistency with SDT predictions is therefore expected by construction and does not constitute independent empirical validation of the theory.

**Threshold Dynamics in Social Systems:** The 80-90% zone exhibits steep threshold behavior: small parameter changes near this region produce disproportionately large outcome changes, consistent with nonlinear dynamics in complex adaptive systems. Unlike physical phase transitions, which require specific mathematical criteria (power-law scaling, diverging correlation lengths), we use "threshold effect" to describe this empirical pattern. Crucially, this threshold is policy-sensitive rather than fixed.

**Social Contagion Amplification:** The sharp increase in sink between steps 20-40 suggests contagion dynamics. Individual displacement effects are multiplied through social networks, creating emergent collective collapse exceeding individual-level predictions.

### 4.2 Policy Implications

**Multi-pillar necessity:** No single intervention suffices at extreme automation. At PL=0.95 in the full-grid sweep, `ubi_only` shows sink 0.743 and 87.3% collapse probability, while `roles` lowers sink to 0.472 but still leaves a large subpopulation in sink states. Policy portfolios must address income (UBI), meaning (role substitution, virtual worlds), and connection (collectivism structures). The `all_bundle` condition (sink 0.115, 0% collapse) demonstrates the advantage of combined approaches.

**Virtual infrastructure investment:** Virtual worlds show the largest marginal benefit when added to other interventions, and are now especially critical because UBI alone does not restore role access. In the full-grid sweep, adding virtual worlds to UBI lowers sink from 0.743 to 0.535 and reduces collapse from 87.3% to 0% at PL=0.95.

**Transition management:** Our controlled speed comparison shows similar late-run aggregate outcomes for rapid and gradual automation once the same target displacement is reached, but gradual ramps accumulate more distress during the transition. This conclusion is conditional on the equilibrium ABM design, which does not model persistent individual displacement, scarring, or retraining trajectories; a persistent-displacement model is needed before drawing operational guidance about transition speed management. Within that framing, intervention provision matters more than automation speed in shaping the model's late-run state.

**Cultural tailoring:** Collectivism effects suggest UBI programs should be designed differently in different cultural contexts. Even at maximum collectivism, `ubi_only` still shows 31% collapse at PL=0.95, while the same condition collapses in 97% of runs at collectivism 0.0. Cultural infrastructure alone is therefore insufficient without role-targeted interventions.

**Early warning systems:** The archetype trajectory (Productive → Beautiful One → Withdrawn → Collapsed, with Aggressors at 1.6% by step 80 in the baseline time series) provides a potential early warning framework. Rising Beautiful One and Withdrawn fractions may predict approaching collapse before sink indices cross thresholds.

### 4.3 Limitations and Self-Critique

**Residual determinism:** V5 carries forward V4's increased noise (σ=0.08, plus agent-level shocks). In the baseline sensitivity table, the between-run standard deviation of `meaning_index` is 0.0081 at PL=0.80 and 0.0078 at PL=0.95. The model remains more deterministic than typical behavioral science data (where Cohen's d of 1-3 is common). The mean-reverting dynamics, while theoretically motivated, still dominate over noise at 80 timesteps. Consequently, conventional inferential statistics (p-values, power) are not meaningful given these effect sizes; we report point estimates and SEM as descriptive summaries only. Future versions should explore alternative update rules (e.g., multiplicative noise, regime-switching dynamics) to achieve realistic between-run variance.

**Intervention structure:** While our experimental design varies interventions individually and in combination, V5 cleanly separates UBI (income_support) from role substitution (role_access). The implementation includes coupling between UBI and fairness effects, and between role programs and competence development (detailed in §2.4). Real policies interact in ways not captured: UBI might reduce work motivation (negative with roles), virtual worlds might displace real-world socializing (negative with collectivism), fairness perception might depend on who benefits from role programs. The V5 separation ensures the core finding — that meaning channels dominate economic channels — is not an artifact of bundling.

**Underrepresented aggressors:** V5 carries forward V4's recalibrated aggressor thresholds, but prevalence remains low in the reported high-displacement outputs: 1.6% at step 80 in the baseline PL=0.80 time-series sweep and 3.3% in the baseline PL=0.95 full-grid condition. This is still below the 10-20% aggression prevalence often associated with Calhoun's observations. The aggression formula `(1-meaning)*(1-social_capital)*0.5 > 0.3` requires extremely low social capital (< 0.14) combined with low meaning — a narrow parameter region. The model therefore treats behavioral sink as withdrawal-dominated and underrepresents the aggression dimension.

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

The central insight is that economic redistribution alone (UBI) is insufficient at extreme displacement. In the PL=0.95 full-grid condition, `ubi_only` averages sink 0.743, mean `collapsed_frac` 0.325, and 87.3% collapse probability under the paper's run-level definition (`sink_index > 0.7`). The V5 structural separation therefore sharpens the substantive interpretation: meaning-generating participation (through role programs, virtual infrastructure, and social cohesion) is not merely complementary to economic policy but a central determinant of whether collapse is avoided. Role substitution alone averages sink 0.472 with 0% collapse probability, and multi-pillar bundles achieve the best outcomes (`all_bundle` sink 0.115, 0% collapse).

The model's sensitivity to social cohesion — with `ubi_only` collapse falling from 97% to 31% as collectivism rises from 0.0 to 1.0 at PL=0.95 — highlights that identical economic policies are associated with dramatically different outcomes depending on the social substrate. However, even maximum collectivism cannot prevent collapse without role-targeted interventions. This finding is consistent with the paper's illustrative historical contrast between more collapse-prone and more stable post-labor societies and suggests that cultural and institutional context deserves as much attention as economic policy design.

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

All simulation code, primary data (6 sweeps + 2 ablation studies, 18,500 runs), supplementary CSVs for the clean speed comparison, sensitivity analysis, and horizon robustness, and the analysis scripts used to generate the figures are available at: https://github.com/wukao1985/post-scarcity-abm

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

**Figure 1.** Threshold effect — sink index and collapse probability across post-labor levels under baseline conditions. Collapse probability is 2% at PL=0.80, 86% at PL=0.90, and 100% at PL=0.95.
![Figure 1](figures/sweep1_phase_transition.png)

**Figure 2.** Virtual world quality effect on sink index at 80% and 95% post-labor. In the baseline PL=0.95 condition, sink falls from 0.793 at quality 0.0 to 0.520 at quality 1.0, with collapse probability reaching 0% by quality 0.8.
![Figure 2](figures/sweep3_virtual_world.png)

**Figure 3.** Speed comparison — rapid vs gradual automation. In the clean comparison, baseline sink is 0.780 under gradual automation versus 0.638 under rapid automation at t+10 after target displacement, narrowing to 0.790 versus 0.777 by t+40.
![Figure 3](figures/sweep2_automation_speed.png)

**Figure 4.** UBI × collectivism interaction at 95% post-labor. Under `ubi_only`, sink decreases from 0.769 at collectivism 0.0 to 0.684 at collectivism 1.0, while collapse probability falls from 97% to 31%.
![Figure 4](figures/sweep4_ubi_collectivism_interaction.png)

**Figure 5.** Intervention ranking by sink index at 95% post-labor across 10 scenarios. Multi-pillar bundles dominate; `ubi_only` shows sink 0.743 and 87.3% collapse probability, whereas `roles` shows sink 0.472 and 0% collapse probability.
![Figure 5](figures/sweep6_scenario_ranking.png)

**Figure 6.** Archetype distribution over 80 timesteps — baseline (top) vs full bundle (bottom) at 80% post-labor. The seeded state is 70.5% Productive and 29.5% Beautiful Ones; by step 80, sink is 0.624 in baseline versus 0.195 in `full_bundle`.
![Figure 6](figures/sweep5_archetypes.png)

**Figure 7.** Historical analogues — model predictions mapped to Nauru (baseline collapse) and Gulf states (`UBI+collectivism` stability). The illustrative mappings use PL=0.95 baseline (meaning 0.330, sink 0.790) and PL=0.80 `UBI+collectivism` (meaning 0.416, sink 0.526).
![Figure 7](figures/historical_analogues.png)
