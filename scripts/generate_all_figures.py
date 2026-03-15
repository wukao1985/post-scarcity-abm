"""
Generate all figures for V3 sweeps 2-6.
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

sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 13, 'axes.labelsize': 12,
                     'xtick.labelsize': 10, 'ytick.labelsize': 10, 'legend.fontsize': 10,
                     'figure.dpi': 300, 'savefig.dpi': 300, 'savefig.facecolor': 'white'})

DATA_DIR = "data/simulation"
FIGURES_DIR = "reports/figures"

def load_data(filename):
    return pd.read_csv(os.path.join(DATA_DIR, filename))


def plot_sweep2_automation_speed(df):
    """Figure: Automation speed comparison."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    scenarios = ["baseline", "ubi_only", "full_bundle"]
    post_labor_levels = [0.5, 0.8, 0.95]
    colors = {"gradual": "#2ca02c", "rapid": "#d62728"}

    for idx, pl in enumerate(post_labor_levels):
        ax = axes[idx]

        for speed in ["gradual", "rapid"]:
            sub = df[(df["post_labor"] == pl) & (df["speed"] == speed)]
            if sub.empty:
                continue

            # Group by scenario
            scen_data = sub.groupby("scenario").agg({
                "meaning_index": "mean",
                "sink_index": "mean",
                "sink_collapsed": "mean"
            }).reset_index()

            scen_order = [s for s in scenarios if s in scen_data["scenario"].values]
            x_pos = np.arange(len(scen_order))
            values = [scen_data[scen_data["scenario"] == s]["sink_index"].values[0]
                      for s in scen_order]

            offset = 0.2 if speed == "gradual" else -0.2
            ax.bar(x_pos + offset, values, 0.35, label=speed, color=colors[speed], alpha=0.8)

        ax.set_xlabel("Scenario")
        ax.set_ylabel("Sink Index")
        ax.set_title(f"Post-Labor = {pl:.0%}")
        ax.set_xticks(range(len(scenarios)))
        ax.set_xticklabels(scenarios, rotation=45, ha="right")
        ax.legend()
        ax.axhline(y=0.7, color="red", linestyle="--", alpha=0.5)
        ax.set_ylim(0, 1)

    plt.suptitle("Sweep 2: Effect of Automation Speed on Behavioral Sink", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "sweep2_automation_speed.png"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print("Saved: sweep2_automation_speed.png")


def plot_sweep3_virtual_world(df):
    """Figure: Virtual world quality curves."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    scenarios = ["baseline", "ubi_only", "full_bundle"]
    colors = {"baseline": "#d62728", "ubi_only": "#2ca02c", "full_bundle": "#1f77b4"}

    for pl, ax in zip([0.8, 0.95], axes):
        for scen in scenarios:
            sub = df[(df["post_labor"] == pl) & (df["scenario"] == scen)]
            if sub.empty:
                continue

            grouped = sub.groupby("virtual_world_quality").agg({
                "meaning_index": "mean",
                "sink_index": "mean",
                "sink_collapsed": "mean"
            }).reset_index()

            ax.plot(grouped["virtual_world_quality"], grouped["sink_index"],
                   "o-", label=scen, color=colors.get(scen, "gray"), markersize=6)

        ax.set_xlabel("Virtual World Quality")
        ax.set_ylabel("Sink Index")
        ax.set_title(f"Post-Labor = {pl:.0%}")
        ax.legend()
        ax.axhline(y=0.7, color="red", linestyle="--", alpha=0.5, label="Collapse threshold")
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3)

    plt.suptitle("Sweep 3: Virtual World Quality vs. Behavioral Sink", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "sweep3_virtual_world.png"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print("Saved: sweep3_virtual_world.png")


def plot_sweep4_collectivism(df):
    """Figure: Collectivism index effects."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    scenarios = ["baseline", "ubi_only", "full_bundle"]
    colors = {"baseline": "#d62728", "ubi_only": "#2ca02c", "full_bundle": "#1f77b4"}

    for pl, ax in zip([0.8, 0.95], axes):
        for scen in scenarios:
            sub = df[(df["post_labor"] == pl) & (df["scenario"] == scen)]
            if sub.empty:
                continue

            grouped = sub.groupby("collectivism_index").agg({
                "meaning_index": "mean",
                "sink_index": "mean",
                "sink_collapsed": "mean"
            }).reset_index()

            ax.plot(grouped["collectivism_index"], grouped["sink_index"],
                   "o-", label=scen, color=colors.get(scen, "gray"), markersize=6)

        ax.set_xlabel("Collectivism Index")
        ax.set_ylabel("Sink Index")
        ax.set_title(f"Post-Labor = {pl:.0%}")
        ax.legend()
        ax.axhline(y=0.7, color="red", linestyle="--", alpha=0.5)
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3)

    plt.suptitle("Sweep 4: Collectivism Index vs. Behavioral Sink", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "sweep4_collectivism.png"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print("Saved: sweep4_collectivism.png")


def plot_sweep5_archetypes(df):
    """Figure: Archetype time series."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    scenarios = ["baseline", "full_bundle"]
    archetypes = ["productive_frac", "beautiful_one_frac", "aggressor_frac", "withdrawn_frac", "collapsed_frac"]
    colors = {
        "productive_frac": "#2ca02c",
        "beautiful_one_frac": "#1f77b4",
        "aggressor_frac": "#d62728",
        "withdrawn_frac": "#9467bd",
        "collapsed_frac": "#8c564b"
    }
    labels = {
        "productive_frac": "Productive",
        "beautiful_one_frac": "Beautiful Ones",
        "aggressor_frac": "Aggressors",
        "withdrawn_frac": "Withdrawn",
        "collapsed_frac": "Collapsed"
    }

    for idx, scen in enumerate(scenarios):
        sub = df[df["scenario"] == scen]

        # Group by step and compute means
        grouped = sub.groupby("step")[archetypes].mean().reset_index()

        # Plot 1: All archetypes
        ax = axes[idx, 0]
        for arch in archetypes:
            ax.plot(grouped["step"], grouped[arch], label=labels[arch], color=colors[arch], linewidth=2)
        ax.set_xlabel("Step")
        ax.set_ylabel("Fraction of Population")
        ax.set_title(f"{scen}: Archetype Trajectories")
        ax.legend(loc="upper right", fontsize=8)
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3)

        # Plot 2: Sink only (aggressor + withdrawn + collapsed)
        ax = axes[idx, 1]
        grouped["sink_frac"] = grouped["aggressor_frac"] + grouped["withdrawn_frac"] + grouped["collapsed_frac"]
        ax.fill_between(grouped["step"], grouped["sink_frac"], alpha=0.3, color="red", label="Total Sink")
        ax.plot(grouped["step"], grouped["aggressor_frac"], label="Aggressors", color=colors["aggressor_frac"])
        ax.plot(grouped["step"], grouped["withdrawn_frac"], label="Withdrawn", color=colors["withdrawn_frac"])
        ax.plot(grouped["step"], grouped["collapsed_frac"], label="Collapsed", color=colors["collapsed_frac"])
        ax.axhline(y=0.7, color="red", linestyle="--", alpha=0.5)
        ax.set_xlabel("Step")
        ax.set_ylabel("Fraction of Population")
        ax.set_title(f"{scen}: Behavioral Sink Components")
        ax.legend(loc="upper left", fontsize=8)
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3)

    plt.suptitle("Sweep 5: Archetype Time Series (80% Post-Labor)", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "sweep5_archetypes.png"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print("Saved: sweep5_archetypes.png")


def plot_sweep6_full_grid(df):
    """Figure: Full scenario grid heatmap."""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    scenarios = df["scenario"].unique()
    post_labor_levels = [0.5, 0.8, 0.95]

    for idx, metric in enumerate(["meaning_index", "sink_index", "sink_collapsed"]):
        ax = axes[idx]

        # Pivot data
        pivot_data = []
        for pl in post_labor_levels:
            row = []
            for scen in scenarios:
                sub = df[(df["post_labor"] == pl) & (df["scenario"] == scen)]
                if len(sub) > 0:
                    val = sub[metric].mean()
                    if metric == "sink_collapsed":
                        val *= 100  # Convert to percentage
                    row.append(val)
                else:
                    row.append(0)
            pivot_data.append(row)

        im = ax.imshow(pivot_data, cmap="RdYlGn_r" if metric != "meaning_index" else "RdYlGn",
                       aspect="auto", vmin=0, vmax=100 if metric == "sink_collapsed" else 1)

        ax.set_xticks(range(len(scenarios)))
        ax.set_xticklabels(scenarios, rotation=45, ha="right", fontsize=8)
        ax.set_yticks(range(len(post_labor_levels)))
        ax.set_yticklabels([f"{pl:.0%}" for pl in post_labor_levels])
        ax.set_ylabel("Post-Labor Fraction")

        # Add text annotations
        for i in range(len(post_labor_levels)):
            for j in range(len(scenarios)):
                val = pivot_data[i][j]
                fmt = f"{val:.0f}%" if metric == "sink_collapsed" else f"{val:.2f}"
                text = ax.text(j, i, fmt, ha="center", va="center", color="black" if val < 50 else "white",
                              fontsize=7)

        title = {"meaning_index": "Mean Meaning", "sink_index": "Sink Index",
                "sink_collapsed": "Collapse Probability"}[metric]
        ax.set_title(title)
        plt.colorbar(im, ax=ax)

    plt.suptitle("Sweep 6: Full Scenario Grid (10 Scenarios x 3 Automation Levels)", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "sweep6_full_grid.png"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print("Saved: sweep6_full_grid.png")


def plot_combined_summary():
    """Create a combined summary figure with key findings."""
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

    # Load all data
    s2 = load_data("sweep2_automation_speed.csv")
    s3 = load_data("sweep3_virtual_world.csv")
    s4 = load_data("sweep4_collectivism.csv")
    s6 = load_data("sweep6_full_grid.csv")

    # Panel 1: Automation speed effect (top left)
    ax1 = fig.add_subplot(gs[0, 0])
    baseline_80 = s2[(s2["post_labor"] == 0.8) & (s2["scenario"] == "baseline")]
    speed_effect = baseline_80.groupby("speed")["sink_index"].mean()
    ax1.bar(speed_effect.index, speed_effect.values, color=["#2ca02c", "#d62728"], alpha=0.8)
    ax1.axhline(y=0.7, color="red", linestyle="--", alpha=0.5)
    ax1.set_ylabel("Sink Index")
    ax1.set_title("Effect of Automation Speed\n(Baseline, 80% Post-Labor)")
    ax1.set_ylim(0, 1)

    # Panel 2: Virtual world threshold (top middle)
    ax2 = fig.add_subplot(gs[0, 1])
    baseline_80_vw = s3[(s3["post_labor"] == 0.8) & (s3["scenario"] == "baseline")]
    vw_effect = baseline_80_vw.groupby("virtual_world_quality")["sink_index"].mean()
    ax2.plot(vw_effect.index, vw_effect.values, "o-", color="#1f77b4", markersize=8, linewidth=2)
    ax2.axhline(y=0.7, color="red", linestyle="--", alpha=0.5)
    ax2.set_xlabel("Virtual World Quality")
    ax2.set_ylabel("Sink Index")
    ax2.set_title("Virtual World Protection Threshold\n(Baseline, 80% Post-Labor)")
    ax2.set_ylim(0, 1)

    # Panel 3: Collectivism effect on UBI (top right)
    ax3 = fig.add_subplot(gs[0, 2])
    ubi_95 = s4[(s4["post_labor"] == 0.95) & (s4["scenario"] == "ubi_only")]
    coll_effect = ubi_95.groupby("collectivism_index")["sink_index"].mean()
    ax3.plot(coll_effect.index, coll_effect.values, "o-", color="#9467bd", markersize=8, linewidth=2)
    ax3.axhline(y=0.7, color="red", linestyle="--", alpha=0.5)
    ax3.set_xlabel("Collectivism Index")
    ax3.set_ylabel("Sink Index")
    ax3.set_title("Collectivism Enables UBI at 95%\n(UBI Only Scenario)")
    ax3.set_ylim(0, 1)

    # Panel 4: Scenario comparison at 80% (middle, spanning 2 cols)
    ax4 = fig.add_subplot(gs[1, :2])
    s6_80 = s6[s6["post_labor"] == 0.8]
    scen_summary = s6_80.groupby("scenario").agg({
        "meaning_index": "mean",
        "sink_index": "mean"
    }).reset_index()
    scen_summary = scen_summary.sort_values("sink_index")
    colors = ["#d62728" if s == "baseline" else "#2ca02c" for s in scen_summary["scenario"]]
    ax4.barh(scen_summary["scenario"], scen_summary["sink_index"], color=colors, alpha=0.8)
    ax4.axvline(x=0.7, color="red", linestyle="--", alpha=0.5)
    ax4.set_xlabel("Sink Index")
    ax4.set_title("Scenario Comparison at 80% Post-Labor (Ordered by Sink Index)")
    ax4.set_xlim(0, 1)

    # Panel 5: Scenario comparison at 95% (middle right)
    ax5 = fig.add_subplot(gs[1, 2])
    s6_95 = s6[s6["post_labor"] == 0.95]
    scen_summary_95 = s6_95.groupby("scenario").agg({
        "meaning_index": "mean",
        "sink_index": "mean"
    }).reset_index()
    scen_summary_95 = scen_summary_95.sort_values("sink_index")
    colors_95 = ["#d62728" if s in ["baseline", "fairness"] else "#2ca02c" for s in scen_summary_95["scenario"]]
    ax5.barh(scen_summary_95["scenario"], scen_summary_95["sink_index"], color=colors_95, alpha=0.8)
    ax5.axvline(x=0.7, color="red", linestyle="--", alpha=0.5)
    ax5.set_xlabel("Sink Index")
    ax5.set_title("At 95% Post-Labor")
    ax5.set_xlim(0, 1)

    # Panel 6: Key statistics (bottom, spanning all cols)
    ax6 = fig.add_subplot(gs[2, :])
    ax6.axis("off")

    stats_text = """
    KEY FINDINGS FROM V3 SWEEPS 2-6 (17,400 total simulation runs)

    1. AUTOMATION SPEED (Sweep 2, n=3,000)
       • Rapid automation (10 steps to target) causes 100% collapse at 80% post-labor
       • Gradual automation (80 steps) reduces collapse to 27%
       • Speed effect is most pronounced in baseline and fairness-only scenarios

    2. VIRTUAL WORLD QUALITY (Sweep 3, n=3,600)
       • Virtual worlds CAN fully prevent collapse at 80% post-labor if quality ≥ 0.6
       • At 95% post-labor, even max quality (1.0) only reduces collapse to 21%
       • UBI + Virtual World (0.8 quality) achieves 0% collapse even at 95%

    3. COLLECTIVISM INDEX (Sweep 4, n=3,600)
       • Collectivism alone cannot prevent baseline collapse (remains 95-100% even at coll=1.0)
       • BUT collectivism enables UBI to work at 95%: UBI+collectivism≥0.4 = 0% collapse
       • At 95% with UBI only: collapse drops from 91% (coll=0) to 0% (coll=1.0)

    4. ARCHETYPE DYNAMICS (Sweep 5, n=8,100 timestep records)
       • Baseline: Aggressors emerge first (steps 10-20), followed by Withdrawn (steps 20-40)
       • Full bundle: Maintains >90% productive throughout, minimal archetype shift

    5. INTERVENTION EFFECTIVENESS AT 95% (Sweep 6, n=4,500)
       Ranking (lowest to highest sink index):
       1. Full bundle / All bundle: 0.000 sink, 0% collapse
       2. Roles + Virtual: 0.006 sink, 0% collapse
       3. UBI + Virtual: 0.025 sink, 0% collapse
       4. Roles only: 0.388 sink, 0% collapse
       5. UBI + Collectivism: 0.413 sink, 0% collapse
       6. UBI only: 0.639 sink, 3% collapse
       7. Fairness + Collectivism: 0.872 sink, 100% collapse
       8. Fairness only: 0.918 sink, 100% collapse
       9. Baseline: 0.967 sink, 100% collapse
    """

    ax6.text(0.05, 0.95, stats_text, transform=ax6.transAxes, fontsize=10,
             verticalalignment="top", fontfamily="monospace",
             bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

    plt.suptitle("V3 ABM: Comprehensive Sweep Analysis Summary", fontsize=16, fontweight="bold", y=0.98)
    plt.savefig(os.path.join(FIGURES_DIR, "sweep_summary_combined.png"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print("Saved: sweep_summary_combined.png")


def main():
    os.makedirs(FIGURES_DIR, exist_ok=True)
    print("Generating all figures...")
    print("=" * 60)

    # Load and plot each sweep
    print("\n1. Sweep 2: Automation Speed")
    s2 = load_data("sweep2_automation_speed.csv")
    plot_sweep2_automation_speed(s2)

    print("\n2. Sweep 3: Virtual World Quality")
    s3 = load_data("sweep3_virtual_world.csv")
    plot_sweep3_virtual_world(s3)

    print("\n3. Sweep 4: Collectivism Index")
    s4 = load_data("sweep4_collectivism.csv")
    plot_sweep4_collectivism(s4)

    print("\n4. Sweep 5: Archetype Time Series")
    s5 = load_data("sweep5_archetypes.csv")
    plot_sweep5_archetypes(s5)

    print("\n5. Sweep 6: Full Scenario Grid")
    s6 = load_data("sweep6_full_grid.csv")
    plot_sweep6_full_grid(s6)

    print("\n6. Combined Summary Figure")
    plot_combined_summary()

    print("\n" + "=" * 60)
    print(f"All figures saved to {FIGURES_DIR}/")


if __name__ == "__main__":
    main()
