# Pre-Registration: The Contract Buffer — Does Employment Contract Protection, Not Just AI Substitutability, Govern Where Generative AI Hits First?

**Study code:** RT-04B. **Status:** 🔒 **FROZEN (2026-05-31).** Hypotheses, class and
exposure definitions, sample window, estimator, falsification tests, and decision rules below
are locked *before* any post-shock employment outcome is examined. Only data structure, variable
codings, weight scaling, and crosswalk construction have been inspected at freeze time — **no
employment trend, level, or differential across the 2022-11 shock has been computed.** Any change
after this point is logged as a dated amendment in §12; the original frozen text is never silently
edited.

**Modeled on** `so_sdt_study/DESIGN.md` — the project's template for a pre-registered, placebo-
controlled study where a null is an acceptable, publishable outcome.

---

## 0. One-sentence summary

Holding generative-AI **substitutability** roughly constant (same detailed occupation, same
occupation-level AI-exposure score), we test whether workers with **no employment-contract buffer**
(unincorporated self-employed) lost employment **earlier and more deeply** after the 30 November 2022
ChatGPT shock than **salaried** workers in the same exposed occupations — the prediction that
distinguishes the book's *contract-buffer* mechanism from the rival *pure-substitutability* account.

---

## 1. Background and the exact gap this fills

The book's Chapter 4 ("The First to Hit the Wall") rests on a hinge inference: Stack Overflow
collapsed ~95% after ChatGPT because it had **no employment contract** holding it together, whereas
salaried white-collar work has not visibly cratered because **contractual stickiness** (contracts,
severance, organisational friction) is *delaying* the same force. From this the book infers that
exposed professionals are **forerunners** for everyone — living, early and unbuffered, what
contracts are merely postponing for the rest of work.

A reviewer raised the strongest rival explanation, which the book now honestly steelmans:
maybe SO collapsed not for lack of a contract but because it was a **perfectly substitutable special
case** (asking a coding question end-to-end ≈ exactly what a chatbot does). If substitutability is
the whole story, then most white-collar work — tangled with judgment, accountability, relationships —
is safer than SO's collapse implies, and the "forerunner" extrapolation breaks.

The two accounts are presently both consistent with the aggregate facts, so the hinge is honestly
labelled an unproven 🟡 inference (analogical/mechanistic) in the book. **No prior study has held
AI-exposure fixed and varied only the contract buffer.** That is the gap. The existing evidence
brackets the question from its two extremes but never tests the contrast directly:

- **No-contract extreme (freelance):** Hui, Reshef & Zhou (2024, arXiv 2308.05201) and "Winners and
  Losers of Generative AI" (*J. Econ. Behavior & Org.*, 2025) find freelancer **demand/postings** for
  substitutable skills (writing, translation) fell 20–50% vs counterfactual. These measure demand,
  not employment, and never compare to salaried workers in the same occupation.
- **Salaried extreme:** Brynjolfsson et al. ("Canaries in the Coal Mine?", Stanford Digital Economy
  Lab, ADP payroll) find 22–25-year-olds in the most AI-exposed occupations down ~13–16% relative,
  older workers in the same jobs up 6–9%. ADP covers **payroll (salaried) only** — by construction it
  cannot see the no-contract side.

This study supplies the missing within-occupation, employment-based, head-to-head contrast on a
single nationally representative dataset.

### The clean intuition (and what it can and cannot prove)

A freelance translator and a salaried translator are, to first order, **equally substitutable by the
model**. If the freelancer's employment falls first and harder, the operative difference is the
**contract**, not substitutability. Occupation fixed effects hold average occupational
substitutability constant; the residual threat — that freelancers within an occupation may perform
more substitutable *sub-tasks* than salaried workers in that same occupation — is named as a
limitation (§3), partly probed (§7), and conceded where it cannot be removed. This design can move the
hinge from 🟡 toward 🟢; it cannot, alone, settle it.

---

## 2. Hypotheses (directional, falsifiable, frozen)

Let **Exp_o** be the generative-AI exposure of occupation *o* (z-scored occupation-level Language-
Modeling AIOE; §5). Let class *c* be **no-contract** (unincorporated self-employed) vs **salaried**
(private-sector wage/salary). Let **Post_t = 1** for months on/after 2022-11. The contract-buffer
mechanism and the substitutability rival make *opposite* predictions for the same quantity.

### H1 — primary (contract buffer): deeper

Within exposed occupations, the post-shock relative employment decline is **larger for no-contract
than for salaried** workers. In the triple-difference (DDD) regression of §7, the coefficient on
**Post × Exp × NoContract** is **β₃ < 0**.

- **Contract-buffer prediction:** β₃ < 0 (no-contract workers in high-exposure occupations shrink
  faster than salaried workers in the same occupations).
- **Pure-substitutability prediction (rival):** β₃ = 0 (exposure hits both arrangements equally; only
  the *common* exposure effect Post × Exp is negative — the contract is irrelevant).

**Falsification of H1:** β₃ not statistically below 0 (CI includes or exceeds 0). A null β₃ alongside
a negative Post × Exp is *positive evidence for the rival* and against the book's mechanism — and will
be reported as such.

### H1b — primary (contract buffer): earlier

The no-contract penalty appears **sooner** in event time. In the event-study (§7), the
Post × Exp × NoContract interaction crosses below zero in an **earlier post-shock window** for
no-contract than the common exposure response does for salaried. Operationalised as: β₃ is already
negative and significant in the **early post window (2022-11 … 2023-12)**, not only in later years.

**Falsification of H1b:** β₃ in the early window is null while only later windows move (consistent
with slow, symmetric diffusion rather than a contract-mediated head start).

### H2 — secondary (dose-response across the buffer gradient)

If the buffer — not substitutability — is what matters, the post-shock exposure penalty should order
**monotonically by contract strength**: unincorporated self-employed (no buffer) > incorporated
self-employed (a legal/organisational buffer, but still self-directed) > private wage/salary
(full contract buffer). I.e. the Post × Exp penalty is most negative for class 7, intermediate for
class 6, least for class 4.

**Falsification of H2:** no monotonic ordering, or incorporated self-employed not intermediate.

### What would convince us the mechanism is WRONG (pre-committed)

- **β₃ ≥ 0 / null** with Post × Exp < 0 → exposure hits no-contract and salaried equally → the
  *substitutability* rival is favoured; the book's contract-buffer hinge **fails its first direct
  test**. (Reported as an informative null; Ch.4 keeps 🟡 and cites the test that failed to confirm.)
- **Placebo shock (fake date in the clean pre-ChatGPT stretch) reproduces β₃ < 0** → the no-contract/
  salaried exposure gap is a pre-existing trend, not a ChatGPT response → identification broken, H1
  void (exactly the move that killed the headline effect in `so_sdt_study`).
- **Non-flat pre-trends** in the event study before 2022-11 → parallel-trends fails; H1 downgraded.
- **Result flips sign or vanishes** under the base-AIOE exposure measure, the ≥-respondent cell
  thresholds, or the age bands → not robust; downgraded to exploratory.

We commit to writing the paper around whichever of these occurs. A clean null is publishable and
on-brand (the SO study was a pre-registered null).

---

## 3. The hard limitations that shaped this design (stated up front, honestly)

1. **No earnings for the self-employed.** CPS collects usual earnings only for wage/salary workers
   (outgoing rotation groups), explicitly excluding the self-employed. → The head-to-head outcome is
   **employment level**, not pay. This aligns with the ADP "Canaries" finding that AI adjustment runs
   through employment, not wages. Earnings effects on the no-contract side exist only in the freelance
   demand papers (§1), used solely as qualitative triangulation, never merged as an outcome.
2. **Thin cells.** Basic-monthly CPS is ~60k households; a single narrow occupation ×
   unincorporated-self-employed × month is small. → The estimator pools across months and uses
   **continuous occupation-level exposure with occupation fixed effects** (not single-occupation point
   estimates), plus a Poisson/PPML count model that tolerates small and zero cells. "Translators" is a
   narrative example, **not** an estimator.
3. **Self-employment ≠ a clean no-contract experiment (selection).** Unincorporated self-employed
   differ from employees in unobserved ways (who selects into freelancing, and why). Cell fixed
   effects absorb *time-invariant* differences; identification rests on **parallel trends**, tested by
   event-study pre-trends and a placebo shock. The residual threat — within-occupation differences in
   *task* substitutability between freelancers and employees — cannot be fully removed and is conceded.
4. **No basic-monthly independent-contractor flag in window.** The independent-contractor question
   lives in the periodic Contingent Worker Supplement, not the basic monthly file (confirmed by
   inspecting the 2022-11 record layout). → **Unincorporated self-employment is THE no-contract proxy**
   (always available). The IC supplement is out of scope for this study.
5. **COVID-era self-employment shock.** Self-employment was severely and differentially disrupted in
   2020–2021. → The primary window is **entirely post-COVID-acute** (starts 2021-07); the acute COVID
   period is never in the estimation sample. The 2021–2022 self-employment recovery ("great
   resignation") is a residual trend the event-study pre-trend check and placebo mitigate but cannot
   fully erase — conceded, mirroring how `so_sdt_study` conceded SO's secular decline.

---

## 4. Data

### 4.1 Labour outcomes — CPS basic monthly microdata (public, no registration)

- **Primary source, 2021-07 … 2022-12:** NBER pre-converted Stata files,
  `https://data.nber.org/cps-basic2/dta/cpsbYYYYMM.dta` (harmonised variable names; verified
  reachable and parseable 2026-05-31; coverage ends 2023-11).
- **Primary source, 2023-01 … latest available (≈2026-04):** U.S. Census Bureau public-use basic
  monthly fixed-width files, `https://www2.census.gov/programs-surveys/cps/datasets/YYYY/basic/`
  (`mmmYYpub.zip`), parsed with the matching Census record-layout dictionary (2023+ layout; verified
  reachable, current through 2026-04, 2026-05-31).
- **Validation (pre-committed):** for the overlap months 2023-01 … 2023-11, the Census-parsed extract
  and the NBER extract must reproduce the same weighted employment counts by class of worker (within
  rounding). A failed cross-check halts the analysis until the parse is fixed. This doubles as the
  reproducibility audit the project requires.

The 2023-01 source seam coincides with both the CPS sample-redesign byte-layout break and the NBER
coverage end, so each source spans exactly one layout era.

**Variables (CPS names; all confirmed present and coded as below in the 2022-11 file):**

| Concept | Variable | Use |
|---|---|---|
| Class of worker, main job | `PEIO1COW` | 4 = private for-profit (salaried); 5 = private nonprofit; 6 = self-emp **incorporated**; 7 = self-emp **unincorporated** (no-contract); 1–3 = government; 8 = without pay |
| Detailed occupation, main job | `PEIO1OCD` | 4-digit 2018-census occupation code (524 codes in 2022-11); joined to AIOE via crosswalk (§5) |
| Labour-force status | `PEMLR` | employed = {1 at work, 2 absent}; everything else not counted as employed |
| Age | `PRTAGE` | sample restriction (§6) |
| Usual hours, main job | `PEHRUSL1` | secondary outcome (hours) |
| Final weight | `PWCMPWGT` | composited final person weight; **4 implied decimals (divide by 10⁴)**; all estimates weighted |
| Month / year | `HRMONTH`,`HRYEAR4` | calendar time |

**Occupation-basis note (frozen):** CPS adopted 2018-census occupation codes in January 2020; the
primary window (2021-07 onward) is therefore entirely on the 2018 basis, so a single occupation→SOC
crosswalk applies throughout. 2019 and earlier (2010-basis) are excluded from the primary sample.

### 4.2 AI-exposure index — AIOE (Felten, Raj & Seamans), in hand

- **Primary exposure:** **Language-Modeling AIOE** — the LLM-specific occupational-exposure variant, by
  6-digit SOC, 774 occupations (`AIOE-Data/AIOE`, `Language Modeling AIOE and AIIE.xlsx`, sheet
  `LM AIOE`; downloaded and inspected 2026-05-31). Chosen because the shock is a *language model*.
- **Robustness exposure:** base **AIOE** (general AI-occupational-exposure, same repo, Appendix A).
- Committed to `exposure_inputs/` (small).

### 4.3 Occupation crosswalk — Census 2018, in hand

`2018-occupation-code-list-and-crosswalk.xlsx` (Census; downloaded 2026-05-31). The
"Summary of 2018 Changes" sheet gives a clean **2018-census-occupation-code → 2018-SOC-code** mapping
(one SOC per census code), which bridges `PEIO1OCD` to the SOC-indexed AIOE scores.

---

## 5. Exposure construction (FROZEN before outcomes)

1. **Crosswalk:** `PEIO1OCD` (4-digit census occ) → 2018 SOC code, from the Census crosswalk sheet.
2. **Attach AIOE:** join census→SOC→Language-Modeling-AIOE. Where the census code maps to a *broad*
   SOC (e.g. `11-2030`) rather than a 6-digit detailed SOC, the occupation's exposure is the **simple
   mean** of Language-Modeling-AIOE over all 6-digit SOCs nested under that broad code. Military codes
   and any unmatched census codes receive no exposure and are dropped from exposure-based estimation.
3. **Exp_o (primary):** the occupation's Language-Modeling-AIOE, **z-scored (unweighted) across the
   matched census-occupation codes.** Continuous; enters the model directly.
4. **Quartile bins (companion, for figures/interpretation only):** occupations assigned to exposure
   quartiles Q1…Q4 using **pre-period employment-weighted** breakpoints. Used for plots and "top-vs-
   bottom-quartile" effect sentences, never as the basis of the headline statistical claim. (Mirrors
   the SO study's continuous-primary + categorical-companion discipline.)
5. **Robustness:** repeat steps 1–4 with base AIOE; the H1 result must survive (§2 falsification).

All of §5 is frozen here before any post-shock outcome is read.

---

## 6. Sample, classes, and window (FROZEN)

- **Persons:** employed status defined by `PEMLR ∈ {1,2}`; counts are weighted by `PWCMPWGT`/10⁴.
- **Age:** **primary 18–64**; robustness 25–54 and 16+.
- **Classes compared (the contract gradient):**
  - **No-contract (treatment):** `PEIO1COW = 7` — self-employed, unincorporated. Primary proxy.
  - **Salaried (control):** `PEIO1COW = 4` — private for-profit wage/salary. The cleanest same-sector
    comparison.
  - **Incorporated self-employed (middle rung, H2):** `PEIO1COW = 6`.
  - Government (1–3), nonprofit (5), without-pay (8) excluded from the primary contrast (government has
    extreme, qualitatively different contract stickiness; may appear only as a robustness benchmark).
- **Primary window:** **2021-07 … latest available (≈2026-04)** — entirely post-COVID-acute, single
  occupation-code basis.
- **Real shock:** **2022-11** (ChatGPT public release). Pre = 2021-07…2022-10 (16 mo);
  Post = 2022-11…end (~42 mo). No washout (employment adjusts gradually, with no novelty spike to
  exclude); effects additionally reported by calendar year (2023/2024/2025/2026) to show the ramp.
- **Placebo shock:** **2022-05** — a fake shock in the middle of the clean pre-ChatGPT stretch. Placebo
  sample restricted to 2021-07…2022-10 (AI-clean): pre = 2021-07…2022-04, post = 2022-05…2022-10.
  Pre-committed expectation: **β₃ ≈ 0**. A significant negative β₃ here voids the H1 identification.
- **Extended-pre robustness (stretch):** prepend 2020-01…2020-02 (post-2018-basis, pre-COVID) and, if
  the 2010→2018 occupation crosswalk is applied, 2019; the acute COVID window 2020-03…2021-06 is
  **never** included. Not part of the primary; reported only if it materially changes inference.

The realized data endpoint and any source fallback are reported in `PAPER.md`/`RESULTS.md`; the
hypotheses, classes, exposure, estimator, and falsification tests above are frozen regardless.

---

## 7. Estimator and analysis plan (FROZEN)

**Unit:** cell = occupation *o* × class *c* × month *t*, with weighted employment count
`E[o,c,t]` (sum of `PWCMPWGT`/10⁴ over employed persons in the cell).

**Primary model — PPML triple-difference.** Poisson pseudo-maximum-likelihood (statsmodels GLM,
Poisson family) of the employment *count* on:

> `E[o,c,t] ~ PPML( α[o×c] + δ[t] + β₁·Post_t·Exp_o + β₂·Post_t·NoContract_c + β₃·Post_t·Exp_o·NoContract_c )`

- `α[o×c]` = occupation×class fixed effects (absorb cell size and the time-invariant Exp_o,
  NoContract_c, and Exp×NoContract level terms).
- `δ[t]` = calendar-month fixed effects (absorb all aggregate/seasonal employment movement, incl.
  business cycle).
- **β₃ (Post × Exp × NoContract) is THE contract-buffer coefficient.** H1 ⇔ β₃ < 0.
- PPML chosen because it models counts in levels (coefficients ≈ proportional effects), is consistent
  under heteroskedasticity, and tolerates thin/zero cells (Silva & Tenreyro). Classes restricted to
  {salaried = 4, no-contract = 7} for the primary two-way DDD; {4,6,7} for the H2 gradient.
- **Inference:** standard errors clustered by occupation. Because no-contract cells are thin and the
  cluster structure is unbalanced, β₃ is additionally subjected to a **wild-cluster bootstrap** (and a
  month-block permutation of `Post`) p-value; the headline claim must hold under the bootstrap.

**Event-study (dynamics, H1b).** Replace `Post_t` with event-time-bin indicators (pre-period bins to
test pre-trends; post bins by quarters/years) interacted with `Exp_o·NoContract_c`. Pre-period bin
coefficients ≈ 0 (parallel trends) is required; the post bins trace whether the no-contract penalty
appears early and grows. Plotted with CIs.

**Companion (interpretation/figure).** Quartile-bin DDD: top vs bottom exposure quartile × class ×
pre/post, giving an interpretable "no-contract employment in top-exposure occupations fell X% more
than salaried" sentence and the headline figure. Never the basis of the headline inference.

**Pre-committed robustness battery (all reported, whatever they show):**

1. **Placebo shock 2022-05** (§6) — expect β₃ ≈ 0. *Identification gate.*
2. **Base AIOE** exposure reproduces the sign/significance of the Language-Modeling-AIOE result.
3. **Cell threshold:** drop occ×class cells with < 10 raw respondents in a month; re-run at < 5 and
   < 20.
4. **Age bands:** 25–54 and 16+ beside the 18–64 primary.
5. **Share-based outcome:** no-contract share of employment within occupation (denominator-robust
   alternative to counts).
6. **Hours** (`PEHRUSL1`) as a secondary intensive-margin outcome.
7. **Incorporated-SE gradient** (H2): does class 6 land between 4 and 7?
8. **Extended-pre window** (§6 stretch), COVID-acute always excluded.

The H1 conclusion is declared **robust** only if the sign and significance of β₃ survive 1–4; results
that hinge on a single specification are reported as exploratory.

---

## 8. From result to book (pre-committed both ways)

- **If H1 holds** (β₃ < 0, survives placebo + robustness): Chapter 4's forerunner hinge moves from an
  explicit 🟡 inference toward 🟢 *in prose* (claim-type carried in words, no emoji in reader-facing
  text, per `STYLE.md`). Update `evidence_base.md`, `SYNTHESIS.md`; flip RT-04B to ✅ in
  `RESEARCH_TODO.md`; add the study as a second self-owned 🟢 pillar beside `so_sdt_study`.
- **If null / mixed** (β₃ null, or killed by placebo): Chapter 4 keeps the 🟡 honesty but now **cites a
  direct test that failed to confirm the contract-buffer mechanism** — itself a credibility gain, and a
  point *for* the substitutability rival the chapter already steelmans. Either way the book gets more
  honest, not merely more confident.

---

## 9. Why this is "more like science" than a vibe

| Loose version | This study |
|---|---|
| "Freelancers got hit first" (anecdote) | Within-occupation DDD on nationally representative microdata |
| Substitutability and contract confounded | Occupation FE holds substitutability ~constant; only the buffer varies |
| Cherry-picked occupations | Continuous exposure over all occupations; "translators" is narrative, not the estimator |
| Effect assumed | Placebo shock + pre-trend test can void it; null pre-committed as publishable |
| Post-hoc story | Hypotheses, classes, exposure, estimator frozen here before outcomes |

---

## 10. Scope discipline (the lesson from the retired ABM)

ONE contrast (no-contract vs salaried), ONE shock (2022-11), ONE exposure construct (with a base-AIOE
robustness), a small set of frozen predictions (H1 deeper, H1b earlier, H2 gradient), each with a
built-in null and a placebo. No multi-scenario grids, no hand-tuned parameters. If H1 holds cleanly,
that is a pillar. If it fails cleanly, that is also a result — and a more honest book. Either way it is
falsifiable, which the retired model was not.

---

## 11. Reproducibility

`build_extract.py` pulls the needed CPS months (NBER + Census), keeps only the needed columns and
employed records, attaches the committed crosswalk + AIOE exposure, validates Census vs NBER on the
2023 overlap, and writes a **slim committed cell-level analysis file** (occupation × class × month
counts, a few MB). Raw multi-GB monthly microdata are never committed (`.gitignore`). The exposure and
crosswalk inputs (small) are committed. Analysis scripts run from the committed slim file. Stack:
pandas, numpy, statsmodels (PPML/GLM), matplotlib; `pyreadstat` for NBER `.dta`.

---

## 12. Amendment log

Any change to the frozen design after 2026-05-31 is recorded here (date, what, why). The original
frozen text above is amended only with a visible pointer here; never silently rewritten.

- *(none yet — frozen 2026-05-31)*
