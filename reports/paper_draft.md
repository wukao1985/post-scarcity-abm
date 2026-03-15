# Equilibrium Dynamics of Meaning and Behavioral Sink in Post-Labor Societies: A Stylized Agent-Based Analysis

**Authors:** Anonymous Authors (under review)

**Keywords:** post-labor displacement, behavioral sink, self-determination theory, agent-based modeling, role substitution, social cohesion, universal basic income

---

## Abstract

What equilibrium states does a society reach when large fractions of the population lack productive roles? We present a stylized agent-based model (ABM) integrating Self-Determination Theory (SDT) with social contagion dynamics to characterize population-level equilibria under sustained role displacement. The model does not represent individual unemployment trajectories; instead, it identifies what stable configurations of meaning, behavioral archetypes, and social cohesion emerge at different displacement levels and intervention regimes. Across six parameter sweeps and two structural ablation studies totaling 18,500 simulation runs, we find:

1. A steep threshold effect occurs in the 80-90% role displacement zone under baseline parameterization (specific percentages are model-dependent), and this threshold is policy-sensitive — shifting higher with combined interventions. Rapid displacement affects transition duration but not the final equilibrium.

2. Income support (UBI) alone leaves substantial residual sink: at 95% displacement, UBI-only conditions show a sink index of ~0.52 with elevated distress even without full collapse.

3. Under default parameterization, role substitution shows modest advantage over income transfers (sink ~0.46 ± 0.02 vs ~0.52 ± 0.02 at 95% displacement), though this advantage is parameter-dependent and reverses when restoration strength is equalized (see §3.5).

4. Social cohesion moderates sink severity: higher collectivism is associated with substantially lower UBI-associated sink under UBI conditions at 95% displacement.

5. Transition speed is transient: when matched on time since reaching target displacement, rapid and gradual automation converge to the same equilibrium. The displacement level and intervention regime, not the transition path, determine the final state.

These equilibrium findings suggest that meaning infrastructure (role programs, social cohesion, virtual role substitutes) is as critical as economic redistribution in determining the stable state a post-labor society reaches. *Note: aggressive behavior is a known validation gap (~2% modeled vs. Calhoun's 10-20% observed); results characterize withdrawal-dominated dynamics and should not be extrapolated to high-aggression scenarios.*

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

**Social Contagion Theory:** Behavioral sink spreads through social networks via complex contagion — behaviors requiring social reinforcement from multiple contacts rather than simple exposure (Centola & Macy, 2007; Christakis & Fowler, 2007). Our model incorporates contagion dynamics where collapsed agents increase collapse risk among network neighbors.

**Institutional Capacity:** Following Acemoglu & Robinson (2012), we model interventions as institutional capacities—policy choices that shape how societies respond to technological shocks.

---

## 2. Methods

### 2.1 Model Overview

We developed a network-based agent-based model (ABM) using Mesa 3.5 (Kazil et al., 2021), following ODD protocol conventions (Grimm et al., 2020), with 200 agents interacting over 80 timesteps. **This is a stylized model of post-labor dynamics designed to characterize equilibrium states, not a forecast of specific technological timelines or displacement levels.** The model extends prior work (V1, V2) with refined psychological dynamics and five intervention dimensions.

**Modeling displacement as a population-level rate.** In this model, `post_labor_fraction` represents the share of the population lacking productive roles at any given timestep, not a permanent individual state. At each step, this fraction is drawn from the agent pool, representing the turnover inherent in labor markets even under high automation. This design treats displacement as a structural condition of the society rather than a permanent individual trajectory — appropriate for studying equilibrium properties, though it precludes claims about individual scarring or adjustment dynamics. Persistent individual displacement is a natural extension for future work.

**Agent state variables:**
- Psychological: autonomy, competence, relatedness, status (0-1 scales)
- Role: economic_role (displacement status), virtual_role (virtual world engagement)
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

where contribution = 0.8×economic_role + 0.1×virtual_role, and contagion is the neighborhood sink exposure scaled by contagion_strength. The direct contagion and resilience terms capture social network effects and individual buffering beyond the SDT components.

**Weight justification:**

| Weight | Value | Basis |
|--------|-------|-------|
| Autonomy, Competence, Relatedness | 0.25 each | SDT: three core needs weighted equally (Deci & Ryan, 2000) |
| Status | 0.10 | Calibration: status matters but is not a core SDT need |
| Contribution | 0.15 | Calibration: captures "mattering" dimension absent from SDT triad |
| Economic contribution | 0.80 | Assumption: real-world productive roles provide primary meaning |
| Virtual contribution | 0.10 | Assumption: virtual roles provide partial but limited meaning substitute |
| Decay rate | 0.08 | Calibration: produces equilibration within ~30 steps |
| Noise σ | 0.08 | Calibration: V4 recalibration for realistic between-run variance |
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

**Intervention coupling.** In our implementation, the UBI scenario includes a fairness boost (reflecting UBI's social legitimacy signal), and role programs enhance both economic role and competence directly. These couplings are intentional design choices reflecting real-world co-occurrence of interventions, but mean that UBI and fairness effects are not fully orthogonal.

**Validation:** V4 reproduces the directional pattern of V2 findings (threshold behavior in the 80-90% zone under baseline conditions), with broader confidence intervals due to increased stochasticity. Note that V4 was calibrated to approximate V2 outputs; this comparison validates implementation consistency, not independent replication.

**Horizon robustness.** We verified that outcomes are near-stationary by step 80: extending simulations to T=160 and T=240 changes mean sink_index by less than 0.01 across all 9 tested conditions (3 scenarios × 3 displacement levels). The maximum delta between T=80 and T=120 is 0.009, well below the 0.02 convergence threshold. We therefore use T=80 as a reliable approximation of the near-equilibrium state. Full convergence table in Supplementary Methods.

### 2.5 Sensitivity Analysis

We conducted one-at-a-time perturbation of three key internal parameters (noise σ, decay rate, contagion strength) by ±20%, with 50 runs per condition at PL=0.80 and PL=0.95 baseline. Core findings are directionally consistent across tested parameter ranges: at PL=0.95, collapse occurs in 92-100% of runs across all perturbations; at PL=0.80, collapse remains rare (2-12%). The most sensitive parameter is contagion strength, which governs the positive feedback loop driving collective collapse (+20% raises PL=0.80 collapse from 2% to 12%). Full sensitivity results are reported in the Methods Appendix.

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

Under baseline conditions (no interventions, gradual automation), the model exhibits a steep threshold effect in the 80-90% post-labor zone (Figure 1). At 80% post-labor, baseline collapse probability is 2%; at 90%, it rises to 86%; at 95%, 100%.

![Figure 1: Threshold effect — sink index and collapse probability across post-labor levels under baseline conditions](figures/sweep1_phase_transition.png) The transition zone — rather than a knife-edge threshold — is consistent with complex adaptive systems theory and more realistic than a sharp critical point. This zone proves highly sensitive to policy and contextual factors.

**Speed affects transition duration, not equilibrium:** At matched time-since-target-displacement (t+10 after reaching PL=0.95), rapid and gradual automation converge to the same equilibrium (see §3.3). Naive comparisons at fixed T=80 confound speed with time-at-target; matched analysis shows the displacement level, not the transition path, determines the final state.

**Virtual worlds extend threshold higher:** With virtual_world_quality ≥ 0.6, collapse probability at 80% post-labor is 3% without virtual infrastructure vs. 0% with it. Under high-quality virtual conditions, collapse is not observed below 90% displacement (though this is based on n=50 runs; treat as directional).

**Combined interventions push threshold to 95%:** Full intervention bundles (UBI + role substitution + fairness + virtual worlds + collectivism) achieve 0% collapse even at 95% post-labor.

**V4 validation note:** We re-ran key sweeps with increased stochasticity (σ=0.08, up from 0.02, plus agent-level shocks). Core findings replicated with a broader transition zone and wider confidence intervals. The shift from a sharp 80% threshold to an 80-90% transition zone reflects more realistic noise levels — the earlier sharp threshold was partially an artifact of insufficient stochasticity.

### 3.2 Virtual Worlds as Substitutes (RQ2)

Virtual worlds provide significant and graded protection (Figure 2).

![Figure 2: Virtual world quality effect on sink index at 80% and 95% post-labor](figures/sweep3_virtual_world.png)

At 80% post-labor:
- Zero virtual quality: 3% collapse, sink 0.627
- Moderate quality (0.6): 0% collapse, sink 0.475
- Maximum quality (1.0): 0% collapse, meaning 0.471, sink 0.353

At 95% post-labor:
- Zero virtual quality: 100% collapse, sink 0.792
- Moderate quality (0.6): 6% collapse, sink 0.658
- Maximum quality (1.0): 0% collapse, meaning 0.416, sink 0.517
- UBI + virtual quality 0.8: 0% collapse, sink 0.294

The marginal benefit of virtual quality is concave — substantial gains occur between 0.0 and 0.6, with diminishing returns above 0.8. At 95% displacement, virtual worlds alone reduce collapse from 100% to 0%, though elevated sink (0.517) persists even at maximum quality, indicating partial but incomplete substitution.

The model's contribution weighting (virtual contribution counts 0.1 vs. 0.8 for economic roles) creates a ceiling effect: even maximum virtual quality leaves a meaning gap. Combining virtual worlds with UBI closes this gap substantially (sink 0.294 vs 0.517 with virtual alone).

**Sensitivity to contribution weights.** The virtual-world ceiling is partially structural: our default 8:1 contribution weight (economic vs virtual) was varied from 3:1 to ∞ in an ablation study (1,000 runs). At ratios below 5:1, virtual-world-only scenarios approach UBI performance (sink difference < 0.04). At the current 8:1 assumption, the gap is negligible (0.514 vs 0.509). At ratios above 12:1, UBI clearly dominates virtual-only (sink 0.542 vs 0.514). This confirms the finding is assumption-sensitive: societies where virtual engagement carries greater psychological weight would see different equilibria. However, two results are directionally consistent across all tested ratios: (1) virtual-only always prevents collapse (0% across all ratios), and (2) UBI+virtual always dominates either single intervention.

### 3.3 Speed of Automation (RQ3)

To isolate speed effects from exposure-time confounds, we conducted a controlled comparison (Figure 3) measuring outcomes at matched intervals after each scenario reaches its target displacement (PL=0.95).

![Figure 3: Speed comparison — rapid vs gradual automation convergence to same equilibrium](figures/sweep2_automation_speed.png) Rapid automation (speed=0.20) reaches the target in ~5 steps; gradual automation (speed≈0.006) reaches it in ~160 steps.

**Finding: speed is transient, not structural.** At matched time-since-target-displacement (10 steps after reaching PL=0.95), both speeds show similar sink levels converging toward the same equilibrium:

| Speed | Sink (t+10) | Sink (t+40) | Equilibrium |
|-------|-------------|-------------|-------------|
| Rapid | 0.645 | 0.789 | ~0.79 |
| Gradual | 0.775 | 0.797 | ~0.80 |

Counterintuitively, gradual automation produces *higher* sink at matched exposure times (0.775 vs 0.645 at t+10), because the extended ramp period allows social contagion to accumulate during partial displacement. The original naive comparison (both measured at T=80) confounded speed with exposure time: rapid had 75 steps at full displacement while gradual had just reached its target.

At equilibrium (t+40), both speeds converge to nearly identical outcomes (~0.79 sink for baseline). This is consistent with the interpretation that **the displacement level, not the path taken, determines the final state**. Interventions dominate speed effects: full_bundle produces sink ≈ 0.12-0.13 regardless of speed.

These findings suggest that transition velocity affects transition duration but not the final equilibrium state, as confirmed by our horizon robustness analysis; formal intervention timing analysis is left to future work.

### 3.4 Collectivism as Social Buffer (RQ4)

Collectivism alone cannot prevent baseline collapse (Figure 4).

![Figure 4: UBI × collectivism interaction — collapse probability and sink index at 95% post-labor](figures/sweep4_ubi_collectivism_interaction.png)

**Baseline at 95% post-labor (no interventions):**
- Collectivism 0.0: 100% collapse, sink 0.812
- Collectivism 1.0: 92% collapse, sink 0.743 (modest reduction, collapse still near-certain)

**UBI at 95% post-labor (collectivism as moderator):**
- Collectivism 0.0: 0% collapse, sink 0.549
- Collectivism 0.4: 0% collapse, sink 0.504
- Collectivism 0.8: 0% collapse, sink 0.462
- Collectivism 1.0: 0% collapse, sink 0.443 (19% lower sink than collectivism 0.0)

The UBI × collectivism interaction is striking: under UBI conditions at 95% displacement, higher collectivism is associated with substantially lower sink severity — sink ranges from 0.549 at collectivism=0.0 to 0.443 at collectivism=1.0, though collapse probability remains 0% across all collectivism levels.

The collectivism effect is a continuous moderator rather than a threshold switch: higher collectivism is progressively associated with lower sink index across all conditions, but does not independently prevent collapse in baseline scenarios. The mechanism operates through relatedness maintenance — collectivist structures provide alternative social connection sources when workplace ties are severed.

This finding suggests cultural context is associated with the severity of post-labor distress. Societies with higher baseline collectivism (East Asian, Nordic) show lower sink levels at equivalent displacement. Under UBI conditions at high displacement, higher collectivism is associated with lower sink indices.

### 3.5 Intervention Combinations at Extreme Automation (RQ5)

At 95% post-labor — the stress test for any post-labor policy — we rank intervention effectiveness by sink index (Figure 6):

![Figure 6: Intervention ranking by sink index at 95% post-labor across 10 scenarios](figures/sweep6_scenario_ranking.png)

**Tier 1 (0% collapse, sink < 0.15):**
- All bundle (+ virtual + collectivism): 0.090 sink
- Full bundle (UBI + roles + fairness): 0.130 sink

**Tier 2 (0% collapse, sink 0.2-0.5):**
- Roles + Virtual: 0.247 sink
- UBI + Virtual: 0.293 sink
- Roles only: 0.459 sink
- UBI + Collectivism: 0.466 sink
- UBI only: 0.518 sink

**Tier 3 (collapse > 0%):**
- Fairness + Collectivism: 0.614 sink, 1% collapse
- Fairness only: 0.661 sink, 12% collapse
- Baseline: 0.790 sink, 100% collapse

**Critical insights:**

1. **Multi-pillar interventions dominate:** Full and all bundles achieve the lowest sink (<0.15), confirming that addressing multiple psychological needs simultaneously is most effective.

2. **Virtual worlds are the most potent addition to single interventions:** Adding virtual worlds to UBI is associated with a 43% reduction in sink (0.518 → 0.293). Adding virtual worlds to roles is associated with a 46% reduction in sink (0.459 → 0.247).

3. **Role substitution shows advantage over income support under default parameterization:** At 95%, roles-only (~0.46 sink) shows lower sink than UBI-only (~0.52 sink) under default parameters, though this ranking is parameter-dependent (see decomposition below).

**Decomposing the roles advantage.** To isolate the source of role programs' advantage, we ran a matched comparison (450 runs) where UBI and roles were equalized on economic_role restoration strength (both at 0.30). Under this condition, roles_matched (no competence boost, matched strength) produces sink 0.575 ± 0.003 — *worse* than ubi_pure (sink 0.516 ± 0.003), because UBI includes an implicit fairness co-benefit that roles lack. The full roles advantage (sink 0.460 ± 0.003 vs 0.516 ± 0.003) therefore decomposes into: competence pathway + higher default strength (Δsink = 0.115) minus UBI's fairness advantage (Δsink = 0.059), yielding a net advantage of 0.056. This suggests role programs' superiority is partly mechanistic (competence development provides genuine benefit that income cannot) and partly parameterization (stronger default restoration strength). When equalized on strength, UBI's fairness co-benefit actually dominates roles' competence pathway alone.

4. **Fairness redistribution is insufficient alone:** Fairness-only scenarios show 12% collapse and high sink (0.661) because they don't address role absence.

5. **No single intervention eliminates elevated sink:** Even the best single intervention (roles, 0.459) leaves nearly half the population in suboptimal states at 95% displacement.

### 3.6 Archetype Trajectories (RQ5 Continued)

Time-series analysis reveals archetype emergence patterns (Figure 5):

![Figure 5: Archetype distribution over 80 timesteps — baseline vs full bundle at 80% post-labor](figures/sweep5_archetypes.png)

**Baseline trajectory (80% post-labor):**
- Steps 0-10: Productive drops from 100% to 60%, Beautiful Ones emerge (29%)
- Steps 10-25: Withdrawn surge (9% → 28%), Collapsed emerge (1% → 10%)
- Steps 25-80: Gradual stabilization (10% Productive, 28% Beautiful Ones, 37% Withdrawn, 24% Collapsed, ~2% Aggressors)

**Full bundle trajectory:**
- Productive remains ~60% throughout (down from 100% at step 0)
- Beautiful Ones at ~32%, small Withdrawn fraction (~8%)
- Sink index stable at ~0.09

The dominant pathway is Productive → Beautiful One → Withdrawn → Collapsed, with aggression remaining rare (~1-2%) throughout. The Beautiful One phase — surface-level functioning without productive engagement — is the most common transitional state, consistent with Calhoun's observation of "beautiful ones" as a withdrawal archetype. Our results are consistent with the hypothesis that earlier intervention preserves social cohesion, though the model does not include an explicit deployment timing parameter.

### 3.7 Historical Validation: Nauru vs. Gulf States

To assess qualitative plausibility, we mapped two historical natural experiments to model conditions (Figure 7). These cases were selected post-hoc as contrasting archetypes; this is not a prospective validation test.

![Figure 7: Historical analogues — model predictions vs Nauru (collapse) and Gulf states (stability)](figures/historical_analogues.png) The Republic of Nauru experienced rapid resource-driven wealth from phosphate mining (1960s-1990s), providing citizens with income eliminating the need for employment — a natural experiment in UBI-without-purpose. The result was social dissolution: 94% obesity, 31% diabetes, alcohol abuse, and family breakdown. Our model's baseline condition at PL=0.95 predicts meaning=0.330, sink=0.790, collapse=100% — consistent with Nauru's near-total social dysfunction despite material sufficiency.

Gulf states (UAE, Qatar, Kuwait) achieved comparable post-scarcity through oil wealth with radically different outcomes (Ross, 2012). The key structural difference: collectivist social institutions (tribal structures, Islamic community norms). Our model predicts collectivism=0.8 + UBI at PL=0.80 → meaning=0.476, sink=0.323, collapse=0% — consistent with the Gulf pattern of stability with some disengagement but no systemic collapse.

The collectivism variable is associated with sink severity differences: at PL=0.95 with UBI, sink is 0.549 at collectivism=0.0 (Nauru-like) vs. 0.462 at collectivism=0.8 (Gulf-like). While both avoid outright collapse with UBI, higher collectivism produces meaningfully lower distress. The model was not fitted to either case; this divergence emerges from the theoretical framework alone. This comparison is illustrative only; both cases were selected post-hoc and differ on numerous dimensions beyond collectivism. We emphasize that this comparison is post-hoc pattern matching against two cases selected to differ maximally; it does not constitute formal empirical validation. While subject to extensive confounding (geography, colonial history, population size, resource type), the directional consistency provides qualitative plausibility evidence for the model's core mechanisms.

---

## 4. Discussion

### 4.1 Theoretical Implications

**Self-Determination Theory in Economic Context:** Our findings extend SDT by demonstrating that the three core needs (autonomy, competence, relatedness) can be satisfied through diverse channels. Economic roles are the default source, but virtual worlds (autonomy, competence) and collectivism (relatedness) provide partial substitutes. However, the ceiling effects suggest these substitutes are imperfect—extreme automation may exceed substitution capacity. Note that SDT needs are operationalized directly in our model's meaning function; consistency with SDT predictions is therefore expected by construction and does not constitute independent empirical validation of the theory.

**Threshold Dynamics in Social Systems:** The 80-90% zone exhibits steep threshold behavior: small parameter changes near this region produce disproportionately large outcome changes, consistent with nonlinear dynamics in complex adaptive systems. Unlike physical phase transitions, which require specific mathematical criteria (power-law scaling, diverging correlation lengths), we use "threshold effect" to describe this empirical pattern. Crucially, this threshold is policy-sensitive rather than fixed.

**Social Contagion Amplification:** The sharp increase in sink between steps 20-40 suggests contagion dynamics. Individual displacement effects are multiplied through social networks, creating emergent collective collapse exceeding individual-level predictions.

### 4.2 Policy Implications

**Multi-pillar necessity:** No single intervention suffices at extreme automation. Policy portfolios must address income (UBI), meaning (role substitution, virtual worlds), and connection (collectivism structures).

**Virtual infrastructure investment:** Virtual worlds show the largest marginal benefit when added to other interventions. Investment in high-quality virtual role systems—games, creative platforms, virtual civic engagement—may be as important as physical infrastructure.

**Transition management:** Our controlled speed comparison reveals that rapid and gradual automation converge to the same equilibrium — suggesting that *what interventions are in place* matters more than *how fast* automation occurs. The policy priority is ensuring adequate interventions exist, rather than managing automation speed per se.

**Cultural tailoring:** Collectivism effects suggest UBI programs should be designed differently in different cultural contexts. Individualist societies may need stronger supplementary interventions.

**Early warning systems:** The archetype trajectory (Productive → Beautiful One → Withdrawn → Collapsed, with Aggressor emergence rare at ~2%) provides a potential early warning framework. Rising Beautiful One and Withdrawn fractions may predict approaching collapse before sink indices cross thresholds.

### 4.3 Limitations and Self-Critique

**Residual determinism:** V4 increased noise (σ=0.08, plus agent-level shocks) to address V3's excessive determinism. Between-run standard deviations improved from ~0.002 to ~0.008 for meaning index, and Cohen's d between conditions dropped from 8-48 to ~9-12. While substantially improved, the model remains more deterministic than typical behavioral science data (where Cohen's d of 1-3 is common). The mean-reverting dynamics, while theoretically motivated, still dominate over noise at 80 timesteps. Consequently, conventional inferential statistics (p-values, power) are not meaningful given these effect sizes; we report point estimates and SEM as descriptive summaries only. Future versions should explore alternative update rules (e.g., multiplicative noise, regime-switching dynamics) to achieve realistic between-run variance.

**Intervention structure:** While our experimental design varies interventions individually and in combination, the implementation includes coupling between UBI and fairness effects, and between role programs and competence development (detailed in §2.4). Fully orthogonal comparisons would require further model decoupling. Real policies interact in ways not captured: UBI might reduce work motivation (negative with roles), virtual worlds might displace real-world socializing (negative with collectivism), fairness perception might depend on who benefits from role programs.

**Underrepresented aggressors:** V4 recalibrated aggressor thresholds, increasing prevalence from <1% to ~2-3% at high displacement. However, this remains below the 10-20% expected from Calhoun's observations. The aggression formula `(1-meaning)*(1-social_capital)*0.5 > 0.3` requires extremely low social capital (< 0.14) combined with low meaning — a narrow parameter region. The model effectively treats behavioral sink as withdrawal-dominated, underrepresenting the aggression dimension. Future work should explore alternative aggression mechanisms (e.g., relative deprivation, frustration-aggression dynamics).

**Displacement as population-level rate.** The model treats role displacement as a cross-sectional share rather than a permanent individual state. Each timestep, the displaced fraction is redrawn from the agent pool. This enables equilibrium analysis but precludes conclusions about individual adjustment trajectories, unemployment scarring, or the dynamics of managed transitions. Future work should model persistent individual displacement with explicit re-employment mechanisms.

**Intervention coupling.** Our UBI and roles scenarios have partially overlapping effects in the implementation (UBI affects fairness; roles affect competence directly). Ablation analysis (see Supplementary) shows the directional finding (roles > UBI) is consistent across ±20% parameter perturbation, but the magnitude depends on assumptions about the relative potency of different interventions. When equalized on economic restoration strength, UBI's fairness co-benefit actually outweighs roles' competence pathway, reversing the ranking. The intervention hierarchy reported in §3.5 should therefore be interpreted as conditional on the default parameterization.

**No endogenous adaptation:** Agents cannot create new institutions, discover novel purposes, form social movements, or develop emergent cultural responses. Human societies have repeatedly demonstrated capacity for institutional innovation under stress — the Industrial Revolution, post-WWII reconstruction, the digital economy. Our model assumes a fixed institutional landscape, which likely overstates collapse risk.

**Threshold-dependent results:** Many headline findings occur near the threshold zone (80-90% displacement) where small parameter changes produce large outcome shifts. While characteristic of complex systems, this sensitivity means our quantitative predictions are unreliable — the qualitative direction matters, but specific percentages should be treated with extreme caution.

**Model simplifications:**
- Static network structure (real networks rewire during disruption)
- Binary displacement (no gradations of underemployment)
- Homogeneous agents (no age, education, or skill variation)
- Single generation (no demographic replacement)
- No economic dynamics (markets, prices, innovation)

**Historical validation limitations:**
- Post-hoc case selection (not prospective prediction)
- Multiple confounders between Nauru and Gulf states beyond collectivism
- "Collectivism" reduces complex cultural systems to a single scalar
- Quantitative match is to qualitative patterns, not measured outcomes

### 4.4 Triangulation: System Dynamics Model (Pathway C)

To test whether our findings are method-dependent, we developed a parallel system dynamics (SD) model using stock-flow ODEs with three state variables: MeaningStock, SinkStock, and SocialTrust. The SD model was calibrated independently to the Nauru historical trajectory (1970-2000: resource wealth without purpose → social collapse) and then tested against the Gulf states comparison case (collectivist structures + resource wealth → stability).

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

**V5 extensions.** These findings suggest several natural extensions. First, a V5 model with persistent individual displacement states would enable study of unemployment scarring, managed transitions, and trajectory heterogeneity that the current equilibrium model cannot address. Second, empirical calibration of the economic-to-virtual contribution weight ratio from survey data on meaningful engagement would transform our sensitivity finding into a testable prediction. Third, a multi-site validation using deindustrialization data (Rust Belt, post-Soviet transitions) and resource-curse cases beyond Nauru and Gulf states would strengthen construct validity.

---

## 5. Conclusion

This stylized model identifies mechanisms by which post-labor displacement can drive behavioral sink — and mechanisms by which it can be prevented. Our findings do not predict when or whether AI will displace specific populations, but they characterize the dynamics that would follow such displacement.

The central insight is that income support, while necessary, is insufficient to prevent meaning loss. The mechanisms that drive behavioral sink — loss of competence, autonomy, social role, and contribution — require targeted intervention beyond economic redistribution. Role substitution programs, virtual role infrastructure, and social cohesion structures each address distinct psychological needs that income cannot satisfy.

The model's sensitivity to social cohesion — with higher collectivism being associated with lower UBI-associated sink, from 0.549 to 0.443 at 95% displacement — highlights that identical economic policies are associated with different severity outcomes depending on the social substrate. This finding is consistent with historical divergences between post-labor societies (Nauru vs. Gulf states) and suggests that cultural and institutional context deserves as much attention as economic policy design.

As a stylized model, these results identify mechanisms and qualitative relationships rather than precise thresholds. The specific numbers (80-90% transition zone, sink indices) are model-dependent and should not be interpreted as predictions. What the model contributes is a framework for thinking about which dimensions of human well-being are at risk under role displacement, and which intervention categories address which risks.

---

## References

Acemoglu, D., & Restrepo, P. (2018). The wrong kind of AI? Artificial intelligence and the future of labour demand. *Cambridge Journal of Regions, Economy and Society*, 11(1), 29-44.

Acemoglu, D., & Robinson, J. A. (2012). *Why nations fail: The origins of power, prosperity, and poverty*. Crown Business.

Autor, D. H. (2015). Why are there still so many jobs? The history and future of workplace automation. *Journal of Economic Perspectives*, 29(3), 3-30.

Brynjolfsson, E., & McAfee, A. (2014). *The second machine age: Work, progress, and prosperity in a time of brilliant technologies*. WW Norton & Company.

Calhoun, J. B. (1962). Population density and social pathology. *Scientific American*, 206(2), 139-148.

Case, A., & Deaton, A. (2020). *Deaths of Despair and the Future of Capitalism*. Princeton University Press.

Centola, D., & Macy, M. (2007). Complex contagions and the weakness of long ties. *American Journal of Sociology*, 113(3), 702-734.

Christakis, N. A., & Fowler, J. H. (2007). The spread of obesity in a large social network over 32 years. *New England Journal of Medicine*, 357(4), 370-379.

Connell, J. (2006). Nauru: The first failed Pacific state? *The Round Table*, 95(383), 47-63.

Deci, E. L., & Ryan, R. M. (2000). The "what" and "why" of goal pursuits: Human needs and the self-determination of behavior. *Psychological Inquiry*, 11(4), 227-268.

Felten, E. W., Raj, M., & Seamans, R. (2021). Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. *Strategic Management Journal*, 42(12), 2195-2217.

Frey, C. B., & Osborne, M. A. (2017). The future of employment: How susceptible are jobs to computerisation? *Technological Forecasting and Social Change*, 114, 254-280.

Grimm, V., et al. (2020). The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism. *JASSS*, 23(2), 7.

Hertog, S. (2010). *Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia*. Cornell University Press.

Hofstede, G. (2001). *Culture's Consequences: Comparing Values, Behaviors, Institutions, and Organizations Across Nations*. Sage.

Jahoda, M. (1982). *Employment and unemployment: A social-psychological analysis*. Cambridge University Press.

Kazil, J., Masad, D., & Crooks, A. (2021). Utilizing Python for agent-based modeling: The Mesa framework. In *Agent-Based Simulation of Organizational Behavior* (pp. 308-344). Springer.

Ross, M. (2012). *The oil curse: How petroleum wealth shapes the development of nations*. Princeton University Press.

Rosso, B. D., Dekas, K. H., & Wrzesniewski, A. (2010). On the meaning of work: A theoretical integration and review. *Research in Organizational Behavior*, 30, 91-127.

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
- **V4 Validation:** Detailed V3 vs V4 comparison showing effect of increased stochasticity on headline results
- **Weight Ablation:** Economic:virtual contribution ratio sensitivity (3:1 to ∞), 1,000 runs
- **Intervention Decoupling:** Matched-strength comparison of UBI vs roles, 450 runs
- **ODD Protocol:** Full ODD-compliant model description (Grimm et al., 2020)

---

## Appendix: Figures

**Figure 1.** Threshold effect — sink index and collapse probability across post-labor levels under baseline conditions. The transition zone (80–90%) broadens under V4 stochasticity.
![Figure 1](figures/sweep1_phase_transition.png)

**Figure 2.** Virtual world quality effect on sink index at 80% and 95% post-labor. Marginal benefit is concave, with largest gains between quality 0.0 and 0.6.
![Figure 2](figures/sweep3_virtual_world.png)

**Figure 3.** Speed comparison — rapid vs gradual automation. Both paths converge to the same equilibrium; speed is associated with transition duration but not with the final equilibrium state.
![Figure 3](figures/sweep2_automation_speed.png)

**Figure 4.** UBI × collectivism interaction at 95% post-labor. Under UBI, sink index is 0.549 in individualist societies (collectivism=0.0) and decreases to 0.443 in highly collectivist ones (collectivism=1.0), with 0% collapse across all collectivism levels.
![Figure 4](figures/sweep4_ubi_collectivism_interaction.png)

**Figure 5.** Archetype distribution over 80 timesteps — baseline (top) vs full bundle (bottom) at 80% post-labor. Dominant pathway: Productive → Beautiful One → Withdrawn → Collapsed.
![Figure 5](figures/sweep5_archetypes.png)

**Figure 6.** Intervention ranking by sink index at 95% post-labor across 10 scenarios. Multi-pillar bundles dominate; no single intervention achieves sink < 0.4.
![Figure 6](figures/sweep6_scenario_ranking.png)

**Figure 7.** Historical analogues — model predictions mapped to Nauru (baseline collapse) and Gulf states (collectivism + UBI stability). Post-hoc pattern matching, not formal validation.
![Figure 7](figures/historical_analogues.png)
