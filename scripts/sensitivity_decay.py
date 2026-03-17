"""
Sensitivity analysis for decay parameter.

Sweeps decay values and measures trigger_rate (fraction of agents with meaning in [0.35, 0.65])
and other calibration metrics.
"""
import numpy as np
import pandas as pd
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.pathway_a_abm.model import PostLaborModel


def run_single(decay, post_labor_fraction=0.95, intervention=None, steps=80, seed=None):
    """Run a single simulation and return late-run metrics."""
    model = PostLaborModel(
        post_labor_fraction=post_labor_fraction,
        intervention=intervention,
        decay=decay,
        seed=seed
    )

    for _ in range(steps):
        model.step()

    # Get late-run window (steps 61-80)
    df = model.datacollector.get_model_vars_dataframe()
    late_run = df.iloc[61:81] if len(df) >= 81 else df.iloc[-20:]

    # Calculate metrics
    mean_meaning = late_run['meaning_index'].mean()
    trigger_rate_mean = late_run['trigger_rate'].mean()

    # Calculate fraction_in_band as fraction of time agents spend in band
    # This requires computing across all agent histories, but we approximate
    # using the trigger_rate which is already computed per-step
    fraction_in_band_mean = late_run['trigger_rate'].mean()

    return {
        'mean_meaning': mean_meaning,
        'trigger_rate_mean': trigger_rate_mean,
        'fraction_in_band_mean': fraction_in_band_mean,
    }


def run_sweep(decay_values, n_runs=50, post_labor_fraction=0.95, intervention=None):
    """Run sensitivity sweep over decay values."""
    results = []

    for decay in decay_values:
        print(f"Running decay={decay:.2f}...", flush=True)

        run_results = []
        for run_idx in range(n_runs):
            seed = run_idx + int(decay * 1000)  # Unique seed per run
            metrics = run_single(
                decay=decay,
                post_labor_fraction=post_labor_fraction,
                intervention=intervention,
                seed=seed
            )
            run_results.append(metrics)

        # Aggregate across runs
        mean_meanings = [r['mean_meaning'] for r in run_results]
        trigger_rates = [r['trigger_rate_mean'] for r in run_results]
        fraction_in_bands = [r['fraction_in_band_mean'] for r in run_results]

        results.append({
            'decay_value': decay,
            'mean_meaning': np.mean(mean_meanings),
            'mean_meaning_std': np.std(mean_meanings),
            'trigger_rate_mean': np.mean(trigger_rates),
            'trigger_rate_std': np.std(trigger_rates),
            'fraction_in_band_mean': np.mean(fraction_in_bands),
            'fraction_in_band_std': np.std(fraction_in_bands),
            'n_runs': n_runs,
        })

    return pd.DataFrame(results)


def main():
    # Configuration
    decay_values = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
    n_runs = 50
    post_labor_fraction = 0.95
    intervention = {"ubi": 0.7}

    # Run sweep
    print("=" * 60)
    print("Sensitivity Analysis: decay parameter")
    print(f"Scenario: UBI only (ubi=0.7), post_labor={post_labor_fraction}")
    print(f"Runs per point: {n_runs}")
    print("=" * 60)

    df = run_sweep(
        decay_values=decay_values,
        n_runs=n_runs,
        post_labor_fraction=post_labor_fraction,
        intervention=intervention
    )

    # Save results
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'simulation')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'sensitivity_decay.csv')
    df.to_csv(output_path, index=False)

    # Print clean table
    print("\n" + "=" * 80)
    print("RESULTS")
    print("=" * 80)
    print(f"{'decay':>8} | {'mean_meaning':>12} | {'trigger_rate':>12} | {'frac_in_band':>12}")
    print("-" * 80)

    for _, row in df.iterrows():
        print(f"{row['decay_value']:>8.2f} | {row['mean_meaning']:>12.4f} | {row['trigger_rate_mean']:>12.4f} | {row['fraction_in_band_mean']:>12.4f}")

    print("-" * 80)
    print(f"\nSaved to: {output_path}")

    return df


if __name__ == "__main__":
    main()
