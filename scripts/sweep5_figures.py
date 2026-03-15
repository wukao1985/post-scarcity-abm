"""Sweep 5 Analysis: Archetype Time Series"""
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

df = pd.read_csv('data/simulation/sweep5_archetypes.csv')

# ============================================================
# Figure 1: Stacked Area - Archetype Evolution (Main Result)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

colors = {
    'productive_frac': '#4CAF50',
    'beautiful_one_frac': '#FFC107',
    'withdrawn_frac': '#FF9800',
    'collapsed_frac': '#F44336',
    'aggressor_frac': '#9C27B0',
}
labels = {
    'productive_frac': 'Productive',
    'beautiful_one_frac': 'Beautiful Ones',
    'withdrawn_frac': 'Withdrawn',
    'collapsed_frac': 'Collapsed',
    'aggressor_frac': 'Aggressor',
}

arch_cols = ['productive_frac', 'beautiful_one_frac', 'withdrawn_frac', 'collapsed_frac', 'aggressor_frac']

for ax_i, sc in enumerate(['baseline', 'full_bundle']):
    ax = axes[ax_i]
    subset = df[df['scenario'] == sc]
    means = subset.groupby('step')[arch_cols].mean()

    ax.stackplot(means.index,
                [means[c] for c in arch_cols],
                labels=[labels[c] for c in arch_cols],
                colors=[colors[c] for c in arch_cols],
                alpha=0.85)
    ax.set_xlabel('Time Step')
    ax.set_ylabel('Population Fraction')
    ax.set_title(sc.replace('_', ' ').title())
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 1)

axes[0].legend(loc='center right', fontsize=9)
fig.suptitle('Behavioral Archetype Evolution Over Time\n(Post-Labor = 0.80, 50 runs averaged)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep5_archetype_stacked.png', bbox_inches='tight')
plt.close()
print("Figure 1 saved")

# ============================================================
# Figure 2: Line Plot with CI bands
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

for ax_i, sc in enumerate(['baseline', 'full_bundle']):
    ax = axes[ax_i]
    subset = df[df['scenario'] == sc]

    for col in arch_cols:
        if col == 'aggressor_frac':
            continue  # Too small to see
        means = subset.groupby('step')[col].mean()
        stds = subset.groupby('step')[col].std()
        sems = stds / np.sqrt(50)
        ci95 = sems * 1.96

        ax.plot(means.index, means, label=labels[col], color=colors[col], linewidth=2)
        ax.fill_between(means.index, means - ci95, means + ci95,
                        color=colors[col], alpha=0.2)

    ax.set_xlabel('Time Step')
    ax.set_ylabel('Population Fraction')
    ax.set_title(sc.replace('_', ' ').title())
    ax.set_xlim(0, 80)
    ax.legend(fontsize=9)

fig.suptitle('Archetype Trajectories with 95% CI\n(Post-Labor = 0.80)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep5_archetype_trajectories.png', bbox_inches='tight')
plt.close()
print("Figure 2 saved")

# ============================================================
# Figure 3: Meaning + Sink Index over time
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for metric, label, ax in [('meaning_index', 'Meaning Index', axes[0]),
                           ('sink_index', 'Sink Index', axes[1])]:
    for sc, color, ls in [('baseline', '#F44336', '-'), ('full_bundle', '#4CAF50', '--')]:
        subset = df[df['scenario'] == sc]
        means = subset.groupby('step')[metric].mean()
        stds = subset.groupby('step')[metric].std()
        ci95 = (stds / np.sqrt(50)) * 1.96

        ax.plot(means.index, means, label=sc.replace('_', ' ').title(),
               color=color, linestyle=ls, linewidth=2)
        ax.fill_between(means.index, means - ci95, means + ci95,
                        color=color, alpha=0.15)

    ax.set_xlabel('Time Step')
    ax.set_ylabel(label)
    ax.set_title(label)
    ax.legend()

    if metric == 'sink_index':
        ax.axhline(y=0.7, color='gray', linestyle=':', label='Collapse threshold', alpha=0.5)

fig.suptitle('Aggregate Indices Over Time (Post-Labor = 0.80)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep5_indices_timeseries.png', bbox_inches='tight')
plt.close()
print("Figure 3 saved")

# ============================================================
# Figure 4: Key transition moments
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

baseline = df[df['scenario'] == 'baseline']
means = baseline.groupby('step')[['productive_frac', 'beautiful_one_frac',
                                    'withdrawn_frac', 'collapsed_frac']].mean()

# Find crossover points
prod = means['productive_frac']
bo = means['beautiful_one_frac']
wdr = means['withdrawn_frac']

# Plot with annotations
ax.plot(means.index, prod, 'o-', color='#4CAF50', label='Productive', markersize=3, linewidth=2)
ax.plot(means.index, bo, 's-', color='#FFC107', label='Beautiful Ones', markersize=3, linewidth=2)
ax.plot(means.index, wdr, '^-', color='#FF9800', label='Withdrawn', markersize=3, linewidth=2)
ax.plot(means.index, means['collapsed_frac'], 'v-', color='#F44336', label='Collapsed', markersize=3, linewidth=2)

# Find where productive crosses below beautiful_one
for step in range(1, 80):
    if prod.iloc[step] < bo.iloc[step] and prod.iloc[step-1] >= bo.iloc[step-1]:
        ax.axvline(x=step, color='gray', linestyle=':', alpha=0.5)
        ax.annotate(f'Prod < BO\n(step {step})', (step, 0.5), fontsize=9, ha='center')
    if wdr.iloc[step] > bo.iloc[step] and wdr.iloc[step-1] <= bo.iloc[step-1]:
        ax.axvline(x=step, color='gray', linestyle=':', alpha=0.5)
        ax.annotate(f'Wdr > BO\n(step {step})', (step, 0.4), fontsize=9, ha='center')

ax.set_xlabel('Time Step')
ax.set_ylabel('Population Fraction')
ax.set_title('Behavioral Cascade: Baseline at PL=0.80\n(Calhoun Sequence: Productive → Beautiful Ones → Withdrawn → Collapsed)',
             fontweight='bold')
ax.legend(loc='center right')
ax.set_xlim(0, 80)
plt.tight_layout()
plt.savefig('reports/figures/sweep5_cascade_sequence.png', bbox_inches='tight')
plt.close()
print("Figure 4 saved")

# ============================================================
# Figure 5: Post-labor ramp vs archetype response
# ============================================================
fig, ax1 = plt.subplots(figsize=(10, 6))

baseline = df[df['scenario'] == 'baseline']
means = baseline.groupby('step')[['post_labor_current', 'sink_index', 'meaning_index']].mean()

ax1.plot(means.index, means['post_labor_current'], 'k-', linewidth=2, label='Automation Level')
ax1.set_xlabel('Time Step')
ax1.set_ylabel('Post-Labor Fraction', color='black')

ax2 = ax1.twinx()
ax2.plot(means.index, means['sink_index'], 'r-', linewidth=2, label='Sink Index')
ax2.plot(means.index, means['meaning_index'], 'b--', linewidth=2, label='Meaning Index')
ax2.set_ylabel('Index Value')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center left')

ax1.set_title('Automation Ramp vs. Psychological Response (Baseline)',
              fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/sweep5_automation_response.png', bbox_inches='tight')
plt.close()
print("Figure 5 saved")

print("\nDone!")
