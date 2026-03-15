"""
Generate V3 Sweep 1 validation report with figures.
"""
import sys
sys.path.insert(0, '/Users/cloud/Documents/claude/post-scarcity-abm')

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

REPORTS_DIR = "reports"
FIGURES_DIR = "reports/figures"
DATA_DIR = "data/simulation"

# Publication-quality figure defaults
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10

# V2 reference data
V2_REFERENCE = {
    ("baseline", 0.80): {"meaning": 0.450, "sink": 0.769, "collapse": 97},
    ("ubi_only", 0.80): {"meaning": 0.581, "sink": 0.336, "collapse": 0},
    ("full_bundle", 0.80): {"meaning": 0.693, "sink": 0.042, "collapse": 0},
    ("full_bundle", 0.95): {"meaning": 0.685, "sink": 0.044, "collapse": 0},
}


def load_sweep_data(path=None):
    path = path or os.path.join(DATA_DIR, "sweep1_results.csv")
    return pd.read_csv(path)


def compute_summary(df):
    summary = df.groupby(["post_labor", "scenario"]).agg(
        meaning_mean=("meaning_index", "mean"),
        meaning_std=("meaning_index", "std"),
        sink_mean=("sink_index", "mean"),
        sink_std=("sink_index", "std"),
        collapse_prob=("sink_collapsed", "mean"),
        birth_intention=("birth_intention", "mean"),
        social_trust=("social_trust", "mean"),
        n_runs=("run_id", "count"),
    ).reset_index()
    summary["collapse_prob"] *= 100
    return summary


def plot_phase_transition(summary):
    """Plot meaning and sink vs post-labor fraction for all scenarios."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    scenarios = summary["scenario"].unique()
    colors = {"baseline": "#d62728", "ubi_only": "#2ca02c", "roles_only": "#9467bd",
              "fairness_only": "#ff7f0e", "full_bundle": "#1f77b4"}

    for scenario in scenarios:
        sub = summary[summary["scenario"] == scenario]
        color = colors.get(scenario, "gray")

        axes[0].plot(sub["post_labor"], sub["meaning_mean"], "o-",
                     label=scenario, color=color, markersize=5)
        axes[0].fill_between(sub["post_labor"],
                             sub["meaning_mean"] - sub["meaning_std"],
                             sub["meaning_mean"] + sub["meaning_std"],
                             alpha=0.15, color=color)

        axes[1].plot(sub["post_labor"], sub["sink_mean"], "o-",
                     label=scenario, color=color, markersize=5)

    # V2 reference points
    for (scen, pl), v2 in V2_REFERENCE.items():
        axes[0].scatter([pl], [v2["meaning"]], marker="x", s=100, c="black", zorder=5)
        axes[1].scatter([pl], [v2["sink"]], marker="x", s=100, c="black", zorder=5)

    axes[0].set_xlabel("Post-Labor Fraction")
    axes[0].set_ylabel("Mean Meaning Index")
    axes[0].set_title("Meaning vs. Automation Level")
    axes[0].legend(fontsize=8)
    axes[0].set_ylim(0, 1)
    axes[0].axhline(y=0.45, color="gray", linestyle="--", alpha=0.5, label="V2 baseline threshold")
    axes[0].grid(True, alpha=0.3)

    axes[1].set_xlabel("Post-Labor Fraction")
    axes[1].set_ylabel("Sink Index")
    axes[1].set_title("Behavioral Sink vs. Automation Level")
    axes[1].legend(fontsize=8)
    axes[1].set_ylim(0, 1)
    axes[1].axhline(y=0.7, color="red", linestyle="--", alpha=0.5, label="Collapse threshold")
    axes[1].grid(True, alpha=0.3)

    plt.suptitle("V3 Sweep 1: Phase Transition Curves (V2 Replication)", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "sweep1_phase_transition.png"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()


def plot_collapse_probability(summary):
    """Plot collapse probability vs post-labor for all scenarios."""
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = {"baseline": "#d62728", "ubi_only": "#2ca02c", "roles_only": "#9467bd",
              "fairness_only": "#ff7f0e", "full_bundle": "#1f77b4"}

    for scenario in summary["scenario"].unique():
        sub = summary[summary["scenario"] == scenario]
        ax.plot(sub["post_labor"], sub["collapse_prob"], "o-",
                label=scenario, color=colors.get(scenario, "gray"), markersize=5)

    ax.set_xlabel("Post-Labor Fraction")
    ax.set_ylabel("Collapse Probability (%)")
    ax.set_title("Collapse Probability vs. Automation Level")
    ax.legend()
    ax.set_ylim(-5, 105)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "sweep1_collapse_prob.png"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()


def plot_scenario_comparison(summary):
    """Bar chart comparing scenarios at 80% post-labor."""
    sub = summary[summary["post_labor"] == 0.8].copy()
    if sub.empty:
        return

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    metrics = [
        ("meaning_mean", "Mean Meaning Index", axes[0]),
        ("sink_mean", "Sink Index", axes[1]),
        ("collapse_prob", "Collapse Probability (%)", axes[2]),
    ]

    colors = {"baseline": "#d62728", "ubi_only": "#2ca02c", "roles_only": "#9467bd",
              "fairness_only": "#ff7f0e", "full_bundle": "#1f77b4"}
    bar_colors = [colors.get(s, "gray") for s in sub["scenario"]]

    for metric, ylabel, ax in metrics:
        bars = ax.bar(range(len(sub)), sub[metric], color=bar_colors)
        ax.set_xticks(range(len(sub)))
        ax.set_xticklabels(sub["scenario"], rotation=45, ha="right", fontsize=8)
        ax.set_ylabel(ylabel)
        ax.grid(True, alpha=0.3, axis="y")

    plt.suptitle("Scenario Comparison at 80% Post-Labor", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "sweep1_scenario_comparison.png"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()


def plot_v2_comparison(summary):
    """Direct comparison table: V3 vs V2 at key points."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis("off")

    headers = ["Scenario", "Post-Labor", "V3 Meaning", "V2 Meaning", "V3 Sink", "V2 Sink", "V3 Collapse%", "V2 Collapse%"]
    rows = []
    for (scen, pl), v2 in sorted(V2_REFERENCE.items()):
        v3 = summary[(summary["scenario"] == scen) & (summary["post_labor"] == pl)]
        if not v3.empty:
            v3 = v3.iloc[0]
            rows.append([
                scen, f"{pl:.2f}",
                f"{v3['meaning_mean']:.3f}", f"{v2['meaning']:.3f}",
                f"{v3['sink_mean']:.3f}", f"{v2['sink']:.3f}",
                f"{v3['collapse_prob']:.0f}%", f"{v2['collapse']:.0f}%",
            ])

    table = ax.table(cellText=rows, colLabels=headers, loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 1.5)
    for i in range(len(headers)):
        table[0, i].set_facecolor("#4472C4")
        table[0, i].set_text_props(color="white", fontweight="bold")

    plt.title("V3 vs V2 Comparison at Key Parameter Points", fontsize=14, fontweight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "sweep1_v2_comparison.png"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()


def generate_report():
    os.makedirs(FIGURES_DIR, exist_ok=True)
    os.makedirs(REPORTS_DIR, exist_ok=True)

    print("Loading sweep data...")
    df = load_sweep_data()
    summary = compute_summary(df)

    print("Generating figures...")
    plot_phase_transition(summary)
    plot_collapse_probability(summary)
    plot_scenario_comparison(summary)
    plot_v2_comparison(summary)

    # Save summary CSV
    summary.to_csv(os.path.join(DATA_DIR, "sweep1_summary.csv"), index=False)

    # Print key results
    print("\n" + "=" * 70)
    print("V3 SWEEP 1 VALIDATION RESULTS")
    print("=" * 70)

    key = summary[
        summary["post_labor"].isin([0.0, 0.5, 0.8, 0.95]) &
        summary["scenario"].isin(["baseline", "ubi_only", "full_bundle"])
    ].sort_values(["post_labor", "scenario"])

    print(f"\n{'Scenario':<15} {'PL':>5} {'Meaning':>8} {'Sink':>8} {'Collapse':>10}")
    print("-" * 50)
    for _, row in key.iterrows():
        print(f"{row['scenario']:<15} {row['post_labor']:>5.2f} "
              f"{row['meaning_mean']:>8.3f} {row['sink_mean']:>8.3f} "
              f"{row['collapse_prob']:>9.0f}%")

    print("\n--- V2 Reference ---")
    for (scen, pl), v2 in sorted(V2_REFERENCE.items()):
        print(f"{scen:<15} {pl:>5.2f} {v2['meaning']:>8.3f} {v2['sink']:>8.3f} {v2['collapse']:>9.0f}%")

    print(f"\nFigures saved to {FIGURES_DIR}/")
    print(f"Summary saved to {DATA_DIR}/sweep1_summary.csv")
    print("=" * 70)


if __name__ == "__main__":
    generate_report()
