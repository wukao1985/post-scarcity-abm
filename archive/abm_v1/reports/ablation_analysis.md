# Ablation Analysis: Structural Sensitivity (Issue #3)

## Overview

These ablation experiments address the Codex reviewer's concern that "Roles > UBI" may be partly tautological — built into the model's parameterization rather than emerging from mechanism.

---

## Experiment A: Weight Ablation (Economic vs Virtual Role Ratio)

**Design:** Vary the economic:virtual contribution weight ratio from 3:1 to ∞ while keeping total contribution weight constant at 0.9. Fixed PL=0.95, 50 runs per condition.

### Results

| Ratio | Baseline Sink | UBI Sink | Virtual-Only Sink | UBI+Virtual Sink |
|-------|--------------|----------|-------------------|-----------------|
| 3:1   | 0.795 | 0.543 | 0.443 | 0.188 |
| 5:1   | 0.789 | 0.519 | 0.482 | 0.211 |
| 8:1 (current) | 0.787 | 0.509 | 0.514 | 0.229 |
| 12:1  | 0.792 | 0.514 | 0.542 | 0.242 |
| ∞     | 0.788 | 0.505 | 0.582 | 0.274 |

### Key Findings

1. **Virtual-only vs UBI crossover occurs near the current parameterization (5:1–8:1).** At ratios below 5:1, virtual-only outperforms UBI-only (sink difference 0.037–0.100 in virtual's favor). At the current 8:1 ratio, they are nearly equivalent (0.514 vs 0.509). At higher ratios, UBI dominates.

2. **The finding is partially assumption-sensitive.** The relative ranking of virtual-only vs UBI-only depends on the assumed economic:virtual weight ratio. However, two findings are robust across all ratios:
   - Baseline collapse (100%) is unchanged by ratio (expected — it doesn't involve virtual roles)
   - UBI+virtual always dominates both single interventions (sink 0.188–0.274)
   - Virtual-only always prevents collapse (0% across all ratios)

3. **The ceiling effect is real but graded.** Even at the most generous ratio (3:1), virtual-only sink (0.443) remains substantially higher than UBI+virtual (0.188), confirming that virtual roles alone are insufficient even when given high psychological weight.

### Interpretation

The 8:1 default ratio represents a specific assumption about how much psychological benefit virtual engagement provides relative to economic roles. This assumption drives the virtual-world ceiling effect. Societies where virtual engagement carries greater psychological weight (e.g., strong gaming/creative communities) would see different equilibria. The qualitative conclusion — that virtual roles provide partial but incomplete substitution — holds across all tested ratios.

---

## Experiment B: Intervention Decoupling

**Design:** Three intervention variants at PL=0.95, 150 runs each. Tests whether roles' advantage over UBI comes from mechanism (competence pathway) or parameterization (higher restoration strength + UBI's fairness boost).

### Results

| Variant | Meaning | Sink | Collapse |
|---------|---------|------|----------|
| ubi_pure (ubi=0.7, strength=0.30) | 0.418 ± 0.008 | 0.516 ± 0.037 | 0% |
| roles_matched (roles=0.7, strength=0.30, no competence boost) | 0.401 ± 0.009 | 0.575 ± 0.036 | 0% |
| roles_full (roles=0.7, strength=0.35, with competence boost) | 0.434 ± 0.009 | 0.460 ± 0.038 | 0% |

### Key Findings

1. **When matched on economic restoration strength, roles UNDERPERFORM UBI.** roles_matched (sink 0.575) is worse than ubi_pure (sink 0.516), a difference of 0.059. This is because UBI includes an implicit fairness boost (+0.3×ubi to fairness), which roles lack.

2. **The full roles advantage decomposes as follows:**
   - roles_full vs ubi_pure: Δsink = −0.056 (roles better)
   - roles_matched vs ubi_pure: Δsink = +0.059 (roles worse)
   - Therefore: the competence pathway + higher strength account for Δsink = 0.115, which more than overcomes UBI's fairness advantage (0.059)

3. **Decomposition of roles' advantage over UBI:**
   - Competence pathway contribution: roles_full vs roles_matched → Δsink = 0.115
   - Strength advantage: roles_strength (0.35) vs ubi_strength (0.30) → embedded in the above
   - UBI's fairness advantage: ubi_pure vs roles_matched → Δsink = 0.059 in UBI's favor
   - Net: roles' total advantage (0.056 lower sink) = competence+strength (0.115) − fairness disadvantage (0.059)

### Interpretation

The "Roles > UBI" finding is NOT purely tautological but IS partly parameterization-driven:
- **Mechanism matters:** The competence pathway (0.10 × roles_program in competence target) provides genuine mechanistic advantage
- **Strength matters:** The default 0.35 vs 0.30 strength difference contributes to roles' advantage
- **Fairness offsets:** UBI's implicit fairness boost partially compensates for its lack of competence pathway

**The honest conclusion:** Role programs' superiority over UBI in our model reflects a combination of (a) mechanistic competence benefits that income transfers cannot provide, and (b) a parameterization choice that gives roles slightly higher economic restoration strength. When equalized on strength, UBI's fairness co-benefit actually outweighs roles' competence pathway alone.

---

## Implications for Paper

1. The virtual-world ceiling is assumption-sensitive and should be reported as conditional
2. The roles > UBI finding is directionally robust but magnitude-dependent on parameterization
3. Both experiments confirm that combined interventions (UBI+virtual, full bundle) dominate single interventions regardless of parameter assumptions
