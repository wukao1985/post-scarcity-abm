# Platform-level trend (Stack Apps API) — context for the SO study

A lightweight, platform-level supplement to the core cohort study. **Not part of the frozen
analysis** — it does not touch the causal results (H1, H3). It provides the macro backdrop.

## What it is
Monthly platform-wide counts pulled from the Stack Exchange API (Stack Apps key), for Stack
Overflow: new **questions**, new **answers**, new **users**. Baseline = 2021-01 to 2022-11
(pre-ChatGPT). Data in `so_platform_monthly_api.csv`.

## Headline (monthly averages vs pre-ChatGPT baseline)

| Metric | pre-ChatGPT | 2023 | 2024 | 2025 | 2026 Jan–May |
|---|---|---|---|---|---|
| Questions | ~120.7k/mo | −45.5% | −72.4% | −92.1% | −97.4% |
| Answers | ~155.7k/mo | −45.1% | −69.6% | −89.8% | −95.0% |
| New users | ~242.6k/mo | −22.8% | **+98.6%** | +6.1% | −46.3% |

## What it shows (and doesn't)
- **Public knowledge-contribution activity collapsed** after ChatGPT — questions and answers
  fell ~45% in year 1 and ~95% by early 2026. This is the right thing to report.
- **"User count" is a bad/misleading metric.** New-user counts are noisy and even rose ~99%
  in 2024 (almost certainly bot/spam/account-creation artifact). So: do **not** say "Stack
  Overflow lost users"; say "public contribution activity collapsed."
- **Cross-check with our cohort:** platform-wide answers fell ~45% in 2023; our 50,305
  pre-shock core contributors fell ~50% over the same window (47.0k → 94.9k/mo baseline).
  Nearly identical → the early collapse is driven mainly by **existing core contributors
  ceasing to produce**, not just by newcomers staying away. This independently corroborates
  the core study's exodus finding (63% of the cohort silent ≥6 months by K=6).

## Limits
- API gives platform-level monthly trends only. It **cannot** do cohort construction, SDT
  motivation typing, or survival analysis — that requires SEDE (see `../data_collection/`).
- New-user series is unreliable (bot noise); use questions/answers only for the trend.
- Reproducibility: pulled via Stack Exchange API; exact pull script not committed (the numbers
  are recorded here as reported). A reproducible puller is a future to-do if this becomes
  load-bearing.
