# Project Tasks — Post-Scarcity ABM

## 🟡 Next Up

### Pathway B — LLM Agents
- [ ] Design agent personality profiles (resilient/balanced/vulnerable)
- [ ] Write agent system prompts with SDT need states
- [ ] Design 3-phase experimental protocol
- [ ] Run pilot (10 agents, 30 steps)
- [ ] Code qualitative outputs for behavioral typology

### Model Improvements (remaining)
- [ ] Add non-additive intervention interactions
- [ ] Add endogenous adaptation mechanism
- [ ] Further reduce Cohen's d (target 1-5, currently ~9-12)
- [ ] Increase aggressor prevalence to 10-20% (currently ~2-3%)

### Paper Improvements
- [ ] Sensitivity analysis: ±20% on top 3 parameters (add to methods appendix)
- [ ] Expand paper to JASSS target length (currently ~3,950 words, target 8,000-12,000)
- [ ] Pathway C formal calibration to additional historical cases

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
- [x] V4: Increase stochasticity (noise σ 0.02→0.08 + agent shocks)
- [x] V4: Fix gradual speed artifact (runner computes target/80)
- [x] V4: Re-parameterize aggressor threshold (meaning < 0.40)
- [x] V4: Re-run Sweep 1 validation (2,250 runs)
- [x] V4: Re-run Sweep 2 automation speed (3,000 runs)
- [x] V4: Validation report (reports/v4_validation.md)
- [x] V4: Update paper draft with V4 results
- [x] Methods appendix (reports/methods_appendix.md)
- [x] Pathway C: SD model (models/pathway_c_sd/sd_model.py)
- [x] Pathway C: Nauru + Gulf calibration
- [x] Pathway C: ABM-SD directional comparison
- [x] Pathway C: Initial report (reports/pathway_c_initial.md)
- **Total simulation runs: ~22,300** (17,050 V3 + 5,250 V4)
