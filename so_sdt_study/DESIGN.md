# Pre-Registration: Motivational Heterogeneity in Contributor Exodus from Stack Overflow after ChatGPT

**Status:** DRAFT design / pre-registration. To be frozen *before* any outcome (post-shock) data is examined.
**Last updated:** 2026-05-30
**Working title:** *Why they left: a self-determination account of differential contributor exodus from an online knowledge community after a generative-AI shock*

---

## 0. One-sentence summary

We test whether contributors who differed, *before* ChatGPT, in the **kind of motivation** their Stack Overflow (SO) activity reveals — mastery/competence-seeking, status-seeking, or relatedness-seeking — left the platform at **different rates** after the ChatGPT shock (2022-11-30), and whether that ordering survives controls for pre-shock activity volume and tenure.

---

## 1. Background and the gap we are filling

The post-ChatGPT decline of Stack Overflow is now well documented:

- del Rio-Chanona, Laurentsyeva & Wachs (2024, *PNAS Nexus*): ~25% drop in SO activity within 6 months, difference-in-differences against Russian/Chinese SO and Math StackExchange, using the public Stack Exchange dump.
- Burtch, Lee & Chen (2024, *Scientific Reports*): ~16–20% drop within 15 weeks, event study with Reddit as a negative control.
- Quinn & Gutt (2025, *JMIS*): heterogeneous effects — **casual** users reduced questions ~18%, while **intensive/top** users barely changed.
- Helic & Santos (2025, arXiv): easy questions fell, hard questions rose.

**What is already settled:** that activity fell, by roughly how much, and that the decline is concentrated among *casual / newer / less-embedded* users (base truncation, not "hollowing out" of experts).

**What is NOT done:** every one of these studies measures activity *volume* and segments users by *volume / tenure*. None segments users by the **psychological function** their participation served, and none tests a **theory-driven** prediction about *which motivation* is most vulnerable to AI substitution. The parallel experimental literature (e.g. Nature *Sci. Rep.* 2025/2026 on AI undermining intrinsic motivation, self-efficacy, and meaning; CHI 2026 "Automating the Joy Out of Work") shows the *mechanism* exists in the lab but has never been connected to *observed behavioral exodus* in a real community.

**Our contribution is the bridge:** a Self-Determination-Theory (SDT) reading of *who* leaves, tested as a falsifiable behavioral prediction on public data.

### How this differs from Quinn & Gutt (2025) — the novelty hinge

Quinn & Gutt split users by **how much** they participate (casual vs intensive). We split users by **why** they appear to participate (which SDT need their behavior serves). These are different axes: a "casual" user can be relatedness-driven, an "intensive" user can be status-driven. **The critical test of our novelty is whether motivation type predicts exodus *after controlling for pre-shock activity volume and tenure.*** If it does not — if motivation type is just a proxy for volume — we have *not* added anything beyond Quinn & Gutt, and we will report that honestly as a null contribution.

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

### H3 (secondary, the original UBI-era intuition, repurposed)

This is the surviving kernel of the abandoned post-labor model: *removing the activity that carried meaning is not compensated by the activity remaining available.* Operationally: post-shock, the **drop in answering** among status-driven users is **not** offset by increased low-effort engagement (voting, commenting); they disengage rather than substitute. (Exploratory; reported descriptively.)

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

### 5b. From indices to types — two pre-committed strategies, reported side by side

- **Strategy A (theory-driven, primary):** z-score each index across the cohort; assign each user a **dominant type** = argmax of the three z-scored indices. Also keep the continuous indices for regression (preferred: treat type *continuously*, not categorically, to avoid arbitrary cutoffs).
- **Strategy B (data-driven, confirmatory):** factor analysis / k-means on the index battery; *then* map discovered clusters onto SDT needs and check whether the structure matches Strategy A. If A and B disagree sharply, we report that the typology is not robust and downgrade H1 to exploratory.

**Validation (committed in advance):** hand-inspect 30 random users per type, verify the label is face-valid against their profile/history; report inter-rater agreement between two human coders on a 50-user sample. If face validity fails, the typology is rejected.

### 5c. Difficulty proxy (frozen)

Question difficulty = standardized combination of: (i) inverse of eventual answer count, (ii) tag rarity (inverse tag frequency), (iii) time-to-first-answer. Validated against a held-out human-rated sample of ~100 questions.

---

## 6. Outcome variables (post-shock only)

- **Primary — exodus (survival):** time from shock to a user's *last answer*, censored at end of data. "Exited" = no answer for ≥6 consecutive months and none thereafter in the window.
- **Secondary — answering intensity:** change in monthly answers (pre vs post), within-user.
- **Secondary — difficulty shift (H2):** change in mean difficulty of answered questions.
- **Exploratory — substitution (H3):** change in low-effort engagement (votes/comments) among those who stopped answering.

---

## 7. Analysis plan (frozen)

1. **Primary model:** Cox proportional-hazards on exodus, predictors = the three continuous motivation indices (z-scored), covariates = log pre-shock answer volume, tenure, pre-shock reputation, primary tag domain. Report hazard ratios with CIs. H1 = status index HR > 1, relatedness index HR < 1, competence intermediate.
2. **Categorical companion:** same with dominant-type factor (relatedness = reference).
3. **DiD robustness:** difference-in-differences on answering intensity, SO vs Math SE, interacted with motivation type, to confirm the type×shock interaction is AI-specific.
4. **Placebo test:** entire pipeline at 2021-11-30 shock date; expect null.
5. **H2:** within-user difficulty-shift regression, type as predictor.
6. **Sensitivity:** cohort thresholds (3/5/10 answers), continuous vs categorical typing, Strategy A vs B, with/without reputation control.

### What would convince us we are WRONG (pre-committed)

- Motivation indices lose significance once volume/tenure are controlled → no contribution beyond Quinn & Gutt.
- Placebo shock reproduces the effect → identification broken.
- Strategy A and B typologies disagree → typology not real.
- Human validation of types fails face validity.

We commit to writing the paper around whichever of these outcomes occurs.

---

## 8. Why this is "more like science" than the abandoned model

| Abandoned ABM | This study |
|---|---|
| Hypothetical 80% post-labor future | A shock that actually happened (2022-11-30) |
| Conclusions derivable from the meaning-function definition (circular) | Classifier frozen on pre-shock data; outcomes are post-shock; result can contradict us |
| No ground truth, unfalsifiable | Real data; explicit falsification + placebo test |
| 15 hand-tuned parameters | Behavioral indices validated against human coding |
| "behavioral sink" never actually produced | We measure real disengagement directly |

---

## 9. Open design questions for the researcher (to resolve before freezing)

1. **Categorical vs continuous typing as primary.** Recommendation: continuous (avoids arbitrary cutoffs, more honest). Categorical as companion for interpretability.
2. **Full SO (huge: Posts ~100GB+) vs start on a smaller Stack Exchange site to debug the pipeline.** Recommendation: build & validate the entire pipeline on a medium site (e.g. a smaller tech SE) first, then scale to SO. Possibly use BigQuery to avoid local 100GB+ downloads.
3. **Autonomy need:** we fold autonomy into competence (self-directed mastery) rather than typing it separately, because it has no clean behavioral proxy on SO. Flag as a limitation.
4. **Relatedness data availability:** Meta/review-queue participation may not be fully in the dump. Confirm before relying on it.

---

## 10. Scope discipline (the lesson from v1)

ONE community. ONE shock. ONE theory-driven prediction with a built-in null and a placebo. No virtual worlds, no collectivism, no 10-scenario grids. If H1 holds cleanly, *that is a paper*. If it fails cleanly, *that is also a paper* (a theory-driven null on a high-profile phenomenon). Either way it is falsifiable, which the previous work was not.
