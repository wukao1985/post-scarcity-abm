"""Sweep 3 Analysis: Virtual World Quality Effects"""
import sys
sys.path.insert(0, '/Users/cloud/Documents/claude/post-scarcity-abm')
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", font_scale=1.1)
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300

df = pd.read_csv('data/simulation/sweep3_virtual_world.csv')

# ============================================================
# Figure 1: VW Quality Effect on Key Metrics (line plots)
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

for i, (metric, label) in enumerate([
    ('meaning_index', 'Mean Meaning Index'),
    ('sink_index', 'Mean Sink Index'),
    ('sink_collapsed', 'Collapse Rate')
]):
    ax = axes[i]
    for pl in [0.8, 0.95]:
        for sc, color, ls in [('baseline', '#F44336', '-'), ('ubi_only', '#2196F3', '--'), ('full_bundle', '#4CAF50', ':')]:
            subset = df[(df['post_labor'] == pl) & (df['scenario'] == sc)]
            grouped = subset.groupby('virtual_world_quality')[metric].agg(['mean', 'sem'])
            ci95 = grouped['sem'] * 1.96
            marker = 'o' if pl == 0.8 else 's'
            alpha = 1.0 if pl == 0.8 else 0.6
            lbl = f"{sc} (PL={pl})"
            ax.errorbar(grouped.index, grouped['mean'], yerr=ci95, label=lbl,
                       marker=marker, color=color, linestyle=ls, alpha=alpha,
                       capsize=3, linewidth=2, markersize=6)
    ax.set_xlabel('Virtual World Quality')
    ax.set_ylabel(label)
    ax.set_title(label)

axes[0].legend(fontsize=7, loc='upper left')
fig.suptitle('Effect of Virtual World Quality on Post-Labor Outcomes', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep3_vw_quality_curves.png', bbox_inches='tight')
plt.close()
print("Figure 1 saved")

# ============================================================
# Figure 2: VW as substitute — baseline collapse threshold
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax_i, pl in enumerate([0.8, 0.95]):
    ax = axes[ax_i]
    baseline = df[(df['post_labor'] == pl) & (df['scenario'] == 'baseline')]
    grouped = baseline.groupby('virtual_world_quality').agg(
        collapse=('sink_collapsed', 'mean'),
        sink=('sink_index', 'mean'),
        meaning=('meaning_index', 'mean')
    )

    ax2 = ax.twinx()
    ax.bar(grouped.index, grouped['collapse'], width=0.15, color='#F44336', alpha=0.7, label='Collapse Rate')
    ax2.plot(grouped.index, grouped['meaning'], 'o-', color='#2196F3', linewidth=2, markersize=8, label='Meaning')
    ax2.plot(grouped.index, grouped['sink'], 's--', color='#FF9800', linewidth=2, markersize=8, label='Sink Index')

    ax.set_xlabel('Virtual World Quality')
    ax.set_ylabel('Collapse Rate', color='#F44336')
    ax2.set_ylabel('Index Value', color='#2196F3')
    ax.set_title(f'Baseline at PL={pl}')
    ax.set_ylim(0, 1.1)
    ax2.set_ylim(0, 1.05)

    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='center left')

fig.suptitle('Virtual Worlds as Role Substitution (Baseline, No Policy)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep3_vw_collapse_threshold.png', bbox_inches='tight')
plt.close()
print("Figure 2 saved")

# ============================================================
# Figure 3: Marginal value of VW by scenario (heatmap)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax_i, metric in enumerate(['meaning_index', 'sink_index']):
    ax = axes[ax_i]
    pivot = df.groupby(['virtual_world_quality', 'scenario'])[metric].mean().unstack()
    # Take only PL=0.8 for clarity
    subset = df[df['post_labor'] == 0.8]
    pivot = subset.groupby(['virtual_world_quality', 'scenario'])[metric].mean().unstack()
    pivot = pivot[['baseline', 'ubi_only', 'full_bundle']]

    cmap = 'RdYlGn' if metric == 'meaning_index' else 'RdYlGn_r'
    sns.heatmap(pivot, annot=True, fmt='.3f', cmap=cmap, ax=ax)

    title = 'Meaning' if metric == 'meaning_index' else 'Sink'
    ax.set_title(f'{title} Index by VW Quality × Scenario (PL=0.8)')
    ax.set_ylabel('Virtual World Quality')

fig.suptitle('Interaction of Virtual World Quality with Policy Scenarios',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep3_vw_scenario_heatmap.png', bbox_inches='tight')
plt.close()
print("Figure 3 saved")

# ============================================================
# Figure 4: Diminishing returns of VW quality
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

for sc, color, marker in [('baseline', '#F44336', 'o'), ('ubi_only', '#2196F3', 's')]:
    for pl in [0.8, 0.95]:
        subset = df[(df['post_labor'] == pl) & (df['scenario'] == sc)]
        grouped = subset.groupby('virtual_world_quality')['meaning_index'].mean()
        # Marginal gain
        marginal = grouped.diff()
        ls = '-' if pl == 0.8 else '--'
        alpha = 1.0 if pl == 0.8 else 0.6
        ax.plot(marginal.index[1:], marginal.values[1:], f'{marker}{ls}',
               color=color, alpha=alpha, linewidth=2, markersize=8,
               label=f'{sc} (PL={pl})')

ax.axhline(y=0, color='gray', linestyle=':', linewidth=0.5)
ax.set_xlabel('Virtual World Quality')
ax.set_ylabel('Marginal Meaning Gain (per +0.2 VW)')
ax.set_title('Diminishing Returns of Virtual World Quality Investment',
             fontweight='bold')
ax.legend()
plt.tight_layout()
plt.savefig('reports/figures/sweep3_vw_marginal_returns.png', bbox_inches='tight')
plt.close()
print("Figure 4 saved")

print("\nDone! All sweep3 figures saved.")
