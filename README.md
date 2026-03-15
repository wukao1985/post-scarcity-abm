# Post-Scarcity ABM
### Behavioral Sink Under Post-Labor Displacement

> When most people are displaced from productive roles — what happens to meaning, social cohesion, and well-being?

A simulation study of the psychological and social consequences of large-scale labor displacement, grounded in Calhoun's behavioral sink theory, Self-Determination Theory, and complex systems research.

This repository should currently be read as a **mature ABM research prototype with planned triangulation extensions**, not yet as a fully completed three-pathway project.

---

## Current Status

**Pathway A (ABM):** Substantially complete — 6 parameter sweeps, 22,000+ runs, historical validation, paper draft.
**Pathway B (LLM agents):** Planned — not yet implemented.
**Pathway C (System Dynamics):** Initial implementation — basic ODE model with Nauru/Gulf calibration, directional agreement with ABM confirmed.

| Pathway | Method | Status |
|---------|--------|--------|
| **A** | Agent-Based Model (Python Mesa) | **Substantially complete** — V4 model, 6 sweeps, 10 scenarios |
| B | LLM Generative Agents | Planned — not yet started |
| C | System Dynamics (scipy ODEs) | **Initial** — stock-flow model, historical calibration |

**Triangulation rule (planned):** A finding is robust only if it appears in >=2 of 3 pathways. Currently only Pathway A is mature enough to draw conclusions from; Pathway C provides initial directional support.

## Quick Start

```bash
git clone https://github.com/wukao1985/post-scarcity-abm.git
cd post-scarcity-abm
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Run Sweep 1 (Pathway A only — ~5 minutes, 2,250 runs)
python models/pathway_a_abm/runner.py 1

# Generate Sweep 1 figures
python models/pathway_a_abm/report.py

# Run Pathway C SD model (optional — ~1 second)
python models/pathway_c_sd/sd_model.py
```

Currently reproducible scope: **Pathway A sweeps 1-6** and **Pathway C initial model**. See [REPRODUCE.md](REPRODUCE.md) for full instructions.

## Research Question

What mechanisms drive or prevent behavioral sink in post-labor societies, and which intervention combinations are effective at different displacement levels?

## Model Findings (Pathway A)

These are findings from the ABM, not empirical claims. They identify mechanisms and qualitative relationships within the model's assumptions:

- **Phase transition zone at ~80-90% displacement**: Baseline collapse probability rises sharply from 2% at 80% to 100% at 95% post-labor. The transition zone — rather than a knife-edge threshold — reflects realistic stochasticity in the V4 model.
- **UBI is necessary but insufficient**: At 95% displacement, UBI alone produces a sink index of 0.515 with elevated distress across the population.
- **Role programs outperform income transfers in the model**: Roles (sink=0.458) vs UBI (sink=0.515) at 95% displacement.
- **Virtual worlds complement but cannot fully substitute**: VW+UBI achieves near-zero sink; VW alone provides only partial protection at extreme displacement.
- **Social cohesion moderates intervention effectiveness**: The model predicts collectivist structures substantially reduce UBI-associated sink, consistent with the Nauru (collapse) vs Gulf states (stability) historical divergence.
- **Speed matters**: Rapid displacement produces 46 percentage points more collapse than gradual at 95% automation.

## Project Structure

```
post-scarcity-abm/
├── models/
│   ├── pathway_a_abm/
│   │   ├── model.py           # PostLaborAgent + PostLaborModel (V4)
│   │   ├── runner.py          # Sweep runners (1-6)
│   │   └── report.py          # Sweep 1 figure generation
│   └── pathway_c_sd/
│       └── sd_model.py        # System dynamics ODE model (initial)
├── scripts/
│   └── sweep{2-6}_figures.py  # Figure generation scripts
├── data/
│   └── simulation/            # Output CSVs (see data/simulation/README.md)
├── reports/
│   ├── paper_draft.md         # Paper draft (JASSS target)
│   ├── methods_appendix.md    # Parameter justifications
│   ├── v4_validation.md       # V3 vs V4 comparison
│   ├── pathway_c_initial.md   # SD model report
│   ├── sweep{2-6}_analysis.md # Per-sweep analysis with critique
│   ├── historical_validation.md
│   └── figures/               # All generated figures
├── tests/
│   └── test_model.py          # 14 model tests
├── docs/
│   ├── v3-experiment-design.md
│   ├── paper_to_repo_map.md   # Paper section → code/data mapping
│   └── reproduction_checklist.md
├── requirements.txt           # Pinned dependencies
├── Makefile                   # Build targets
├── REPRODUCE.md               # Reproduction instructions
└── outputs_manifest.md        # Complete output file listing
```

## Theoretical Framework

- **Calhoun (1973)** — Universe 25 behavioral sink: role deprivation → collapse
- **Deci & Ryan (1985)** — SDT: autonomy + competence + relatedness as core needs
- **Tainter (1988)** — Complex systems collapse: phase transitions and irreversibility
- **Case & Deaton (2020)** — Deaths of Despair: natural experiment for role deprivation

## Reports

- [Paper Draft](reports/paper_draft.md)
- [Methods Appendix](reports/methods_appendix.md) — parameter justifications (SDT theory / calibration / convenience)
- [V4 Validation](reports/v4_validation.md) — V3 vs V4 comparison
- [Pathway C Initial](reports/pathway_c_initial.md) — SD model triangulation
- [V3 Experiment Design](docs/v3-experiment-design.md)
- [Sweep Analysis Reports](reports/) — per-sweep findings with self-critique
- [Paper-to-Repo Map](docs/paper_to_repo_map.md) — maps every paper section to code/data
- [Reproduction Checklist](docs/reproduction_checklist.md) — submission readiness status

## Obsidian Knowledge Base

Literature notes and research proposal: https://evergreen-notes.vercel.app
