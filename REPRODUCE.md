# Reproducing Results

## 1. Environment Setup

Developed on Python 3.14.2; compatible with Python 3.12+.

```bash
git clone https://github.com/wukao1985/post-scarcity-abm.git
cd post-scarcity-abm
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Key dependencies (exact versions in `requirements_locked.txt`):
| Package | Version | Purpose |
|---------|---------|---------|
| Mesa | 3.5.0 | Agent-based modeling framework |
| numpy | 2.4.3 | Numerical computation |
| pandas | 3.0.1 | Data handling |
| matplotlib | 3.10.8 | Figure generation |
| seaborn | 0.13.2 | Statistical plots |
| networkx | 3.6.1 | Small-world network |
| scipy | 1.17.1 | System dynamics (Pathway C) |
| pytest | 9.0.2 | Test suite |

## 2. Figure-to-Script Map

Every figure and table referenced in the paper:

| Paper Location | Description | Generation Script | Input Data |
|---|---|---|---|
| §3.1, Figure 1 | Phase transition curve (sink vs post-labor) | `models/pathway_a_abm/report.py` | `data/simulation/sweep1_results.csv` |
| §3.2, Figure 2 | Virtual world quality effect | `scripts/sweep3_figures.py` | `data/simulation/sweep3_virtual_world.csv` |
| §3.3 | Speed comparison table | Inline from `data/simulation/speed_clean_comparison.csv` | `data/simulation/speed_clean_comparison.csv` |
| §3.4, Figure 4 | Collectivism as moderator | `scripts/sweep4_figures.py` | `data/simulation/sweep4_collectivism.csv` |
| §3.5 | Intervention ranking table | Inline from sweep6 data | `data/simulation/sweep6_full_grid.csv` |
| §3.6, Figure 5 | Archetype trajectories | `scripts/sweep5_figures.py` | `data/simulation/sweep5_archetypes.csv` |
| §3.7 | Historical validation (Nauru/Gulf) | `scripts/sweep6_figures.py` | `data/simulation/sweep6_full_grid.csv` |
| §2.5 | Sensitivity analysis table | Inline from sensitivity data | `data/simulation/sensitivity_analysis.csv` |
| §2.4 | Horizon robustness table | Inline from convergence data | `data/simulation/convergence_summary.csv` |
| §3.2 (ablation) | Weight ablation results | `scripts/run_ablation_weights.py` | `data/simulation/ablation_weights.csv` |
| §3.5 (decoupling) | Intervention decoupling results | `scripts/run_ablation_interventions.py` | `data/simulation/ablation_interventions.csv` |
| §4.4 | Pathway C comparison | `models/pathway_c_sd/sd_model.py` | Generated inline |

## 3. Full Reproduction Order

From a fresh clone, run these steps in order:

```bash
# Step 0: Setup
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Step 1: Run all 6 primary sweeps (~2 hours total)
python models/pathway_a_abm/runner.py 1    # Sweep 1: baseline (2,250 runs, ~15 min)
python models/pathway_a_abm/runner.py 2    # Sweep 2: automation speed (3,000 runs, ~20 min)
python models/pathway_a_abm/runner.py 3    # Sweep 3: virtual world (3,600 runs, ~25 min)
python models/pathway_a_abm/runner.py 4    # Sweep 4: collectivism (3,600 runs, ~25 min)
python models/pathway_a_abm/runner.py 5    # Sweep 5: archetypes (100 runs, ~5 min)
python models/pathway_a_abm/runner.py 6    # Sweep 6: full grid (4,500 runs, ~30 min)

# Step 2: Run ablation studies (~15 min total)
python scripts/run_ablation_weights.py         # Weight ablation (1,000 runs, ~8 min)
python scripts/run_ablation_interventions.py   # Intervention decoupling (450 runs, ~5 min)

# Step 3: Generate all figures
python models/pathway_a_abm/report.py    # Sweep 1 figures
python scripts/sweep2_figures.py         # Sweep 2 figures
python scripts/sweep3_figures.py         # Sweep 3 figures
python scripts/sweep4_figures.py         # Sweep 4 figures
python scripts/sweep5_figures.py         # Sweep 5 figures
python scripts/sweep6_figures.py         # Sweep 6 figures

# Step 4: Run Pathway C (system dynamics)
python models/pathway_c_sd/sd_model.py

# Step 5: Verify
python -m pytest tests/ -v
```

Or use the Makefile shortcuts:
```bash
make all-sweeps    # Steps 1
make figures       # Step 3
make test          # Step 5
```

Note: Sensitivity analysis, horizon robustness, and speed comparison CSVs were generated in interactive analysis sessions and are committed to the repository. The primary sweeps and ablation studies are fully reproducible from the scripts above.

## 4. Expected Runtime

| Step | Sweep | Runs | Estimated Time |
|------|-------|------|---------------|
| 1 | Sweep 1 (baseline) | 2,250 | ~15 min |
| 1 | Sweep 2 (automation speed) | 3,000 | ~20 min |
| 1 | Sweep 3 (virtual world) | 3,600 | ~25 min |
| 1 | Sweep 4 (collectivism) | 3,600 | ~25 min |
| 1 | Sweep 5 (archetypes) | 100 | ~5 min |
| 1 | Sweep 6 (full grid) | 4,500 | ~30 min |
| 2 | Ablation: weights | 1,000 | ~8 min |
| 2 | Ablation: interventions | 450 | ~5 min |
| 3 | Figure generation | — | ~2 min |
| 4 | Pathway C | — | ~1 sec |
| **Total** | | **18,500** | **~2.5 hours** |

Estimates based on Apple M-series. Intel/AMD may be ~2x slower.

## 5. Verification

After running all sweeps:

```bash
python -m pytest tests/ -v
```

Expected: 14 tests pass (with FutureWarning about Mesa `seed` → `rng` migration).

## Reproducibility Notes

- All simulations use deterministic seeding via `seed` parameter
- Results should be identical across runs on the same platform
- Minor floating-point differences may occur across Python/NumPy versions
- Each sweep's runner prints progress to stdout
- See `data/simulation/README.md` for column descriptions of each CSV
- See `outputs_manifest.md` for a complete list of every generated file
