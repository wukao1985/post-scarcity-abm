# Calibration Diagnosis

Date: 2026-03-17

## Bottom Line

The root-cause diagnosis in the request is **not verified by the current code** in `models/pathway_a_abm/model.py`.

What the code actually shows:

1. `decay` is hardcoded to `0.08` inside `PostLaborAgent.step()`. A convergence-rate sweep can only affect behavior if the source code itself was edited.
2. The model has **no** `meaning_direct_support` parameter.
3. The model has **no** explicit trigger band `[0.35, 0.65]`; that band is an external analysis construct, not a built-in mechanism.
4. Displacement is **re-randomized every step** in `PostLaborModel.step()`, so agents do not stay permanently displaced.
5. Under the implemented equations, the representative displaced-agent fixed points are already around **0.44 to 0.45**, not `0.109` and `0.197`.

The practical implication is that the reported invariant `trigger_rate=0.422` is more likely a problem with the **sensitivity design or metric definition** than with meaning equilibria being below the band.

## 1. Verification Against Code

### 1.1 What matters in `model.py`

- `decay = 0.08` is hardcoded in `PostLaborAgent.step()`.
- Psychological states update toward linear targets plus noise.
- Meaning is recomputed as:

```python
meaning = (
    0.25 * autonomy
    + 0.25 * competence
    + 0.25 * relatedness
    + 0.10 * status
    + 0.15 * contribution
    - contagion * 0.08
    + 0.08 * resilience
)
```

- UBI changes `economic_role` through:

```python
economic_role = ubi * ubi_strength + roles_program * roles_strength
```

- At each model step, the displaced set is drawn again with `random.sample(...)`.

That last point matters. The actual model is not "agent is displaced once, then converges to one fixed point." It is "agent is displaced with probability equal to current post-labor share each step."

### 1.2 Why the submitted diagnosis does not match the implementation

The supplied equilibrium values (`UBI ~= 0.109`, `MI ~= 0.197`) are not compatible with the current equations.

Even under a harsh deterministic case with:

- `economic_role = 0.0`
- `fairness = 0.1`
- `aggressor_frac = 1.0`
- `contagion = 0.5` (the model's maximum, since `sink_exposure <= 1` and `contagion_strength = 0.5`)

the representative balanced-agent fixed point is still:

- `meaning = 0.263674`

So the reported `0.109` value cannot come from the current `model.py` without using different equations.

### 1.3 Likely explanation for the repeated `0.422`

Inference from the repo artifacts:

- The value `0.422...` appears repeatedly in existing simulation CSVs as a **meaning-like magnitude**.
- There is no built-in `trigger_rate` variable anywhere in the repository.

That makes the previous output

```text
CR=0.10: trigger_rate=0.422
CR=0.20: trigger_rate=0.422
CR=0.30: trigger_rate=0.422
```

look more like a mislabeled aggregate meaning statistic than a true crossing-rate metric.

## 2. Exact Analytical Equilibria

The fixed points below are exact for the deterministic part of the implemented equations, under the standard simplifying assumptions used for policy interpretation:

- representative balanced agent:
  - `resilience = 0.5`
  - `social_capital = 0.5`
  - `skill_transferability = 0.5`
- `virtual_world_quality = 0.0`
- `virtual_role = 0.0`
- `collectivism_index = 0.3`
- `status_concentration = 1.0`
- `aggressor_frac = 0.0`
- `contagion = 0.0`

### 2.1 UBI-only, permanently displaced

With:

- `ubi = 0.7`
- `ubi_strength = 0.30`
- `economic_role = 0.7 * 0.30 = 0.21`
- `fairness = 0.1 + 0.7 * 0.3 = 0.31`
- `inequality_index = 1 - 0.31 = 0.69`

the exact deterministic fixed point is:

| Component | Value |
| --- | ---: |
| autonomy | 0.430794 |
| competence | 0.432500 |
| relatedness | 0.485800 |
| status | 0.347564 |
| meaning | 0.437230 |

Closed form for UBI-only displaced meaning under the current code:

```text
M_UBI_displaced(s) = 0.3704184 + 0.222705 * s
```

So at `s = 0.30`:

```text
M_UBI_displaced(0.30) = 0.4372299
```

### 2.2 MI-only, permanently displaced

With:

- `roles = 0.7`
- `roles_strength = 0.35`
- `economic_role = 0.7 * 0.35 = 0.245`
- `fairness = 0.1`
- `inequality_index = 0.9`
- `roles_comp = 0.10 * 0.7 = 0.07`

the exact deterministic fixed point is:

| Component | Value |
| --- | ---: |
| autonomy | 0.410480 |
| competence | 0.511250 |
| relatedness | 0.472500 |
| status | 0.338450 |
| meaning | 0.451802 |

Closed form for MI-only displaced meaning under the current code:

```text
M_MI_displaced(r) = 0.373084 + 0.22491 * r
```

So at `r = 0.35`:

```text
M_MI_displaced(0.35) = 0.4518025
```

### 2.3 Mean-field equilibrium under the actual re-randomized displacement process

At `post_labor_fraction = 0.95`, each agent is displaced with probability `0.95` each step.
If we take expectations through the linear target equations, the relevant mean-field economic role is:

```text
E[economic_role] = 0.95 * e_displaced + 0.05 * 1.0
```

This gives:

| Scenario | Expected economic_role | Mean-field meaning |
| --- | ---: | ---: |
| UBI-only (`ubi_strength=0.30`) | 0.249500 | 0.449797 |
| MI-only (`roles_strength=0.35`) | 0.282750 | 0.463932 |

Those values are the better analytical benchmark for the current implementation, because agents are not persistently displaced.

## 3. Interpretation

### 3.1 What `decay` can and cannot change

In this model, `decay` changes:

- the speed with which states approach their current targets
- the size of transient lag after displacement status changes

It does **not** change:

- the deterministic fixed point implied by the target equations
- the fact that displacement assignment is re-randomized every step

So a null sensitivity result is plausible when:

- the metric is measured late in the run, after transient differences have washed out
- the metric is actually a steady-state mean
- the displacement process itself already mixes agents across displaced / non-displaced states each step

### 3.2 Why the current code does not support the "equilibrium below band" story

Under the implemented equations:

- UBI displaced fixed point: `0.437230`
- MI displaced fixed point: `0.451802`

Both are already inside `[0.35, 0.65]`.

So the defensible diagnosis is:

> The current sensitivity problem is primarily an experimental-design issue:
> `decay` is hardcoded, the reported metric is not defined in the codebase, and
> per-step displacement re-randomization weakens any clean one-dimensional
> crossing-time interpretation.

## 4. Recommendation

### 4.1 Best choice among the proposed fixes

For a JASSS paper, the most defensible option is **Option 2**, but with a narrower claim than the one in the request:

- If you want to calibrate policy potency, sweep `ubi_strength` and `roles_strength`.
- Do **not** add a `meaning_floor`.
- Do **not** add a direct additive `meaning_direct_support` term unless you are willing to re-theorize it as an explicit need-level mechanism.

Reason:

- `ubi_strength` and `roles_strength` already exist in the model.
- They map cleanly to policy potency: how much economic-role function the intervention restores.
- A direct meaning floor is ad hoc and hard to defend theoretically.
- A direct meaning addend is also weakly grounded unless decomposed into autonomy / competence / relatedness / status channels.

### 4.2 Immediate methodological fix

The immediate fix is **not** "raise equilibrium into the band," because the current code already does that.

The immediate fix is:

1. Make `decay` an exposed model parameter instead of a hardcoded constant.
2. Use a metric that actually captures crossing dynamics.
3. If the theoretical story requires persistent displacement trajectories, stop re-randomizing the displaced set every step.

Without those changes, a convergence-rate sensitivity test is structurally hard to interpret.

## 5. Targeted Calibration Experiment

### Design

Sweep:

- `ubi_strength in {0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50}`

Hold fixed:

- scenario: UBI-only (`intervention={"ubi": 0.7}`)
- `post_labor_fraction = 0.95`
- `automation_speed = 0.03`
- `virtual_world_quality = 0.0`
- `collectivism_index = 0.3`
- `contagion_strength = 0.5`

Runs:

- `100` Monte Carlo runs per point
- `80` steps per run
- late-run window: steps `61-80`

Metrics:

- `analytic_displaced_meaning`
- `analytic_mixed_meaning`
- `equilibrium_meaning`: late-run mean of model-wide mean meaning
- `trigger_rate`: late-run share of agent-step transitions entering `[0.35, 0.65]`
- `fraction_in_band`: late-run share of agents in `[0.35, 0.65]`

Why this experiment:

- it uses a parameter that actually exists
- it distinguishes occupancy from entry dynamics
- it matches the model's actual re-randomized displacement process

## 6. Script Output

The script at `scripts/calibrate_meaning_support.py` writes:

- `data/simulation/calibration_meaning_support.csv`

Implementation notes:

- I swept `ubi_strength`, not `meaning_direct_support`, because `meaning_direct_support` is not implemented in the current codebase.
- I defined `trigger_rate` explicitly in the script because the repository has no built-in trigger metric.

## 7. Expected Reading of the Sweep

Observed 100-run sweep results:

| ubi_strength | analytic_displaced | analytic_mixed | empirical_meaning | trigger_rate | fraction_in_band |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0.15 | 0.403824 | 0.418061 | 0.382646 | 0.076963 | 0.591412 |
| 0.20 | 0.414959 | 0.428640 | 0.393426 | 0.075925 | 0.623773 |
| 0.25 | 0.426095 | 0.439218 | 0.405989 | 0.073442 | 0.661730 |
| 0.30 | 0.437230 | 0.449797 | 0.419821 | 0.070718 | 0.699165 |
| 0.35 | 0.448365 | 0.460375 | 0.432766 | 0.068625 | 0.732548 |
| 0.40 | 0.459500 | 0.470954 | 0.442913 | 0.065532 | 0.751918 |
| 0.45 | 0.470636 | 0.481532 | 0.454927 | 0.064337 | 0.771388 |
| 0.50 | 0.481771 | 0.492111 | 0.468410 | 0.061715 | 0.790120 |

The sweep reads cleanly:

- higher `ubi_strength` should raise both analytical and empirical meaning
- higher `ubi_strength` should usually raise band occupancy
- higher `ubi_strength` can lower entry-rate `trigger_rate`, because more agents remain in-band instead of repeatedly entering it from outside

That is a feature of the metric definition, not a bug.

## 8. Residual Risks

Two residual issues remain even after this calibration pass:

1. `decay` is still hardcoded in the model, so the original convergence-rate question is not yet testable from configuration alone.
2. Randomly redrawing displaced agents each step may be a substantive modeling choice worth revisiting, because it makes individual adaptation trajectories hard to interpret.
