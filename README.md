# Post-Scarcity ABM

**What is this?** An agent-based model simulating behavioral sink in post-labor societies—what happens to meaning, social cohesion, and well-being when most people are displaced from productive roles?

**Paper status:** Under review at JASSS

---

## Quick Start

```bash
# Run main simulation (Sweep 1: 2,250 runs, ~5 minutes)
python models/pathway_a_abm/runner.py 1

# Generate figures
python models/pathway_a_abm/report.py

# Run all tests
python -m pytest tests/ -v
```

See [REPRODUCE.md](REPRODUCE.md) for full reproduction of all 22,000+ runs.

---

## Key Files

| File | Purpose |
|------|---------|
| `models/pathway_a_abm/model.py` | Main ABM (PostLaborAgent + PostLaborModel classes) |
| `models/pathway_a_abm/runner.py` | Run sweeps 1-6: `python runner.py [1-6]` |
| `models/pathway_a_abm/report.py` | Generate Sweep 1 figures |
| `reports/paper_draft.md` | Paper draft (JASSS format) |
| `REPRODUCE.md` | Full reproduction instructions |

---

## Project Structure

```
models/pathway_a_abm/    # Main ABM code (Pathway A)
models/pathway_c_sd/     # System dynamics (Pathway C)
data/simulation/         # Simulation outputs (CSV)
reports/                 # Figures, paper draft, analysis
scripts/                 # Additional figure generation
 tests/                   # Test suite (14 tests)
```

---

## Model Findings (Pathway A)

Key findings from 22,000+ simulation runs:

- **Phase transition at ~80-90% displacement**: Baseline collapse rises sharply from 2% to 100%
- **UBI necessary but insufficient**: At 95% displacement, UBI alone produces sink=0.518
- **Role programs outperform income transfers**: Roles (sink=0.459) vs UBI (sink=0.518) at 95% displacement
- **Virtual worlds complement but cannot substitute**: VW+UBI achieves near-zero sink; VW alone provides partial protection
- **Social cohesion moderates intervention effectiveness**: Collectivist structures reduce UBI-associated sink

---

## Documentation

- [Paper Draft](reports/paper_draft.md)
- [Methods Appendix](reports/methods_appendix.md) — parameter justifications
- [V3 Experiment Design](docs/v3-experiment-design.md)
- [Paper-to-Repo Map](docs/paper_to_repo_map.md)
- [Reproduction Checklist](docs/reproduction_checklist.md)

---

## Citation

If using this model, please cite the forthcoming JASSS paper.
