"""
Calibrate UBI policy support against meaning-band dynamics.

This script sweeps `ubi_strength`, the policy-strength mechanism that already
exists in `models/pathway_a_abm/model.py`.

Operational definitions used here:
- `analytic_displaced_meaning`: deterministic fixed point for a representative
  displaced agent with no contagion, no aggressor exposure, and no virtual role
- `analytic_mixed_meaning`: deterministic mean-field fixed point under the
  model's actual per-step random displacement process at the chosen
  `post_labor_fraction`
- `trigger_rate`: share of agent-step transitions that ENTER the band
  [0.35, 0.65] (NOT the same as band_occupancy in model.py datacollector)
- `fraction_in_band`: share of agents in the band [0.35, 0.65]

Note: This script's `trigger_rate` measures band ENTRY transitions, which is
different from `band_occupancy` in model.py (fraction of agents currently IN
the band). This is intentional for calibration analysis.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from models.pathway_a_abm.model import PostLaborModel


BAND_LOW = 0.35
BAND_HIGH = 0.65
N_RUNS = 100
N_STEPS = 80
BURN_IN = 60
POST_LABOR = 0.95
OUTPUT_PATH = ROOT / "data" / "simulation" / "calibration_meaning_support.csv"
SWEEP_VALUES = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]

# Representative balanced-agent parameters from model.py.
BALANCED_PROFILE = {
    "resilience": 0.5,
    "social_capital": 0.5,
    "skill_transferability": 0.5,
}


def fixed_point_for_role(
    *,
    economic_role: float,
    fairness: float,
    inequality_index: float,
    roles_program: float,
    roles_competence_boost: bool,
    resilience: float,
    social_capital: float,
    skill_transferability: float,
    collectivism_index: float = 0.3,
    virtual_world_quality: float = 0.0,
    status_concentration: float = 1.0,
    economic_weight: float = 0.8,
    virtual_weight: float = 0.1,
    virtual_role: float = 0.0,
    aggressor_frac: float = 0.0,
    contagion: float = 0.0,
) -> dict[str, float]:
    """Deterministic one-step fixed point for the current target equations."""
    base = 0.32
    roles_comp = 0.10 * roles_program if roles_competence_boost else 0.0
    status_gap = np.clip(inequality_index * (1.0 - economic_role), 0.0, 1.0)

    autonomy = base + (
        0.25 * economic_role
        + 0.10 * virtual_role
        + 0.10 * fairness
        + 0.12 * resilience
        - 0.06 * status_gap
        - 0.05 * contagion
    )
    competence = base + (
        0.25 * economic_role
        + 0.10 * virtual_role * virtual_world_quality
        + 0.12 * skill_transferability
        + roles_comp
        - 0.05 * contagion
    )
    relatedness = base + (
        0.18 * social_capital
        + 0.10 * collectivism_index
        + 0.10 * economic_role
        + 0.05 * virtual_world_quality
        + 0.08 * fairness
        - 0.12 * aggressor_frac
        - 0.05 * contagion
    )
    status = base + (
        0.25 * economic_role
        + 0.10 * fairness
        + 0.08 * relatedness
        - 0.12 * status_concentration * (1.0 - economic_role)
        - 0.04 * contagion
    )

    contribution = economic_role * economic_weight + virtual_role * virtual_weight
    meaning = (
        0.25 * autonomy
        + 0.25 * competence
        + 0.25 * relatedness
        + 0.10 * status
        + 0.15 * contribution
        - 0.08 * contagion
        + 0.08 * resilience
    )

    return {
        "autonomy": autonomy,
        "competence": competence,
        "relatedness": relatedness,
        "status": status,
        "meaning": meaning,
        "economic_role": economic_role,
    }


def analytical_ubi_equilibria(
    ubi_strength: float,
    *,
    ubi: float = 0.7,
    post_labor_fraction: float = POST_LABOR,
) -> dict[str, float]:
    """Representative fixed points for the UBI-only scenario used in calibration."""
    fairness = 0.1 + ubi * 0.3
    inequality_index = np.clip(1.0 - fairness, 0.0, 1.0)
    displaced_role = ubi * ubi_strength
    mixed_role = post_labor_fraction * displaced_role + (1.0 - post_labor_fraction) * 1.0

    displaced = fixed_point_for_role(
        economic_role=displaced_role,
        fairness=fairness,
        inequality_index=inequality_index,
        roles_program=0.0,
        roles_competence_boost=True,
        **BALANCED_PROFILE,
    )
    mixed = fixed_point_for_role(
        economic_role=mixed_role,
        fairness=fairness,
        inequality_index=inequality_index,
        roles_program=0.0,
        roles_competence_boost=True,
        **BALANCED_PROFILE,
    )

    return {
        "analytic_displaced_meaning": displaced["meaning"],
        "analytic_mixed_meaning": mixed["meaning"],
        "analytic_displaced_autonomy": displaced["autonomy"],
        "analytic_displaced_competence": displaced["competence"],
        "analytic_displaced_relatedness": displaced["relatedness"],
        "analytic_displaced_status": displaced["status"],
        "analytic_displaced_economic_role": displaced["economic_role"],
        "analytic_mixed_economic_role": mixed["economic_role"],
    }


def run_calibration_run(ubi_strength: float, *, seed: int) -> dict[str, float]:
    """Run one UBI-only trajectory and compute late-run calibration metrics."""
    model = PostLaborModel(
        n_agents=200,
        post_labor_fraction=POST_LABOR,
        automation_speed=0.03,
        virtual_world_quality=0.0,
        collectivism_index=0.3,
        contagion_strength=0.5,
        intervention={"ubi": 0.7},
        ubi_strength=ubi_strength,
        seed=seed,
    )

    mean_meaning = []
    fraction_in_band = []
    trigger_entries = []
    prev_meanings = None

    for step in range(N_STEPS):
        model.step()
        meanings = np.array([agent.meaning for agent in model.agents], dtype=float)
        in_band = (meanings >= BAND_LOW) & (meanings <= BAND_HIGH)

        mean_meaning.append(float(meanings.mean()))
        fraction_in_band.append(float(in_band.mean()))

        if prev_meanings is not None:
            prev_in_band = (prev_meanings >= BAND_LOW) & (prev_meanings <= BAND_HIGH)
            trigger_entries.append(float((~prev_in_band & in_band).mean()))

        prev_meanings = meanings

    late_meaning = np.array(mean_meaning[BURN_IN:], dtype=float)
    late_band = np.array(fraction_in_band[BURN_IN:], dtype=float)
    late_entries = np.array(trigger_entries[BURN_IN - 1 :], dtype=float)

    return {
        "equilibrium_meaning": float(late_meaning.mean()),
        "trigger_rate": float(late_entries.mean()),
        "fraction_in_band": float(late_band.mean()),
    }


def run_sweep() -> pd.DataFrame:
    """Execute the full sweep and save the summary table."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    results = []

    print("Calibrating UBI support with PL=0.95, UBI-only")
    print(f"Sweep values: {SWEEP_VALUES}")
    print(
        "Metrics: analytic displaced meaning, analytic mixed meaning, "
        "late-run empirical meaning, trigger entry rate, band occupancy"
    )
    print(f"Runs per point: {N_RUNS}")
    print("-" * 72)

    for index, ubi_strength in enumerate(SWEEP_VALUES):
        analytic = analytical_ubi_equilibria(ubi_strength)
        run_metrics = []

        for run_id in range(N_RUNS):
            seed = index * 100_000 + run_id * 1_000
            run_metrics.append(run_calibration_run(ubi_strength, seed=seed))

        equilibrium = np.array([row["equilibrium_meaning"] for row in run_metrics], dtype=float)
        trigger_rate = np.array([row["trigger_rate"] for row in run_metrics], dtype=float)
        fraction_in_band = np.array([row["fraction_in_band"] for row in run_metrics], dtype=float)

        summary = {
            "parameter": "ubi_strength",
            "value": ubi_strength,
            "post_labor": POST_LABOR,
            "analytic_displaced_meaning": analytic["analytic_displaced_meaning"],
            "analytic_mixed_meaning": analytic["analytic_mixed_meaning"],
            "analytic_displaced_autonomy": analytic["analytic_displaced_autonomy"],
            "analytic_displaced_competence": analytic["analytic_displaced_competence"],
            "analytic_displaced_relatedness": analytic["analytic_displaced_relatedness"],
            "analytic_displaced_status": analytic["analytic_displaced_status"],
            "analytic_displaced_economic_role": analytic["analytic_displaced_economic_role"],
            "analytic_mixed_economic_role": analytic["analytic_mixed_economic_role"],
            "equilibrium_meaning_mean": float(equilibrium.mean()),
            "equilibrium_meaning_std": float(equilibrium.std(ddof=0)),
            "trigger_rate_mean": float(trigger_rate.mean()),
            "trigger_rate_std": float(trigger_rate.std(ddof=0)),
            "fraction_in_band_mean": float(fraction_in_band.mean()),
            "fraction_in_band_std": float(fraction_in_band.std(ddof=0)),
            "n_runs": N_RUNS,
            "n_steps": N_STEPS,
            "burn_in": BURN_IN,
        }
        results.append(summary)

        print(
            f"ubi_strength={ubi_strength:.2f} | "
            f"analytic_displaced={summary['analytic_displaced_meaning']:.3f} | "
            f"analytic_mixed={summary['analytic_mixed_meaning']:.3f} | "
            f"empirical={summary['equilibrium_meaning_mean']:.3f} +/- "
            f"{summary['equilibrium_meaning_std']:.3f} | "
            f"trigger={summary['trigger_rate_mean']:.3f} | "
            f"band={summary['fraction_in_band_mean']:.3f}"
        )

    results_df = pd.DataFrame(results)
    results_df.to_csv(OUTPUT_PATH, index=False)
    print("-" * 72)
    print(f"Saved {len(results_df)} rows to {OUTPUT_PATH}")
    return results_df


def main() -> None:
    run_sweep()


if __name__ == "__main__":
    main()
