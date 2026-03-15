# Claude Code Task — Iteration 2
**Generated from:** Codex review (iteration1)  
**Priority:** P1 first (data integrity), then P2 (reproducibility)

## Context
Read tasks/codex_review_iteration1.md before starting.
Read CLAUDE.md for project context.

## Tasks (in order)

### Task 1 — Re-run Sweeps 3–6 with V4 model [CRITICAL]
The paper currently presents Sweeps 3–6 as V4 results but the CSVs are from V3.
Re-run all four sweeps:
```bash
.venv/bin/python models/pathway_a_abm/runner.py 3   # virtual world quality
.venv/bin/python models/pathway_a_abm/runner.py 4   # collectivism
.venv/bin/python models/pathway_a_abm/runner.py 5   # archetypes
.venv/bin/python models/pathway_a_abm/runner.py 6   # full grid
```
After each sweep: verify CSV written to data/simulation/

### Task 2 — Fix requirements.txt
Add: `pytest>=7.0`

### Task 3 — Fix Pathway C matplotlib backend
In models/pathway_c_sd/sd_model.py, add near the top (before any import matplotlib.pyplot):
```python
import matplotlib
matplotlib.use('Agg')
```

### Task 4 — Fix compare_with_abm() stale values
In models/pathway_c_sd/sd_model.py, compare_with_abm() currently uses hardcoded V3 ABM values.
Replace with dynamic read from data/simulation/sweep1_results.csv:
```python
df = pd.read_csv('data/simulation/sweep1_results.csv')
# compute actual V4 baseline values from CSV
```

### Task 5 — Update paper numbers if sweeps changed significantly
After re-running sweeps 3–6, compare new results with paper_draft.md.
If any headline numbers changed by >5%, update paper_draft.md accordingly.
If stable, add one sentence to Methods: "Sweeps 3–6 confirmed numerically consistent with Sweeps 1–2 under V4 model."

## Completion criteria
- [ ] sweep3_virtual_world.csv, sweep4_collectivism.csv, sweep5_archetypes.csv, sweep6_full_grid.csv all fresh V4 data
- [ ] `pip install -r requirements.txt && python -m pytest tests/` passes on clean install
- [ ] `python models/pathway_c_sd/sd_model.py` runs without error on headless
- [ ] compare_with_abm() uses V4 values from CSV
- [ ] git commit: "Iteration 2: V4 sweeps 3-6 + reproducibility fixes"

## Time estimate
Sweeps 3–6 combined: ~2.5–3 hours compute
Code fixes: ~20 min
