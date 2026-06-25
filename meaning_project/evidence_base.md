# Evidence Base — 🟢 Empirical Anchors

The running catalogue of real, data-backed evidence the Meaning Project can stand on. Each
entry is a 🟢 anchor: something we *know* (with the usual caveats), not something we infer or
wish. Add to this over time. When an article cites a 🟢 claim, it should trace to here.

Format per entry: **Claim** — source(s) — what it does/doesn't show — how solid.

---

## Work as a source of non-financial meaning

- **Jahoda's latent functions of work.** Marie Jahoda (1982), building on the 1930s Marienthal
  unemployment study. Work provides five latent functions beyond income: time structure,
  social contact, collective purpose, status/identity, regular activity. *Shows:* unemployment
  harms wellbeing even when income is replaced. *Solid* (foundational, replicated in spirit).
- **Deaths of despair.** Case & Deaton (2020). Rising mortality (suicide, overdose, alcohol)
  among US working-class whites as stable work/community eroded. *Shows:* collapse of work +
  meaning + community tracks real mortality. *Solid but correlational/confounded.*

## "Money without work" natural experiments

- **Retirement & wellbeing.** Mixed literature; retirement can raise life satisfaction (relief
  from bad jobs) OR raise depression/cognitive decline (loss of structure/purpose),
  conditional on health, voluntariness, social ties. *Shows:* removing work is not uniformly
  good or bad — mediators matter. *Moderately solid; heterogeneous.*
- **Lottery winners.** Studies (e.g. Swedish lottery data) find large wealth modestly raises
  life satisfaction but not mental health much; many keep working. *Shows:* money alone is a
  weak lever on deeper wellbeing. *Reasonably solid (some good natural experiments).*
- **UBI / unconditional cash experiments** (see also so_sdt_study lit review):
  - Finland (2017–18): 2,000 unemployed, €560/mo. Employment barely moved (~0.39 days yr 1);
    recipients reported better mental wellbeing, less depression/loneliness, stronger economic
    security. Public microdata (FSD). *Shows:* cash reduces stress + lifts wellbeing modestly —
    relief/security, not restored purpose. VERIFIED 2026-05 (VATT / Finnish Gov / Kela results).
  - OpenResearch / Altman ($1k/mo, 3yr, 1000 recipients, 2020–2023; results Jul 2024):
    stress & mental distress improved in **year 1** but **faded by year 2**. Researchers
    attribute the fade partly to confounds: year-1 overlap with COVID relief payments, and
    inflation eroding the fixed $1k. Also: spending went to essentials (rent/food/transport),
    minimal physical-health effects, slight drop in work hours, parenting gains for lowest-income.
    *Shows:* cash → real but bounded/temporary psychological relief; "fade" is confounded, so
    don't over-read it as "money's comfort always evaporates." VERIFIED 2026-05 (multiple
    secondary sources incl. openresearchlab.org findings, CBS, Michigan Ross summaries).
  - GiveDirectly Kenya: wellbeing + aspiration gains; framing (community vs basic-needs) matters.
  - **Germany — Pilotprojekt Grundeinkommen (RCT).** Bohmann, Fiedler, Kasy, Schupp & Schwerter
    (DIW Berlin / WU Vienna / Mein Grundeinkommen); DIW Wochenbericht 15/2025; working paper *"Cash
    Transfers, Mental Health, and Agency: Evidence from an RCT in Germany"* (9 Apr 2025).
    Randomised controlled trial: €1,200/mo for 3 yr (Jun-2021…May-2024), N=107 recipients.
    *Shows:* mental health **+0.347 SD**, **purpose in life +0.250 SD**, life satisfaction
    **+0.417 SD**, **stable across all three years (no fade)**; **no withdrawal from the labour
    market**. *Limits:* small sample (N=107), single country, self-report; 0.25 SD is the smallest
    of the three effects. *Use (state honestly):* a **modest but well-identified counterweight** to
    the "money buys relief, not meaning" synthesis below — unconditional cash here produced a
    *stable purpose* gain, and the no-fade contrasts with the (confounded) Altman fade. Does not
    overturn the anchor; it caveats it: cash *can* nudge purpose, not only relief. VERIFIED 2026-06
    (multiple secondary sources citing the DIW primary; German primary not read directly).
    https://www.diw.de/en/diw_01.c.796681.en/projects/basic_income_pilot_project.html
  - Meta-analyses: cash → small positive subjective-wellbeing (d≈0.13), larger on
    depression/anxiety, often not sustained post-program.
  - **Synthesis:** money reliably buys *relief from material stress*; its lever on *meaning/purpose*
    is weak **but not zero** — the German RCT (above) found a *stable* +0.25 SD purpose-in-life gain,
    the first well-identified crack in a too-strong reading. Net: money is a *weak-but-real* lever on
    purpose, a *strong* one on relief. Still the project's most important recurring 🟢 result —
    stated with the German caveat. (Caveat added 2026-W24.)

## Resource abundance → divergent social outcomes

- **Nauru vs Gulf states.** Resource wealth without productive roles (Nauru: obesity, diabetes,
  social dysfunction) vs Gulf states (role preservation via government employment, civic/tribal
  structures). *Shows:* abundance alone doesn't determine outcomes; role/meaning structures do.
  *Weak as causal evidence — heavily confounded, post-hoc. Use only illustratively (🟡).*

## AI's actual effect on contribution communities (the SO line)

- del Rio-Chanona et al. 2024 (PNAS Nexus); Burtch et al. 2024 (Sci Rep); Quinn & Gutt 2025
  (JMIS); Li & Kim 2024 (Mktg Letters); Shan & Qiu (ISR). SO activity fell ~16–25%; decline
  concentrated in peripheral users; status/reputation contributors demotivated; learning
  effects can *raise* per-user output. All verified from primary text (`so_sdt_study/
  related_work_check.md`).
- **Our own SO null result** (`so_sdt_study/PAPER.md`): motivation type predicts behaviour,
  but the motivation→behaviour structure is *stable across* the ChatGPT shock (placebo-
  confirmed). *Shows:* AI lowered volume without selectively restructuring the community along
  motivational lines. A 🟢 pillar and a cautionary case study for the writing.
- **Our own SO platform-level trend** (`so_sdt_study/platform_trend/`, Stack Exchange API):
  public contribution activity collapsed — answers −45% (2023) → −95% (early 2026); questions
  similar. New-user counts are noisy (a ~99% spike in 2024 = bot artifact), so report
  *contribution activity*, not *user counts*. Platform-wide ~45% first-year answer drop ≈ our
  cohort's ~50% → early collapse is driven by existing contributors ceasing to produce.
  *Shows:* SO is an early "post-labour lab" — voluntary, no employment stickiness, so AI's hit
  lands unbuffered and fast. VERIFIED 2026-05 (own API pull).
- **Our own contract-buffer null** (`contract_buffer_study/PAPER.md`, RT-04B): pre-registered
  triple-difference on CPS basic-monthly microdata (2021-07…2026-04) × Language-Modeling AIOE
  exposure, testing whether **no-contract** workers (unincorporated self-employed) lose
  employment faster than **salaried** workers in the *same* AI-exposed occupations after ChatGPT.
  *Shows (null):* no significant differential — β₃ = −2.2%/SD (p=0.21, 95% CI [−5.5%,+1.2%]);
  a placebo shock one year *before* ChatGPT reproduces the same −2.2% (p=0.37), so even the faint
  tilt is not shock-driven; event-study pre-trends flat, no post-shock descent; the buffer-gradient
  test runs the *wrong* way; null across base AIOE, age bands, cell thresholds, hours. Crucially
  β₁ (common exposure effect) = **+1.7%** — AI exposure produced *no* employment decline in CPS
  by 2026 even for salaried workers, so the test is partly too-early / under-powered.
  *Use:* a 🟢 pillar that **fails to confirm the contract-buffer mechanism** behind the Ch.4
  forerunner hinge. It does not refute it, but it weakens the broad-generalisation claim and lends
  weight to the rival reading that the SO collapse was a uniquely substitutable special case. A
  second self-owned, pre-registered **null** beside the SO study; the book now cites it openly and
  lowers its confidence accordingly. VERIFIED 2026-05 (own NBER+Census pull; parser validated vs NBER).

## Productivity / labour-market effects of generative AI (for the economics layer)

- Brynjolfsson, Li & Raymond 2023 (call-center: AI lifts novices most); Noy & Zhang 2023
  (writing tasks); occupational-exposure studies (Felten; Eloundou et al.). *Shows:* real,
  measurable, uneven near-term effects. *Growing, moderately solid.*
- **Stanford Digital Economy Lab — "Canaries in the Coal Mine?"** (Brynjolfsson, Chandar & Chen,
  working paper, Nov 2025). High-frequency **ADP payroll** records. *Shows:* workers aged 22–25
  in the most AI-exposed occupations saw a **~16% relative decline** in employment after genAI
  spread (≈6% absolute decline late-2022→Jul-2025), while older workers in the same roles grew
  6–9%. Declines concentrated where AI **automates** rather than augments. The single clearest
  🟢 signal of labor harm so far — and it's narrow (young + entry-level). VERIFIED 2026-05.
  **⚠️ CONFOUND (added 2026-W23):** the NY Fed remote-work paper (Emanuel/Harrington/Pallais,
  below) finds remote work — not AI — explains ~two-thirds of the *same* young-grad unemployment
  rise in 2022–24, with AI exposure not explaining the divergence in that window. The drop is
  real; its *cause* is now genuinely contested (AI-automation vs remote-work mentorship loss).
  Cite ADP with this caveat; do not present the young-cohort signal as settled AI harm.
- **NY Fed — "Remote work, not AI, sidelined recent college graduates"** (Natalia Emanuel [NY
  Fed], Emma Harrington [UVA], Amanda Pallais [Harvard]; *Liberty Street Economics*, 1 Jun 2026).
  Federal employment data + an occupational remotability index, plus a single Fortune-500 tech-
  firm case study. *Shows:* unemployment among college grads <29 rose ~20% post-pandemic (2022–24
  vs 2017–19) while older grads' held/fell; the gap concentrates in **"remotable" jobs**; remote
  work accounts for **~64%** of the rise; mechanism is reduced mentoring/feedback for juniors
  hired remotely (engineers got ~20% more feedback seated near colleagues; the case firm shifted
  hiring ~a decade older after going remote, reversed on return-to-office). **AI exposure "didn't
  explain the divergence" in 2022–24** (authors note it could in later years). *Limits:* one
  case firm + index-based macro analysis; observational; the AI-null is window-specific.
  *Use:* the load-bearing **confounder** on the entry-rung/experience-creep thread — a well-
  identified rival to the AI reading of the young-cohort drop. In the spirit of the contract-
  buffer null: the AI-attribution is weaker than the headline. VERIFIED 2026-06 (multi-source;
  primary blog 503'd at fetch, specifics corroborated across NPR/CNBC/KCLU coverage).
  https://libertystreeteconomics.newyorkfed.org/
- **Anthropic Economic Index** (5th report, 2026; ~1M Claude.ai + API conversations). *Shows:*
  ~40% of US employees use AI at work (up from ~20% in 2023); on Claude.ai, **Nov 2025 split ≈
  52% augmentation / 45% automation** (automation briefly led in Aug 2025; API skews automated).
  Human capital enables AI use (input/output education level r>0.92; experienced users automate
  better). *Caveat:* single-provider usage data, not the whole economy. VERIFIED 2026-05.
  → use for the "what's being automated" + augmentation-vs-automation watchlist (Q5/Q6).
- **Anthropic Economic Index — "Learning curves" report** (Mar 2026; Nov 2025→Feb 2026 data).
  *Shows:* on Claude.ai **augmentation increased slightly** (validation/learning patterns) and
  still leads (>half), while **automation decreased sharply in the 1P API**; coding is migrating
  from augmentative (Claude.ai) toward automated (API); customer-service & automated-trading API
  workflows ~doubled. New: **6-month+ tenured users have a ~10% higher conversation success rate**
  (after controls) — "skill-biased technological change," early-adopter advantage compounding.
  *Honesty note:* this resolves a 2026-06-01 daily flag — the Yale Budget Lab secondary framing
  ("Claude usage now more automation than augmentation") conflated API with consumer; on the
  **consumer** surface augmentation still leads. So the project's "augmentation-dominant on the
  human-facing side" reading **holds** (verified from primary, not the headline). VERIFIED
  2026-06 (primary report). → augmentation-vs-automation watchlist; the dual (economic+
  psychological) breakpoint.
- **IMF Staff Discussion Note SDN/2026/001, "Bridging Skill Gaps … New Jobs Creation in the AI
  Age"** (Goraya, Mendes Tavares et al., IMF, 9 Jan 2026; Lightcast job-postings). *Shows:*
  new-skill postings carry a 2–3.4% wage premium and +1.3pp local employment — **but
  AI-specific** skill postings carry higher wages (~7.5–8% UK) with **no overall employment gain**
  in local US markets; middle-skilled workers capture no significant benefit; polarisation
  reinforced. *Limits:* postings ≠ filled jobs; Lightcast skews formal employment. *Use:* the
  honest empirical basis for "the 'new jobs' mechanism holds for general new skills but, for the
  AI-specific slice, delivers **wages without headcount** and skips the middle." Pairs with the
  Stanford/ADP young-cohort finding. VERIFIED 2026-06.
- **Macro/labour texture, June 2026** (compact 🟢-with-caveats note; details in daily logs
  2026-06-04…08). *Goldman Sachs* payroll decomposition: gross AI substitution ~25K jobs/mo,
  augmentation ~+9K, net ~−11–16K — and the offsetting "new jobs" are **data-centre construction,
  not re-employed admin workers** (proprietary model, read via journalism). *BLS May 2026:* +172K
  payrolls, U 4.3%, but **financial activities −107K/12mo** and **information −342K since Nov-22**
  persist in high-exposure sectors while growth comes from low-exposure ones (hospitality, health,
  local gov) — BLS assigns no cause. *Dallas Fed TBOS:* 66% of TX firms use AI; 10% already cut
  headcount need, 30% expect to. *NACEWEB:* entry-level AI-skill demand ~tripled in two survey
  quarters; **40% of early-career workers report changing career plans because of AI.** *Use:*
  macro still calm; sector pattern cohering with selective high-exposure displacement; skills
  goalposts moving faster than any retraining cycle. None individually a pillar; together they
  texture the "early innings, loop not closing for the displaced" reading. VERIFIED 2026-06.
- **Massenkoff & McCrory, "Labor Market Impacts of AI: A New Measure and Early Evidence"**
  (Anthropic Research, 5 Mar 2026). 🟢 **with a prominent provider-conflict caveat** — Anthropic
  authors using Claude usage as the "observed exposure" measure (what AI is *actually* automating,
  not what it *could*). *Shows:* (a) **no unemployment-stock rise** in the most-exposed occupations
  since Nov-2022; (b) a **suggestive narrowing of the hiring rate** of younger workers *into* exposed
  roles since ~2024 — a *flow* signal that could precede a *stock* signal; (c) programmers (~75%),
  data-entry (~67%), customer-service (~65%) most exposed. Names a "white-collar Great Recession"
  (3%→6% top-quartile unemployment) as detectable-but-not-yet. *Limits:* single-provider exposure
  data; author interest; short window; flow signal only "suggestive." *Use:* methodological advance
  (deployment, not capability) + an early-warning *flow* indicator — but see the NY Fed postings null
  directly below, with which it is in tension. VERIFIED 2026-06. https://www.anthropic.com/research/labor-market-impacts
- **Audoly, Guerin & Topa, "Do Job Postings Show Early Labor-Market Effects of AI?"** (NY Fed
  *Liberty Street Economics*, 14 May 2026). 🟢 (Fed economists; Lightcast postings; blog-format staff
  analysis, US-only). *Shows:* high-exposure occupations have relatively lower vacancies, **but the
  divergence began *before* Nov-2022 ChatGPT**, and there is **no junior/senior divergence** within
  exposed occupations; firms intend to absorb AI via *retraining*, not hiring cuts; <10% of US
  workers/vacancies are in occupations with exposure ≥0.4. *Use:* the strongest **attribution-sceptic**
  finding yet — and it **cuts against the "entry-rung closing" / experience-creep reading** on its own
  terms, while sitting in unresolved **tension with Massenkoff & McCrory's hiring-flow narrowing**. The
  fourth institutional null/complication after our contract-buffer null, the NY Fed remote-work confound,
  and the M&M stock-null. VERIFIED 2026-06. https://libertystreeteconomics.newyorkfed.org/2026/05/do-job-postings-show-early-labor-market-effects-of-ai/
- **PwC 2026 Global AI Jobs Barometer — "the raised floor"** (PwC, 15 Jun 2026; >1B job ads, 27
  countries). 🟡 **only** (descriptive job-ad analysis from a firm that *sells* AI advisory —
  structural conflict of interest; proprietary undisclosed methodology; postings ≠ filled jobs; no
  causal identification). *Shows:* AI-skill jobs grew 69% vs 9% market-wide; the meaning-relevant
  finding is the entry level — **AI-exposed entry roles grew 35% since 2019 (non-exposed fell 10%)
  but now require ~7× more traditionally senior-level skills** (judgment, leadership, creativity); a
  "professionalised vs democratised" two-track split. *Use:* a **reframe** of experience creep — the
  entry problem may be less "the door is closed" (NY Fed postings find no junior/senior divergence)
  than **"the floor of expected competence has been raised out of reach,"** disrupting the SDT
  *competence*-building developmental arc of early work. Logged 🟡, not as a 🟢 anchor: conflicted
  source, in unresolved tension with the NY Fed postings null and the IMF wages-without-headcount
  finding. VERIFIED 2026-06 (secondary).
  https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html
- **ILO macro pair (J-curve / micro-signal, macro-null)** — *"The Impact of GenAI on Jobs,
  Productivity and Work Organization"* (1 Jun 2026, 7 countries) and *"The Aggregation Paradox of
  AI"* (6 May 2026). 🟡 (institutional synthesis; **primary text not retrieved — flagged for
  retrieval before any 🟢 use**). *Show:* a consistent **micro-signal / macro-null** — real but uneven,
  often unverified task-level productivity gains that have **not** translated into measured output,
  earnings, employment, or any official aggregate productivity signal; AI sits early on a **J-curve**,
  with the electrification/ICT precedent implying the aggregate payoff lags *organisational and
  institutional* adaptation by years-to-decades. *Use:* sharpens the **speed-vs-adjustment** breakpoint
  — the live question is not "will AI pay off?" but "what do people do for meaning *in the lag*?"; the
  measurement gap itself weakens the near-term political case for distributing AI gains (and funding
  meaning-sustaining institutions). VERIFIED 2026-06 (secondary; primary pending).
  https://www.ilo.org/publications/impact-genai-jobs-productivity-and-work-organization-review-empirical
- **Mertens, Kuzee et al., "Crashing Waves vs. Rising Tides"** (MIT FutureTech, arXiv:2604.01363,
  Apr 2026). 🟢 (17,000+ worker evaluations of 3,000+ text-based O*NET tasks; preprint; 2029 figures
  are extrapolations). *Shows:* little evidence of "crashing waves" (sudden occupational wipeouts);
  strong evidence of "**rising tides**" — broad, gradual capability growth across *all* text-based
  tasks at once. Pace: AI completed ~50% of 3–4-hour human tasks in Q2-2024, ~65% by Q3-2025;
  projected 80–95% by 2029. *Limits:* preliminary preprint, subjective "task completion," text-tasks
  only (no physical/relational), extrapolated projection, friendly (not independent) review. *Use:*
  the first task-level **pace** quantification for the speed-vs-adjustment breakpoint — and an
  empirical tide-line under "the retreat that runs out of high ground": no safe cognitive refuge, the
  floor rises everywhere at once. Reframes the question from "which jobs survive?" to "what is human
  text-based contribution at an 80–95% floor?" VERIFIED 2026-06. https://arxiv.org/abs/2604.01363
- **ILO–World Bank, "Disruption without dividend?"** (27 Mar 2026; 135 countries, ~⅔ of global
  employment). 🟡/🟢 (exposure modelling). *Shows:* GenAI exposure is uneven — wealthier nations
  higher (admin/professional); a "**disruption paradox**" — automation-vulnerable workers in poorer
  regions already have the connectivity for job loss to land *fast*, while those positioned for
  productivity *gains* lack reliable internet, so gains lag. *Use:* the global-distributional companion
  to the domestic attribution debate; mostly economics-layer. Distinct from ILO WP170 (below).
  VERIFIED 2026-06. https://www.ilo.org/resource/news/new-ilo-world-bank-paper-highlights-uneven-global-impact-generative-ai-jobs

## Deaths of despair (the 🟢 floor for the "how bad" chapter)

- **Case & Deaton** (2015 onward; *Deaths of Despair and the Future of Capitalism*, 2020).
  "Deaths of despair" = suicide + drug/alcohol poisoning + alcoholic liver disease. *Shows:*
  rising mortality among **middle-aged, non-college-educated white Americans** (45–54); 1998–2017
  overdose deaths up >4×, alcoholic liver disease +~50%, suicide +~37%; they attribute it to loss
  of employment, security, mobility — i.e. work-and-meaning erosion, not just income. *Limits
  (state honestly):* correlational, heavily confounded (opioid supply, healthcare, specific
  demographic/era); shows the stakes are mortal, does NOT prove a future post-work society repeats
  it. VERIFIED 2026-05.
- **⚠️ 2024 reversal (added 2026-W24).** *TFAH/Well Being Trust, "Pain in the Nation 2026"* (NCHS
  data, May/Jun 2026): deaths of despair fell **16% in 2024 vs 2023** (overdose −26%, alcohol −4%,
  suicide −3%) — the **first national decline since 1999**, present across demographic/geographic
  groups. *But:* attributed to naloxone access / fentanyl-awareness / treatment uptake, **not** any
  repair of the work-and-meaning conditions Case & Deaton named; Appalachia still ~33% above the
  national rate; SAMHSA lost ~$1B in early-2026 grants (the infrastructure behind the decline is now
  at risk). *Use:* the **monotonic-worsening framing is out of date** — cite the 2024 reversal. The
  stakes argument stands (persistence, structural risk, funding cuts), but no longer as an unbroken
  upward trend. VERIFIED 2026-06 (NCHS provenance via TFAH).
  https://www.tfah.org/report-details/pain-in-the-nation-2026-report/
- **Involuntary job loss causally accelerates cognitive decline.** Kouchekinia, Neumark & Bruckner,
  NBER WP 35117 (Apr 2026, rev. May). Bartik-IV using local labour-demand shocks; HRS. *Shows:*
  job loss from negative demand shocks **causally** accelerates cognitive decline — ~**2 extra
  years** of normal ageing — concentrated in **men 51–64**, via the *employment* channel (not income
  alone). *Limits:* Bartik-IV validity debated; older sample; data pre-genAI, so the AI-displacement
  link is an *inference*; the 2-year figure is from secondary coverage. *Use:* a **third stakes
  dimension** beside deaths-of-despair and Emile's purpose→mortality — displacement may carry
  *neurological* cost, and the affected demographic overlaps mid-career workers in the declining
  high-exposure white-collar sectors. Weakens "just find meaning elsewhere." VERIFIED 2026-06.
  https://www.nber.org/papers/w35117

## Relatedness / care as AI-resistant (direct test of "can AI supply mattering?")

- **"People prefer human empathy even when AI says the same thing"** (9 experiments, >6,000
  participants; 2025). *Shows:* identical LLM-written responses are rated **more empathic,
  supportive, and emotionally satisfying when labelled "human" than when labelled "AI"**; a
  one-sentence AI disclosure *reduces* felt empathy; people will wait longer for a human reply.
  This is a **direct 🟢 test** of Q3's open question ("can virtual/AI supply *mattering*?") — and
  the answer leans no: the value of care depends partly on a *human* being its source. Anchors
  Ch.6's relatedness path and Q7. VERIFIED 2026-05.
- **AI companions crowd out human connection (Replika)** — Aalto University; *CHI 2026*.
  Quasi-experiment: ~2,000 Replika users' public Reddit language, year-before vs year-after first
  use, matched controls. *Shows:* short-term comfort, but over time **more** loneliness,
  depression and suicidal-ideation signals than controls; mechanism is a **crowd-out** — AI
  companionship "raises the perceived cost of human relationships," so users reach out to people
  less. *Limits:* observational (reverse causality possible — the distressed may seek companions),
  single platform, Reddit language a proxy. *Use:* the **behavioural** counterpart to the
  empathy-preference result above — together they push Q3 toward "AI cannot supply relatedness,
  and deployed as a loneliness fix it may backfire." VERIFIED 2026-06.
  https://dl.acm.org/doi/10.1145/3772318.3790558
- **Random human peer beats a purpose-built empathic chatbot (RCT)** — Li, Folk, Singh, Ungar &
  Dunn, *J. Experimental Social Psychology* 125:104911 (2026). Pre-registered three-arm RCT, N=296
  first-years (OSF materials): text a random human stranger / text "Sam" (a chatbot custom-built
  for maximal empathy) / journal (active control) for 2 weeks. *Shows:* only the **human-peer** arm
  significantly reduced loneliness; the empathic chatbot was **indistinguishable from journaling to
  no one**. *Limits:* single university, student sample, 2-week window, custom (not commercial)
  chatbot, self-report. *Use:* the **causal** layer Q3 lacked — even under optimistic design, AI
  doesn't move loneliness while a *stranger* does. VERIFIED 2026-06.
  https://www.sciencedirect.com/science/article/pii/S0022103126000417
- **AI companionship predicts *subsequent* loneliness (12-month panel)** — Folk & Dunn,
  *Psychological Science* (2026). 4-wave prospective panel, N>2,000, four English-speaking countries.
  *Shows:* a **bidirectional loop** — loneliness predicts later AI-companion use *and* AI-companion
  use predicts *higher later* loneliness; proposed mechanism: simulated connection meets the
  immediate craving without building human-relationship skill/habit. *Limits:* observational
  (reverse causality/confounding possible despite prospective design), self-report, no chatbot-type
  breakdown, English-speaking only. *Use:* prospective, direct-measure counterpart to Aalto's
  Reddit proxy — two methods, same direction. VERIFIED 2026-06. https://doi.org/10.1177/09567976261427747
- **Q3 status (updated 2026-W24):** with Aalto (quasi-experiment), Folk & Dunn (prospective panel)
  and Li et al. (RCT) now converging — plus the empathy-preference result and Emile/OECD mortality —
  the relatedness sub-question moves from "evidence leans no" to **"consistent multi-method evidence:
  AI cannot supply relatedness, and deployed as a loneliness fix it likely worsens the deficit."**
  This is the project's best-evidenced sub-question.
- **OECD, "Social Connections and Loneliness in OECD Countries"** (OECD, Oct 2025). Cross-national
  survey synthesis; descriptive, not causal. *Shows:* in-person interaction declining across the
  OECD; **young people (16–24) and men** saw the steepest recent deteriorations; loneliness + low
  social interaction associated with ~**871,000 premature deaths/yr** globally. *Limits:*
  descriptive trends; cross-national comparability caveats; the mortality figure is a global
  estimate under varying assumptions. *Use:* demographic precision the canon lacks — the socially
  most-at-risk group (young men) is the same group taking the early entry-level hit ("double
  exposure"); pairs with Emile's mortality mediation. VERIFIED 2026-06.
  https://www.oecd.org/en/publications/social-connections-and-loneliness-in-oecd-countries_6df2d6a0-en.html
- **Subjective loneliness — not objective isolation — predicts cognitive impairment and shorter
  life.** Yoneda et al. (24-author international team, UC Davis-led); *Journal of Personality and
  Social Psychology* (15 Jun 2026). 175,000 adults aged 50+ across 18 countries, **harmonized
  coordinated-analysis** design (multiple cohorts modelled in parallel — a strong replication frame).
  *Shows:* with loneliness and isolation statistically separated, **subjective loneliness** (the
  *feeling* of disconnection) consistently predicts higher risk of severe cognitive impairment (a
  10% rise in reported loneliness ≈ 8–9% higher impairment risk), shorter life, and ~3% lower chance
  of recovering from mild impairment — while **objective social isolation showed no consistent
  cognitive link** and only a weak mortality association. Authors recommend screening loneliness as a
  clinical **"vital sign."** *Limits:* observational; older-adult sample (mean 50+); loneliness
  self-reported; **primary text not retrieved — specifics from the UC Davis/UC press release and
  secondary coverage.** *Use:* the **mechanism** upgrade to Q3 — it names the *pathogenic variable*
  (the felt experience, not the contact count). This closes the AI-companion loop: companions reduce
  *isolation* ("talking to someone") without moving *loneliness*, and loneliness is what carries the
  cognitive/mortality cost — so companions target the wrong variable. Adds **cognitive decline** as a
  third relatedness health-stake (beside purpose-erosion and premature mortality) and pairs with
  Kouchekinia et al. (job loss → ~2 yrs' cognitive ageing): work supplies both structured contact and
  purpose, so its erosion reaches the same neurological endpoint by two routes. VERIFIED 2026-06
  (secondary). https://www.ucdavis.edu/news/loneliness-drives-cognitive-impairment-and-shorter-life-more-social-isolation-new-study

## How AI is used (not whether) governs its meaning effect — the augmentation/automation axis as psychology

- **Lee et al., "Relying on AI at work reduces self-efficacy, ownership, and meaning while active
  collaboration mitigates the effects"** — *Scientific Reports* 16:13583 (2026). Pre-registered
  experiment (N=269) + follow-up (N=270). *Shows:* **passive** AI use (copy the output) reliably
  undermined self-efficacy, psychological ownership and perceived work meaningfulness — and the
  declines **persisted** after returning to manual work; **active** collaboration (draft first,
  then AI-refine) preserved all three at levels indistinguishable from independent work. *Use:*
  AI use *per se* does not corrode the psychological sources of meaning — *how* you use it does.
  Makes augmentation-vs-automation a **psychological** category, not only an economic one; pairs
  with the SO study and the human-empathy/care findings. VERIFIED 2026-06.
- **Ranjit et al., "Are We Automating the Joy Out of Work?"** — arXiv:2603.14963; *CHI 2026*.
  Survey of workers/developers rating 171 representative tasks, then LM-scaled to 10,131 O*NET
  computer-assisted tasks. *Shows:* tasks workers associate with **agency and happiness are
  disproportionately AI-exposed** relative to tasks they rate routine/low-meaning; plus a
  worker↔developer mismatch on what AI should optimise. *Limits:* self-reported meaning ratings,
  LM-inferred scaling (not independent measurement), design-advocacy venue, no causal/longitudinal
  arm. *Use:* the **task-selection** layer above Lee et al.'s individual mechanism — reframes the
  risk from "some jobs vanish" to "the parts of jobs that *produce* wellbeing are the parts being
  targeted." VERIFIED 2026-06. https://arxiv.org/abs/2603.14963
- **Giuntella, Koenig & Stella, "AI and the wellbeing of workers"** — *Scientific Reports* 15:20087
  (Jun 2025). German SOEP, two decades, DiD/event-study; observational; data ends ~2020 (pre-
  generative-AI). *Shows:* **no average harm** from AI occupational exposure to mental health/
  subjective wellbeing (slight health gains via reduced physical job intensity) — **but** among
  workers who *actually report using AI tools*, "indications of declining life and job
  satisfaction." *Limits:* occupational exposure ≠ individual use; self-report subsample smaller/
  selected; German co-determination may buffer harms. *Use:* the **reconciliation** anchor — the
  population-average null and Lee et al.'s task-level mechanism operate at different levels; the
  actual-user nuance bridges them and warns the null may not survive deeper AI penetration.
  VERIFIED 2026-06. https://www.nature.com/articles/s41598-025-98241-3
- **ILO Working Paper 170, "AI systems @ work: a changing psychosocial work environment"** (ILO,
  30 Apr 2026). 🟡 (institutional synthesis; **primary text not retrieved — reconstructed from ILO
  release + secondary coverage**; treat as indicative). *Shows:* algorithmic management and AI-driven
  workplace surveillance are linked to monitoring anxiety, eroded dignity/privacy and **reduced
  autonomy**; technostress and work intensification recur. *Use:* opens a **new pathway** — AI deployed
  *on* workers (control architecture), not only as task substitution — threatening the SDT **autonomy**
  need for the *employed-but-controlled*. Extends Lee et al. (individual choice) to the structural
  level; pairs with Ranjit (task selection) and BCG/HBR (time/intensification) to give a three-level
  "work reshaped in meaning-diminishing directions" picture. Policy lever: algorithmic-management
  regulation, not income support. *Caveat:* effect sizes/quality unverifiable from summaries.
  VERIFIED 2026-06 (secondary). https://www.ilo.org/publications/ai-systems-work-changing-psychosocial-work-environment

## Purpose as a measurable health (mortality) variable — the 🟢 floor under "meaning matters"

- **Emile, "Loneliness predicts mortality risk via the erosion of purpose in life"** — *Social
  Science & Medicine* 368 (23 Jan 2026). Prospective, Health and Retirement Study, N=8,351 US
  adults, 11-yr follow-up. *Shows:* purpose in life statistically explains **~88%** of the
  loneliness→premature-mortality association; the mediation runs primarily through *changes* in
  purpose over time (not baseline alone); robust to adjustment for depression, social isolation,
  neuroticism. *Limits (state honestly):* observational, older-adult sample (mean age ~68) — so
  causality and generalisation to working-age populations require care. *Use:* the clearest 🟢 yet
  that "purpose erosion" is not a soft cultural concern but a **measurable mediator of a mortality
  outcome** — grounds Q3 ("can AI supply mattering?") and the "meaning as a health variable"
  framing. VERIFIED 2026-06.

## Intrinsic vs extrinsic goals — the 🟢 spine of Ch.6's "turn"

- **Kasser & Ryan / SDT aspirations research** (1990s onward, replicated across cultures & ages).
  *Shows:* pursuing **extrinsic** goals (money, status, image, others' approval) is associated
  with **lower** wellbeing and more distress; pursuing **intrinsic** goals (growth, relationships,
  community/contribution) supports wellbeing via need satisfaction. VERIFIED 2026-05.
- **Niemiec, Ryan & Deci (2009), "The Path Taken," J. Research in Personality** (1-yr post-college
  longitudinal). *The killer finding:* **attaining** intrinsic aspirations raised wellbeing and
  lowered ill-being — but **attaining extrinsic aspirations did NOT raise wellbeing and actually
  related to ill-being.** i.e. even *succeeding* at money/status/recognition didn't help. This is
  the strongest 🟢 empirical backing for Ch.6's central turn (anchor meaning to process / what you
  control, not to external outcomes — AI is now devaluing exactly the external outcomes, and even
  winning them wouldn't have delivered the meaning). VERIFIED 2026-05.

## Retraining / active labor market policy — the honest 🟢 for Ch.7

- **US worker-retraining evaluations** (WIA/WIOA national randomized eval; TAA studies; LaLonde
  Hamilton Project review). *Shows:* training streams largely **did not** improve earnings or
  employment vs control over 30 months; TAA participants sometimes earned *less*. Active labor
  market retraining has "produced disappointing results relative to cost and expectations."
  *Use honestly:* the obvious policy answer to displacement (just retrain people) mostly doesn't
  work as advertised — so Ch.7 must NOT lean on it as a 🟢 solution; it's a cautionary 🟢.
  VERIFIED 2026-05.

## Robust Decision Making (the formal method behind Ch.7's "robust bet")

- **RDM — Lempert & colleagues, RAND** (foundational 2003/2006; widely used for "decisionmaking
  under deep uncertainty," DMDU). *Shows / provides:* a formal method to "make good decisions
  *without* predictions" — stress-test strategies across many plausible futures and pick those
  that hold up broadly, rather than betting on one forecast. This is the named, citable backing
  for Ch.7's "robust bet" standard (and the project's 🔴-policy posture generally). VERIFIED 2026-05.

## UBI fiscal / political-economy honesty (Ch.7, distinct from Ch.2's psychological evidence)

- *Fiscal scale:* Yang's $1k/mo-per-adult costed at ~$2.8–3.0T/yr (Tax Foundation); not supportable
  under current US fiscal structure without major reform. *Dividend idea:* fund from the AI surplus
  via sovereign-fund / equity-stake / land-value models (Alaska Permanent Fund analogy); one
  analysis estimates AI need only reach ~5–6× current automation productivity to finance an
  ~11%-of-GDP UBI even if no new tasks appear. *The catch (political economy):* the AI dividend
  accrues to **capital first** (2025 hyperscaler capex ~$142B/quarter), wages later and unevenly —
  so "can we afford UBI" is less a technical question than a *distributional/political* one. This is
  the honest backing for Ch.7's "distributing the gains is the political question." VERIFIED 2026-05.
- **The public wants work's *role* preserved, not just its income — Chueri et al.** "AI, the Future
  of Work, and the Politics of the Welfare State," *Perspectives on Politics* (Cambridge, 28 Apr
  2026; OECD "Risks that Matter" 2024 survey; replication data on Harvard Dataverse). 🟡/🟢
  (peer-reviewed political science; cross-national *attitudinal* survey — observational, stated not
  revealed preferences; pre-dates the fullest post-ChatGPT debate; **primary text not retrieved — from
  the Cambridge abstract + secondary**). *Shows:* fear of AI automation is widespread across
  educational groups and does **not** chiefly raise support for traditional income-support
  (unemployment benefits, retraining); it drives demand for measures that **preserve the social role
  of work** — robot taxes, guaranteed income *regardless of employment status*. *Use:* a rare
  *political-science* 🟢-quality datum and the **demand-side mirror** of the project's economic–meaning
  decoupling — the public, asked, does not say "just replace the income"; it implicitly recognises
  Jahoda's latent functions and wants work's *role* protected. Empirical counterweight to the
  techno-optimist "income support alone will do" reading; feeds Ch.7's 🔴 policy layer. VERIFIED
  2026-06 (secondary).
  https://www.cambridge.org/core/journals/perspectives-on-politics/article/ai-the-future-of-work-and-the-politics-of-the-welfare-state/92E806B812B86A8944003B77038DCAA8

---

## Gaps to fill (future 🟢 pillars to consider)

- Honest re-analysis of FIRE / early-retirement communities' wellbeing trajectories.
- Systematic re-synthesis of UBI psychological (not just financial) outcomes.
- Cross-platform: does relatedness-structure predict community resilience to AI?
