"""
Sweep 1 runner — replicates V2 parameter sweep for validation.
"""
import sys
sys.path.insert(0, '/Users/cloud/Documents/claude/post-scarcity-abm')

import numpy as np
import pandas as pd
import os

from models.pathway_a_abm.model import PostLaborModel


def run_single(params, seed=None):
    """Run one simulation for 80 steps, return final-step metrics."""
    m = PostLaborModel(**params, seed=seed)
    for _ in range(80):
        m.step()
    df = m.datacollector.get_model_vars_dataframe()
    final = df.iloc[-1].to_dict()
    final["sink_collapsed"] = 1 if final["sink_index"] > 0.7 else 0
    return final


def run_sweep_1(n_runs=50, output_dir="data/simulation"):
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs("reports/figures", exist_ok=True)

    post_labor_values = [0.0, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
    scenarios = {
        "baseline":     {},
        "ubi_only":     {"ubi": 0.7},
        "roles_only":   {"roles": 0.7},
        "fairness_only":{"fairness": 0.7},
        "full_bundle":  {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
    }

    results = []
    total = len(post_labor_values) * len(scenarios) * n_runs
    done = 0

    for pl in post_labor_values:
        for scenario_name, iv in scenarios.items():
            run_meanings  = []
            run_sinks     = []
            run_collapsed = []

            for run in range(n_runs):
                params = {
                    "n_agents":             200,
                    "post_labor_fraction":  pl,
                    "automation_speed":     0.03,
                    "virtual_world_quality":0.0,
                    "collectivism_index":   0.3,
                    "contagion_strength":   0.5,
                    "intervention":         iv,
                }
                r = run_single(params, seed=run * 1000 + int(pl * 100))
                r["scenario"]  = scenario_name
                r["post_labor"]= pl
                r["run_id"]    = run
                results.append(r)
                run_meanings.append(r["meaning_index"])
                run_sinks.append(r["sink_index"])
                run_collapsed.append(r["sink_collapsed"])
                done += 1
                if done % 50 == 0:
                    print(f"  {done}/{total} runs complete...")

            collapse_prob = np.mean(run_collapsed) * 100
            print(f"pl={pl:.2f} | {scenario_name:15s} | "
                  f"meaning={np.mean(run_meanings):.3f} | "
                  f"sink={np.mean(run_sinks):.3f} | "
                  f"collapse={collapse_prob:.0f}%")

    df = pd.DataFrame(results)
    df.to_csv(f"{output_dir}/sweep1_results.csv", index=False)
    print(f"\nResults saved to {output_dir}/sweep1_results.csv")
    return df


if __name__ == "__main__":
    print("Running Sweep 1 (V2 replication, 50 runs/point)...")
    df = run_sweep_1(n_runs=50)

    # Summary table
    summary = df.groupby(["post_labor", "scenario"]).agg(
        meaning=("meaning_index", "mean"),
        sink=("sink_index", "mean"),
        collapse_prob=("sink_collapsed", "mean"),
    ).reset_index()
    summary["collapse_prob"] *= 100

    key_rows = summary[
        summary["post_labor"].isin([0.2, 0.5, 0.8, 0.95]) &
        summary["scenario"].isin(["baseline", "ubi_only", "full_bundle"])
    ]
    print("\n=== KEY RESULTS TABLE ===")
    print(key_rows.to_string(index=False))
