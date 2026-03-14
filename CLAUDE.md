# CLAUDE.md — Post-Scarcity ABM

## Project Overview
Multi-pathway simulation of behavioral sink under AI automation.
Read `docs/v3-experiment-design.md` before starting any work.
Read `tasks/todo.md` for current task status.

## Stack
- Python 3.11+
- Mesa (agent-based modeling)
- PySD (system dynamics)
- pandas, numpy, matplotlib, seaborn
- Jupyter notebooks for analysis

## Setup
```bash
pip install mesa pysd pandas numpy matplotlib seaborn jupyter
```

## Project Structure
```
models/pathway_a_abm/    # Main ABM code
models/pathway_b_llm/    # LLM agent experiments
models/pathway_c_sd/     # System dynamics
data/historical/         # Calibration datasets (CSV)
data/simulation/         # Model outputs (CSV/JSON)
reports/                 # PDF reports
notebooks/               # Analysis .ipynb files
```

## Coding Standards
- Every model run must save parameters + outputs to data/simulation/
- Use seed for reproducibility: `np.random.seed(42)` per run
- Monte Carlo: always 150 runs minimum per parameter point
- Output format: CSV with columns [run_id, step, param_*, metric_*]
- Report generation: use matplotlib, save to reports/

## Key Constants (from V2)
- Population: 200 agents
- Time horizon: 80 steps
- Collapse threshold: sink_index > 0.7
- Known threshold: ~80% post-labor

## Git
```bash
git add -A
git commit -m "description"
git push origin main
```
Remote: https://github.com/wukao1985/post-scarcity-abm

## After Each Task
Update tasks/todo.md with completed items.
