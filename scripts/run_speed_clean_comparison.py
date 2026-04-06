"""
Generate the exposure-time-controlled speed comparison dataset.

This reproduces the clean comparison described in tasks/iteration4.md:
- PL = 0.95
- rapid speed = 0.20, sampled at t+10, t+20, t+40 -> steps 15, 25, 45
- gradual speed = 0.95 / 160, sampled at t+10, t+20, t+40 -> steps 170, 180, 200
- scenarios = baseline, ubi_only, full_bundle
- 50 runs per condition
"""
import os
import sys

import pandas as pd

sys.path.insert(0, "/Users/cloud/Documents/claude/post-scarcity-abm")

from models.pathway_a_abm.model import PostLaborModel


OUTPUT = "data/simulation/speed_clean_comparison.csv"
PL = 0.95
N_RUNS = 50

SCENARIOS = {
    "baseline": {},
    "ubi_only": {"ubi": 0.7},
    "full_bundle": {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
}

SPEED_CONFIGS = {
    "rapid": {
        "automation_speed": 0.20,
        "sample_steps": {10: 15, 20: 25, 40: 45},
        "seed_offset": 0,
    },
    "gradual": {
        "automation_speed": PL / 160.0,
        "sample_steps": {10: 170, 20: 180, 40: 200},
        "seed_offset": 50_000,
    },
}


def collect_run(speed_name, scenario_name, intervention, run_id):
    cfg = SPEED_CONFIGS[speed_name]
    model = PostLaborModel(
        n_agents=200,
        post_labor_fraction=PL,
        automation_speed=cfg["automation_speed"],
        virtual_world_quality=0.0,
        collectivism_index=0.3,
        contagion_strength=0.5,
        intervention=intervention,
        seed=run_id * 1000 + cfg["seed_offset"] + hash(scenario_name) % 10000,
    )

    target_steps = set(cfg["sample_steps"].values())
    max_step = max(target_steps)
    rows = []

    for step in range(1, max_step + 1):
        model.step()
        if step not in target_steps:
            continue

        snapshot = model.datacollector.get_model_vars_dataframe().iloc[-1]
        steps_after_target = next(
            delta for delta, sample_step in cfg["sample_steps"].items() if sample_step == step
        )
        rows.append(
            {
                "speed": speed_name,
                "scenario": scenario_name,
                "step": step,
                "steps_after_target": steps_after_target,
                "run_id": run_id,
                "sink_index": snapshot["sink_index"],
                "meaning_index": snapshot["meaning_index"],
                "post_labor_current": snapshot["post_labor_current"],
            }
        )

    return rows


def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    results = []
    total = len(SPEED_CONFIGS) * len(SCENARIOS) * N_RUNS
    done = 0

    print(f"Running clean speed comparison ({total} simulations)")
    print("=" * 70)

    for speed_name, cfg in SPEED_CONFIGS.items():
        for scenario_name, intervention in SCENARIOS.items():
            for run_id in range(N_RUNS):
                results.extend(collect_run(speed_name, scenario_name, intervention, run_id))
                done += 1

            subset = pd.DataFrame(
                [
                    row
                    for row in results
                    if row["speed"] == speed_name and row["scenario"] == scenario_name
                ]
            )
            grouped = subset.groupby("steps_after_target")["sink_index"].mean()
            print(
                f"{speed_name:7s} | {scenario_name:11s} | "
                f"t+10={grouped.loc[10]:.3f} | t+20={grouped.loc[20]:.3f} | "
                f"t+40={grouped.loc[40]:.3f} | ({done}/{total})"
            )

    df = pd.DataFrame(results)
    df.to_csv(OUTPUT, index=False)
    print(f"\nSaved to {OUTPUT} ({len(df)} rows)")


if __name__ == "__main__":
    main()
