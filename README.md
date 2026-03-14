# Post-Scarcity ABM
### Behavioral Sink in the Age of Intelligent Machines

> When AI lets 5% of people produce 100% of what everyone needs — what happens to the other 95%?

A multi-pathway simulation project studying the social and psychological consequences of large-scale labor displacement, grounded in Calhoun's behavioral sink theory, Self-Determination Theory, and complex systems collapse research.

---

## Research Question

Is there a critical automation threshold beyond which human societies enter an irreversible behavioral sink — and what interventions can prevent it?

## Three Simulation Pathways

| Pathway | Method | Goal |
|---------|--------|------|
| A | Agent-Based Model (Python Mesa) | Phase transition threshold, behavioral typology ratios |
| B | LLM Generative Agents | Qualitative narratives, mechanism depth |
| C | System Dynamics (PySD) | Historical calibration, policy leverage points |

**Triangulation rule:** A finding is robust only if it appears in ≥2 of 3 pathways.

## Reports

- [V2 Simulation Report](reports/v2_post_scarcity_report.pdf) — Baseline ABM, 9,120 runs, threshold found at ~80%
- V3 Experiment Design → `docs/v3-experiment-design.md`

## Project Structure

```
post-scarcity-abm/
├── docs/                    # Research design documents
├── models/
│   ├── pathway_a_abm/       # Python Mesa ABM
│   ├── pathway_b_llm/       # LLM generative agents
│   └── pathway_c_sd/        # System Dynamics
├── data/
│   ├── historical/          # Calibration datasets
│   └── simulation/          # Output data
├── reports/                 # Generated reports
├── notebooks/               # Analysis notebooks
└── tasks/todo.md            # Project task tracking
```

## Theoretical Framework

- **Calhoun (1973)** — Universe 25 behavioral sink: role deprivation → collapse
- **Deci & Ryan (1985)** — SDT: autonomy + competence + relatedness as core needs
- **Tainter (1988)** — Complex systems collapse: phase transitions and irreversibility
- **Case & Deaton (2020)** — Deaths of Despair: natural experiment for role deprivation

## Key Findings So Far (V2)

- Behavioral sink threshold: **~80% post-labor** (97% collapse probability)
- UBI alone: reduces collapse to 0% but meaning remains degraded (sink 0.336)
- Full intervention bundle: nearly eliminates sink (0.042)
- Fairness/redistribution matters as much as role substitution
- Network topology matters less than displacement level

## Obsidian Knowledge Base

All literature notes, permanent notes, and research proposal stored in Zettelkasten vault.
Published at: https://evergreen-notes.vercel.app
