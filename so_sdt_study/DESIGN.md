# Pre-Registration: Motivational Heterogeneity in Contributor Exodus from Stack Overflow after ChatGPT

**Status:** 🔒 **FROZEN (2026-05-30).** Classifier, hypotheses, thresholds, and analysis
plan below are locked *before* any post-shock outcome data is examined. Changes after this
point must be logged as amendments in §11 with date and rationale; the original frozen
text is never silently edited.
**Working title:** *Who leaves and who stays: a self-determination account of differential
contributor exodus from an online knowledge community after a generative-AI shock*

**What may already be touched (pre-shock):** cohort construction and motivation typing
(classification window 2021-11-30..2022-11-29). Query A has been run on real SO data
(§ RESULTS_A): ~50,305 core contributors, three types with genuine discriminant validity.
**What may NOT be touched until after this freeze:** any post-shock outcome (who exited,
who migrated). That is batch 2.

---

## 0. One-sentence summary

We test whether contributors who differed, *before* ChatGPT, in the **kind of motivation**
their Stack Overflow activity reveals — competence/mastery, status/recognition, or
relatedness/community — followed **different post-shock paths**: status-driven contributors
disproportionately **exit** the platform, relatedness-driven ones **migrate** to lower-effort
community roles (comments/edits), and competence-driven ones shift toward harder questions —
so the community does not uniformly shrink but **restructures along motivation lines**; and we
test whether this survives controls for pre-shock activity volume, tenure, and reputation.

---

## 1. Background and the gap we are filling

The post-ChatGPT decline of Stack Overflow is now well documented. We verified the four
closest papers from primary text (see `related_work_check.md`):

- **del Rio-Chanona, Laurentsyeva & Wachs (2024, *PNAS Nexus*)**: ~25% drop in SO activity within 6 months; DiD against Russian/Chinese SO and Math SE. Activity volume only.
- **Burtch, Lee & Chen (2024, *Scientific Reports*)**: ~16–20% drop within 15 weeks; event study, Reddit negative control. Notes community culture buffers, but does not decompose it into SDT needs.
- **Li & Kim (2024, *Marketing Letters*)**: SO answers, DiD, 9-day window. **Finds reputation/status-valuing contributors most demotivated.** Outcome = answer volume/quality among stayers; only "signals potential attrition" — does not measure churn. No survival analysis, no SDT triad.
- **Shan & Qiu (forthcoming *ISR*)**: SO answers, DiD + synthetic control. Finds AI *raises* contribution (learning effect). **Uses a Cox model — but on inter-answer DURATION (answering faster), not on exodus.** No SDT, no motivation typing, no churn outcome.

**What is already settled:** activity fell on average (though Shan & Qiu and Su et al. find learning effects raising it); and the status/reputation-valuing contributor is hit hardest (Li & Kim).

**What is NOT done:** every study measures activity *volume/quality* and segments by *volume / tenure / reputation*. None (a) segments users by the **full SDT triad** (competence vs status vs relatedness), (b) uses **survival analysis on contributor exodus** (Shan & Qiu's Cox is on answering speed, a different estimand), or (c) distinguishes **exit from migration** to lower-effort roles. The lab literature (Nature *Sci. Rep.* 2025/2026 on AI undermining intrinsic motivation/self-efficacy/meaning; CHI 2026 "Automating the Joy Out of Work") shows the *mechanism* exists but never connects it to *observed exodus* in a real community.

**Our contribution is the bridge:** an SDT reading of *who leaves vs who migrates*, tested as a falsifiable survival prediction on public data.

### Two honest concessions (frozen wording discipline)

1. **"Status-type hit hardest" is not our original claim.** Li & Kim already showed reputation-valuing contributors are most demotivated. We **replicate and extend** it (to exodus, and against competence/relatedness), not claim it as novel.
2. **"Survival analysis on SO" is not unprecedented.** Shan & Qiu used Cox on *inter-answer duration*. We must always state our estimand precisely: **time-to-exodus (permanent departure), not answering speed.** Same tool, different question — they ask "how fast do stayers answer," we ask "does the person stay at all."

### The novelty hinge vs prior segmentation

Prior work splits users by **how much** they participate (casual/intensive — Quinn & Gutt) or by **reputation** (Li & Kim). We split by **which SDT need** their behavior serves. These are different axes: a "casual" user can be relatedness-driven; a high-reputation user can be competence- rather than status-driven. **The critical test of our novelty is whether motivation type predicts exodus *after controlling for pre-shock activity volume, tenure, and reputation.*** If it does not — if motivation type is just a proxy for volume/reputation — we have *not* added beyond Li & Kim / Quinn & Gutt, and we will report that honestly as a null contribution.

**A favorable backdrop:** because Shan & Qiu and Su et al. find AI *raises* average contribution (learning effect), a finding that a *specific motivation type permanently exits* would be counterintuitive against a positive/neutral average — sharper, not weaker.

---

## 2. Theory and the core hypothesis

SDT (Deci & Ryan) posits three needs: **competence** (mastery/efficacy), **relatedness** (social connection), and **autonomy** (self-direction). On a Q&A platform, answering questions can serve different needs for different people:

- **Competence/mastery-seekers** participate to solve hard problems and improve skill. ChatGPT removes *easy* problems but the *hard frontier* remains under-served by AI. Their need can still be met on-platform → **least likely to leave.**
- **Status-seekers** participate for reputation, badges, rank, and the scarcity-value of being the one who answers. ChatGPT makes answers abundant and instantaneous, collapsing the scarcity that made status accrue → **most likely to leave.**
- **Relatedness-seekers** participate for community, recurring interaction, and belonging. ChatGPT does not provide community → their need is AI-resistant → **likely to stay**, intermediate-to-low exodus.

### H1 (primary, directional, falsifiable)

After the ChatGPT shock, the hazard of contributor exodus orders as:

> **Status-driven > Competence-driven ≈/> Relatedness-driven**

controlling for pre-shock activity volume, tenure, and reputation.

**Falsification:** if the three groups show no significant difference in post-shock exodus hazard once controls are included, OR if the ordering is reversed (e.g. relatedness-driven leave fastest), H1 is rejected. We commit to reporting whichever result the data give.

### H2 (secondary, mechanism-consistency)

Among *stayers*, competence-driven users shift their answering toward **harder** questions post-shock (difficulty of answered questions rises more for competence-driven than for status-driven users). This is the behavioral fingerprint of "the need can still be met at the frontier."

**Falsification:** no differential difficulty shift, or status-driven users shift to harder questions as much as competence-driven.

### H3 (PROMOTED to primary — exit vs migration)

This is the surviving kernel of the abandoned post-labor model, now a falsifiable core
claim: *the community does not uniformly shrink; it restructures along motivation lines.*
When AI removes the answering role, contributors split into two paths:

- **Exit** — stops answering AND stops other engagement (comments, edits). Truly gone.
- **Migration** — stops answering BUT keeps/increases low-effort engagement (comments,
  edits, curation). Survives as a different kind of participant.

> **H3:** Status-driven contributors disproportionately **exit** (no substitute outlet for
> the status their answering provided), while relatedness-driven contributors
> disproportionately **migrate** to comment/edit roles (their need is still met there).
> Competence-driven contributors are intermediate (some migrate to harder questions, per H2).

**Falsification:** if exiters vs migrators do not differ by motivation type, or if status-driven
contributors migrate as much as relatedness-driven, H3 is rejected.

**Data caveat (frozen):** migration is measured via **comments and post-edits** (both carry
UserId in the SO dump). **Votes are anonymous in the public dump (no UserId), so voting
cannot be tracked** — we do not rely on it. This narrows "migration" to comment/edit
activity; stated as a limitation.

**Framing payoff:** H3 turns "AI shrinks the community" (known) into "AI *restructures* the
community along motivation lines" (new). It is the study's most distinctive contribution and
the one no prior paper touches.

---

## 3. Data

- **Source:** public Stack Exchange data dump (2025-12-31 community release on archive.org; mirror at communitydatadump.com; cross-check via BigQuery `bigquery-public-data.stackoverflow` and SEDE).
- **Tables used:** `Users` (creation date, reputation), `Posts` (questions/answers, timestamps, tags, scores, accepted flag), `Comments` (timestamps, author), `Votes` (aggregate per post), `Badges` (type, date), `PostHistory` (edits), `Tags`.
- **Primary unit:** registered user with non-trivial pre-shock activity (see cohort definition).
- **Control community (for DiD robustness):** Math StackExchange (less AI-substitutable in the relevant period) and/or non-CS Stack Exchange sites. Used to confirm effects are AI-shock-specific, not secular platform decline.

### Time windows (FROZEN)

- **Shock date:** 2022-11-30 (ChatGPT public release).
- **Pre-shock window ("classification window"):** 2021-11-30 → 2022-11-29 (12 months). **All user typing uses ONLY this window.**
- **Washout:** 2022-11-30 → 2023-01-31 (excluded from outcome to avoid immediate novelty spike).
- **Outcome window ("exodus window"):** 2023-02-01 → 2024-01-31 (12 months), with survival follow-up extended where data allow.
- **Placebo shock (for falsification of the design itself):** 2021-11-30. We re-run the entire pipeline pretending the shock was one year earlier. If we find the "same" effect at the placebo date, our identification is broken and H1 results are void.

---

## 4. Cohort definition (FROZEN before outcomes)

Include a user if, **in the classification window**, they:

- created an account on or before 2022-08-31 (≥3 months tenure at shock, so typing is stable), AND
- posted **≥ 5 answers** in the classification window (we are studying *contributors*, the population whose meaning-bearing activity AI targets; pure askers are a separate, already-studied population we analyze only as a comparison baseline).

We will report cohort size and sensitivity to the ≥5 threshold (also run at ≥3 and ≥10).

---

## 5. Operationalizing motivation type — the scientific crux

**This is where the study lives or dies.** The danger is circularity: if we define "status-driven" using a variable that mechanically predicts leaving, we prove nothing. Guardrails:

1. **Classification uses ONLY pre-shock behavior.** Outcomes use ONLY post-shock behavior. No outcome variable may enter the classifier.
2. **No variable that is itself "amount of activity"** may define a type (volume is a *control*, not a type). Types are about *composition/style*, not *quantity*.
3. The classifier formula is **frozen in this document** before any post-shock data is read.

### 5a. Behavioral indices (computed on classification window only)

Each is a per-user ratio or normalized score, deliberately volume-invariant:

**Competence / mastery index** (high = answers hard things, invests in correctness, indifferent to easy wins):
- mean difficulty of questions answered (difficulty proxy = question's eventual answer count inverted, and tag rarity; lower answer-count questions = harder; see 5c)
- share of answers to questions with **0 existing answers at time of posting** (pioneering hard/unanswered problems)
- self-edit rate of own answers (revisiting for correctness)
- *negative* loading: share of answers to high-traffic "easy point" questions

**Status index** (high = optimizes for reputation/recognition):
- badge-acquisition rate (esp. reputation-linked badges)
- share of answers posted **fast** on high-view/high-score questions (racing for points)
- answering questions that already have ≥3 answers (competing for marginal reputation)
- sensitivity to acceptance (share of effort on questions likely to accept)

**Relatedness index** (high = social/community engagement beyond answering):
- comments-per-answer ratio
- share of interactions that are **repeat** interactions with the same users (recurring dyads)
- participation on Meta / discussion / review queues (if recoverable)
- editing *others'* posts (community maintenance)

### 5b. From indices to types — FROZEN: continuous primary + categorical companion

Each user gets three z-scored indices (competence_z, status_z, relatedness_z), computed
over the cohort on the classification window only.

- **PRIMARY — continuous.** The three continuous z-scored indices enter the Cox model
  directly as predictors. No user is forced into a box; full strength information is retained;
  this is the model that cleanly answers "does motivation predict exodus *net of* volume,
  tenure, reputation." All headline statistical claims come from here.
- **COMPANION — categorical.** Each user is also assigned a **dominant type** = argmax of
  the three z-scores. Used only for interpretable storytelling: Kaplan–Meier survival curves
  by type, and "type X exits at N× the rate of type Y" sentences. Never the basis of a
  headline causal claim.
- **CONFIRMATORY — data-driven structure.** factor analysis / k-means on the index battery;
  map discovered clusters onto SDT needs; check they match the a-priori typing. If the
  data-driven structure sharply contradicts the theoretical one, the typology is reported as
  not robust and H1/H3 downgraded to exploratory.

#### FROZEN rule: continuous–categorical inconsistency → mandatory deep dive

The continuous model is authoritative. **But if the categorical companion (KM curves / type
HRs) contradicts the continuous model in direction, this triggers a mandatory,
pre-committed investigation** (not a quiet choice of the nicer result). Check, in order:

1. **Fence-sitters.** Within each dominant-type group, distribution of the *margin* by which
   the leading z-score wins. Many barely-classified users bias the categorical result →
   continuous is more trustworthy.
2. **Collinearity.** Correlations / VIF among the three indices. If highly correlated,
   continuous coefficients are unstable → categorical may be more trustworthy.
3. **Nonlinearity.** Is a need's effect non-monotone (e.g. mid-status riskiest, extreme-status
   stays)? → neither is complete; add splines / piecewise terms.
4. **Report whatever is found.** An inconsistency is itself a finding about *how* motivation
   acts, not a blemish to hide. The paper is written around it either way.

**Validation (committed in advance):** hand-inspect 30 random users per dominant type, verify
the label is face-valid against their public profile/history; report inter-rater agreement
between two human coders on a 50-user sample. If face validity fails, the typology is rejected.
**Specifically flagged for this step:** the relatedness group's very high comment/answer proxy
(5.53 in Query A) — confirm these are genuine community participants, not artifacts of users
who barely answer.

### 5c. Difficulty proxy (frozen)

Question difficulty = standardized combination of: (i) inverse of eventual answer count, (ii) tag rarity (inverse tag frequency), (iii) time-to-first-answer. Validated against a held-out human-rated sample of ~100 questions.

---

## 6. Outcome variables (post-shock only — BATCH 2, not before freeze)

- **Primary — exodus (survival):** time from shock to a user's *last answer*, censored at end
  of data. "Exited" = no answer for ≥ K consecutive months and none thereafter.
  **K is reported at 3, 6, and 9 months — all three, pre-committed, whatever they show.**
  6 months is the headline; 3 and 9 are robustness. The same K applies identically to all
  three motivation types (a common ruler), so cross-type *comparison* is largely insensitive
  to K's absolute value even if the absolute exodus rate is not.
- **Primary — exit vs migration (H3):** among users who stopped answering (per the K=6 rule),
  classify each as **exit** (also stopped commenting/editing) vs **migration** (kept/increased
  comment+edit activity post-shock). Votes excluded (anonymous in dump).
- **Secondary — answering intensity:** within-user change in monthly answers (pre vs post).
- **Secondary — difficulty shift (H2):** within-user change in mean difficulty of answered
  questions.

---

## 7. Analysis plan (FROZEN)

1. **Primary model (H1) — continuous Cox.** Cox proportional-hazards on time-to-exodus;
   predictors = the three continuous z-scored motivation indices; covariates = log pre-shock
   answer volume, tenure, pre-shock reputation, primary tag domain. Hazard ratios with CIs.
   H1 = status_z HR > 1, relatedness_z HR < 1, competence_z intermediate. Check proportional-
   hazards assumption (Schoenfeld residuals); if violated, add time-interactions / stratify.
2. **Categorical companion.** Kaplan–Meier curves + Cox with dominant-type factor
   (relatedness = reference) for interpretable effect sizes and figures. **If this contradicts
   model 1 in direction → run the §5b mandatory deep-dive (fence-sitters / collinearity /
   nonlinearity) and report the finding.**
3. **H3 — exit vs migration.** Among answer-stoppers, logistic regression of exit (vs
   migration) on the continuous motivation indices + controls. H3 = status_z raises P(exit),
   relatedness_z lowers it. Companion: cross-tab of dominant type × {exit, migration}.
4. **H2 — difficulty shift.** Within-user regression of post-vs-pre change in answered-question
   difficulty on motivation indices; H2 = competence_z predicts shift toward harder questions.
5. **DiD robustness.** Difference-in-differences on answering intensity, SO vs Math SE,
   interacted with motivation type, to confirm the type×shock interaction is AI-specific.
6. **Placebo test.** Entire pipeline with a fake shock at 2021-11-30 (one year early); expect
   null. A non-null here voids the identification and the H1 results.
7. **Sensitivity (all pre-committed, all reported):** exodus threshold K = 3/6/9 months;
   cohort inclusion 3/5/10 answers; continuous vs categorical typing; a-priori vs data-driven
   typology; with/without reputation control.

### What would convince us we are WRONG (pre-committed)

- Motivation indices lose significance once volume / tenure / reputation are controlled → no
  contribution beyond Li & Kim / Quinn & Gutt. (Report as null.)
- Placebo shock reproduces the effect → identification broken; H1 void.
- Data-driven and a-priori typologies disagree → typology not real; downgrade to exploratory.
- Human face-validity of types fails → typology rejected.
- H3: exiters and migrators do not differ by motivation type → community shrinks uniformly,
  not along motivation lines; the distinctive claim falls.

We commit to writing the paper around whichever of these outcomes occurs.

---

## 8. Why this is "more like science" than the abandoned model

| Abandoned ABM | This study |
|---|---|
| Hypothetical 80% post-labor future | A shock that actually happened (2022-11-30) |
| Conclusions derivable from the meaning-function definition (circular) | Classifier frozen on pre-shock data; outcomes are post-shock; result can contradict us |
| No ground truth, unfalsifiable | Real data; explicit falsification + placebo test |
| 15 hand-tuned parameters | Behavioral indices with discriminant validity (Query A) + human face-validity check |
| "behavioral sink" never actually produced | We measure real exit/migration directly |

The behavioral-sink intuition from the abandoned model survives here in falsifiable form:
"removing the role that carried meaning is not compensated by what remains" becomes the
testable exit-vs-migration split (H3) — and the data can refute it.

---

## 9. Design questions — RESOLVED at freeze

1. **Continuous vs categorical typing** → **RESOLVED: continuous primary + categorical
   companion + frozen inconsistency-deep-dive rule** (§5b, §7.2). (User decision, 2026-05-30.)
2. **Full SO vs smaller site for the pipeline** → **RESOLVED:** environment blocks
   archive.org/SEDE/BigQuery from the analysis container, but GitHub is reachable. Pipeline
   logic validated on a real mid-size SE dump (`scripts/validate_pipeline_local.py`). The
   *analysis object is Stack Overflow*; data is exported by the researcher via SEDE (in
   browser) and committed to the repo as CSV subsets. Query A already returned real SO
   pre-shock results (~50,305 contributors). (Tested 2026-05-30.)
3. **Autonomy need** → **RESOLVED: folded into competence** (self-directed mastery); no clean
   standalone behavioral proxy on SO. Stated as a limitation. The "triad" we test is therefore
   competence / status / relatedness.
4. **Relatedness data availability** → comments and post-edits carry UserId and are in the
   dump (confirmed sufficient). Meta/review-queue participation may be incomplete; not relied
   upon for the core relatedness index. Votes are anonymous → excluded.

---

## 10. Scope discipline (the lesson from v1)

ONE community. ONE shock. A small set of theory-driven predictions (H1 differential exodus,
H2 difficulty migration, H3 exit-vs-migration), each with a built-in null and a placebo. No
virtual worlds, no collectivism, no 10-scenario grids. If H1/H3 hold cleanly, *that is a
paper*. If they fail cleanly, *that is also a paper* (a theory-driven null + the restructuring
result on a high-profile phenomenon). Either way it is falsifiable, which the previous work
was not.

---

## 11. Amendment log

Any change to the frozen design after 2026-05-30 is recorded here (date, what, why). The
original frozen text above is amended in place only with a visible note pointing here; it is
never silently rewritten.

- *(none yet — frozen 2026-05-30)*
