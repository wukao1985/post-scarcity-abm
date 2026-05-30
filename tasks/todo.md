# Project Tasks — Post-Scarcity ABM

> ## ⛔ 方向变更声明（2026-05-30）
>
> **旧的 ABM 后稀缺/behavioral-sink 模拟路线已停止。**
>
> 原因：经 ~20 轮评审，该模型卡在两个结构性、无法治愈的问题上：
> (1) **循环论证** — 核心结论几乎被 meaning 函数的定义直接推出，非模型涌现；
> (2) **不可证伪** — 模拟假想的 80% 失业未来，无 ground truth。
>
> **新方向**见 `so_sdt_study/`：用 ChatGPT 冲击（2022-11-30）这一真实自然实验 +
> 公开 Stack Exchange 数据，检验"按 SDT 动机类型分组的贡献者差异化流失"这一可证伪假说。
> 详见 `so_sdt_study/DESIGN.md`（预注册式设计文档）。
>
> 下方旧的 ABM 任务清单**仅作历史保留**，不再推进。

---

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
- [x] Iteration 5: Weight ablation — economic:virtual ratio sensitivity (1,000 runs)
- [x] Iteration 6: Intervention decoupling — matched UBI vs roles comparison (450 runs)
- [x] Iteration 7: ODD protocol (reports/ODD_protocol.md)
- [x] Ablation analysis report (reports/ablation_analysis.md)
- [x] Paper updated: weight ablation in §3.2, decoupling in §3.5, limitations, V5 future work
- **Total simulation runs: ~23,750** (17,050 V3 + 5,250 V4 + 1,450 ablation)
