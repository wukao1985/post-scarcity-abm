"""
Sweep 2 Analysis: Automation Speed Effects
Generate publication-quality figures.
"""
import sys
sys.path.insert(0, '/Users/cloud/Documents/claude/post-scarcity-abm')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
from scipy import stats

sns.set_theme(style="whitegrid", font_scale=1.1)
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'sans-serif'

df = pd.read_csv('data/simulation/sweep2_automation_speed.csv')

# ============================================================
# Figure 1: Speed × Post-Labor × Outcome (Main Result)
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for i, metric in enumerate(['meaning_index', 'sink_index', 'sink_collapsed']):
    ax = axes[i]
    labels = {'meaning_index': 'Mean Meaning Index',
              'sink_index': 'Mean Sink Index',
              'sink_collapsed': 'Collapse Rate'}

    for speed in ['gradual', 'rapid']:
        baseline = df[(df['scenario'] == 'baseline') & (df['speed'] == speed)]
        grouped = baseline.groupby('post_labor')[metric].agg(['mean', 'std', 'sem'])
        ci95 = grouped['sem'] * 1.96

        marker = 'o' if speed == 'gradual' else 's'
        color = '#2196F3' if speed == 'gradual' else '#F44336'
        ax.errorbar(grouped.index, grouped['mean'], yerr=ci95,
                   label=speed.capitalize(), marker=marker, color=color,
                   capsize=4, linewidth=2, markersize=8)

    ax.set_xlabel('Post-Labor Fraction')
    ax.set_ylabel(labels[metric])
    ax.legend()
    ax.set_title(labels[metric])

fig.suptitle('Automation Speed Effect on Baseline Outcomes\n(Gradual = 0.01/step, Rapid = 0.08/step)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep2_speed_baseline.png', bbox_inches='tight')
plt.close()
print("Figure 1 saved")

# ============================================================
# Figure 2: Speed × Scenario Heatmap (at pl=0.8 and 0.95)
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

for col, metric in enumerate(['meaning_index', 'sink_index']):
    for row, pl in enumerate([0.8, 0.95]):
        ax = axes[row, col]
        subset = df[df['post_labor'] == pl]
        pivot = subset.groupby(['scenario', 'speed'])[metric].mean().unstack()

        # Reorder scenarios
        order = ['baseline', 'fairness_only', 'ubi_only', 'roles_only', 'full_bundle']
        pivot = pivot.reindex(order)

        cmap = 'RdYlGn' if metric == 'meaning_index' else 'RdYlGn_r'
        sns.heatmap(pivot, annot=True, fmt='.3f', cmap=cmap, ax=ax,
                   vmin=pivot.values.min() * 0.95, vmax=pivot.values.max() * 1.05)

        title_metric = 'Meaning' if metric == 'meaning_index' else 'Sink'
        ax.set_title(f'{title_metric} Index (Post-Labor = {pl})')
        ax.set_ylabel('Scenario')
        ax.set_xlabel('Speed')

fig.suptitle('Automation Speed × Scenario Interaction', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep2_speed_scenario_heatmap.png', bbox_inches='tight')
plt.close()
print("Figure 2 saved")

# ============================================================
# Figure 3: Effect Size of Speed (rapid - gradual) by scenario
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for ax_i, pl in enumerate([0.8, 0.95]):
    ax = axes[ax_i]
    scenarios = ['baseline', 'fairness_only', 'ubi_only', 'roles_only', 'full_bundle']

    meaning_diffs = []
    sink_diffs = []
    meaning_cis = []
    sink_cis = []

    for sc in scenarios:
        g = df[(df['speed']=='gradual') & (df['post_labor']==pl) & (df['scenario']==sc)]
        r = df[(df['speed']=='rapid') & (df['post_labor']==pl) & (df['scenario']==sc)]

        m_diff = r['meaning_index'].mean() - g['meaning_index'].mean()
        s_diff = r['sink_index'].mean() - g['sink_index'].mean()

        # Cohen's d for effect size
        m_pooled_std = np.sqrt((g['meaning_index'].std()**2 + r['meaning_index'].std()**2) / 2)
        s_pooled_std = np.sqrt((g['sink_index'].std()**2 + r['sink_index'].std()**2) / 2)

        meaning_diffs.append(m_diff)
        sink_diffs.append(s_diff)

        # 95% CI via bootstrap-like approach (normal approx)
        m_se = np.sqrt(g['meaning_index'].var()/len(g) + r['meaning_index'].var()/len(r))
        s_se = np.sqrt(g['sink_index'].var()/len(g) + r['sink_index'].var()/len(r))
        meaning_cis.append(1.96 * m_se)
        sink_cis.append(1.96 * s_se)

    x = np.arange(len(scenarios))
    width = 0.35

    bars1 = ax.bar(x - width/2, meaning_diffs, width, yerr=meaning_cis,
                   label='Meaning (rapid−gradual)', color='#2196F3', alpha=0.8, capsize=3)
    bars2 = ax.bar(x + width/2, sink_diffs, width, yerr=sink_cis,
                   label='Sink (rapid−gradual)', color='#F44336', alpha=0.8, capsize=3)

    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels([s.replace('_', '\n') for s in scenarios], fontsize=9)
    ax.set_ylabel('Difference (rapid − gradual)')
    ax.set_title(f'Speed Effect Size at Post-Labor = {pl}')
    ax.legend(fontsize=9)

fig.suptitle('Impact of Rapid vs Gradual Automation by Scenario',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep2_speed_effect_size.png', bbox_inches='tight')
plt.close()
print("Figure 3 saved")

# ============================================================
# Figure 4: Archetype Distribution: Gradual vs Rapid (violin)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for ax_i, pl in enumerate([0.8, 0.95]):
    ax = axes[ax_i]
    subset = df[(df['scenario'] == 'baseline') & (df['post_labor'] == pl)]

    arch_cols = ['productive_frac', 'beautiful_one_frac', 'withdrawn_frac', 'collapsed_frac']
    arch_labels = ['Productive', 'Beautiful\nOnes', 'Withdrawn', 'Collapsed']

    plot_data = []
    for col, label in zip(arch_cols, arch_labels):
        for speed in ['gradual', 'rapid']:
            vals = subset[subset['speed'] == speed][col]
            for v in vals:
                plot_data.append({'Archetype': label, 'Speed': speed.capitalize(), 'Fraction': v})

    pdf = pd.DataFrame(plot_data)
    sns.boxplot(data=pdf, x='Archetype', y='Fraction', hue='Speed', ax=ax,
                palette={'Gradual': '#2196F3', 'Rapid': '#F44336'})
    ax.set_title(f'Archetype Distribution at Post-Labor = {pl}')
    ax.set_ylabel('Population Fraction')

fig.suptitle('Behavioral Archetype Distribution by Automation Speed\n(Baseline scenario)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep2_archetypes_by_speed.png', bbox_inches='tight')
plt.close()
print("Figure 4 saved")

# ============================================================
# Figure 5: UBI Effectiveness Under Different Speeds
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

# Compare collapse rates across scenarios for rapid automation
rapid_95 = df[(df['speed'] == 'rapid') & (df['post_labor'] == 0.95)]
gradual_95 = df[(df['speed'] == 'gradual') & (df['post_labor'] == 0.95)]

scenarios = ['baseline', 'fairness_only', 'ubi_only', 'roles_only', 'full_bundle']
scenario_labels = ['Baseline', 'Fairness', 'UBI', 'Roles', 'Full Bundle']

x = np.arange(len(scenarios))
width = 0.35

grad_collapse = [gradual_95[gradual_95['scenario']==s]['sink_collapsed'].mean() for s in scenarios]
rapid_collapse = [rapid_95[rapid_95['scenario']==s]['sink_collapsed'].mean() for s in scenarios]

bars1 = ax.bar(x - width/2, grad_collapse, width, label='Gradual', color='#2196F3', alpha=0.8)
bars2 = ax.bar(x + width/2, rapid_collapse, width, label='Rapid', color='#F44336', alpha=0.8)

ax.set_ylabel('Collapse Probability')
ax.set_title('Intervention Effectiveness Under Rapid vs Gradual Automation\n(Post-Labor = 0.95)',
             fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(scenario_labels)
ax.legend()
ax.set_ylim(0, 1.1)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0.01:
            ax.annotate(f'{height:.0%}', xy=(bar.get_x() + bar.get_width()/2, height),
                       xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('reports/figures/sweep2_intervention_robustness.png', bbox_inches='tight')
plt.close()
print("Figure 5 saved")

# ============================================================
# Statistical Tests
# ============================================================
print("\n=== STATISTICAL TESTS ===")
for pl in [0.8, 0.95]:
    print(f"\n--- Post-Labor = {pl} ---")
    for sc in scenarios:
        g = df[(df['speed']=='gradual') & (df['post_labor']==pl) & (df['scenario']==sc)]
        r = df[(df['speed']=='rapid') & (df['post_labor']==pl) & (df['scenario']==sc)]

        t_m, p_m = stats.ttest_ind(g['meaning_index'], r['meaning_index'])
        t_s, p_s = stats.ttest_ind(g['sink_index'], r['sink_index'])

        # Cohen's d
        d_m = (r['meaning_index'].mean() - g['meaning_index'].mean()) / np.sqrt(
            (g['meaning_index'].std()**2 + r['meaning_index'].std()**2) / 2)
        d_s = (r['sink_index'].mean() - g['sink_index'].mean()) / np.sqrt(
            (g['sink_index'].std()**2 + r['sink_index'].std()**2) / 2)

        print(f"{sc:15s}: meaning t={t_m:7.2f} p={p_m:.2e} d={d_m:+.2f} | "
              f"sink t={t_s:7.2f} p={p_s:.2e} d={d_s:+.2f}")

# Key artifact check
print("\n=== ARTIFACT CHECK: Gradual speed cap ===")
print("Gradual speed = 0.01/step × 80 steps = 0.80 max automation")
print("Therefore gradual/0.95 NEVER reaches 0.95 — only reaches 0.80")
g80 = df[(df['speed']=='gradual') & (df['post_labor']==0.80) & (df['scenario']=='baseline')]
g95 = df[(df['speed']=='gradual') & (df['post_labor']==0.95) & (df['scenario']=='baseline')]
print(f"Gradual pl=0.80 meaning: {g80['meaning_index'].mean():.6f}")
print(f"Gradual pl=0.95 meaning: {g95['meaning_index'].mean():.6f}")
print(f"Difference: {abs(g80['meaning_index'].mean() - g95['meaning_index'].mean()):.6f}")
print(f"post_labor_current at end: gradual/0.80={g80['post_labor_current'].mean():.3f}, gradual/0.95={g95['post_labor_current'].mean():.3f}")

print("\nDone! All figures saved to reports/figures/")
