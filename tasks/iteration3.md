# Claude Code Task — Iteration 3: Route A Reframing
**Source:** tasks/academic_review_iteration2.txt (Codex review)
**Goal:** Reframe paper to match what the model actually does. No code changes. Paper only.

---

## The Core Problem
The paper claims to study "chronic role deprivation → meaning loss → behavioral cascade."
But the model doesn't implement chronic displacement — it re-samples who is displaced each step.
This makes Issues #1 and #2 fatal flaws under the current framing.

## The Fix (Route A)
Reframe the research question as: "What equilibrium states does a post-labor society reach at different displacement levels, and how do interventions shift those equilibria?"
This is what the model actually measures. It's a legitimate contribution. Issues #1 and #2 become design choices, not flaws.

---

## Specific Changes (in order)

### 1. Rewrite Title
Old: "Behavioral Sink Under Post-Labor Displacement: Mechanisms of Meaning Loss, Social Contagion, and Intervention"
New: "Equilibrium Dynamics of Meaning and Behavioral Sink in Post-Labor Societies: A Stylized Agent-Based Analysis"
(Or similar — captures "equilibrium" and "stylized" explicitly)

### 2. Rewrite Abstract
- Remove: "mechanisms of meaning loss", "behavioral cascade", "chronic role deprivation"
- Add: "cross-sectional equilibrium analysis", "what stable states societies reach at different displacement levels"
- Keep: all 4 numbered findings (they're still valid as equilibrium findings)
- Add sentence: "The model does not represent individual unemployment trajectories; instead, it characterizes population-level equilibria under sustained role displacement."

### 3. Rewrite Introduction / Research Questions
Replace RQ framing from:
  "What mechanisms drive behavioral sink?" (implies dynamic process)
To:
  "What equilibrium configurations characterize post-labor societies under different displacement levels and intervention regimes?"
  "How do social cohesion and intervention combinations shift the collapse threshold?"

Remove phrases throughout intro: "chronic deprivation", "scarring", "transition trajectories", "cumulative exclusion"

### 4. Fix Methods Section — Model Description
In §2.1 or §2.2, add explicit paragraph:
"**Modeling displacement as a population-level rate.** In this model, post_labor_fraction represents the share of the population lacking productive roles at any given timestep, not a permanent individual state. At each step, this fraction is drawn from the agent pool, representing the turnover inherent in labor markets even under high automation. This design treats displacement as a structural condition of the society rather than a permanent individual trajectory — appropriate for studying equilibrium properties, though it precludes claims about individual scarring or transition dynamics. Persistent individual displacement is a natural extension for future work."

### 5. Fix §2.3 Speed of Automation
Current claim: "gradual automation reaches 95% by step 80"
This is mathematically impossible at 0.01/step (0.01 × 80 = 0.80).
Fix: Clarify that Sweep 2 compares automation at 80% (gradual = 80 steps to reach it) vs rapid (reaching it in ~5 steps). Do NOT claim gradual reaches 95% — remove those claims.
The speed effect finding is still valid at PL=0.80 comparison.

### 6. Fix §2.2 Meaning Formula
Paper says meaning = weighted sum. Code also subtracts contagion and adds resilience shock.
Fix: Update the formula in the paper to match the actual code implementation exactly.
Delete all references to "contribution_to_nonplayers" — this variable does not exist in the code.

### 7. Fix §3.3 Intervention Independence Claim
Paper implies UBI, roles, fairness are independent interventions.
But: UBI partly sets fairness (model.py:211-213), roles affect both economic_role and competence.
Fix: Add sentence in Methods §2.4: "Note that in our implementation, the UBI scenario includes a fairness boost (reflecting UBI's social legitimacy signal), and role programs enhance both economic role and competence directly. These couplings are intentional design choices reflecting real-world co-occurrence of interventions."

### 8. Add Missing Literature (§References + cite in text)
Add these 6 citations with in-text hooks:

a) Jahoda, M. (1982). Employment and unemployment: A social-psychological analysis. Cambridge University Press.
   Hook: in Introduction where we discuss psychological functions of work (§1.1)

b) Acemoglu, D., & Restrepo, P. (2018). The wrong kind of AI? Artificial intelligence and the future of labour demand. Cambridge Journal of Regions, Economy and Society, 11(1), 29-44.
   Hook: §1.1 automation and labor

c) Grimm, V., et al. (2020). The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism. JASSS, 23(2), 7.
   Hook: §2.1 "following ODD protocol conventions..."

d) Centola, D., & Macy, M. (2007). Complex contagions and the weakness of long ties. American Journal of Sociology, 113(3), 702-734.
   Hook: §2.1 where we describe contagion mechanism

e) Ross, M. (2012). The oil curse: How petroleum wealth shapes the development of nations. Princeton University Press.
   Hook: §3.7 historical validation, Gulf states

f) Rosso, B. D., Dekas, K. H., & Wrzesniewski, A. (2010). On the meaning of work: A theoretical integration and review. Research in Organizational Behavior, 30, 91-127.
   Hook: §1.2 "meaning" construct definition

### 9. Update Limitations Section
Add/expand:
"**Displacement as population-level rate.** The model treats role displacement as a cross-sectional share rather than a permanent individual state. This enables equilibrium analysis but precludes conclusions about individual adjustment trajectories, unemployment scarring, or the dynamics of managed transitions. Future work should model persistent individual displacement with explicit re-employment mechanisms."

"**Intervention coupling.** Our UBI and roles scenarios have partially overlapping effects in the implementation (UBI affects fairness; roles affect competence directly). Fully orthogonal intervention comparisons would require additional decoupling in the model architecture."

### 10. Final consistency check
After all changes: grep the paper for these phrases and remove/replace each one:
- "chronic" → if referring to individual displacement, replace with "sustained" or "structural"
- "scarring" → delete
- "transition trajectory" → replace with "cross-sectional snapshot"
- "contribution_to_nonplayers" → delete
- "gradual.*0.95" or "95%.*gradual" → fix per Step 5

---

## Completion Criteria
- [ ] Title updated to reflect equilibrium framing
- [ ] Abstract has "cross-sectional equilibrium" language, no "chronic deprivation"
- [ ] §2 has explicit paragraph about displacement-as-rate design choice
- [ ] Speed claims fixed (no impossible gradual-to-0.95 claim)
- [ ] Meaning formula matches code; contribution_to_nonplayers gone
- [ ] UBI-fairness coupling disclosed in Methods
- [ ] 6 new citations added with in-text hooks
- [ ] Limitations expanded with displacement-as-rate + coupling caveats
- [ ] grep check: no remaining "scarring", "chronic" in individual context, no impossible speed claims
- [ ] Commit: "Route A reframing: equilibrium study positioning + fix Issues #2-6"

## Do NOT change
- Any simulation data or CSV files
- Model code (model.py, runner.py)
- Core quantitative findings
- Overall paper structure
