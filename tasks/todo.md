# Project Tasks — Post-Scarcity ABM

## 🟡 Next Up

### Pathway C — System Dynamics
- [ ] Build stock-flow model in PySD
- [ ] Collect historical calibration data:
  - [ ] Russia 1991–2005 (male life expectancy, birth rate)
  - [ ] Japan hikikomori prevalence 1990–2024
  - [ ] US Appalachia employment vs opioid mortality
  - [ ] Finland UBI pilot 2017–2018
- [ ] Calibrate model to historical data
- [ ] Run 6 policy scenarios

### Pathway B — LLM Agents
- [ ] Design agent personality profiles (resilient/balanced/vulnerable)
- [ ] Write agent system prompts with SDT need states
- [ ] Design 3-phase experimental protocol
- [ ] Run pilot (10 agents, 30 steps)
- [ ] Code qualitative outputs for behavioral typology

### Model Improvements (from self-critique)
- [ ] Increase stochasticity (noise σ from 0.02 to 0.05+)
- [ ] Fix gradual speed artifact (use 0.012/step to reach 0.95)
- [ ] Add non-additive intervention interactions
- [ ] Re-parameterize aggressor threshold
- [ ] Add endogenous adaptation mechanism

## ✅ Completed

- [x] Research Proposal written
- [x] Literature review (12 papers)
- [x] Obsidian knowledge base built
- [x] V2 simulation analyzed
- [x] Evergreen deployed
- [x] V3 experiment design finalized
- [x] GitHub repo created and pushed
- [x] Phase 1: Port V2 model to clean Python Mesa 3.5 codebase
- [x] Phase 1: Add V3 variables (automation_speed, virtual_world_quality, collectivism_index)
- [x] Phase 1: Add V2 scenarios (baseline, UBI, roles, fairness, full_bundle)
- [x] Phase 1: Sweep 1 validation (50 runs/point, 9 PL levels x 5 scenarios = 2,250 runs)
- [x] Phase 1: Validation report + figures generated
- [x] Phase 2: Sweep 2 — Automation speed (3,000 runs)
- [x] Phase 2: Sweep 3 — Virtual world quality (3,600 runs)
- [x] Phase 2: Sweep 4 — Collectivism index (3,600 runs)
- [x] Phase 2: Sweep 5 — Archetype time series (100 runs, 8,100 timesteps)
- [x] Phase 2: Sweep 6 — Full 10-scenario grid (4,500 runs, 150/point)
- [x] Phase 3: Analysis reports for sweeps 2-6
- [x] Phase 3: Publication-quality figures (20+ figures)
- [x] Phase 3: Historical validation (Nauru vs. Gulf states)
- [x] Phase 4: Paper draft (reports/paper_draft.md)
- **Total simulation runs: 17,050**
