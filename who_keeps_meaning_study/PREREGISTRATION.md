# Pre-registration — Who keeps meaning without work?
# 预注册：不工作之后，谁撑得住？

**Frozen:** 2026-11-16, before any outcome-by-predictor tabulation was run. The only data inspected before
freezing were variable availability (non-missing counts by year), the marginal distribution of `wrkstat`,
`attend`, `socfrend` and `race`, and the list of weight variables. No outcome (`life`, `happy`) was cross-tabulated
with anything. The commit that adds this file is the timestamp. Any deviation after this commit is logged in
`DEVIATIONS.md`, never edited in here.

**Author:** Kao (project owner); analysis drafted by Claude (AI research assistant) under the project's honesty rules
(`../CLAUDE.md`, `../LESSONS.md`).

## 1. Why this study (and how it connects to Paper 1)

Paper 1 (`archive/abm_v1`, "Beyond Income versus Roles", under review) ranked meaning channels — competence and
contribution above roles and income — but an equal-path control (Nov 2026, `/abm-equal-path`) showed the ranking is
reproduced almost exactly by the *input coefficients* (r = 0.997): the model assumed the answer. The missing piece is
data on **which real-world resources actually buffer people when work disappears**. This study estimates that from
50 years of US survey data, so a later stage can replace assumed coefficients with measured ones (§8).

It also feeds the project's new output line: practical, population-specific guidance (by age group especially). If
the buffers differ by life stage, the guidance must too.

## 2. Data

- **GSS Cumulative 1972–2024 (release 3)** and **GSS panels 2006–2010, 2008–2012, 2010–2014** (three waves each),
  as packaged in the public `gssr` R data package, GitHub `kjhealy/gssr` commit `769d48c` (2026-03-12).
  SHA-256: `gss_all.rda 38712b98…4627f`, `gss_panel06_long.rda 83eafebb…e7f4`, `gss_panel08_long.rda 8aab3a12…f767f871`
  (full hashes in `scripts/DATA_SOURCES.md`). The 2020 panel is not used (two-wave, COVID-confounded, mode change).
- Weights: `wtssps` (post-stratified). If `wtssps` is missing for a respondent, use `wtssall`. Unweighted results
  reported as a robustness check.

## 3. Sample

Respondents aged **25–64** (prime working age), excluding students (`wrkstat`=6). Retirement at 65+ is a normative
transition and is analysed only as a secondary contrast (§6, S3).

## 4. Measures

**Exposure — not working (`NW`).** From `wrkstat`: working = 1 full-time, 2 part-time, 3 has a job but temporarily
not at work. Not working = 4 unemployed/laid off, 5 retired, 7 keeping house, 8 other. Pooled `NW` is primary;
type-specific contrasts are secondary.

**Outcomes.**
- **O1 (primary) — engaged life:** `life` = "In general, do you find life exciting, pretty routine, or dull?" Coded
  1 if *exciting*, 0 otherwise. *Honest label:* this is a vitality/engagement proxy, **not** a validated
  meaning-in-life scale. Results will be described as "finds life exciting", never as "has meaning", in 🟢 claims.
- **O2 — happiness:** `happy`. O2a = 1 if *very happy*; O2b = 1 if *not too happy* (distress proxy).

**Moderators (pre-specified, the "buffers").**
- **M1 friends:** `socfrend` ≤ 3 (spends a social evening with friends at least several times a month).
- **M2 religious attendance:** `attend` ≥ 6 (nearly every week or more).
- **M3 married:** `marital` = 1.
- **M4 income:** `realinc` converted to within-year terciles; top vs bottom tercile (middle as reference in the full
  model; the H5 test uses the top tercile).

**Controls:** age, age², sex, race (3 categories), degree (5 categories), self-rated health (`health`, 4 categories),
survey-year fixed effects. Health is included because ill health causes both non-work and low vitality; a no-health
model is reported as a robustness check (it will show larger penalties; the health-adjusted one is primary).

## 5. Hypotheses (directional, written before seeing outcomes)

Cross-sectional, pooled 1973–2024 (O1 asked in most years; `socfrend` only on some ballots, so M1 models use a
smaller N — stated, not hidden):

- **H1 — the penalty exists.** `NW` is associated with lower P(O1). Expected sign: negative.
- **H2 — friends buffer.** `NW × M1` > 0 on O1 (the penalty is smaller for people who see friends often).
- **H3 — religion buffers.** `NW × M2` > 0 on O1.
- **H4 — marriage buffers.** `NW × M3` > 0 on O1.
- **H5 — money buys relief more than engagement.** (a) Among top-income-tercile respondents the `NW` penalty on O1
  is still negative and its 95% CI excludes zero. (b) Income moderates the O2b (distress) penalty more than the O1
  penalty: the standardised `NW × top-tercile` interaction is larger in magnitude for O2b than for O1. *(This is the
  project's "money buys relief, not meaning" claim, tested on new data.)*
- **H6 — life stage.** The O1 penalty is largest at **40–54** than at 25–39 or 55–64. *(Direction is a hunch from the
  identity literature; flagged as the weakest prior.)*

Panel, within-person (2006–2014 panels stacked; person fixed effects; linear probability model; wave dummies and
time-varying controls age², marital, health, log real income):

- **H7 — exit hurts within person.** Moving from working to `NW` between waves lowers O1 relative to staying at work.
- **H8 — baseline friends buffer the exit.** `exit × M1(at the last working wave)` > 0.

**Placebo (pre-committed).**
- **P1 — anticipation / reverse-causation check.** For people who leave work between waves 2 and 3, their O1 change
  between waves 1 and 2 (while still working) should not differ from stayers'. If it does (a pre-exit decline), the
  H7 estimate is at least partly decline-causes-exit, and will be reported as such.

## 6. Analysis plan

- Cross-section: weighted logit, robust (HC1) standard errors, year FE. Report average marginal effects of `NW`
  and of `NW` at each moderator level; test interactions on the logit scale **and** as differences in AMEs (the
  latter is what will be interpreted). Linear-probability replication reported.
- Multiplicity: H2–H4 and H5b are one family → Holm correction at α = 0.05. H1, H5a, H6, H7, H8 stand alone at
  α = 0.05 two-sided.
- Secondary (labelled exploratory, no confirmatory claims): S1 penalty by `NW` type (unemployed / early retired /
  keeping house / other) and by sex; S2 decade trend of the penalty; S3 65+ retirees vs workers; S4 `socrel`
  (relatives) instead of friends; S5 the same models on O2a.
- Missing data: listwise within each model; Ns reported per model.

## 7. What would count as what

- If H2–H4 survive Holm: those buffers become 🟢 *associational* evidence (cross-sectional) — still not causal.
- If H7/H8 also hold **and P1 is clean**: upgrade to "within-person, not anticipated" — the strongest claim this
  design allows. Still not randomised.
- If H5a holds (top-income non-workers still less engaged): supports "money buys relief, not meaning". If it fails,
  the project's flagship 🟢 claim is weakened and **SYNTHESIS Q2 gets edited accordingly**.
- Nulls are reported in full with the same prominence as positives (see `../so_sdt_study`, `../contract_buffer_study`).

## 8. Stage 2 (specified later, separately pre-registered)

Map estimated buffers onto Paper 1's channels where a defensible mapping exists (friends → relatedness; marriage /
keeping-house → roles; income → income) and rerun the reconstructed Route A with data-derived relative weights.
Channels with no GSS counterpart (competence, autonomy, contribution) stay assumed and are labelled so. The mapping
will be written and committed before the rerun.

## 9. Known limitations (stated up front)

GSS is US-only; `life` is a single item; cross-sectional associations carry selection (people who stop working
differ); panel transitions are few (expected low hundreds) so H7/H8 may be underpowered — a null there is
uninformative, not evidence of no effect; none of these non-workers stopped working *because of AI*. This is the
best available analogue sample, not the post-labour future.
