# Full-Scale Decay Sensitivity (150 runs/point)

## Results Table

| decay | band_occupancy_mean +- std | mean_meaning +- std |
| --- | --- | --- |
| 0.05 | 0.6809 +- 0.0222 | 0.4328 +- 0.0082 |
| 0.10 | 0.7075 +- 0.0208 | 0.4154 +- 0.0067 |
| 0.15 | 0.7276 +- 0.0196 | 0.4103 +- 0.0053 |
| 0.20 | 0.7413 +- 0.0175 | 0.4080 +- 0.0042 |
| 0.25 | 0.7523 +- 0.0158 | 0.4071 +- 0.0036 |
| 0.30 | 0.7609 +- 0.0139 | 0.4066 +- 0.0030 |

## Interpretation

The effect of `decay` on `band_occupancy` is statistically meaningful in this sweep. `band_occupancy_mean` increases monotonically across all six tested decay values, from `0.6809` at `0.05` to `0.7609` at `0.30`.

Using the aggregated sweep means, a linear fit of `band_occupancy_mean ~ decay` gives `r = 0.9778` and `p = 7.32e-4`. Using the per-point standard deviations with `n = 150` runs per decay, the endpoint difference (`0.30` minus `0.05`) is about `37.35` pooled standard errors, so the rise is far larger than run-to-run noise.

`mean_meaning` declines as decay rises, but the drop is modest in absolute terms compared with the gain in band occupancy.

## Effect Size

Delta `band_occupancy_mean` from minimum to maximum tested decay:

`0.7609 - 0.6809 = 0.0799`

This is an absolute gain of about `8.0` percentage points in band occupancy over the tested decay range.

## Recommendation

If the objective is to maximize `band_occupancy`, the best tested value is `decay = 0.30`. It delivers the highest occupancy in the sweep (`0.7609`) while only slightly reducing `mean_meaning` relative to lower-decay settings.

If a more conservative setting is preferred because of diminishing returns, `decay = 0.25` is the closest near-plateau alternative, but `0.30` remains the strongest choice on the primary occupancy metric.
