# Horizon Robustness Analysis

## Purpose

The paper claims results represent "equilibrium states" but only measures at T=80. This analysis tests whether outcomes are near-stationary by T=80 by extending simulations to T=240.

## 1. Convergence Results

| Scenario | PL | Sink@80 | Sink@120 | Sink@160 | Sink@240 | Δ(80→120) | Converged? |
|----------|------|---------|----------|----------|----------|-----------|------------|
| baseline | 0.50 | 0.292 | 0.295 | 0.297 | 0.298 | 0.0036 | YES |
| baseline | 0.80 | 0.629 | 0.635 | 0.620 | 0.625 | 0.0053 | YES |
| baseline | 0.95 | 0.788 | 0.794 | 0.788 | 0.789 | 0.0066 | YES |
| ubi_only | 0.50 | 0.157 | 0.165 | 0.161 | 0.162 | 0.0075 | YES |
| ubi_only | 0.80 | 0.383 | 0.380 | 0.379 | 0.378 | 0.0025 | YES |
| ubi_only | 0.95 | 0.515 | 0.524 | 0.514 | 0.517 | 0.0092 | YES |
| full_bundle | 0.50 | 0.038 | 0.039 | 0.040 | 0.037 | 0.0010 | YES |
| full_bundle | 0.80 | 0.089 | 0.088 | 0.094 | 0.087 | 0.0009 | YES |
| full_bundle | 0.95 | 0.130 | 0.128 | 0.128 | 0.127 | 0.0020 | YES |

**Convergence criterion:** |sink(T=120) - sink(T=80)| < 0.02

**Verdict: ALL 9 conditions converged by T=80.** Maximum delta across all conditions is 0.0092 (ubi_only at PL=0.95). The T=80 values oscillate within ±0.01 out to T=240, confirming these are genuine near-equilibrium states, not transient snapshots.

The fastest convergence occurs in full_bundle conditions (Δ < 0.002), consistent with the strong institutional support creating a stable attractor. The slowest convergence is in ubi_only at high displacement (Δ = 0.009), where the intermediate sink level allows more fluctuation around the equilibrium.

## 2. Speed Comparison (Exposure-Time Controlled)

The original speed comparison (Sweep 2) compared rapid and gradual at the same calendar step (T=80), confounding speed with exposure time. This analysis controls for exposure by measuring outcomes at matched intervals after each scenario reaches its target displacement.

### Design

- **Rapid:** speed=0.20, reaches PL=0.95 at step ~5. Measured at steps 15, 25, 45.
- **Gradual:** speed=0.95/160 ≈ 0.006, reaches PL=0.95 at step ~160. Measured at steps 170, 180, 200.

### Results (10 steps after target reached)

| Speed | Scenario | Sink (t+10) | Sink (t+20) | Sink (t+40) |
|-------|----------|-------------|-------------|-------------|
| rapid | baseline | 0.645 | 0.735 | 0.789 |
| gradual | baseline | 0.775 | 0.781 | 0.797 |
| rapid | ubi_only | 0.388 | 0.468 | 0.513 |
| gradual | ubi_only | 0.494 | 0.510 | 0.526 |
| rapid | full_bundle | 0.116 | 0.125 | 0.132 |
| gradual | full_bundle | 0.122 | 0.125 | 0.127 |

### Interpretation

**When controlling for exposure time, gradual automation produces HIGHER sink than rapid at matched post-target intervals.** At 10 steps after reaching PL=0.95, gradual baseline sink is 0.775 vs rapid 0.645 — a reversal of the naive comparison.

This occurs because gradual automation accumulates contagion damage during the extended ramp period. By the time gradual reaches PL=0.95, the population has been partially displaced for 160 steps, giving social contagion more time to propagate. Rapid displacement, while more disruptive initially, starts from a healthier baseline.

**At t+40 (equilibrium):** Both speeds converge to similar sink levels (rapid 0.789 vs gradual 0.797 for baseline), confirming that the final equilibrium depends primarily on the displacement level, not the path taken. The speed effect is transient.

**For full_bundle:** Speed has negligible effect (0.116 vs 0.122 at t+10), confirming that strong interventions dominate speed effects.

### Implication for the paper

The original speed finding ("rapid produces 46pp more collapse than gradual") reflected a confound: it measured rapid at T=80 (75 steps of exposure at full displacement) against gradual at T=80 (which reaches 0.95 only at the final step, with 0 steps of exposure). The controlled comparison shows speed is transient — equilibrium outcomes depend on the displacement level and interventions, not the transition path.

## 3. Conclusion

1. **"Equilibrium" language is justified.** All conditions stabilize by T=80 (max Δ < 0.01).
2. **Speed effect is transient, not structural.** At matched exposure times, both speeds converge to the same equilibrium. The original speed finding was a measurement artifact.
3. **Displacement level and interventions are the primary determinants** of equilibrium state, consistent with the paper's core contribution.
