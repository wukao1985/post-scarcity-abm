# V4 Validation Report

## V4 Model Changes

Three modifications from V3:
1. **Increased stochasticity:** noise σ raised from 0.02 to 0.08 (4×), plus per-step agent-level shocks (σ=0.03)
2. **Gradual speed fix:** runner now computes `speed = target/80` so gradual automation always reaches its target endpoint by step 80
3. **Aggressor recalibration:** threshold adjusted (`aggression_drive > 0.3` with `aggression_drive = (1-meaning)*(1-social_capital)*0.5`, meaning threshold relaxed to < 0.40)

## Sweep 1: V3 vs V4 Comparison

### Key Metrics at Benchmark Points

| Scenario | PL | V3 Meaning | V4 Meaning | V3 Sink | V4 Sink | V3 Collapse | V4 Collapse | V3 Aggressor | V4 Aggressor |
|----------|------|-----------|-----------|---------|---------|-------------|-------------|-------------|-------------|
| baseline | 0.50 | 0.496 | 0.495 | 0.217 | 0.292 | 0% | 0% | 0.000 | 0.002 |
| baseline | 0.80 | 0.365 | 0.382 | 0.797 | 0.629 | 100% | 2% | 0.001 | 0.017 |
| baseline | 0.95 | 0.307 | 0.330 | 0.967 | 0.788 | 100% | 100% | 0.009 | 0.034 |
| ubi_only | 0.50 | 0.555 | 0.546 | 0.011 | 0.157 | 0% | 0% | 0.000 | 0.001 |
| ubi_only | 0.80 | 0.468 | 0.459 | 0.222 | 0.383 | 0% | 0% | 0.000 | 0.004 |
| ubi_only | 0.95 | 0.406 | 0.417 | 0.646 | 0.515 | 2% | 0% | 0.000 | 0.008 |
| full_bundle | 0.50 | 0.641 | 0.631 | 0.000 | 0.038 | 0% | 0% | 0.000 | 0.000 |
| full_bundle | 0.80 | 0.588 | 0.576 | 0.000 | 0.089 | 0% | 0% | 0.000 | 0.000 |
| full_bundle | 0.95 | 0.561 | 0.549 | 0.000 | 0.130 | 0% | 0% | 0.000 | 0.000 |

### What Changed

**Phase transition shifted from ~80% to ~90%.** The most significant change: V3 showed 100% collapse at PL=0.80 baseline; V4 shows only 2%. The increased noise prevents the deterministic convergence to extreme sink states that V3 exhibited. Collapse now reliably occurs at PL=0.90 (86%) and PL=0.95 (100%).

**Interpretation:** The V3 80% threshold was partially an artifact of insufficient stochasticity. With realistic noise, the transition zone broadens to ~80-90%, with the critical point around PL=0.88. This is arguably more realistic — real social transitions don't show knife-edge thresholds.

**Aggressors improved but below target.** V4 produces ~1.7% aggressors at PL=0.80 (up from 0.1% in V3), and ~3.4% at PL=0.95. This is a 10-17× improvement but still below the 10-20% target. The threshold formula `(1-meaning)*(1-social_capital)*0.5 > 0.3` requires very low social capital (< 0.14) combined with meaning < 0.30 — a narrow parameter region. Only the most vulnerable agents with bad luck in social capital assignment cross this threshold.

**Variance improved but still high.** Between-run SD for meaning index increased from ~0.002 to ~0.008 (4× improvement). Cohen's d between baseline and UBI at PL=0.80 dropped from ~48 to ~9.4. The target of 1-5 was not met. The mean-reverting dynamics still dominate over noise at 80 timesteps.

**Sink index no longer binary.** V3's full_bundle produced exactly 0.000 sink at all levels; V4 produces 0.038-0.130. This is more realistic — even well-supported populations have some individuals in suboptimal states.

### Directional Findings Preserved

Despite quantitative changes, all qualitative conclusions from V3 hold:
1. Phase transition exists (shifted slightly higher)
2. UBI prevents collapse but doesn't eliminate elevated sink
3. Full bundle remains most effective
4. Roles > UBI > Fairness ordering preserved
5. Intervention hierarchy unchanged

### What the Paper Must Update

1. Replace "~80% threshold" with "~80-90% transition zone" or "~88% critical point"
2. Specific collapse probabilities need updating (e.g., baseline/0.80: 100% → 2%)
3. Note that broader transition zone is a consequence of increased stochasticity
4. Aggressors remain underrepresented — acknowledge as ongoing limitation
5. Cohen's d improved from 8-48 to ~9-12 — better but model remains more deterministic than real behavioral science

## Sweep 2: Automation Speed (V4)

### V4 Fix: Gradual Speed Now Reaches Target

The V3 gradual speed (0.01/step × 80 steps = 0.80 max) could never reach PL=0.95. V4 computes gradual speed as `target/80`, so gradual/0.95 uses 0.011875/step and reaches 0.95 by step 80.

### Results

| Speed | PL | Scenario | Meaning | Sink | Collapse |
|-------|------|----------|---------|------|----------|
| gradual | 0.50 | baseline | 0.510 | 0.259 | 0% |
| gradual | 0.80 | baseline | 0.408 | 0.552 | 0% |
| gradual | 0.95 | baseline | 0.360 | 0.703 | 54% |
| rapid | 0.50 | baseline | 0.493 | 0.296 | 0% |
| rapid | 0.80 | baseline | 0.385 | 0.623 | 2% |
| rapid | 0.95 | baseline | 0.329 | 0.792 | 100% |
| gradual | 0.95 | ubi_only | 0.443 | 0.428 | 0% |
| rapid | 0.95 | ubi_only | 0.416 | 0.517 | 0% |
| gradual | 0.95 | full_bundle | 0.564 | 0.103 | 0% |
| rapid | 0.95 | full_bundle | 0.548 | 0.131 | 0% |

### Speed Effect Analysis

At PL=0.95 baseline:
- **Gradual:** meaning=0.360, sink=0.703, collapse=54%
- **Rapid:** meaning=0.329, sink=0.792, collapse=100%
- **Speed gap:** 46 percentage points in collapse probability

At PL=0.80 baseline:
- **Gradual:** meaning=0.408, sink=0.552, collapse=0%
- **Rapid:** meaning=0.385, sink=0.623, collapse=2%
- **Speed gap:** 2 percentage points (less dramatic than V3's 73pp gap)

**Key finding:** The V4 speed effect is most pronounced at PL=0.95 (46pp collapse difference) rather than PL=0.80 (2pp). This is because V4's shifted phase transition puts 0.80 in the pre-collapse zone for both speeds, while 0.95 straddles the transition for gradual but is solidly in collapse territory for rapid.

**Gradual speed fix impact:** With the fix, gradual/0.95 now actually reaches 0.95 displacement, producing 54% collapse (instead of the V3 artifact where it only reached 0.80 and showed 27% collapse). This is a more honest comparison — gradual automation to 95% is still dangerous, just less catastrophic than rapid.

### Directional Findings

The core finding that "speed matters" is preserved, though the magnitude shifted:
- V3 headline: "73 percentage point more collapse with rapid automation" (at PL=0.80)
- V4 headline: "46 percentage point more collapse with rapid automation" (at PL=0.95)
- Interventions still attenuate speed effects (full_bundle: 0% collapse at both speeds)
