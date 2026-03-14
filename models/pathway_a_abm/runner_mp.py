"""
Multiprocessing sweep runner for faster execution.
"""
import sys
sys.path.insert(0, '/Users/cloud/Documents/claude/post-scarcity-abm')

import numpy as np
import pandas as pd
import os
from multiprocessing import Pool, cpu_count
from models.pathway_a_abm.model import PostLaborModel


def run_single(args):
    """Run one simulation - must be at module level for multiprocessing."""
    params, seed, meta = args
    try:
        m = PostLaborModel(**params, seed=seed)
        for _ in range(80):
            m.step()
        df = m.datacollector.get_model_vars_dataframe()
        final = df.iloc[-1].to_dict()
        final["sink_collapsed"] = 1 if final["sink_index"] > 0.7 else 0
        final.update(meta)
        return final
    except Exception as e:
        print(f"Error in run_single: {e}")
        return None


def parallel_run(param_list, n_workers=None):
    """Run simulations in parallel."""
    if n_workers is None:
        n_workers = max(1, cpu_count() - 1)

    with Pool(n_workers) as pool:
        results = pool.map(run_single, param_list)

    return [r for r in results if r is not None]


def run_sweep_3_mp(n_runs=100, output_dir="data/simulation", n_workers=None):
    """Sweep 3: Virtual World Quality (multiprocessing)."""
    os.makedirs(output_dir, exist_ok=True)

    vw_levels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    post_labor_levels = [0.8, 0.95]
    scenarios = {
        "baseline": {},
        "ubi_only": {"ubi": 0.7},
        "full_bundle": {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
    }

    # Build parameter list
    param_list = []
    run_id = 0
    for vw in vw_levels:
        for pl in post_labor_levels:
            for scenario_name, iv in scenarios.items():
                for run in range(n_runs):
                    params = {
                        "n_agents": 200,
                        "post_labor_fraction": pl,
                        "automation_speed": 0.03,
                        "virtual_world_quality": vw,
                        "collectivism_index": 0.3,
                        "contagion_strength": 0.5,
                        "intervention": iv,
                    }
                    seed = run * 1000 + int(vw * 100) + int(pl * 10)
                    meta = {"scenario": scenario_name, "post_labor": pl,
                            "virtual_world_quality": vw, "run_id": run}
                    param_list.append((params, seed, meta))

    total = len(param_list)
    print(f"Sweep 3: {total} runs using {n_workers or max(1, cpu_count()-1)} workers")
    print("=" * 60)

    results = parallel_run(param_list, n_workers)

    df = pd.DataFrame(results)
    df.to_csv(f"{output_dir}/sweep3_virtual_world.csv", index=False)

    # Print summary
    for vw in vw_levels:
        for pl in post_labor_levels:
            for scen in scenarios.keys():
                sub = df[(df["virtual_world_quality"] == vw) &
                         (df["post_labor"] == pl) &
                         (df["scenario"] == scen)]
                if len(sub) > 0:
                    print(f"vw={vw:.1f} | pl={pl:.2f} | {scen:15s} | "
                          f"meaning={sub['meaning_index'].mean():.3f} | "
                          f"sink={sub['sink_index'].mean():.3f} | "
                          f"collapse={sub['sink_collapsed'].mean()*100:.0f}%")

    print(f"\nSaved to {output_dir}/sweep3_virtual_world.csv")
    return df


def run_sweep_4_mp(n_runs=100, output_dir="data/simulation", n_workers=None):
    """Sweep 4: Collectivism Index (multiprocessing)."""
    os.makedirs(output_dir, exist_ok=True)

    coll_levels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    post_labor_levels = [0.8, 0.95]
    scenarios = {
        "baseline": {},
        "ubi_only": {"ubi": 0.7},
        "full_bundle": {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
    }

    param_list = []
    for coll in coll_levels:
        for pl in post_labor_levels:
            for scenario_name, iv in scenarios.items():
                for run in range(n_runs):
                    params = {
                        "n_agents": 200,
                        "post_labor_fraction": pl,
                        "automation_speed": 0.03,
                        "virtual_world_quality": 0.0,
                        "collectivism_index": coll,
                        "contagion_strength": 0.5,
                        "intervention": iv,
                    }
                    seed = run * 1000 + int(coll * 100) + int(pl * 10)
                    meta = {"scenario": scenario_name, "post_labor": pl,
                            "collectivism_index": coll, "run_id": run}
                    param_list.append((params, seed, meta))

    total = len(param_list)
    print(f"Sweep 4: {total} runs using {n_workers or max(1, cpu_count()-1)} workers")
    print("=" * 60)

    results = parallel_run(param_list, n_workers)
    df = pd.DataFrame(results)
    df.to_csv(f"{output_dir}/sweep4_collectivism.csv", index=False)

    for coll in coll_levels:
        for pl in post_labor_levels:
            for scen in scenarios.keys():
                sub = df[(df["collectivism_index"] == coll) &
                         (df["post_labor"] == pl) &
                         (df["scenario"] == scen)]
                if len(sub) > 0:
                    print(f"coll={coll:.1f} | pl={pl:.2f} | {scen:15s} | "
                          f"meaning={sub['meaning_index'].mean():.3f} | "
                          f"sink={sub['sink_index'].mean():.3f} | "
                          f"collapse={sub['sink_collapsed'].mean()*100:.0f}%")

    print(f"\nSaved to {output_dir}/sweep4_collectivism.csv")
    return df


def run_sweep_6_mp(n_runs=150, output_dir="data/simulation", n_workers=None):
    """Sweep 6: Full 10-Scenario Grid (multiprocessing)."""
    os.makedirs(output_dir, exist_ok=True)

    post_labor_levels = [0.5, 0.8, 0.95]
    scenarios = {
        "baseline": {},
        "ubi_only": {"ubi": 0.7},
        "roles": {"roles": 0.7},
        "fairness": {"fairness": 0.7},
        "full_bundle": {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
        "UBI+virtual": {"ubi": 0.7},
        "UBI+collectivism": {"ubi": 0.7},
        "roles+virtual": {"roles": 0.7},
        "fairness+collectivism": {"fairness": 0.7},
        "all_bundle": {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
    }
    scenario_params = {
        "UBI+virtual": {"virtual_world_quality": 0.8},
        "UBI+collectivism": {"collectivism_index": 0.8},
        "roles+virtual": {"virtual_world_quality": 0.8},
        "fairness+collectivism": {"collectivism_index": 0.8},
        "all_bundle": {"virtual_world_quality": 0.8, "collectivism_index": 0.8},
    }

    param_list = []
    for pl in post_labor_levels:
        for scenario_name, iv in scenarios.items():
            special = scenario_params.get(scenario_name, {})
            vw = special.get("virtual_world_quality", 0.0)
            coll = special.get("collectivism_index", 0.3)

            for run in range(n_runs):
                params = {
                    "n_agents": 200,
                    "post_labor_fraction": pl,
                    "automation_speed": 0.03,
                    "virtual_world_quality": vw,
                    "collectivism_index": coll,
                    "contagion_strength": 0.5,
                    "intervention": iv,
                }
                seed = run * 1000 + int(pl * 100)
                meta = {"scenario": scenario_name, "post_labor": pl, "run_id": run}
                param_list.append((params, seed, meta))

    total = len(param_list)
    print(f"Sweep 6: {total} runs using {n_workers or max(1, cpu_count()-1)} workers")
    print("=" * 60)

    results = parallel_run(param_list, n_workers)
    df = pd.DataFrame(results)
    df.to_csv(f"{output_dir}/sweep6_full_grid.csv", index=False)

    for pl in post_labor_levels:
        for scen in scenarios.keys():
            sub = df[(df["post_labor"] == pl) & (df["scenario"] == scen)]
            if len(sub) > 0:
                print(f"pl={pl:.2f} | {scen:20s} | "
                      f"meaning={sub['meaning_index'].mean():.3f} | "
                      f"sink={sub['sink_index'].mean():.3f} | "
                      f"collapse={sub['sink_collapsed'].mean()*100:.0f}%")

    print(f"\nSaved to {output_dir}/sweep6_full_grid.csv")
    return df


def run_sweep_5(n_runs=50, output_dir="data/simulation"):
    """Sweep 5: Archetype Time Series (single-threaded, smaller)."""
    os.makedirs(output_dir, exist_ok=True)

    post_labor = 0.8
    scenarios = {
        "baseline": {},
        "full_bundle": {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
    }

    results = []
    total = len(scenarios) * n_runs

    print(f"Running Sweep 5: Archetype Time Series ({total} runs)")
    print("=" * 60)

    for scenario_name, iv in scenarios.items():
        for run in range(n_runs):
            params = {
                "n_agents": 200,
                "post_labor_fraction": post_labor,
                "automation_speed": 0.03,
                "virtual_world_quality": 0.0,
                "collectivism_index": 0.3,
                "contagion_strength": 0.5,
                "intervention": iv,
            }
            m = PostLaborModel(**params, seed=run * 1000)
            for _ in range(80):
                m.step()

            df = m.datacollector.get_model_vars_dataframe()
            df["step"] = df.index
            df["scenario"] = scenario_name
            df["run_id"] = run
            df["post_labor"] = post_labor
            results.append(df)

            if (run + 1) % 10 == 0:
                print(f"  {scenario_name} run {run+1}/{n_runs} complete...")

    full_df = pd.concat(results, ignore_index=True)
    full_df.to_csv(f"{output_dir}/sweep5_archetypes.csv", index=False)
    print(f"\nSaved to {output_dir}/sweep5_archetypes.csv")
    return full_df


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        sweep = sys.argv[1]
        if sweep == "3":
            run_sweep_3_mp()
        elif sweep == "4":
            run_sweep_4_mp()
        elif sweep == "5":
            run_sweep_5()
        elif sweep == "6":
            run_sweep_6_mp()
        else:
            print("Usage: python runner_mp.py [3|4|5|6]")
    else:
        print("Running all sweeps...")
        run_sweep_3_mp()
        run_sweep_4_mp()
        run_sweep_5()
        run_sweep_6_mp()
