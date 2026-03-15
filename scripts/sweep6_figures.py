"""Sweep 6 Analysis: Full 10-Scenario Grid"""
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

df = pd.read_csv('data/simulation/sweep6_full_grid.csv')

scenario_order = ['baseline', 'fairness', 'fairness+collectivism', 'ubi_only',
                  'UBI+collectivism', 'roles', 'UBI+virtual', 'roles+virtual',
                  'full_bundle', 'all_bundle']
scenario_labels = ['Baseline', 'Fairness', 'Fair+Coll', 'UBI',
                   'UBI+Coll', 'Roles', 'UBI+VW', 'Roles+VW',
                   'Full Bundle', 'All Bundle']

# ============================================================
# Figure 1: Grand Comparison Heatmap
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 7))

for ax_i, (metric, label, cmap) in enumerate([
    ('meaning_index', 'Meaning Index', 'RdYlGn'),
    ('sink_index', 'Sink Index', 'RdYlGn_r'),
    ('sink_collapsed', 'Collapse Rate', 'RdYlGn_r')
]):
    ax = axes[ax_i]
    pivot = df.groupby(['scenario', 'post_labor'])[metric].mean().unstack()
    pivot = pivot.reindex(scenario_order)

    fmt = '.3f' if metric != 'sink_collapsed' else '.0%'
    if metric == 'sink_collapsed':
        pivot_display = pivot.copy()
    else:
        pivot_display = pivot

    sns.heatmap(pivot_display, annot=True, fmt='.3f' if metric != 'sink_collapsed' else '.2f',
                cmap=cmap, ax=ax, yticklabels=scenario_labels)
    ax.set_title(label, fontsize=13)
    ax.set_ylabel('Scenario')
    ax.set_xlabel('Post-Labor Level')

fig.suptitle('Full 10-Scenario Grid: Outcomes at 0.5, 0.8, 0.95 Post-Labor\n(150 runs per cell)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep6_grand_heatmap.png', bbox_inches='tight')
plt.close()
print("Figure 1 saved")

# ============================================================
# Figure 2: Scenario Ranking at PL=0.95 (the critical test)
# ============================================================
fig, ax = plt.subplots(figsize=(12, 7))

subset = df[df['post_labor'] == 0.95]
summary = subset.groupby('scenario').agg(
    meaning=('meaning_index', 'mean'),
    meaning_sem=('meaning_index', 'sem'),
    sink=('sink_index', 'mean'),
    collapse=('sink_collapsed', 'mean')
).reindex(scenario_order)

x = np.arange(len(scenario_order))
width = 0.3

bars1 = ax.bar(x - width, summary['meaning'], width, yerr=summary['meaning_sem']*1.96,
               label='Meaning', color='#2196F3', alpha=0.8, capsize=3)
bars2 = ax.bar(x, summary['sink'], width,
               label='Sink Index', color='#FF9800', alpha=0.8)
bars3 = ax.bar(x + width, summary['collapse'], width,
               label='Collapse Rate', color='#F44336', alpha=0.8)

ax.set_xticks(x)
ax.set_xticklabels(scenario_labels, rotation=45, ha='right', fontsize=10)
ax.set_ylabel('Value')
ax.set_title('Scenario Performance at 95% Automation (PL=0.95, n=150 each)',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.set_ylim(0, 1.1)

plt.tight_layout()
plt.savefig('reports/figures/sweep6_scenario_ranking.png', bbox_inches='tight')
plt.close()
print("Figure 2 saved")

# ============================================================
# Figure 3: Intervention Decomposition (marginal contribution)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for ax_i, pl in enumerate([0.8, 0.95]):
    ax = axes[ax_i]
    s = df[df['post_labor'] == pl].groupby('scenario')['sink_index'].mean()

    # Decompose: baseline → each single → combos → full
    baseline_sink = s['baseline']

    interventions = {
        'Fairness': baseline_sink - s['fairness'],
        'UBI': baseline_sink - s['ubi_only'],
        'Roles': baseline_sink - s['roles'],
        'UBI+VW': baseline_sink - s['UBI+virtual'],
        'UBI+Coll': baseline_sink - s['UBI+collectivism'],
        'Roles+VW': baseline_sink - s['roles+virtual'],
        'Fair+Coll': baseline_sink - s['fairness+collectivism'],
        'Full Bundle': baseline_sink - s['full_bundle'],
        'All Bundle': baseline_sink - s['all_bundle'],
    }

    names = list(interventions.keys())
    values = list(interventions.values())
    colors = ['#FF9800' if v < 0.5 else '#4CAF50' if v < 0.8 else '#2196F3' for v in values]

    bars = ax.barh(names, values, color=colors, alpha=0.8)
    ax.set_xlabel('Sink Reduction from Baseline')
    ax.set_title(f'Intervention Effectiveness (PL={pl})')
    ax.axvline(x=baseline_sink, color='red', linestyle=':', label=f'Baseline sink={baseline_sink:.3f}')

    for bar, val in zip(bars, values):
        ax.text(val + 0.01, bar.get_y() + bar.get_height()/2,
               f'{val:.3f}', va='center', fontsize=9)

fig.suptitle('Marginal Intervention Effect on Sink Index', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep6_intervention_decomposition.png', bbox_inches='tight')
plt.close()
print("Figure 3 saved")

# ============================================================
# Figure 4: Violin plots for key scenarios at PL=0.95
# ============================================================
fig, ax = plt.subplots(figsize=(14, 6))

key_scenarios = ['baseline', 'ubi_only', 'UBI+virtual', 'roles', 'roles+virtual',
                 'full_bundle', 'all_bundle']
key_labels = ['Baseline', 'UBI', 'UBI+VW', 'Roles', 'Roles+VW', 'Full', 'All']

subset = df[(df['post_labor'] == 0.95) & (df['scenario'].isin(key_scenarios))]
subset = subset.copy()
subset['scenario'] = pd.Categorical(subset['scenario'], categories=key_scenarios, ordered=True)

sns.violinplot(data=subset, x='scenario', y='meaning_index', ax=ax,
               palette='RdYlGn', inner='box', scale='width')
ax.set_xticklabels(key_labels)
ax.set_ylabel('Meaning Index')
ax.set_xlabel('Scenario')
ax.axhline(y=0.55, color='gray', linestyle=':', alpha=0.5, label='Productive threshold')
ax.axhline(y=0.42, color='red', linestyle=':', alpha=0.5, label='Withdrawal threshold')
ax.legend(fontsize=9)
ax.set_title('Distribution of Meaning Index Across Scenarios at PL=0.95\n(n=150 per scenario)',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep6_meaning_violins.png', bbox_inches='tight')
plt.close()
print("Figure 4 saved")

print("\nDone!")
