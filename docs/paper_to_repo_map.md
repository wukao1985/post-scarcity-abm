# Paper-to-Repository Map

Maps every section of `reports/paper_draft.md` to the specific code, data, and analysis files that support it.

## Paper Section → Code/Data Mapping

| Paper Section | Repository File(s) | Notes |
|---|---|---|
| **Abstract** | `reports/paper_draft.md` | Summary numbers from sweep results |
| **1. Introduction** | `README.md`, `docs/v3-experiment-design.md` | Research questions, theoretical framing |
| **2.1 Model Overview** | `models/pathway_a_abm/model.py` | `PostLaborAgent` + `PostLaborModel` classes |
| **2.2 Psychological Update** | `models/pathway_a_abm/model.py:73-167` | `step()` method: mean-reverting dynamics |
| **2.2 Meaning Function** | `models/pathway_a_abm/model.py:48-56` | `_compute_meaning()` weights |
| **2.2 Weight Justification** | `reports/methods_appendix.md` §2 | SDT vs calibration vs convenience |
| **2.3 Archetype Classification** | `models/pathway_a_abm/model.py:170-180` | Threshold rules in `step()` |
| **2.4 Simulation Design** | `models/pathway_a_abm/runner.py` | `run_sweep_1()` through `run_sweep_6()` |
| **2.5 Analysis** | `scripts/sweep*_figures.py`, `models/pathway_a_abm/report.py` | Figure generation |
| **3.1 Phase Transition (RQ1)** | `data/simulation/sweep1_results.csv` | 2,250 runs, 9 PL levels × 5 scenarios |
| **3.2 Virtual Worlds (RQ2)** | `data/simulation/sweep3_virtual_world.csv` | 3,600 runs, 6 VW levels |
| **3.3 Speed of Collapse (RQ3)** | `data/simulation/sweep2_automation_speed.csv` | 3,000 runs, gradual vs rapid |
| **3.4 Collectivism (RQ4)** | `data/simulation/sweep4_collectivism.csv` | 3,600 runs, 6 collectivism levels |
| **3.5 Interventions (RQ5)** | `data/simulation/sweep6_full_grid.csv` | 4,500 runs, 10 scenarios × 3 PL levels |
| **3.6 Archetype Trajectories** | `data/simulation/sweep5_archetypes.csv` | 100 runs, full 81-step time series |
| **3.7 Historical Analogues** | `reports/historical_validation.md` | Nauru vs Gulf states mapping |
| **4.1-4.3 Discussion** | `reports/paper_draft.md` | Interpretation + limitations |
| **4.4 Pathway C Triangulation** | `models/pathway_c_sd/sd_model.py`, `reports/pathway_c_initial.md` | SD model + comparison |
| **V4 Validation** | `reports/v4_validation.md` | V3 vs V4 comparison table |
| **Methods Appendix** | `reports/methods_appendix.md` | Full parameter documentation |
| **Figures** | `reports/figures/` | All generated PNG figures |

## Data Files

| File | Sweep | Runs | Key Variables |
|---|---|---|---|
| `sweep1_results.csv` | 1: Post-labor levels | 2,250 | meaning_index, sink_index, sink_collapsed, archetype fracs |
| `sweep2_automation_speed.csv` | 2: Speed | 3,000 | + speed (gradual/rapid) |
| `sweep3_virtual_world.csv` | 3: Virtual worlds | 3,600 | + virtual_world_quality |
| `sweep4_collectivism.csv` | 4: Collectivism | 3,600 | + collectivism_index |
| `sweep5_archetypes.csv` | 5: Time series | 8,100 rows | Full 81-step trajectories |
| `sweep6_full_grid.csv` | 6: Full grid | 4,500 | 10 scenarios × 3 PL levels |

## Figure Scripts

| Figure in Paper | Script | Output |
|---|---|---|
| Figure 1 (phase transition) | `models/pathway_a_abm/report.py` | `reports/figures/sweep1_*.png` |
| Figure 2 (virtual worlds) | `scripts/sweep3_figures.py` | `reports/figures/sweep3_*.png` |
| Figure 3 (speed effect) | `scripts/sweep2_figures.py` | `reports/figures/sweep2_*.png` |
| Figure 4 (collectivism) | `scripts/sweep4_figures.py` | `reports/figures/sweep4_*.png` |
| Figure 5 (archetypes) | `scripts/sweep5_figures.py` | `reports/figures/sweep5_*.png` |
| Pathway C comparison | `models/pathway_c_sd/sd_model.py` | `reports/figures/pathway_c_comparison.png` |

## Tests

| Test File | Coverage |
|---|---|
| `tests/test_model.py` | 17 tests: agent creation, dynamics, interventions, reproducibility, virtual role |

Run: `python -m pytest tests/ -v`
