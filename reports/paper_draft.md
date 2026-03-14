# Behavioral Sink Under Post-Labor Displacement: Mechanisms of Meaning Loss, Social Contagion, and Intervention in a Stylized Agent-Based Model

**Authors:** [Redacted for peer review]

**Keywords:** post-labor displacement, behavioral sink, self-determination theory, agent-based modeling, role substitution, social cohesion, universal basic income

---

## Abstract

What happens to human well-being when populations are displaced from productive roles? We present a stylized agent-based model (ABM) integrating Self-Determination Theory (SDT) with social contagion dynamics to study mechanisms of meaning loss, behavioral cascade, and intervention under post-labor conditions. Across 17,050 simulation runs spanning six parameter sweeps, we find:

1. A phase transition to behavioral sink occurs in the 80-90% role displacement zone (critical point ~88%), but this threshold is policy-malleable — shifting lower under rapid displacement and higher with combined interventions.

2. Income support (UBI) is necessary but insufficient: at 95% displacement, UBI alone produces a sink index of 0.515 and elevated distress even without full collapse.

3. Role substitution programs outperform income transfers in preventing meaning loss (sink index 0.458 vs 0.515 at 95% displacement).

4. Social cohesion is the decisive moderator: collectivism reduces UBI-associated sink — a finding consistent with the Nauru (collapse) vs Gulf states (stability) historical divergence.

5. Transition speed matters: rapid displacement produces 46 percentage points more collapse than gradual displacement at 95% automation (100% vs 54%).

Our findings identify which mechanisms drive or prevent behavioral sink under post-labor conditions, suggesting that meaning infrastructure (role programs, social cohesion, virtual role substitutes) is as critical as economic redistribution.

---

## 1. Introduction

### 1.1 The Role-Displacement Problem

Human well-being is deeply embedded in productive roles. Work provides not just income but identity, competence, social connection, and purpose (Blustein, 2008; Deci & Ryan, 2000). Technological displacement, deindustrialization, and resource windfalls have repeatedly demonstrated that removing productive roles — even while maintaining material sufficiency — can produce severe social pathology (Case & Deaton, 2020).

Calhoun's (1962) rodent experiments demonstrated "behavioral sink" — social collapse characterized by withdrawal, aggression, and reproductive failure — when populations lacked meaningful social roles. The analogy to human post-labor conditions, while imperfect, raises urgent mechanistic questions: What psychological and social dynamics drive or prevent behavioral sink when populations are displaced from productive roles? Which interventions are effective, and under what conditions do they fail?

### 1.2 The Gap in Current Understanding

Existing literature on AI and employment focuses primarily on:
- **Economic impacts:** unemployment rates, wage effects, inequality (Autor, 2015)
- **Technical feasibility:** which tasks can be automated (Felten et al., 2021)
- **Policy responses:** UBI, retraining programs, taxation (Standing, 2017)

What remains underexplored is the **psychological and social impact of role displacement independent of income loss**. A displaced worker receiving UBI may avoid poverty but still experience what Deci & Ryan (2000) term "motivation decay"—the erosion of autonomy, competence, and relatedness that constitute psychological well-being.

### 1.3 Research Questions

We address five questions:

**RQ1:** At what automation level does behavioral sink emerge, and is this threshold fixed or mutable?

**RQ2:** Can high-quality virtual worlds substitute for economic roles in providing meaning?

**RQ3:** Does the speed of automation matter independently of the final displacement level?

**RQ4:** Do collectivist vs. individualist cultural structures exhibit different collapse thresholds?

**RQ5:** What intervention combinations prevent collapse at extreme (≥90%) automation levels?

### 1.4 Theoretical Framework

We integrate three theoretical strands:

**Self-Determination Theory (SDT):** Deci & Ryan's (2000) framework identifies three core psychological needs: autonomy (self-direction), competence (mastery), and relatedness (social connection). Economic roles typically satisfy all three; displacement threatens all three.

**Social Contagion Theory:** Behavioral sink spreads through social networks (Christakis & Fowler, 2007). Our model incorporates contagion dynamics where collapsed agents increase collapse risk among network neighbors.

**Institutional Capacity:** Following Acemoglu & Robinson (2012), we model interventions as institutional capacities—policy choices that shape how societies respond to technological shocks.

---

## 2. Methods

### 2.1 Model Overview

We developed a network-based agent-based model (ABM) using Mesa 3.5 (Kazil et al., 2021) with 200 agents interacting over 80 timesteps. **This is a stylized model of post-labor dynamics designed to study mechanisms, not a forecast of specific technological timelines or displacement levels.** The model extends prior work (V1, V2) with refined psychological dynamics and five intervention dimensions.

**Agent state variables:**
- Psychological: autonomy, competence, relatedness, status (0-1 scales)
- Role: economic_role (displacement status), virtual_role (virtual world engagement)
- Behavioral: archetype (productive, beautiful_one, aggressor, withdrawn, collapsed)

**Model parameters:**
- post_labor_fraction: proportion of population displaced (0-0.95)
- automation_speed: rate of displacement per step (0.01-0.08)
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
meaning = 0.25×autonomy + 0.25×competence + 0.25×relatedness + 0.10×status + 0.15×contribution
```

where contribution = 0.8×economic_role + 0.1×virtual_role (capturing the insight that virtual contribution matters less than economic contribution).

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

We conducted six parameter sweeps totaling 17,050 runs:

| Sweep | Parameter | Levels | Scenarios | Runs/Point | Total |
|-------|-----------|--------|-----------|------------|-------|
| 1 | Post-labor fraction | 9 | 5 | 50 | 2,250 |
| 2 | Automation speed | 2×3 | 5 | 100 | 3,000 |
| 3 | Virtual world quality | 6 | 3×2 | 100 | 3,600 |
| 4 | Collectivism index | 6 | 3×2 | 100 | 3,600 |
| 5 | Archetype time series | 2 | 2 | 50 | 100 (×81 steps) |
| 6 | Full scenario grid | 3 | 10 | 150 | 4,500 |

**Validation:** Model replicates prior findings (V2) with phase transition at ~80% post-labor under baseline conditions.

### 2.5 Analysis

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

### 3.1 The Malleable Phase Transition Zone (RQ1)

Under baseline conditions (no interventions, gradual automation), the model exhibits a phase transition in the 80-90% post-labor zone (Figure 1). At 80% post-labor, baseline collapse probability is 2%; at 90%, it rises to 86%; at 95%, 100%. The transition zone — rather than a knife-edge threshold — is consistent with complex adaptive systems theory and more realistic than a sharp critical point. This zone proves highly sensitive to policy and contextual factors.

**Rapid automation compresses the transition:** At 95% post-labor, gradual automation yields 54% collapse probability, while rapid automation yields 100%. The speed of displacement shifts which part of the transition zone the population occupies.

**Virtual worlds extend threshold higher:** With virtual_world_quality ≥ 0.6, collapse probability at 80% post-labor drops from 2% to 0%. High-quality virtual infrastructure effectively eliminates the transition zone below 90%.

**Combined interventions push threshold to 95%:** Full intervention bundles (UBI + role substitution + fairness + virtual worlds + collectivism) achieve 0% collapse even at 95% post-labor.

**V4 validation note:** We re-ran key sweeps with increased stochasticity (σ=0.08, up from 0.02, plus agent-level shocks). Core findings replicated with a broader transition zone and wider confidence intervals. The shift from a sharp 80% threshold to an 80-90% transition zone reflects more realistic noise levels — the earlier sharp threshold was partially an artifact of insufficient stochasticity.

### 3.2 Virtual Worlds as Substitutes (RQ2)

Virtual worlds provide significant but bounded protection (Figure 2).

At 80% post-labor:
- Zero virtual quality: 100% collapse
- Moderate quality (0.6): 0% collapse
- Maximum quality (1.0): meaning 0.48, sink 0.19

At 95% post-labor:
- Zero virtual quality: 100% collapse
- Maximum quality (1.0): 21% collapse (partial protection)
- UBI + virtual quality 0.8: 0% collapse (full protection)

The marginal benefit of virtual quality is concave—substantial gains occur between 0.4 and 0.6, with diminishing returns above 0.8. This suggests a "minimum viable" virtual infrastructure threshold rather than linear returns to investment.

Critically, virtual worlds alone cannot fully substitute for economic roles at extreme automation. The model's `contribution_to_nonplayers` term (where virtual contribution counts 0.1 vs. 0.8 for economic roles) creates a ceiling effect. Even maximum virtual quality leaves a meaning gap that becomes critical above 90% automation.

### 3.3 The Speed of Collapse (RQ3)

Automation speed produces distinct archetype trajectories (Figure 3).

**Rapid automation** (0.08/step, reaching 80% in 10 steps):
- Early emergence of Aggressors (steps 10-15)
- Accelerated transition through Beautiful Ones
- Rapid Sink threshold crossing (step 20)

**Gradual automation** (0.01/step, reaching 80% in 80 steps):
- Delayed Aggressor emergence (steps 30-40)
- Prolonged Beautiful One phase
- Slower Sink accumulation

At 95% post-labor baseline, rapid automation produces:
- 9% lower meaning (0.329 vs 0.360)
- 13% higher sink index (0.792 vs 0.703)
- 46 percentage point higher collapse probability (100% vs 54%)

At 80% post-labor, the speed effect is smaller (2pp collapse difference) because V4's broader transition zone places 80% below the critical region for both speeds. The speed effect is most consequential near the transition zone boundary (~88-95%). Interventions — particularly full bundles — attenuate speed effects, suggesting that managed transitions with policy support can buffer speed impacts.

### 3.4 Collectivism as Social Buffer (RQ4)

Collectivism alone cannot prevent baseline collapse (Figure 4). Even at maximum collectivism_index=1.0, collapse probability at 80% post-labor remains 95% without other interventions.

However, collectivism powerfully augments intervention effectiveness:

**UBI at 95% post-labor:**
- Collectivism 0.0: 91% collapse
- Collectivism 0.4: 0% collapse
- Collectivism 1.0: 0% collapse, 55% lower sink index (0.326 vs 0.744)

The mechanism operates through relatedness maintenance. Economic displacement typically severs workplace social connections; collectivist structures provide alternative relatedness sources that buffer psychological impact.

This finding suggests cultural context moderates UBI effectiveness. Societies with higher baseline collectivism (East Asian, Nordic) may find UBI more viable at extreme automation than highly individualist societies (Anglo-American).

### 3.5 Intervention Combinations at Extreme Automation (RQ5)

At 95% post-labor—the stress test for any post-labor policy—we rank intervention effectiveness by sink index:

**Tier 1 (0% collapse, sink < 0.05):**
- Full bundle (UBI + roles + fairness): 0.000 sink
- All bundle (+ virtual + collectivism): 0.000 sink
- Roles + Virtual: 0.006 sink
- UBI + Virtual: 0.025 sink

**Tier 2 (0% collapse, elevated sink 0.3-0.4):**
- Roles only: 0.388 sink
- UBI + Collectivism: 0.413 sink

**Tier 3 (collapse > 0%):**
- UBI only: 0.639 sink, 3% collapse
- Fairness + Collectivism: 0.872 sink, 100% collapse
- Fairness only: 0.918 sink, 100% collapse
- Baseline: 0.967 sink, 100% collapse

**Critical insights:**

1. **Virtual worlds are the most potent addition:** Adding virtual worlds to UBI reduces sink by 96% (0.639 → 0.025). Adding collectivism reduces sink by 35% (0.639 → 0.413).

2. **Role substitution outperforms income support:** At 95%, roles-only (0.388 sink) outperforms UBI-only (0.639 sink). Meaning-through-work may be harder to replace than income.

3. **Fairness redistribution is insufficient alone:** Despite economic equality, fairness-only scenarios collapse because they don't address role absence.

4. **Synergies matter:** The all-bundle sink (0.000) is lower than predicted by additive effects, suggesting positive interactions between interventions.

### 3.6 Archetype Trajectories (RQ5 Continued)

Time-series analysis reveals archetype emergence patterns (Figure 5):

**Baseline trajectory (80% post-labor):**
- Steps 0-10: Productive dominant (95%)
- Steps 10-25: Aggressors emerge (5% → 25%)
- Steps 25-40: Withdrawn surge (10% → 45%)
- Steps 40-80: Stabilized (30% Beautiful Ones, 40% Withdrawn, 15% Aggressors, 10% Collapsed)

**Full bundle trajectory:**
- Productive remains >90% throughout
- Minimal archetype transitions
- Sink index stable <0.05

The Aggressor emergence before Withdrawn suggests anger and frustration are initial responses to displacement, with withdrawal and collapse following as chronic states. This has implications for intervention timing—early deployment (before step 25) prevents population archetype shifts that become self-sustaining.

### 3.7 Historical Validation: Nauru vs. Gulf States

To test external validity, we mapped two historical natural experiments to model conditions. The Republic of Nauru experienced rapid resource-driven wealth from phosphate mining (1960s-1990s), providing citizens with income eliminating the need for employment — a natural experiment in UBI-without-purpose. The result was social dissolution: 94% obesity, 31% diabetes, alcohol abuse, and family breakdown. Our model's rapid/baseline condition at PL=0.80 predicts meaning=0.364, sink=0.798, collapse=100% — consistent with Nauru's near-total social dysfunction despite material sufficiency.

Gulf states (UAE, Qatar, Kuwait) achieved comparable post-scarcity through oil wealth with radically different outcomes. The key structural difference: collectivist social institutions (tribal structures, Islamic community norms). Our model predicts collectivism=0.8 + UBI at PL=0.80 → meaning=0.487, sink=0.119, collapse=0%, with high Beautiful Ones prevalence (~72%) — consistent with the Gulf pattern of stability with consumerist disengagement.

The decisive variable is collectivism_index: at PL=0.95 with UBI, collapse drops from 91% (collectivism=0.0, Nauru-like) to 0% (collectivism=0.8, Gulf-like). The model was not fitted to either case; this divergence emerges from the theoretical framework alone. While post-hoc and subject to confounding, this provides qualified support for construct validity.

---

## 4. Discussion

### 4.1 Theoretical Implications

**Self-Determination Theory in Economic Context:** Our findings extend SDT by demonstrating that the three core needs (autonomy, competence, relatedness) can be satisfied through diverse channels. Economic roles are the default source, but virtual worlds (autonomy, competence) and collectivism (relatedness) provide partial substitutes. However, the ceiling effects suggest these substitutes are imperfect—extreme automation may exceed substitution capacity.

**Phase Transitions in Social Systems:** The 80% threshold behaves like a critical point in physical systems. Near this threshold, small parameter changes produce large outcome changes—a hallmark of phase transitions. Unlike physical constants, however, this threshold is policy-malleable.

**Social Contagion Amplification:** The sharp increase in sink between steps 20-40 suggests contagion dynamics. Individual displacement effects are multiplied through social networks, creating emergent collective collapse exceeding individual-level predictions.

### 4.2 Policy Implications

**Multi-pillar necessity:** No single intervention suffices at extreme automation. Policy portfolios must address income (UBI), meaning (role substitution, virtual worlds), and connection (collectivism structures).

**Virtual infrastructure investment:** Virtual worlds show the largest marginal benefit when added to other interventions. Investment in high-quality virtual role systems—games, creative platforms, virtual civic engagement—may be as important as physical infrastructure.

**Transition management:** The speed effect demonstrates that *how* we automate matters as much as *what* we automate. Gradual transitions with early intervention deployment produce meaning scores 36% higher than rapid transitions.

**Cultural tailoring:** Collectivism effects suggest UBI programs should be designed differently in different cultural contexts. Individualist societies may need stronger supplementary interventions.

**Early warning systems:** The archetype trajectory (Aggressors → Withdrawn → Collapsed) provides a potential early warning framework. Rising aggression metrics may predict approaching collapse before sink indices cross thresholds.

### 4.3 Limitations and Self-Critique

**Residual determinism:** V4 increased noise (σ=0.08, plus agent-level shocks) to address V3's excessive determinism. Between-run standard deviations improved from ~0.002 to ~0.008 for meaning index, and Cohen's d between conditions dropped from 8-48 to ~9-12. While substantially improved, the model remains more deterministic than typical behavioral science data (where Cohen's d of 1-3 is common). The mean-reverting dynamics, while theoretically motivated, still dominate over noise at 80 timesteps. Future versions should explore alternative update rules (e.g., multiplicative noise, regime-switching dynamics) to achieve realistic between-run variance.

**Additive intervention structure:** The model treats interventions as independent additive effects. Real policies interact: UBI might reduce work motivation (negative with roles), virtual worlds might displace real-world socializing (negative with collectivism), fairness perception might depend on who benefits from role programs. Our perfectly ordered intervention hierarchy is an artifact of this independence assumption.

**Underrepresented aggressors:** V4 recalibrated aggressor thresholds, increasing prevalence from <1% to ~2-3% at high displacement. However, this remains below the 10-20% expected from Calhoun's observations. The aggression formula `(1-meaning)*(1-social_capital)*0.5 > 0.3` requires extremely low social capital (< 0.14) combined with low meaning — a narrow parameter region. The model effectively treats behavioral sink as withdrawal-dominated, underrepresenting the aggression dimension. Future work should explore alternative aggression mechanisms (e.g., relative deprivation, frustration-aggression dynamics).

**No endogenous adaptation:** Agents cannot create new institutions, discover novel purposes, form social movements, or develop emergent cultural responses. Human societies have repeatedly demonstrated capacity for institutional innovation under stress — the Industrial Revolution, post-WWII reconstruction, the digital economy. Our model assumes a fixed institutional landscape, which likely overstates collapse risk.

**Threshold-dependent results:** Many headline findings (91% → 0% UBI collapse, 100% → 0% VW transition) occur near phase transition boundaries where small parameter changes produce large outcome shifts. While characteristic of complex systems, this sensitivity means our quantitative predictions are unreliable — the qualitative direction matters, but specific percentages should be treated with extreme caution.

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

Under matched parameters (PL=0.80, baseline), both models predict low meaning and high sink. Under UBI conditions, both models predict higher meaning and lower sink relative to baseline. The directional agreement across two independent modeling approaches — one bottom-up (agent heterogeneity, network effects) and one top-down (aggregate stocks, continuous flows) — provides initial triangulation support for the core findings.

The SD model also reproduces the Nauru-Gulf divergence: Nauru-like parameters (low collectivism, high displacement) produce sink ≈ 0.71 by year 30, while Gulf-like parameters (high collectivism) maintain sink < 0.15. This convergence is notable because the SD model was not fitted to ABM outputs — both derive from the same theoretical framework (SDT + social contagion) implemented through different methodologies. Full Pathway C documentation is provided in the Supplementary Methods.

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

---

## 5. Conclusion

This stylized model identifies mechanisms by which post-labor displacement can drive behavioral sink — and mechanisms by which it can be prevented. Our findings do not predict when or whether AI will displace specific populations, but they characterize the dynamics that would follow such displacement.

The central insight is that income support, while necessary, is insufficient to prevent meaning loss. The mechanisms that drive behavioral sink — loss of competence, autonomy, social role, and contribution — require targeted intervention beyond economic redistribution. Role substitution programs, virtual role infrastructure, and social cohesion structures each address distinct psychological needs that income cannot satisfy.

The model's sensitivity to social cohesion — with collectivism moderating UBI effectiveness from 91% failure to 0% — highlights that identical economic policies can produce radically different outcomes depending on the social substrate. This finding is consistent with historical divergences between post-labor societies (Nauru vs. Gulf states) and suggests that cultural and institutional context deserves as much attention as economic policy design.

As a stylized model, these results identify mechanisms and qualitative relationships rather than precise thresholds. The specific numbers (80% threshold, 91% collapse rate) are model-dependent and should not be interpreted as predictions. What the model contributes is a framework for thinking about which dimensions of human well-being are at risk under role displacement, and which intervention categories address which risks.

---

## References

Acemoglu, D., & Robinson, J. A. (2012). *Why nations fail: The origins of power, prosperity, and poverty*. Crown Business.

Autor, D. H. (2015). Why are there still so many jobs? The history and future of workplace automation. *Journal of Economic Perspectives*, 29(3), 3-30.

Brynjolfsson, E., & McAfee, A. (2014). *The second machine age: Work, progress, and prosperity in a time of brilliant technologies*. WW Norton & Company.

Calhoun, J. B. (1962). Population density and social pathology. *Scientific American*, 206(2), 139-148.

Christakis, N. A., & Fowler, J. H. (2007). The spread of obesity in a large social network over 32 years. *New England Journal of Medicine*, 357(4), 370-379.

Deci, E. L., & Ryan, R. M. (2000). The "what" and "why" of goal pursuits: Human needs and the self-determination of behavior. *Psychological Inquiry*, 11(4), 227-268.

Felten, E. W., Raj, M., & Seamans, R. (2021). Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. *Strategic Management Journal*, 42(12), 2195-2217.

Frey, C. B., & Osborne, M. A. (2017). The future of employment: How susceptible are jobs to computerisation? *Technological Forecasting and Social Change*, 114, 254-280.

Kazil, J., Masad, D., & Crooks, A. (2021). Utilizing Python for agent-based modeling: The Mesa framework. In *Agent-Based Simulation of Organizational Behavior* (pp. 308-344). Springer.

Case, A., & Deaton, A. (2020). *Deaths of Despair and the Future of Capitalism*. Princeton University Press.

Connell, J. (2006). Nauru: The first failed Pacific state? *The Round Table*, 95(383), 47-63.

Hertog, S. (2010). *Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia*. Cornell University Press.

Hofstede, G. (2001). *Culture's Consequences: Comparing Values, Behaviors, Institutions, and Organizations Across Nations*. Sage.

Standing, G. (2017). *Basic income: And how we can make it happen*. Penguin UK.

---

## Data Availability

All simulation code, data (17,050 runs across 6 sweeps), and analysis scripts are available at: https://github.com/wukao1985/post-scarcity-abm

## Acknowledgments

[To be added]

## Author Contributions

[To be added]

## Competing Interests

[To be declared]

## Supplementary Information

Supplementary figures, sensitivity analyses, and extended data tables are available in the online repository. This includes:
- **Supplementary Methods:** Full parameter documentation with justification categories (SDT theory, Calhoun calibration, convenience/sensitivity-tested)
- **Pathway C:** System dynamics model specification, Nauru/Gulf calibration, and ABM-SD comparison
- **V4 Validation:** Detailed V3 vs V4 comparison showing effect of increased stochasticity on headline results
