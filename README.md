# Post-Scarcity ABM
### Behavioral Sink Under Post-Labor Displacement

> When most people are displaced from productive roles — what happens to meaning, social cohesion, and well-being?

A multi-pathway simulation project studying the psychological and social consequences of large-scale labor displacement, grounded in Calhoun's behavioral sink theory, Self-Determination Theory, and complex systems research.

---

## Research Question

What mechanisms drive or prevent behavioral sink in post-labor societies, and which intervention combinations are effective at different displacement levels?

## Current Status

**Pathway A (ABM): Complete** — 17,050 simulation runs across 6 parameter sweeps. Paper draft in `reports/paper_draft.md`.

| Pathway | Method | Status |
|---------|--------|--------|
| **A** | Agent-Based Model (Python Mesa) | **Complete** — phase transition, 10 scenarios, 6 sweeps |
| B | LLM Generative Agents | Planned — not yet started |
| C | System Dynamics (PySD) | Planned — next priority |

**Triangulation rule:** A finding is robust only if it appears in ≥2 of 3 pathways.

## Key Findings (Pathway A)

- **Phase transition at ~80% displacement**: Baseline collapse probability jumps from 0% to 100%
- **UBI is necessary but insufficient**: At 95% displacement, UBI alone still has 2.7% collapse; 91% in individualist societies
- **Role programs outperform income transfers**: Roles (sink=0.388) vs UBI (sink=0.639) at 95%
- **Virtual worlds complement but can't substitute**: VW+UBI achieves near-zero sink; VW alone still 21% collapse at 95%
- **Social cohesion is the decisive moderator**: Collectivism drops UBI collapse from 91% → 0%
- **Historical validation**: Model reproduces Nauru (collapse) vs Gulf states (stability) divergence

## Reproducing Results

See [REPRODUCE.md](REPRODUCE.md) for step-by-step instructions.

```bash
git clone https://github.com/wukao1985/post-scarcity-abm.git
cd post-scarcity-abm
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make all-sweeps    # ~2-3 hours
make figures       # ~30 seconds
```

## Project Structure

```
post-scarcity-abm/
├── models/
│   └── pathway_a_abm/
│       ├── model.py           # PostLaborAgent + PostLaborModel
│       ├── runner.py          # Sweep runners (1-6)
│       └── report.py          # Sweep 1 figure generation
├── scripts/
│   └── sweep{2-6}_figures.py  # Figure generation scripts
├── data/
│   └── simulation/            # Output CSVs (see data/simulation/README.md)
├── reports/
│   ├── paper_draft.md         # Paper draft
│   ├── sweep{2-6}_analysis.md # Per-sweep analysis with critique
│   ├── historical_validation.md
│   └── figures/               # All generated figures
├── tests/
│   └── test_model.py          # 14 model tests
├── docs/
│   └── v3-experiment-design.md
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
- [V3 Experiment Design](docs/v3-experiment-design.md)
- [Sweep Analysis Reports](reports/) — per-sweep findings with self-critique
- [Output Manifest](outputs_manifest.md) — every generated file listed

## Obsidian Knowledge Base

Literature notes and research proposal: https://evergreen-notes.vercel.app
