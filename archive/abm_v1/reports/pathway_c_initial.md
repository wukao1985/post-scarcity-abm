# Pathway C: System Dynamics Model -- Initial Report

## 1. Purpose

This report documents the Pathway C system dynamics (SD) model, which provides methodological triangulation for the agent-based model (ABM) developed in Pathway A. Where the ABM captures micro-level heterogeneity -- individual agent archetypes, social contagion on networks, and stochastic variation -- the SD model operates at the macro level, representing population-averaged stocks and flows as a deterministic ODE system. If both independently calibrated models produce the same directional findings regarding post-labor behavioral sink, this strengthens confidence that the results are not artifacts of any single modeling methodology.

## 2. Model Description

The SD model contains three coupled stocks (state variables bounded to [0, 1]):

- **MeaningStock**: Population-level average sense of purpose and role fulfillment. Initialized at 0.7.
- **SinkStock**: Prevalence of behavioral sink (substance abuse, withdrawal, aimlessness). Initialized at 0.05.
- **SocialTrust**: Aggregate social cohesion and institutional trust. Initialized at 0.6.

The dynamics follow three coupled ODEs:

- **dMeaning/dt** = -role_loss_rate * post_labor * (1 - UBI_coeff * ubi) - meaning_decay * Sink + intervention_boost + collectivism_buffer
- **dSink/dt** = sink_accumulation * (1 - Meaning) * (1 + contagion * Sink) - recovery_rate * Meaning
- **dTrust/dt** = -trust_erosion * Sink - isolation_effect * post_labor + collectivism_boost

Key assumptions: (a) post-labor displacement erodes meaning unless offset by UBI-linked purpose programs; (b) behavioral sink grows nonlinearly as meaning declines, with a contagion feedback loop; (c) collectivism provides buffers to both meaning and trust; (d) trust erodes with sink prevalence. The model is solved using scipy's RK45 integrator over 80 time steps.

## 3. Nauru Calibration

Nauru serves as a natural experiment: phosphate wealth from the 1970s eliminated the need for labor, producing an unintended "post-labor" society without structured purpose programs. The SD model was calibrated to approximate the observed trajectory:

| Time Point | Meaning (SD) | Meaning (Target) | Sink (SD) | Sink (Target) | Trust (SD) | Trust (Target) |
|-----------|-------------|------------------|----------|--------------|-----------|---------------|
| t=0 (1970) | 0.700 | 0.70 | 0.050 | 0.05 | 0.600 | 0.60 |
| t=15 (1985) | 0.369 | ~0.40 | 0.157 | ~0.30 | 0.460 | ~0.35 |
| t=30 (2000) | 0.000 | ~0.20 | 0.711 | ~0.70 | 0.210 | ~0.15 |

Parameters: post_labor=0.85, ubi_transfer=0.0 (wealth without purpose programs), collectivism=0.15. The model captures the qualitative arc of collapse: a society that experienced rapid wealth followed by purposelessness, rising behavioral pathology, and social fragmentation. The meaning stock declines slightly faster than the historical target (reaching zero rather than stabilizing near 0.2), which reflects the model's lack of a residual meaning floor from subsistence activities.

## 4. Gulf States Comparison

The Gulf states (UAE, Qatar, Kuwait) experienced a similar resource wealth shock but maintained stronger collectivist cultural institutions. The SD model represents this by setting collectivism=0.8 while keeping other parameters identical to Nauru.

Results at t=30: meaning stabilized at 0.542 (vs. 0.000 for Nauru), sink remained low at 0.121 (vs. 0.711), and trust held at 0.696 (vs. 0.210). This directional finding -- that collectivist social structures buffer against behavioral sink even under post-labor conditions -- is consistent with both the historical record and the ABM's Sweep 4 results showing collectivism as a protective factor.

## 5. ABM-SD Directional Agreement

The critical test is whether the SD model reproduces the ABM's directional findings when run at matched parameters (post_labor=0.8):

| Scenario | ABM Meaning | SD Meaning | ABM Sink | SD Sink | Meaning Direction | Sink Direction |
|----------|------------|-----------|---------|--------|------------------|---------------|
| Baseline | 0.370 | ~0.00 | 0.800 | ~1.00 | (reference) | (reference) |
| UBI only | 0.470 | 0.851 | 0.220 | ~0.00 | MATCH (higher) | MATCH (lower) |
| Full bundle | 0.590 | 0.991 | 0.000 | ~0.00 | MATCH (higher) | MATCH (lower) |

Both models agree on every directional comparison: UBI increases meaning and reduces sink relative to baseline; adding collectivism (full bundle) further improves outcomes. The SD model produces more extreme values (closer to 0 or 1) than the ABM, which is expected given that it lacks the heterogeneity and stochastic buffering present in the agent-based approach.

## 6. Limitations

This SD model has several important limitations:

- **No agent heterogeneity**: The model represents population averages. It cannot capture the differential vulnerability of resilient vs. balanced vs. vulnerable archetypes that the ABM reveals.
- **Rough calibration**: Parameter values were hand-tuned to approximate historical trajectories. No formal optimization or sensitivity analysis has been performed.
- **Deterministic**: Unlike the ABM's Monte Carlo approach with 150+ runs per parameter point, the SD model produces a single deterministic trajectory with no uncertainty quantification.
- **Simplified feedbacks**: The three-stock system omits many plausible feedback loops (e.g., economic productivity effects, political responses, technological adaptation).
- **Static exogenous drivers**: Post-labor fraction is treated as a fixed parameter rather than an endogenous outcome of automation dynamics.

## 7. Next Steps

- Formal parameter optimization using historical time-series data (Nauru health statistics, Gulf state social indicators).
- Sensitivity analysis on all rate constants to identify which parameters most influence outcomes.
- Additional historical case calibrations (e.g., post-industrial Appalachia, Soviet-era guaranteed employment).
- Integration with ABM outputs: use ABM ensemble statistics to constrain SD parameter ranges.
- Time-varying post-labor scenarios to match the ABM's gradual automation sweeps.
