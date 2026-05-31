# RT-04B — Contract-Buffer Study · Handoff for next session

**Written 2026-05-31 by the prior session, for a fresh full-network-access session to execute autonomously.**
**The user does NOT want to do manual data pulls. The previous container was allowlist-restricted
(NBER/Census/IPUMS blocked); your session is full-access, so you can download everything yourself.**

---

## 0. What you are picking up, in one paragraph

This repo hosts a lifelong project on human meaning in the post-AI era, anchored by a **book**
(`meaning_project/book/`). Two independent peer reviews (`REVIEW_01.md`, and a follow-up summarized
in chat) judged the book 8.5/10 but flagged ONE structural weakness: the book's hinge argument —
**"the professionals hit first by AI are *forerunners* for everyone, not a special case"** — rests
on a 🟡 inference (contract-stickiness) that the book now honestly labels as unproven. The cure is
**RT-04B**: a new, falsifiable, pre-registered empirical study that would push that hinge from 🟡
toward 🟢. The author chose to focus on exactly this. Your job is to **freeze a pre-registered
design, pull the data, run it, and report the honest result (which may well be a null — that is
fine and on-brand).** Model the entire effort on the existing `so_sdt_study/` (a pre-registered
NULL done right).

**READ FIRST, in order:** `CLAUDE.md` → `meaning_project/SYNTHESIS.md` → `meaning_project/MANIFESTO.md`
→ `meaning_project/STYLE.md` → `so_sdt_study/DESIGN.md` and `so_sdt_study/PAPER.md` (your template for
pre-registration discipline + honest write-up) → `meaning_project/book/chapters/04_first_to_hit_the_wall.md`
(the argument this study defends) → `meaning_project/book/RESEARCH_TODO.md` (RT-04B entry).

---

## 1. The scientific question (and why it is the load-bearing one)

The book's Ch.4 claims: Stack Overflow (SO) collapsed ~95% after ChatGPT because it had **no
employment contract** buffering it; salaried white-collar work hasn't visibly cratered because
**contractual stickiness** (contracts, severance, org friction) is *delaying* the same force. Hence
the exposed professional is a **forerunner**, living everyone's near-future.

**The competing explanation a reviewer raised (and the book now steelmans):** maybe SO collapsed not
because it lacked a contract, but because it was a **perfectly substitutable special case** (asking a
coding question ≈ exactly what a chatbot does, end-to-end). If so, most white-collar work — tangled
with judgment, accountability, relationships — is safer than SO's collapse implies, and the
"forerunner" extrapolation breaks.

**RT-04B discriminates between these two**, because they make *opposite* predictions when you hold
AI-exposure constant and vary only the contract buffer:

- **Contract-buffer hypothesis (the book's):** within the *same* occupation (same substitutability),
  **no-contract** workers (freelance / unincorporated self-employed) should show employment decline
  **earlier and deeper** after the ChatGPT shock than **salaried** workers in that same occupation.
- **Pure-substitutability hypothesis (the rival):** if substitutability is what matters, both
  arrangements within an occupation should move **together** (the contract is irrelevant).

The cleanest intuition: a **freelance translator and a salaried translator are equally substitutable
by the model** — so if the freelancer gets hit first/harder, the difference is the *contract*, not
substitutability. That is the whole design.

---

## 2. Data sources — ALL VERIFIED 2026-05-31 (with exact access notes)

### 2a. Labour outcome side — CPS basic monthly microdata (NO REGISTRATION NEEDED)
The user could not register for IPUMS; **you do not need IPUMS.** The underlying data is free public-
use microdata from the Census Bureau. Two equivalent no-login routes:

- **NBER (easiest — pre-converted to CSV / Stata .dta, 1989–present):**
  https://www.nber.org/research/data/current-population-survey-cps-basic-monthly-data
  Files named `cpsbYYYYMM`. CSV host path is under `data.nber.org/cps-basic/...`.
  **Prior container got HTTP 403 `host_not_allowed` on data.nber.org — confirm your session can reach
  it; full-access should.**
- **Census Bureau direct (raw fixed-width `.dat` + data dictionary):**
  https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.html
  (also `https://www2.census.gov/programs-surveys/cps/datasets/`). Requires parsing fixed-width with
  the dictionary — heavier but canonical.

Key CPS variables (names per NBER/Census; IPUMS equivalents in parentheses):
- **Class of worker** → distinguishes self-employed *incorporated* vs *unincorporated* vs wage/salary
  private vs government. (IPUMS `CLASSWKR`.) **Use *unincorporated self-employed* as the robust
  "no-contract" proxy.** A basic-monthly **independent-contractor** question also exists in recent
  years (asked to both employees and self-employed) — confirm its availability/coding in your window;
  if present it's a sharper proxy, treat as a bonus/robustness cut.
- **Occupation** (detailed; CPS uses 2018-SOC-based codes since 2020 — stable across our window).
- Age, employment status, usual hours, **final weight** (must weight all estimates).

### 2b. AI-exposure index — ALREADY PULLED, in-container reachable via GitHub
- **AIOE (Felten/Raj/Seamans 2021), incl. a Generative-AI variant** — GitHub `AIOE-Data/AIOE`.
  Prior session downloaded the full repo tarball successfully (GitHub raw = HTTP 200). Contains
  `AIOE_DataAppendix.xlsx` (AIOE scores by 6-digit SOC) and a `Generative AI/` folder with a
  generative-AI-specific construction. **Prefer the generative-AI variant** for this study.
  `https://codeload.github.com/AIOE-Data/AIOE/tar.gz/refs/heads/main`
- **Eloundou et al. "GPTs are GPTs"** (Science 2024; arXiv 2303.10130) — O*NET task-level GPT
  exposure, the most generative-AI-specific measure; use as a second exposure index for robustness.
  Data on GitHub (search the paper's repo; `gptsRgpts_occ_lvl.csv` referenced in EIG-Research/AI-unemployment).
- You'll need an **SOC ↔ CPS-occupation crosswalk** to join exposure scores to CPS occupation codes
  (BLS/Census crosswalks are public).

### 2c. Contract-share by occupation (for choosing/validating bins) — public
- **BLS Contingent Worker Supplement, July 2023:** https://www.bls.gov/news.release/conemp.nr0.htm
  (independent-contractor rates by occupation: arts/design/media 28.1%, personal care 19.7%, etc.)

### 2d. External triangulation (published numbers — verify from primary text, per project rule)
- **No-contract extreme (freelance):** Hui, Reshef & Zhou, "Short-Term Effects of Generative AI on
  Employment," arXiv 2308.05201. And **"Winners and Losers of Generative AI: Early Evidence of Shifts
  in Freelancer Demand,"** *J. Economic Behavior & Organization*, 2025-01-29 (ScienceDirect
  S0167268124004591): substitutable skills (writing, translation) demand fell **20–50%** vs
  counterfactual; complementary skills (ML, chatbots) rose. These measure **demand/postings**, not
  employment — use only as qualitative triangulation, not as a merged outcome.
- **Salaried extreme:** Stanford Digital Economy Lab / ADP "Canaries in the Coal Mine?" (Brynjolfsson
  et al.) — 22–25yo in exposed occupations −13~16% relative; ADP covers **payroll (salaried) only**,
  which is itself the clean asymmetry (freelancers/ICs are not on payroll). Already in `evidence_base.md`.

---

## 3. The three HARD limitations that shaped the design (bake these into DESIGN.md honestly)

1. **No earnings for the self-employed.** CPS collects usual earnings only for **wage/salary** workers
   (outgoing rotation groups), explicitly excluding the self-employed. → The head-to-head outcome must
   be **employment level / hours**, NOT pay. (This actually *aligns* with ADP Canaries, which finds
   adjustment runs through employment, not wages.) Earnings effects on the no-contract side live only
   in the freelance papers (§2d), used as triangulation.
2. **Thin cells.** Basic-monthly CPS ≈ 60k households. A single narrow occupation × unincorporated-
   self-employed × month is tiny. → Analysis unit must be **AI-exposure bins (e.g., quartiles) ×
   class-of-worker**, pooled across months, with occupation fixed effects and an event-study around
   2022m11 — NOT single-occupation point estimates. "Translators" is a narrative example, not an
   estimator.
3. **Gig identification is imperfect.** Use **unincorporated self-employed** as the primary no-contract
   proxy (always available); the basic-monthly independent-contractor flag is a bonus robustness cut
   if present in-window. Self-employed differ from employees in unobserved ways (selection) — state this.

Residual threat to name: even "same occupation" isn't perfectly equal substitutability (freelancers
may do more substitutable sub-tasks). Address via occupation FE + sensitivity, and concede the residual.

---

## 4. Execution plan (do these in order; preserve pre-registration discipline)

1. **Confirm network reach** to NBER (`data.nber.org`) and/or Census in your session. If both fail,
   fall back to the Census API or report back; do NOT silently proceed without the labour data.
2. **Write & FREEZE `contract_buffer_study/DESIGN.md` BEFORE looking at any post-2022m11 outcomes.**
   Mirror `so_sdt_study/DESIGN.md`. Must pre-specify:
   - **H1 (primary):** AI-exposure × unincorporated-self-employed interaction predicts a larger /
     earlier post-2022m11 relative employment decline than the same exposure among wage/salary workers.
   - **Placebo/robustness (pre-specified):** (a) a fake shock date in a pre-ChatGPT year should show no
     effect; (b) low-exposure occupations should show no differential; (c) second exposure index
     (Eloundou) reproduces the AIOE result. Decide the estimator (event-study / diff-in-diff-in-diff),
     the exposure binning, the occupation set, weighting, and the window — all frozen in advance.
   - The three limitations in §3, written as honest caveats up front.
   - State plainly: **a null is an acceptable, publishable outcome** (the SO study was a null; honesty
     is the brand). Do not design toward a positive result.
3. **Write `build_extract.py`** — pulls the needed CPS months from NBER, keeps only needed columns +
   employed records, joins the SOC↔CPS-occ crosswalk + AIOE/Eloundou exposure, outputs a **slim**
   committed analysis file (a few MB; do NOT commit raw multi-GB monthly files). Commit the exposure
   inputs (small) too. Keep it reproducible from committed scripts (project norm).
4. **Only after the design is committed/frozen**, build the extract and run the frozen analysis.
   Resist post-hoc redefinition (the SO write-up's §4.1 lists the tempting moves we refused — read it).
5. **Write `contract_buffer_study/PAPER.md`** in the SO paper's honest register. Then **update the book**:
   - If H1 holds → Ch.4 can upgrade the forerunner pivot from explicit-🟡 toward 🟢 (in prose, per
     STYLE: claim-type in words, NO emoji in reader-facing text). Update `evidence_base.md`,
     `SYNTHESIS.md`, flip RT-04B to ✅ in `RESEARCH_TODO.md`.
   - If null/mixed → Ch.4 keeps the 🟡 honesty but now *cites the test that failed to confirm it* —
     which is itself a credibility gain. Either way the book gets more honest, not just more confident.

---

## 5. Workflow / repo norms (non-negotiable)

- **Branch:** develop on `claude/paper-repo-review-E0GJA`; push there; then fast-forward main via
  `git push origin claude/paper-repo-review-E0GJA:main`. Create the branch locally if missing.
- **Commit-message footer:** end commits with the session URL line (see existing commits for format).
  Do NOT put any model identifier in commits/PRs/code.
- **Honesty discipline:** pre-register before seeing outcomes; freeze designs; use placebos; let the
  data win even if it kills the hypothesis. In book prose, convey claim-type (empirical/analogical/
  normative) in WORDS — 🟢🟡🔴 emoji live ONLY in back-office files (SYNTHESIS, evidence_base,
  RESEARCH_TODO, research-note footers), never in reader-facing chapters.
- **Verify citations from primary text**, not search summaries (lesson from the SO lit review).
- **Stack:** Python — pandas, numpy, scipy, statsmodels (event-study / regression; PHReg only if doing
  survival). Reproducible from committed scripts. (`lifelines` failed to install before; use statsmodels.)
- Don't commit raw multi-GB CPS files; commit the slim extract + the scripts that build it.

## 6. State at handoff
- Book fully revised through REVIEW_02 (8.5/10); both fatal cracks sealed. Latest commit on the branch
  ~`abd628b` plus this handoff. Nothing in `contract_buffer_study/` yet except this file.
- AIOE exposure data confirmed downloadable from GitHub in-container. CPS labour data needs your full
  network access (NBER/Census). No design has been frozen yet — that is your first real step.
