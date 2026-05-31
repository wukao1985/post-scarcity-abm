# Submission Polish — Final 4 Items
**Goal:** Upgrade repo from "research-ready" to "fully submission-ready"

---

## Item 1 — Expand REPRODUCE.md to submission-grade

Current REPRODUCE.md is too short. Rewrite it to include:

### Section 1: Environment Setup (lock exact versions)
- Python 3.14.2 (or 3.12+ compatible)
- Key packages with exact versions from .venv (run `pip freeze` to get them)
- Command: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`

### Section 2: Complete Figure-to-Script Map
Create a table with every figure and table in the paper:
| Figure/Table | Script | Input CSV | Expected output |
|---|---|---|---|
| Fig 1 (phase transition) | ... | sweep1_baseline.csv | ... |
| etc. |

Read paper_draft.md to get all figure references, then map to actual scripts in models/ and reports/

### Section 3: Full Reproduction Order (from empty repo)
Step-by-step numbered list:
1. Setup environment
2. Run Sweep 1 (baseline): `python models/pathway_a_abm/runner.py 1` (~X min)
3. Run Sweep 2...
4. Run horizon robustness: ...
5. Run ablation studies: ...
6. Generate all figures: ...
Total estimated time: X hours

### Section 4: Expected Runtime Table
| Sweep | Runs | CPU time estimate |
|---|---|---|
| Sweep 1 (baseline) | 2,250 | ~8 min |
| etc. |

### Section 5: Verification
After running all sweeps: `pytest tests/ -v` — expected: all pass

---

## Item 2 — README top-section claim clarification

In README.md, find the section that describes the three pathways.
Add/update so the FIRST paragraph or a prominent callout box says:

"**Current paper claim:** This repository supports a paper based primarily on Pathway A (ABM, 18,500+ simulation runs) with initial directional support from Pathway C (system dynamics). Pathway B (LLM agent simulation) is planned as future work and is not part of the current paper's claims."

---

## Item 3 — Figure-to-script lock table (also in README)

Add a new section to README.md: "## Paper Figure Index"
List every figure/table in the paper with exact script and data file:

Example format:
```
| Paper location | Description | Script | Data |
|---|---|---|---|
| §3.1, Fig 1 | Phase transition curve | runner.py sweep 1 | sweep1_baseline.csv |
```

Read paper_draft.md figures (marked as `**Figure X:**`) and map each one.

---

## Item 4 — Dry run check

Run this test:
```bash
cd /Users/cloud/Documents/claude/post-scarcity-abm
source .venv/bin/activate
pip freeze > requirements_locked.txt  # lock exact versions
python models/pathway_a_abm/runner.py 1  # just sweep 1 as smoke test
pytest tests/ -v
```

Report any missing dependencies or broken paths.
Save requirements_locked.txt.

---

## Completion Criteria
- [ ] REPRODUCE.md: figure-to-script map, ordered steps, runtime table, version lock
- [ ] README: first-paragraph paper claim clarified (Pathway A + initial C, not B)
- [ ] README: "Paper Figure Index" table with all figures mapped to scripts/CSVs
- [ ] requirements_locked.txt committed
- [ ] All tests pass in dry run
- [ ] Commit: "Submission polish: reproducibility guide + figure index + dependency lock"
