# V3 Experiment Design
## Post-Scarcity ABM — Behavioral Sink Simulation

*Based on V2 findings (2026-03-13). Designed to address open questions and extend the model.*

---

## V2 Summary & What V3 Must Address

### V2 Key Results
| Scenario | Post-labor | Meaning | Sink | Collapse prob. |
|----------|-----------|---------|------|----------------|
| Baseline | 0.80 | 0.450 | 0.769 | 97% |
| UBI only | 0.80 | 0.581 | 0.336 | 0% |
| Full bundle | 0.80 | 0.693 | 0.042 | 0% |
| Full bundle | 0.95 | 0.685 | 0.044 | 0% |

### V2 Open Questions → V3 Research Questions

**OQ1:** UBI alone prevented collapse in V2 (0% at 80%). Is this robust or a parameter artifact?
→ V3-RQ1: Does UBI's effectiveness depend on fairness perception? Test under high/low inequality.

**OQ2:** Virtual worlds / game substitution for roles not tested.
→ V3-RQ2: Can high-quality virtual role substitutes prevent behavioral sink?

**OQ3:** Speed of automation not tested — only final displacement level.
→ V3-RQ3: Does rapid automation produce worse outcomes than gradual, even at same endpoint?

**OQ4:** Collectivist vs. individualist society hypothesis untested.
→ V3-RQ4: Do collectivist structures show higher resilience thresholds?

**OQ5:** Behavioral archetype distribution not tracked over time.
→ V3-RQ5: What is the temporal sequence of Beautiful Ones / Aggressors / Withdrawers emergence?

---

## V3 Agent Architecture

### Core Psychological State (unchanged from V2)
```python
autonomy: float        # 0-1
competence: float      # 0-1
relatedness: float     # 0-1
status: float          # 0-1
meaning: float         # derived outcome
```

### New Agent Parameters
```python
# Agent profile (sampled at initialization)
profile: enum          # resilient / balanced / vulnerable (V2 had this)
collectivism: float    # 0=individualist, 1=collectivist (NEW)
virtual_engagement: float  # 0-1, propensity to seek virtual roles (NEW)

# Dynamic state
economic_role: float   # 0-1 (post-labor fraction determines distribution)
virtual_role: float    # 0-1, access to meaningful virtual activities (NEW)
role_search_effort: float  # endogenous search (V2 had this)

# Behavioral archetype (tracked per timestep)
archetype: enum        # productive / beautiful_one / aggressor / withdrawn / collapsed
```

### Updated Psychological Update Rules

```
Autonomy_t+1 = f(
    base_autonomy,
    economic_role_access,
    virtual_role_access,        ← NEW
    redistribution_fairness,
    collectivism,               ← NEW (collectivist: relatedness partially substitutes)
    resilience,
    local_social_exposure,
    status_gap
)

Competence_t+1 = f(
    base_competence,
    economic_role,
    virtual_role_quality,       ← NEW (games can satisfy competence)
    skill_transferability,
    local_exposure
)

Relatedness_t+1 = f(
    base_relatedness,
    social_capital,
    collectivism,               ← NEW (higher baseline in collectivist societies)
    economic_role_access,
    virtual_community_quality,  ← NEW (online communities)
    redistribution_fairness,
    local_aggression_exposure
)

Meaning_t+1 = f(
    autonomy, competence, relatedness, status,
    contribution_to_nonplayers,  ← NEW 4th SDT dimension
    role_access,
    contagion_exposure,
    resilience,
    redistribution_fairness
)
```

**Key addition:** `contribution_to_nonplayers` — captures the dimension that virtual worlds cannot satisfy. Even if autonomy/competence/relatedness are met virtually, meaning requires that one's activity matters to people outside the activity.

---

## V3 Simulation Parameters

### Fixed Parameters
```
Population:     200 agents
Time horizon:   80 steps
Monte Carlo:    150 runs per parameter point
Network:        Small-world (Watts-Strogatz, k=6, p=0.1)
                [V2 showed small-world is most realistic]
```

### Main Parameter Sweeps

**Sweep 1: Automation Level** (replicates V2 for comparison)
```
post_labor_fraction: [0.0, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
automation_speed: FIXED at medium
```

**Sweep 2: Automation Speed** (NEW)
```
post_labor_fraction: [0.5, 0.8]  (two key levels)
automation_speed: [slow=0.01/step, medium=0.03/step, rapid=0.08/step]
```

**Sweep 3: Virtual World Quality** (NEW)
```
post_labor_fraction: [0.8, 0.95]
virtual_world_quality: [0.0, 0.3, 0.6, 0.9]
```

**Sweep 4: Collectivism** (NEW)
```
post_labor_fraction: [0.8]
collectivism_index: [0.1, 0.4, 0.7, 0.9]
```

---

## V3 Scenarios

### Base Scenarios (V2 replication)
1. **Baseline** — no intervention
2. **UBI only** — income support, no role substitution
3. **Roles only** — role substitution programs, no income
4. **Fairness only** — redistribution of AI capital gains
5. **Full bundle** — all of the above

### New V3 Scenarios
6. **Virtual World** — high virtual_world_quality (0.8) + UBI
7. **Rapid Automation** — same endpoint as baseline but 3x faster
8. **Collectivist** — collectivism_index = 0.8, baseline intervention
9. **Fairness-first** — redistribution precedes role programs
10. **Meaning Infrastructure** — investment in community/arts/civic roles (contribution_to_nonplayers += 0.3)

---

## V3 Output Metrics

### Existing Metrics (V2)
- `meaning_index` — population mean meaning level
- `sink_index` — proportion in withdrawn/collapsed/aggressor states
- `collapse_probability` — % of runs ending in sink_index > 0.7

### New Metrics (V3)
- **Archetype distribution time series** — track % Beautiful Ones / Aggressors / Withdrawn / Productive at each timestep
- **Birth intention** — population mean birth intention (proxy for reproductive collapse)
- **Social trust** — mean relatedness across dyads
- **Political instability index** — derived from aggressor % + inequality
- **Meaning source breakdown** — what % of meaning comes from economic / virtual / community roles

---

## V3 Hypotheses

**H1 (replicated):** Phase transition threshold at ~80% post-labor. V3 tests if threshold shifts with collectivism and virtual worlds.

**H2 (revised):** UBI prevents collapse but not meaning degradation. V3 adds: UBI effectiveness depends on perceived fairness (Gini coefficient of AI capital distribution).

**H3 (new):** Virtual worlds delay but do not prevent behavioral sink because `contribution_to_nonplayers` remains near zero.

**H4 (new):** Rapid automation produces more Aggressors; gradual automation produces more Beautiful Ones. Speed determines archetype distribution, not just severity.

**H5 (new):** Collectivist societies have threshold at ~85-90% (vs ~80% baseline) due to relatedness buffering autonomy/competence deficits.

---

## Report Structure (V3)

Following V2 report format, adding:

1. Executive Summary
2. V2 → V3 Changes and Rationale
3. Replication of V2 (validation)
4. New findings:
   - Effect of automation speed
   - Virtual world substitution test
   - Collectivist vs. individualist trajectories
   - Behavioral archetype time series
5. Intervention decomposition (extended)
6. Policy implications
7. Limitations and V4 directions

---

## Estimated Run Count

| Sweep | Points | Runs each | Total |
|-------|--------|-----------|-------|
| Main curve (replication) | 9 | 150 | 1,350 |
| Automation speed | 6 | 150 | 900 |
| Virtual world | 8 | 150 | 1,200 |
| Collectivism | 4 | 150 | 600 |
| Scenarios at key levels | 10×3 | 150 | 4,500 |
| **Total** | | | **~8,550** |

---

## Implementation Plan

**Phase 1:** Port V2 to clean Mesa codebase + add V3 agent architecture
**Phase 2:** Run Sweep 1 (replication) — verify V2 results hold
**Phase 3:** Run Sweeps 2-4 (new variables)
**Phase 4:** Run all 10 scenarios at 0.5 / 0.8 / 0.95 post-labor
**Phase 5:** Analysis + report generation

*Target: Pathway A complete before starting Pathway C calibration*
