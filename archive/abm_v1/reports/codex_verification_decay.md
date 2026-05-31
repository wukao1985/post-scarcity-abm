# Decay Fix Verification

> **Naming fix applied: `trigger_rate` renamed to `band_occupancy` in model.py**
> - `band_occupancy` now measures fraction of agents currently IN [0.35, 0.65]
> - Removed duplicate `fraction_in_band_mean` column from sensitivity_decay.py output
> - `trigger_rate` in calibrate_meaning_support.py remains unchanged (measures band ENTRY transitions)

Date: 2026-03-17

## Summary

- Overall verdict: PASS with 1 non-blocking semantic issue in reporting.
- The decay parameterization is implemented correctly in the model.
- The sensitivity script passes `decay`, runs successfully, and produces a clear monotonic response.
- Remaining issue: `trigger_rate_mean` and `fraction_in_band_mean` are identical in `scripts/sensitivity_decay.py`, and the term `trigger_rate` now conflicts with the older transition-based definition used in `scripts/calibrate_meaning_support.py`.

## Check 1: `models/pathway_a_abm/model.py`

- PASS: `PostLaborModel.__init__` includes `decay=0.08` and stores `self.decay` (`model.py:195-221`).
- PASS: `PostLaborAgent.step()` uses `self.model.decay`, not a hardcoded `0.08` (`model.py:89-90`).
- PASS: `trigger_rate` is present in the datacollector as `sum(1 for a in m.agents if 0.35 <= a.meaning <= 0.65) / m.n_agents` (`model.py:246-262`).
- PASS with caveat: I found no other stray hardcoded copies of the decay value. The file still contains many structural constants (`base = 0.32`, `noise_sigma = 0.08`, archetype thresholds, network topology constants), but those appear to be model coefficients rather than missed instances of the decay fix.

## Check 2: `scripts/sensitivity_decay.py`

- PASS: The script passes `decay` directly into `PostLaborModel(...)` (`sensitivity_decay.py:20-25`).
- PASS: The computed metric matches the current datacollector definition. It averages `late_run["trigger_rate"]`, which is the per-step fraction of agents with meaning in `[0.35, 0.65]` (`sensitivity_decay.py:30-46`).
- PASS: The sweep design matches the requested scenario: decay values `[0.05, 0.10, 0.15, 0.20, 0.25, 0.30]`, `n_runs = 50`, `post_labor_fraction = 0.95`, `intervention = {"ubi": 0.7}` (`sensitivity_decay.py:87-105`).
- FAIL (semantic/reporting only, not runtime): `fraction_in_band_mean` is not an independent metric here. It is set equal to `late_run["trigger_rate"].mean()`, so the two reported columns are duplicates (`sensitivity_decay.py:38-46`). This is consistent with the new datacollector, but it is redundant and can confuse downstream interpretation.

## Check 3: Sensitivity Run

Execution note:

- The requested `python` command could not run in this shell because `python` is not installed as an alias.
- I ran the equivalent command with `python3` instead.

Command run:

```bash
python3 scripts/sensitivity_decay.py
```

Result:

- PASS: The script completed without error.
- Non-blocking warning: Mesa emitted a deprecation warning for `seed=...` and recommends `rng=...` in the future.

Observed results from `data/simulation/sensitivity_decay.csv`:

| decay | mean_meaning | mean_meaning_std | trigger_rate | trigger_rate_std |
| --- | ---: | ---: | ---: | ---: |
| 0.05 | 0.430955 | 0.007093 | 0.678840 | 0.023902 |
| 0.10 | 0.415446 | 0.006479 | 0.707130 | 0.022023 |
| 0.15 | 0.410936 | 0.005454 | 0.729215 | 0.018794 |
| 0.20 | 0.408713 | 0.004347 | 0.743365 | 0.016460 |
| 0.25 | 0.407439 | 0.003933 | 0.752955 | 0.016573 |
| 0.30 | 0.406034 | 0.002600 | 0.758440 | 0.012594 |

Assessment:

- PASS: Different decay values produce meaningfully different results.
- `trigger_rate` increases monotonically from `0.678840` at decay `0.05` to `0.758440` at decay `0.30` (`delta = 0.079600`).
- `mean_meaning` decreases monotonically from `0.430955` to `0.406034` (`delta = 0.024920`).
- The effect compresses at the top end, but the full-range separation is clearly larger than the per-point standard error.

## Check 4: Targeted `trigger_rate` Sanity Command

Command run:

```bash
python3 -c "from models.pathway_a_abm.model import PostLaborModel; m = PostLaborModel(decay=0.05); [m.step() for _ in range(10)]; df = m.datacollector.get_model_vars_dataframe(); print(df['trigger_rate'].describe())"
```

Output:

```text
count    11.000000
mean      0.757727
std       0.081742
min       0.695000
25%       0.717500
50%       0.735000
75%       0.757500
max       0.990000
Name: trigger_rate, dtype: float64
```

- PASS: `trigger_rate` is collected and queryable through the datacollector after stepping the model.

## Remaining Issues

- `scripts/sensitivity_decay.py` reports `trigger_rate_mean` and `fraction_in_band_mean` as separate outputs even though they are identical in the current implementation.
- The term `trigger_rate` now means "fraction of agents currently in band" in `model.py`, but `scripts/calibrate_meaning_support.py` still uses `trigger_rate` to mean "entry rate into the band." That cross-script naming mismatch is a documentation and analysis risk.
- Mesa warns that `seed=` is deprecated in favor of `rng=`. This does not block the current run.

## Readiness For Full Scale

- YES, for running the decay sweep itself at `150` runs per point.
- Recommendation before doing that production run: rename or drop the duplicate `fraction_in_band_mean` column, and document that `trigger_rate` in this sweep means band occupancy rather than band-entry transitions.
