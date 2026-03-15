"""
Experiment B: Intervention Decoupling.
Tests how much of Roles > UBI comes from structural advantage vs mechanism.

3 variants × 150 runs = 450 runs
"""
import sys
sys.path.insert(0, '/Users/cloud/Documents/claude/post-scarcity-abm')

import numpy as np
import pandas as pd
import os
from models.pathway_a_abm.runner import run_single

# Three intervention variants at PL=0.95
VARIANTS = {
    "ubi_pure": {
        # UBI restores economic_role = ubi * 0.30 only (no competence boost)
        "intervention": {"ubi": 0.7},
        "ubi_strength": 0.30,
        "roles_strength": 0.35,
        "roles_competence_boost": True,
    },
    "roles_matched": {
        # Roles restore economic_role = roles * 0.30 ONLY (same strength as UBI, no competence boost)
        "intervention": {"roles": 0.7},
        "ubi_strength": 0.30,
        "roles_strength": 0.30,  # matched to UBI strength
        "roles_competence_boost": False,  # no competence boost
    },
    "roles_full": {
        # Current behavior: economic_role = roles * 0.35 + competence boost
        "intervention": {"roles": 0.7},
        "ubi_strength": 0.30,
        "roles_strength": 0.35,
        "roles_competence_boost": True,
    },
}

N_RUNS = 150
PL = 0.95
OUTPUT = "data/simulation/ablation_interventions.csv"

def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    results = []
    total = len(VARIANTS) * N_RUNS
    done = 0

    print(f"Running Intervention Decoupling ({total} total runs)")
    print("=" * 70)

    for variant_name, variant_cfg in VARIANTS.items():
        run_sinks = []
        run_meanings = []
        run_collapsed = []
        run_competences = []

        iv = variant_cfg["intervention"]

        for run in range(N_RUNS):
            params = {
                "n_agents": 200,
                "post_labor_fraction": PL,
                "automation_speed": 0.03,
                "virtual_world_quality": 0.0,
                "collectivism_index": 0.3,
                "contagion_strength": 0.5,
                "intervention": iv,
                "ubi_strength": variant_cfg["ubi_strength"],
                "roles_strength": variant_cfg["roles_strength"],
                "roles_competence_boost": variant_cfg["roles_competence_boost"],
            }
            r = run_single(params, seed=run * 1000 + hash(variant_name) % 10000)
            r["variant"] = variant_name
            r["post_labor"] = PL
            r["run_id"] = run
            results.append(r)
            run_sinks.append(r["sink_index"])
            run_meanings.append(r["meaning_index"])
            run_collapsed.append(r["sink_collapsed"])
            done += 1

        collapse_prob = np.mean(run_collapsed) * 100
        print(f"{variant_name:15s} | "
              f"meaning={np.mean(run_meanings):.3f} ± {np.std(run_meanings):.3f} | "
              f"sink={np.mean(run_sinks):.3f} ± {np.std(run_sinks):.3f} | "
              f"collapse={collapse_prob:.0f}% | ({done}/{total})")

    df = pd.DataFrame(results)
    df.to_csv(OUTPUT, index=False)
    print(f"\nSaved to {OUTPUT} ({len(df)} rows)")
    return df

if __name__ == "__main__":
    main()
