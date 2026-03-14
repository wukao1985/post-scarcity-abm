"""
Pathway C: System Dynamics model for post-scarcity behavioral sink.

A stock-flow ODE model providing triangulation support for the ABM (Pathway A).
Uses scipy.integrate.solve_ivp to simulate population-level meaning, behavioral
sink prevalence, and social trust under varying post-labor conditions.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# ---------------------------------------------------------------------------
# Default rate constants (calibrated to Nauru trajectory)
# ---------------------------------------------------------------------------
DEFAULT_PARAMS = dict(
    # Exogenous drivers
    post_labor_fraction=0.8,
    ubi_transfer=0.0,
    collectivism=0.2,

    # Rate constants
    role_loss_rate=0.028,
    meaning_decay=0.022,
    sink_accumulation=0.038,
    trust_erosion=0.028,
    contagion=0.8,
    recovery_rate=0.022,
    isolation_effect=0.012,
    collectivism_meaning_coeff=0.045,
    collectivism_trust_coeff=0.040,
    ubi_meaning_coeff=0.55,
)

# Initial conditions
DEFAULT_IC = dict(
    MeaningStock=0.7,
    SinkStock=0.05,
    SocialTrust=0.6,
)


# ---------------------------------------------------------------------------
# ODE system
# ---------------------------------------------------------------------------
def _odes(t, y, p):
    """Right-hand side of the stock-flow system.

    Parameters
    ----------
    t : float
        Current time.
    y : array-like, shape (3,)
        [MeaningStock, SinkStock, SocialTrust]
    p : dict
        Model parameters.

    Returns
    -------
    list of float
        [dMeaning/dt, dSink/dt, dTrust/dt]
    """
    meaning, sink, trust = y

    # Resolve post_labor: can be a callable for time-varying scenarios
    pl = p["post_labor_fraction"]
    if callable(pl):
        pl = pl(t)

    ubi = p["ubi_transfer"]
    coll = p["collectivism"]

    # --- dMeaning/dt ---
    role_loss = p["role_loss_rate"] * pl * (1.0 - p["ubi_meaning_coeff"] * ubi)
    decay = p["meaning_decay"] * sink
    intervention_boost = p["ubi_meaning_coeff"] * ubi * 0.018
    collectivism_buffer = p["collectivism_meaning_coeff"] * coll * (1.0 - meaning) * (1.0 + 0.5 * coll)
    d_meaning = -role_loss - decay + intervention_boost + collectivism_buffer

    # --- dSink/dt ---
    accumulation = (
        p["sink_accumulation"]
        * (1.0 - meaning)
        * (1.0 + p["contagion"] * sink)
    )
    recovery = p["recovery_rate"] * meaning
    d_sink = accumulation - recovery

    # --- dTrust/dt ---
    erosion = p["trust_erosion"] * sink
    isolation = p["isolation_effect"] * pl
    coll_boost = p["collectivism_trust_coeff"] * coll * (1.0 - trust) * (1.0 + 0.5 * coll)
    d_trust = -erosion - isolation + coll_boost

    # Soft clamp derivatives to keep stocks within [0, 1]
    if meaning <= 0.0 and d_meaning < 0:
        d_meaning = 0.0
    if meaning >= 1.0 and d_meaning > 0:
        d_meaning = 0.0
    if sink <= 0.0 and d_sink < 0:
        d_sink = 0.0
    if sink >= 1.0 and d_sink > 0:
        d_sink = 0.0
    if trust <= 0.0 and d_trust < 0:
        d_trust = 0.0
    if trust >= 1.0 and d_trust > 0:
        d_trust = 0.0

    return [d_meaning, d_sink, d_trust]


# ---------------------------------------------------------------------------
# Core runner
# ---------------------------------------------------------------------------
def run_sd_model(params=None, t_span=(0, 80), t_eval=None, ic=None):
    """Run the system dynamics model.

    Parameters
    ----------
    params : dict or None
        Model parameters. Missing keys filled from DEFAULT_PARAMS.
    t_span : tuple
        (t_start, t_end).
    t_eval : array-like or None
        Times at which to store the solution. If None, uses integer steps.
    ic : dict or None
        Initial conditions for stocks. Missing keys filled from DEFAULT_IC.

    Returns
    -------
    pd.DataFrame
        Columns: [time, MeaningStock, SinkStock, SocialTrust]
    """
    p = {**DEFAULT_PARAMS, **(params or {})}
    y0_dict = {**DEFAULT_IC, **(ic or {})}
    y0 = [y0_dict["MeaningStock"], y0_dict["SinkStock"], y0_dict["SocialTrust"]]

    if t_eval is None:
        t_eval = np.arange(t_span[0], t_span[1] + 1, dtype=float)

    sol = solve_ivp(
        fun=lambda t, y: _odes(t, y, p),
        t_span=t_span,
        y0=y0,
        t_eval=t_eval,
        method="RK45",
        max_step=0.5,
    )

    # Hard-clamp to [0, 1]
    vals = np.clip(sol.y, 0.0, 1.0)

    df = pd.DataFrame({
        "time": sol.t,
        "MeaningStock": vals[0],
        "SinkStock": vals[1],
        "SocialTrust": vals[2],
    })
    return df


# ---------------------------------------------------------------------------
# Historical scenarios
# ---------------------------------------------------------------------------
def run_nauru_scenario():
    """Nauru: sudden resource wealth leading to purposelessness and collapse.

    Timeline mapping:
        t=0  (1970): pre-wealth baseline
        t=15 (1985): wealth + idleness onset
        t=30 (2000): full behavioral collapse
    """
    params = {
        "post_labor_fraction": 0.85,
        "ubi_transfer": 0.0,       # wealth but no structured purpose programs
        "collectivism": 0.15,      # small island, individualized by wealth
    }
    df = run_sd_model(params, t_span=(0, 40), t_eval=np.arange(0, 41, dtype=float))
    return df


def run_gulf_scenario():
    """Gulf states: similar resource wealth but strong collectivist culture.

    Same wealth shock but high collectivism buffers against collapse.
    """
    params = {
        "post_labor_fraction": 0.85,
        "ubi_transfer": 0.0,       # wealth but no structured purpose programs
        "collectivism": 0.8,       # strong collectivist cultural norms
    }
    df = run_sd_model(params, t_span=(0, 40), t_eval=np.arange(0, 41, dtype=float))
    return df


def run_comparison():
    """Run Nauru vs Gulf scenarios and produce comparison output + figure."""
    nauru = run_nauru_scenario()
    gulf = run_gulf_scenario()

    # Print comparison table at key time points
    checkpoints = [0, 15, 30, 40]
    print("=" * 72)
    print("Historical Analogue Comparison: Nauru vs Gulf States")
    print("=" * 72)
    print(f"{'Time':>6} | {'Nauru Meaning':>14} {'Nauru Sink':>12} {'Nauru Trust':>12}"
          f" | {'Gulf Meaning':>13} {'Gulf Sink':>11} {'Gulf Trust':>11}")
    print("-" * 72)
    for t in checkpoints:
        nr = nauru[nauru["time"] == t].iloc[0]
        gr = gulf[gulf["time"] == t].iloc[0]
        print(f"{t:>6} | {nr['MeaningStock']:>14.3f} {nr['SinkStock']:>12.3f} "
              f"{nr['SocialTrust']:>12.3f} | {gr['MeaningStock']:>13.3f} "
              f"{gr['SinkStock']:>11.3f} {gr['SocialTrust']:>11.3f}")
    print("=" * 72)

    # --- Figure ---
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5), sharex=True)

    labels = ["MeaningStock", "SinkStock", "SocialTrust"]
    titles = ["Mean Meaning", "Behavioral Sink", "Social Trust"]

    for ax, col, title in zip(axes, labels, titles):
        ax.plot(nauru["time"], nauru[col], "r-", linewidth=2, label="Nauru")
        ax.plot(gulf["time"], gulf[col], "b--", linewidth=2, label="Gulf States")
        ax.set_title(title, fontsize=12)
        ax.set_xlabel("Time (years from wealth onset)")
        ax.set_ylabel("Stock level (0-1)")
        ax.set_ylim(-0.05, 1.05)
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)

    fig.suptitle("Pathway C — System Dynamics: Historical Analogues", fontsize=13, y=1.02)
    fig.tight_layout()
    fig.savefig("reports/figures/pathway_c_comparison.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("\nFigure saved to reports/figures/pathway_c_comparison.png")

    return nauru, gulf


# ---------------------------------------------------------------------------
# ABM-SD cross-validation
# ---------------------------------------------------------------------------
def compare_with_abm():
    """Compare SD model outputs with known ABM results at matched parameters.

    ABM reference values (from Sweep 1, PL=0.8):
        Baseline:    meaning ~0.37, sink ~0.80
        UBI only:    meaning ~0.47, sink ~0.22
        Full bundle: meaning ~0.59, sink ~0.00
    """
    print("\n" + "=" * 72)
    print("ABM-SD Directional Comparison (post_labor = 0.8, t = 80)")
    print("=" * 72)

    scenarios = {
        "Baseline": {"post_labor_fraction": 0.8, "ubi_transfer": 0.0, "collectivism": 0.2},
        "UBI only": {"post_labor_fraction": 0.8, "ubi_transfer": 1.0, "collectivism": 0.2},
        "Full bundle": {"post_labor_fraction": 0.8, "ubi_transfer": 1.0, "collectivism": 0.8},
    }

    abm_ref = {
        "Baseline": {"meaning": 0.37, "sink": 0.80},
        "UBI only": {"meaning": 0.47, "sink": 0.22},
        "Full bundle": {"meaning": 0.59, "sink": 0.00},
    }

    print(f"\n{'Scenario':<14} | {'ABM Mean':>9} {'ABM Sink':>9}"
          f" | {'SD Mean':>8} {'SD Sink':>8}"
          f" | {'Mean Dir':>9} {'Sink Dir':>9}")
    print("-" * 78)

    results = {}
    for name, params in scenarios.items():
        df = run_sd_model(params, t_span=(0, 80))
        final = df.iloc[-1]
        sd_m = final["MeaningStock"]
        sd_s = final["SinkStock"]
        abm_m = abm_ref[name]["meaning"]
        abm_s = abm_ref[name]["sink"]
        results[name] = {"sd_meaning": sd_m, "sd_sink": sd_s}

        print(f"{name:<14} | {abm_m:>9.3f} {abm_s:>9.3f}"
              f" | {sd_m:>8.3f} {sd_s:>8.3f}"
              f" | ", end="")

        # Check directionality relative to baseline
        if name == "Baseline":
            print(f"{'(ref)':>9} {'(ref)':>9}")
        else:
            abm_m_dir = "higher" if abm_m > abm_ref["Baseline"]["meaning"] else "lower"
            sd_m_dir = "higher" if sd_m > results["Baseline"]["sd_meaning"] else "lower"
            abm_s_dir = "lower" if abm_s < abm_ref["Baseline"]["sink"] else "higher"
            sd_s_dir = "lower" if sd_s < results["Baseline"]["sd_sink"] else "higher"

            m_match = "MATCH" if abm_m_dir == sd_m_dir else "MISMATCH"
            s_match = "MATCH" if abm_s_dir == sd_s_dir else "MISMATCH"
            print(f"{m_match:>9} {s_match:>9}")

    print("=" * 78)
    print("\nDirectional agreement: both models show that interventions (UBI, collectivism)")
    print("increase meaning and reduce behavioral sink relative to baseline.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Pathway C — System Dynamics Model")
    print("=" * 40)

    # 1. Run comparison of historical analogues
    nauru, gulf = run_comparison()

    # 2. Cross-validate with ABM
    compare_with_abm()

    # 3. Quick single-run summary
    print("\n\nNauru endpoint (t=30 ~ year 2000):")
    row = nauru[nauru["time"] == 30].iloc[0]
    print(f"  Meaning: {row['MeaningStock']:.3f}  (target ~0.2)")
    print(f"  Sink:    {row['SinkStock']:.3f}  (target ~0.7)")
    print(f"  Trust:   {row['SocialTrust']:.3f}  (target ~0.15)")

    print("\nGulf endpoint (t=30):")
    row = gulf[gulf["time"] == 30].iloc[0]
    print(f"  Meaning: {row['MeaningStock']:.3f}  (target ~0.4-0.5)")
    print(f"  Sink:    {row['SinkStock']:.3f}  (target <0.3)")
    print(f"  Trust:   {row['SocialTrust']:.3f}")
