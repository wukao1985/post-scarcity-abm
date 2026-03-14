"""
Chunked sweep runner for memory efficiency.
Processes sweeps in smaller batches and appends to CSV.
"""
import sys
sys.path.insert(0, '/Users/cloud/Documents/claude/post-scarcity-abm')

import numpy as np
import pandas as pd
import os
import gc

from models.pathway_a_abm.model import PostLaborModel


def run_single(params, seed=None):
    """Run one simulation for 80 steps, return final-step metrics."""
    m = PostLaborModel(**params, seed=seed)
    for _ in range(80):
        m.step()
    df = m.datacollector.get_model_vars_dataframe()
    final = df.iloc[-1].to_dict()
    final["sink_collapsed"] = 1 if final["sink_index"] > 0.7 else 0
    del m, df
    gc.collect()
    return final


def run_sweep_3_chunked(n_runs=100, output_dir="data/simulation"):
    """
    Sweep 3: Virtual World Quality (RQ2)
    Variable: virtual_world_quality ∈ [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    Fixed: post-labor = [0.8, 0.95], scenarios = [baseline, UBI_only, full_bundle]
    """
    os.makedirs(output_dir, exist_ok=True)

    vw_levels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    post_labor_levels = [0.8, 0.95]
    scenarios = {
        "baseline":     {},
        "ubi_only":     {"ubi": 0.7},
        "full_bundle":  {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
    }

    output_file = f"{output_dir}/sweep3_virtual_world.csv"

    # Write header if file doesn't exist
    if not os.path.exists(output_file):
        with open(output_file, 'w') as f:
            f.write("meaning_index,sink_index,productive_frac,beautiful_one_frac,aggressor_frac,withdrawn_frac,collapsed_frac,birth_intention,social_trust,post_labor_current,sink_collapsed,scenario,post_labor,virtual_world_quality,run_id\n")

    total = len(vw_levels) * len(post_labor_levels) * len(scenarios) * n_runs
    done = 0

    print(f"Running Sweep 3: Virtual World Quality ({total} total runs)")
    print("=" * 60)

    for vw in vw_levels:
        for pl in post_labor_levels:
            for scenario_name, iv in scenarios.items():
                batch_results = []

                for run in range(n_runs):
                    params = {
                        "n_agents":             200,
                        "post_labor_fraction":  pl,
                        "automation_speed":     0.03,
                        "virtual_world_quality":vw,
                        "collectivism_index":   0.3,
                        "contagion_strength":   0.5,
                        "intervention":         iv,
                    }
                    r = run_single(params, seed=run * 1000 + int(vw * 100) + int(pl * 10))
                    r["scenario"]  = scenario_name
                    r["post_labor"]= pl
                    r["virtual_world_quality"] = vw
                    r["run_id"]    = run
                    batch_results.append(r)
                    done += 1

                # Write batch to file
                df = pd.DataFrame(batch_results)
                df.to_csv(output_file, mode='a', header=False, index=False)

                # Print progress
                collapse_prob = np.mean([r["sink_collapsed"] for r in batch_results]) * 100
                print(f"vw={vw:.1f} | pl={pl:.2f} | {scenario_name:15s} | "
                      f"meaning={np.mean([r['meaning_index'] for r in batch_results]):.3f} | "
                      f"sink={np.mean([r['sink_index'] for r in batch_results]):.3f} | "
                      f"collapse={collapse_prob:.0f}% | "
                      f"({done}/{total})")

                del df, batch_results
                gc.collect()

    print(f"\nSaved to {output_file}")


def run_sweep_4_chunked(n_runs=100, output_dir="data/simulation"):
    """
    Sweep 4: Collectivism Index (RQ4)
    Variable: collectivism_index ∈ [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    Fixed: post-labor = [0.8, 0.95], scenarios = [baseline, UBI_only, full_bundle]
    """
    os.makedirs(output_dir, exist_ok=True)

    coll_levels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    post_labor_levels = [0.8, 0.95]
    scenarios = {
        "baseline":     {},
        "ubi_only":     {"ubi": 0.7},
        "full_bundle":  {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
    }

    output_file = f"{output_dir}/sweep4_collectivism.csv"

    if not os.path.exists(output_file):
        with open(output_file, 'w') as f:
            f.write("meaning_index,sink_index,productive_frac,beautiful_one_frac,aggressor_frac,withdrawn_frac,collapsed_frac,birth_intention,social_trust,post_labor_current,sink_collapsed,scenario,post_labor,collectivism_index,run_id\n")

    total = len(coll_levels) * len(post_labor_levels) * len(scenarios) * n_runs
    done = 0

    print(f"Running Sweep 4: Collectivism Index ({total} total runs)")
    print("=" * 60)

    for coll in coll_levels:
        for pl in post_labor_levels:
            for scenario_name, iv in scenarios.items():
                batch_results = []

                for run in range(n_runs):
                    params = {
                        "n_agents":             200,
                        "post_labor_fraction":  pl,
                        "automation_speed":     0.03,
                        "virtual_world_quality":0.0,
                        "collectivism_index":   coll,
                        "contagion_strength":   0.5,
                        "intervention":         iv,
                    }
                    r = run_single(params, seed=run * 1000 + int(coll * 100) + int(pl * 10))
                    r["scenario"]  = scenario_name
                    r["post_labor"]= pl
                    r["collectivism_index"] = coll
                    r["run_id"]    = run
                    batch_results.append(r)
                    done += 1

                df = pd.DataFrame(batch_results)
                df.to_csv(output_file, mode='a', header=False, index=False)

                collapse_prob = np.mean([r["sink_collapsed"] for r in batch_results]) * 100
                print(f"coll={coll:.1f} | pl={pl:.2f} | {scenario_name:15s} | "
                      f"meaning={np.mean([r['meaning_index'] for r in batch_results]):.3f} | "
                      f"sink={np.mean([r['sink_index'] for r in batch_results]):.3f} | "
                      f"collapse={collapse_prob:.0f}% | "
                      f"({done}/{total})")

                del df, batch_results
                gc.collect()

    print(f"\nSaved to {output_file}")


def run_sweep_6_chunked(n_runs=150, output_dir="data/simulation"):
    """
    Sweep 6: Full 10-Scenario Grid at 0.5/0.8/0.95
    All 10 V3 scenarios x 3 post-labor levels x 150 runs
    """
    os.makedirs(output_dir, exist_ok=True)

    post_labor_levels = [0.5, 0.8, 0.95]
    scenarios = {
        "baseline":                  {},
        "ubi_only":                  {"ubi": 0.7},
        "roles":                     {"roles": 0.7},
        "fairness":                  {"fairness": 0.7},
        "full_bundle":               {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
        "UBI+virtual":               {"ubi": 0.7},
        "UBI+collectivism":          {"ubi": 0.7},
        "roles+virtual":             {"roles": 0.7},
        "fairness+collectivism":     {"fairness": 0.7},
        "all_bundle":                {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
    }

    scenario_params = {
        "UBI+virtual":           {"virtual_world_quality": 0.8},
        "UBI+collectivism":      {"collectivism_index": 0.8},
        "roles+virtual":         {"virtual_world_quality": 0.8},
        "fairness+collectivism": {"collectivism_index": 0.8},
        "all_bundle":            {"virtual_world_quality": 0.8, "collectivism_index": 0.8},
    }

    output_file = f"{output_dir}/sweep6_full_grid.csv"

    if not os.path.exists(output_file):
        with open(output_file, 'w') as f:
            f.write("meaning_index,sink_index,productive_frac,beautiful_one_frac,aggressor_frac,withdrawn_frac,collapsed_frac,birth_intention,social_trust,post_labor_current,sink_collapsed,scenario,post_labor,run_id\n")

    total = len(scenarios) * len(post_labor_levels) * n_runs
    done = 0

    print(f"Running Sweep 6: Full 10-Scenario Grid ({total} total runs)")
    print("=" * 60)

    for pl in post_labor_levels:
        for scenario_name, iv in scenarios.items():
            batch_results = []

            special = scenario_params.get(scenario_name, {})
            vw = special.get("virtual_world_quality", 0.0)
            coll = special.get("collectivism_index", 0.3)

            for run in range(n_runs):
                params = {
                    "n_agents":             200,
                    "post_labor_fraction":  pl,
                    "automation_speed":     0.03,
                    "virtual_world_quality":vw,
                    "collectivism_index":   coll,
                    "contagion_strength":   0.5,
                    "intervention":         iv,
                }
                r = run_single(params, seed=run * 1000 + int(pl * 100))
                r["scenario"]  = scenario_name
                r["post_labor"]= pl
                r["run_id"]    = run
                batch_results.append(r)
                done += 1

            df = pd.DataFrame(batch_results)
            df.to_csv(output_file, mode='a', header=False, index=False)

            collapse_prob = np.mean([r["sink_collapsed"] for r in batch_results]) * 100
            print(f"pl={pl:.2f} | {scenario_name:20s} | "
                  f"meaning={np.mean([r['meaning_index'] for r in batch_results]):.3f} | "
                  f"sink={np.mean([r['sink_index'] for r in batch_results]):.3f} | "
                  f"collapse={collapse_prob:.0f}% | "
                  f"({done}/{total})")

            del df, batch_results
            gc.collect()

    print(f"\nSaved to {output_file}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        sweep_num = sys.argv[1]
        if sweep_num == "3":
            run_sweep_3_chunked()
        elif sweep_num == "4":
            run_sweep_4_chunked()
        elif sweep_num == "6":
            run_sweep_6_chunked()
        else:
            print("Usage: python runner_chunked.py [3|4|6]")
    else:
        print("Usage: python runner_chunked.py [3|4|6]")
