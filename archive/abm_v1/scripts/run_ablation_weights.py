"""
Experiment A: Weight Ablation — virtual vs economic role ratio.
Tests whether "virtual worlds can't replace real roles" is robust or assumption-driven.

5 ratios × 4 scenarios × 50 runs = 1,000 runs
"""
import sys
sys.path.insert(0, '/Users/cloud/Documents/claude/post-scarcity-abm')

import numpy as np
import pandas as pd
import os
from models.pathway_a_abm.model import PostLaborModel
from models.pathway_a_abm.runner import run_single

# Weight ratios: vary economic:virtual while keeping total = 0.9
RATIOS = {
    "3:1":   (0.675, 0.225),
    "5:1":   (0.750, 0.150),
    "8:1":   (0.800, 0.100),  # current default
    "12:1":  (0.831, 0.069),
    "inf":   (0.900, 0.000),
}

SCENARIOS = {
    "baseline":      {"intervention": {}},
    "ubi_only":      {"intervention": {"ubi": 0.7}},
    "virtual_only":  {"intervention": {}, "virtual_world_quality": 1.0},
    "ubi_plus_virtual": {"intervention": {"ubi": 0.7}, "virtual_world_quality": 1.0},
}

N_RUNS = 50
PL = 0.95
OUTPUT = "data/simulation/ablation_weights.csv"

def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    results = []
    total = len(RATIOS) * len(SCENARIOS) * N_RUNS
    done = 0

    print(f"Running Weight Ablation ({total} total runs)")
    print("=" * 70)

    for ratio_name, (ew, vw) in RATIOS.items():
        for scenario_name, scenario_cfg in SCENARIOS.items():
            run_sinks = []
            run_meanings = []
            run_collapsed = []

            iv = scenario_cfg.get("intervention", {})
            vwq = scenario_cfg.get("virtual_world_quality", 0.0)

            for run in range(N_RUNS):
                params = {
                    "n_agents": 200,
                    "post_labor_fraction": PL,
                    "automation_speed": 0.03,
                    "virtual_world_quality": vwq,
                    "collectivism_index": 0.3,
                    "contagion_strength": 0.5,
                    "intervention": iv,
                    "economic_weight": ew,
                    "virtual_weight": vw,
                }
                r = run_single(params, seed=run * 1000 + int(ew * 1000))
                r["ratio"] = ratio_name
                r["economic_weight"] = ew
                r["virtual_weight"] = vw
                r["scenario"] = scenario_name
                r["post_labor"] = PL
                r["run_id"] = run
                results.append(r)
                run_sinks.append(r["sink_index"])
                run_meanings.append(r["meaning_index"])
                run_collapsed.append(r["sink_collapsed"])
                done += 1

            collapse_prob = np.mean(run_collapsed) * 100
            print(f"ratio={ratio_name:5s} | {scenario_name:18s} | "
                  f"meaning={np.mean(run_meanings):.3f} | "
                  f"sink={np.mean(run_sinks):.3f} | "
                  f"collapse={collapse_prob:.0f}% | ({done}/{total})")

    df = pd.DataFrame(results)
    df.to_csv(OUTPUT, index=False)
    print(f"\nSaved to {OUTPUT} ({len(df)} rows)")
    return df

if __name__ == "__main__":
    main()
