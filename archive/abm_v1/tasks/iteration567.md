# Claude Code Task — Iterations 5+6+7: Fix Issue #3 (Structural Sensitivity)
**Source:** tasks/future_research_spec.md — Issue #3
**Goal:** Address the "Roles > UBI is partly tautological" problem. Run ablations, decouple interventions, update paper with honest conditional findings.

## Background
The Codex reviewer flagged that "Roles outperform UBI" is partly built into the model:
- Roles affect: economic_role (0.35 strength) AND competence (extra pathway)
- UBI affects: economic_role only (0.30 strength)
- Virtual role has 0.1 weight vs economic role 0.8 weight (8:1 ratio)

We need to show WHICH part of the advantage is structural assumption vs emergent finding.

---

## Experiment A — Weight Ablation (virtual vs economic role ratio)
Tests whether "virtual worlds can't replace real roles" is robust or purely assumption-driven.

Write a new sweep (in runner.py or a new script):
- Vary the economic_role weight in contribution formula: [0.4, 0.5, 0.6, 0.7, 0.8 (current), 0.9]
- Correspondingly vary virtual_role weight = 1 - economic_weight (keeping sum = 1.0, not 0.9)
  Wait: current is economic=0.8, virtual=0.1, total=0.9. Let's keep other weights fixed.
  Actually: vary RATIO while keeping total contribution the same:
  - Ratio 3:1 → economic=0.675, virtual=0.225 (total stays 0.9)
  - Ratio 5:1 → economic=0.75, virtual=0.15
  - Ratio 8:1 → economic=0.80, virtual=0.10 (current)
  - Ratio 12:1 → economic=0.844, virtual=0.056
  - Ratio infinity → economic=0.9, virtual=0.0

- Fixed: PL=0.95, scenarios: [baseline, ubi_only, virtual_only (ubi=0, vw=1.0), ubi_plus_virtual]
- 50 runs per condition
- Total: 5 ratios × 4 scenarios × 50 = 1,000 runs
- Save to: data/simulation/ablation_weights.csv

Key question: At what ratio does virtual_only approach ubi_only? If only at ratio < 3:1, finding is robust. If it requires > 5:1, finding is assumption-driven.

## Experiment B — Intervention Decoupling
Tests how much of Roles > UBI comes from structural advantage vs mechanism.

Create three intervention variants (modify runner, not model.py permanently):
- ubi_pure: UBI restores economic_role = ubi * 0.30 only (current behavior, no competence)
- roles_matched: roles restore economic_role = roles * 0.30 ONLY (same strength as UBI, no competence boost)
- roles_full: current behavior (economic_role = roles * 0.35 + competence boost)

Run at PL=0.95 with 150 runs each.
Save to: data/simulation/ablation_interventions.csv

Key question: When matched on economic_role restoration strength, does Roles still beat UBI? 
→ If yes: competence pathway matters
→ If no: it was just about strength, not mechanism

## Experiment C — ODD Protocol Compliance
JASSS reviewers expect ODD/ODD+D format. Add an ODD-compliant model description.
Write reports/ODD_protocol.md with sections:
1. Purpose
2. Entities, state variables, scales
3. Process overview and scheduling
4. Design concepts (emergence, adaptation, learning, etc.)
5. Initialization
6. Input data
7. Submodels

Use paper_draft.md + model.py as source. This is documentation, not new code.

---

## Analysis and Paper Updates

After all experiments:

### Weight Ablation Results → paper update:
In §3.2 (virtual worlds section), add:
"The virtual-world ceiling is partially structural: our default 8:1 contribution weight (economic vs virtual) was varied from 3:1 to ∞. At ratios below 5:1, virtual-world-only scenarios approach UBI performance (sink difference < 0.05). At the current 8:1 assumption, the gap is 0.XX. This confirms the finding is assumption-sensitive: societies where virtual engagement carries greater psychological weight would see different equilibria."

### Intervention Decoupling Results → paper update:
In §3.3 (intervention comparison), add:
"To isolate the source of role programs' advantage, we ran a matched comparison where UBI and roles were equalized on economic_role restoration strength. Under this condition, roles_matched (no competence boost) vs ubi_pure shows [result]. The competence pathway accounts for approximately [X]% of the advantage. This suggests role programs' superiority is partly mechanistic (competence development) and partly parameterization (stronger restoration strength by default)."

### Update Limitations section:
Add: "Our intervention comparisons reflect specific parameterization choices about relative strength of UBI vs role programs. Ablation analysis (see Supplementary) shows the directional finding (roles > UBI) is robust across a range of parameter values, but the magnitude depends on assumptions about the relative potency of different interventions."

### Add V5 Future Work paragraph (end of Discussion):
"These findings suggest several natural extensions. First, a V5 model with persistent individual displacement states would enable study of unemployment scarring, managed transitions, and trajectory heterogeneity that the current equilibrium model cannot address. Second, empirical calibration of the economic-to-virtual contribution weight ratio from survey data on meaningful engagement would transform our sensitivity finding into a testable prediction. Third, a multi-site validation using deindustrialization data (Rust Belt, post-Soviet transitions) and resource-curse cases beyond Nauru and Gulf states would strengthen construct validity."

---

## Completion Criteria
- [ ] data/simulation/ablation_weights.csv (1,000 rows)
- [ ] data/simulation/ablation_interventions.csv (450 rows)
- [ ] reports/ablation_analysis.md with key findings
- [ ] reports/ODD_protocol.md (complete ODD description)
- [ ] paper_draft.md updated: weight ablation finding in §3.2, decoupling in §3.3, updated limitations, V5 future work paragraph
- [ ] Commit: "Iteration 5-7: weight ablation + intervention decoupling + ODD protocol"
