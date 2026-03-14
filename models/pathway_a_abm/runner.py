"""
Sweep runners for V3 experiments.
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


def run_single_timeseries(params, seed=None):
    """Run simulation and return full timeseries data."""
    m = PostLaborModel(**params, seed=seed)
    for _ in range(80):
        m.step()
    df = m.datacollector.get_model_vars_dataframe()
    df["step"] = df.index
    df["seed"] = seed
    return df


def run_sweep_1(n_runs=50, output_dir="data/simulation"):
    """Sweep 1: V2 replication - baseline scenarios across post-labor levels."""
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
                done += 1
                if done % 50 == 0:
                    print(f"  {done}/{total} runs complete...")

    df = pd.DataFrame(results)
    df.to_csv(f"{output_dir}/sweep1_results.csv", index=False)
    print(f"\nResults saved to {output_dir}/sweep1_results.csv")
    return df


def run_sweep_2(n_runs=100, output_dir="data/simulation"):
    """
    Sweep 2: Automation Speed (RQ3)
    - rapid: displacement jumps to final level by step 10
    - gradual: linear increase across 80 steps
    Fixed: post-labor levels = [0.5, 0.8, 0.95], all 5 V2 scenarios
    """
    os.makedirs(output_dir, exist_ok=True)

    # Automation speeds: gradual (target/80 per step) vs rapid (0.08/step, hits 0.8 by step 10)
    # V4 fix: gradual speed computed per-target so it always reaches target by step 80
    speed_configs = {
        "gradual": None,   # computed as pl/80 per target level
        "rapid": 0.08,     # 0.8 / 10 steps
    }

    post_labor_levels = [0.5, 0.8, 0.95]
    scenarios = {
        "baseline":     {},
        "ubi_only":     {"ubi": 0.7},
        "roles_only":   {"roles": 0.7},
        "fairness_only":{"fairness": 0.7},
        "full_bundle":  {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
    }

    results = []
    total = len(speed_configs) * len(post_labor_levels) * len(scenarios) * n_runs
    done = 0

    print(f"Running Sweep 2: Automation Speed ({total} total runs)")
    print("=" * 60)

    for speed_name, speed_default in speed_configs.items():
        for pl in post_labor_levels:
            # V4: gradual speed = target/80 so it always reaches target by step 80
            speed_val = pl / 80.0 if speed_default is None else speed_default
            for scenario_name, iv in scenarios.items():
                run_meanings = []
                run_sinks = []
                run_collapsed = []

                for run in range(n_runs):
                    params = {
                        "n_agents":             200,
                        "post_labor_fraction":  pl,
                        "automation_speed":     speed_val,
                        "virtual_world_quality":0.0,
                        "collectivism_index":   0.3,
                        "contagion_strength":   0.5,
                        "intervention":         iv,
                    }
                    r = run_single(params, seed=run * 1000 + int(pl * 100) + (0 if speed_name == "gradual" else 50000))
                    r["scenario"]  = scenario_name
                    r["post_labor"]= pl
                    r["speed"]     = speed_name
                    r["run_id"]    = run
                    results.append(r)
                    run_meanings.append(r["meaning_index"])
                    run_sinks.append(r["sink_index"])
                    run_collapsed.append(r["sink_collapsed"])
                    done += 1

                collapse_prob = np.mean(run_collapsed) * 100
                print(f"{speed_name:8s} | pl={pl:.2f} | {scenario_name:15s} | "
                      f"meaning={np.mean(run_meanings):.3f} | "
                      f"sink={np.mean(run_sinks):.3f} | "
                      f"collapse={collapse_prob:.0f}% | "
                      f"({done}/{total})")

    df = pd.DataFrame(results)
    df.to_csv(f"{output_dir}/sweep2_automation_speed.csv", index=False)
    print(f"\nSaved to {output_dir}/sweep2_automation_speed.csv")
    return df


def run_sweep_3(n_runs=100, output_dir="data/simulation"):
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

    results = []
    total = len(vw_levels) * len(post_labor_levels) * len(scenarios) * n_runs
    done = 0

    print(f"Running Sweep 3: Virtual World Quality ({total} total runs)")
    print("=" * 60)

    for vw in vw_levels:
        for pl in post_labor_levels:
            for scenario_name, iv in scenarios.items():
                run_meanings = []
                run_sinks = []
                run_collapsed = []

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
                    results.append(r)
                    run_meanings.append(r["meaning_index"])
                    run_sinks.append(r["sink_index"])
                    run_collapsed.append(r["sink_collapsed"])
                    done += 1

                collapse_prob = np.mean(run_collapsed) * 100
                print(f"vw={vw:.1f} | pl={pl:.2f} | {scenario_name:15s} | "
                      f"meaning={np.mean(run_meanings):.3f} | "
                      f"sink={np.mean(run_sinks):.3f} | "
                      f"collapse={collapse_prob:.0f}% | "
                      f"({done}/{total})")

    df = pd.DataFrame(results)
    df.to_csv(f"{output_dir}/sweep3_virtual_world.csv", index=False)
    print(f"\nSaved to {output_dir}/sweep3_virtual_world.csv")
    return df


def run_sweep_4(n_runs=100, output_dir="data/simulation"):
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

    results = []
    total = len(coll_levels) * len(post_labor_levels) * len(scenarios) * n_runs
    done = 0

    print(f"Running Sweep 4: Collectivism Index ({total} total runs)")
    print("=" * 60)

    for coll in coll_levels:
        for pl in post_labor_levels:
            for scenario_name, iv in scenarios.items():
                run_meanings = []
                run_sinks = []
                run_collapsed = []

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
                    results.append(r)
                    run_meanings.append(r["meaning_index"])
                    run_sinks.append(r["sink_index"])
                    run_collapsed.append(r["sink_collapsed"])
                    done += 1

                collapse_prob = np.mean(run_collapsed) * 100
                print(f"coll={coll:.1f} | pl={pl:.2f} | {scenario_name:15s} | "
                      f"meaning={np.mean(run_meanings):.3f} | "
                      f"sink={np.mean(run_sinks):.3f} | "
                      f"collapse={collapse_prob:.0f}% | "
                      f"({done}/{total})")

    df = pd.DataFrame(results)
    df.to_csv(f"{output_dir}/sweep4_collectivism.csv", index=False)
    print(f"\nSaved to {output_dir}/sweep4_collectivism.csv")
    return df


def run_sweep_5(n_runs=50, output_dir="data/simulation"):
    """
    Sweep 5: Archetype Time Series (RQ5)
    Track archetype distribution over 80 steps
    Fixed: post-labor = 0.8, scenarios = [baseline, full_bundle]
    """
    os.makedirs(output_dir, exist_ok=True)

    post_labor = 0.8
    scenarios = {
        "baseline":     {},
        "full_bundle":  {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
    }

    results = []
    total = len(scenarios) * n_runs
    done = 0

    print(f"Running Sweep 5: Archetype Time Series ({total} total runs)")
    print("=" * 60)

    for scenario_name, iv in scenarios.items():
        for run in range(n_runs):
            params = {
                "n_agents":             200,
                "post_labor_fraction":  post_labor,
                "automation_speed":     0.03,
                "virtual_world_quality":0.0,
                "collectivism_index":   0.3,
                "contagion_strength":   0.5,
                "intervention":         iv,
            }
            df = run_single_timeseries(params, seed=run * 1000)
            df["scenario"] = scenario_name
            df["run_id"] = run
            df["post_labor"] = post_labor
            results.append(df)
            done += 1
            if done % 10 == 0:
                print(f"  {done}/{total} runs complete...")

    # Combine all results
    full_df = pd.concat(results, ignore_index=True)
    full_df.to_csv(f"{output_dir}/sweep5_archetypes.csv", index=False)
    print(f"\nSaved to {output_dir}/sweep5_archetypes.csv")
    print(f"Total rows: {len(full_df)}")
    return full_df


def run_sweep_6(n_runs=150, output_dir="data/simulation"):
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

    # Special parameters for combo scenarios
    scenario_params = {
        "UBI+virtual":           {"virtual_world_quality": 0.8},
        "UBI+collectivism":      {"collectivism_index": 0.8},
        "roles+virtual":         {"virtual_world_quality": 0.8},
        "fairness+collectivism": {"collectivism_index": 0.8},
        "all_bundle":            {"virtual_world_quality": 0.8, "collectivism_index": 0.8},
    }

    results = []
    total = len(scenarios) * len(post_labor_levels) * n_runs
    done = 0

    print(f"Running Sweep 6: Full 10-Scenario Grid ({total} total runs)")
    print("=" * 60)

    for pl in post_labor_levels:
        for scenario_name, iv in scenarios.items():
            run_meanings = []
            run_sinks = []
            run_collapsed = []

            # Get special params for this scenario
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
                results.append(r)
                run_meanings.append(r["meaning_index"])
                run_sinks.append(r["sink_index"])
                run_collapsed.append(r["sink_collapsed"])
                done += 1

            collapse_prob = np.mean(run_collapsed) * 100
            print(f"pl={pl:.2f} | {scenario_name:20s} | "
                  f"meaning={np.mean(run_meanings):.3f} | "
                  f"sink={np.mean(run_sinks):.3f} | "
                  f"collapse={collapse_prob:.0f}% | "
                  f"({done}/{total})")

    df = pd.DataFrame(results)
    df.to_csv(f"{output_dir}/sweep6_full_grid.csv", index=False)
    print(f"\nSaved to {output_dir}/sweep6_full_grid.csv")
    return df


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        sweep_num = sys.argv[1]
        if sweep_num == "1":
            run_sweep_1()
        elif sweep_num == "2":
            run_sweep_2()
        elif sweep_num == "3":
            run_sweep_3()
        elif sweep_num == "4":
            run_sweep_4()
        elif sweep_num == "5":
            run_sweep_5()
        elif sweep_num == "6":
            run_sweep_6()
        else:
            print("Usage: python runner.py [1|2|3|4|5|6]")
    else:
        print("Running all sweeps sequentially...")
        run_sweep_2()
        run_sweep_3()
        run_sweep_4()
        run_sweep_5()
        run_sweep_6()
