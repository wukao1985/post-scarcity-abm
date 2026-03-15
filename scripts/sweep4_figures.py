"""Sweep 4 Analysis: Collectivism Index Effects"""
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
plt.rcParams['savefig.facecolor'] = 'white'

df = pd.read_csv('data/simulation/sweep4_collectivism.csv')

# ============================================================
# Figure 1: Collectivism effect on key metrics
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
            grouped = subset.groupby('collectivism_index')[metric].agg(['mean', 'sem'])
            ci95 = grouped['sem'] * 1.96
            marker = 'o' if pl == 0.8 else 's'
            alpha = 1.0 if pl == 0.8 else 0.6
            ax.errorbar(grouped.index, grouped['mean'], yerr=ci95,
                       label=f"{sc} (PL={pl})", marker=marker, color=color,
                       linestyle=ls, alpha=alpha, capsize=3, linewidth=2, markersize=6)
    ax.set_xlabel('Collectivism Index')
    ax.set_ylabel(label)
    ax.set_title(label)

axes[2].legend(fontsize=7, loc='upper right')
fig.suptitle('Effect of Collectivism Index on Post-Labor Outcomes', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep4_collectivism_curves.png', bbox_inches='tight')
plt.close()
print("Figure 1 saved")

# ============================================================
# Figure 2: UBI collapse rate vs collectivism (key finding)
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

ubi_95 = df[(df['scenario'] == 'ubi_only') & (df['post_labor'] == 0.95)]
grouped = ubi_95.groupby('collectivism_index').agg(
    collapse=('sink_collapsed', 'mean'),
    sink=('sink_index', 'mean'),
    meaning=('meaning_index', 'mean')
)

ax2 = ax.twinx()
bars = ax.bar(grouped.index, grouped['collapse'], width=0.15, color='#F44336', alpha=0.7, label='Collapse Rate')
ax2.plot(grouped.index, grouped['sink'], 's-', color='#FF9800', linewidth=2, markersize=8, label='Sink Index')
ax2.plot(grouped.index, grouped['meaning'], 'o--', color='#2196F3', linewidth=2, markersize=8, label='Meaning')

ax.set_xlabel('Collectivism Index')
ax.set_ylabel('Collapse Rate', color='#F44336')
ax2.set_ylabel('Index Value')
ax.set_ylim(0, 1.1)
ax2.set_ylim(0, 1.0)

# Annotate key values
for i, (idx, row) in enumerate(grouped.iterrows()):
    if row['collapse'] > 0:
        ax.annotate(f"{row['collapse']:.0%}", (idx, row['collapse'] + 0.03), ha='center', fontsize=10)

lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=10, loc='center right')

ax.set_title('UBI Effectiveness Depends on Social Cohesion\n(Post-Labor = 0.95)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep4_ubi_collectivism_interaction.png', bbox_inches='tight')
plt.close()
print("Figure 2 saved")

# ============================================================
# Figure 3: Heatmap - Collectivism × Scenario
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax_i, pl in enumerate([0.8, 0.95]):
    ax = axes[ax_i]
    subset = df[df['post_labor'] == pl]
    pivot = subset.groupby(['collectivism_index', 'scenario'])['sink_index'].mean().unstack()
    pivot = pivot[['baseline', 'ubi_only', 'full_bundle']]
    sns.heatmap(pivot, annot=True, fmt='.3f', cmap='RdYlGn_r', ax=ax)
    ax.set_title(f'Sink Index (PL={pl})')
    ax.set_ylabel('Collectivism Index')

fig.suptitle('Collectivism × Scenario Interaction on Sink Index', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep4_collectivism_heatmap.png', bbox_inches='tight')
plt.close()
print("Figure 3 saved")

# ============================================================
# Figure 4: Baseline - collectivism barely helps without policy
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

for pl, marker, color in [(0.8, 'o', '#F44336'), (0.95, 's', '#FF5722')]:
    baseline = df[(df['scenario'] == 'baseline') & (df['post_labor'] == pl)]
    grouped = baseline.groupby('collectivism_index')['sink_index'].agg(['mean', 'sem'])
    ci95 = grouped['sem'] * 1.96
    ax.errorbar(grouped.index, grouped['mean'], yerr=ci95,
               label=f'Baseline PL={pl}', marker=marker, color=color,
               capsize=4, linewidth=2, markersize=8)

    ubi = df[(df['scenario'] == 'ubi_only') & (df['post_labor'] == pl)]
    grouped_u = ubi.groupby('collectivism_index')['sink_index'].agg(['mean', 'sem'])
    ci95_u = grouped_u['sem'] * 1.96
    ax.errorbar(grouped_u.index, grouped_u['mean'], yerr=ci95_u,
               label=f'UBI PL={pl}', marker=marker, color='#2196F3',
               linestyle='--', capsize=4, linewidth=2, markersize=8)

ax.axhline(y=0.7, color='gray', linestyle=':', label='Collapse threshold')
ax.set_xlabel('Collectivism Index')
ax.set_ylabel('Sink Index')
ax.set_title('Collectivism: Modest Direct Effect, Strong UBI Interaction',
             fontweight='bold')
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig('reports/figures/sweep4_baseline_vs_ubi.png', bbox_inches='tight')
plt.close()
print("Figure 4 saved")

print("\nDone!")
