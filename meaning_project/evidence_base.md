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
- **CRR — "Are the Careers of Older Workers Being Cut Short by AI?" (the late-career mirror of the
  young-cohort drop; added 2026-W29).** Geoffrey T. Sanzenbacher, Center for Retirement Research at
  Boston College, *Issue in Brief* 26-13 (June 2026; read from the CRR primary PDF). 🟢 **with caveats**
  (CPS longitudinal panel 2014–2026, N=102,097 observations of workers 55+, matched to occupation-level
  AI exposure from Tufts' Digital Planet Initiative; probit with a pre/post-ChatGPT interaction term +
  demographic/job controls). *Shows:* **before** ChatGPT, older workers in more AI-exposed occupations
  were *less* likely to leave work (1-SD exposure → **−0.55pp** exit probability — the normal high-skill
  pattern); **after** ChatGPT the gap reversed to **+0.50pp**, driven specifically by a **+0.28pp rise
  in unemployment (involuntary job loss)** — **not** retirement or voluntary exit (near-zero). Computer
  programmers' predicted non-employment transitions rose 8.7%→11.1% (>25% relative); painters (low
  exposure) 13.5%→13.7% (~2%). Secondary framing: "55+ in AI-exposed jobs ~25% more likely to leave than
  before ChatGPT." *Limits (author's own):* correlational, not a clean natural experiment — Trump-admin
  R&D cuts to AI-exposed sectors could *exaggerate* the estimate, an AI-startup hiring boom could
  *understate* it; occupation-to-Census crosswalk imperfect; single country; data through ~April 2025.
  *Use:* the **older-worker mirror** of the Stanford/ADP young-cohort anchor — together they point to
  **AI-exposed career *edges* (entry 22–25 + late 55+) fraying while the middle holds** (hold the
  cohort-selection caveat: the "edges vs middle" read may partly reflect which cohorts have dedicated
  instruments). Also **corrects an anecdote** — the rise is in the *involuntary* channel, not the
  "workers voluntarily retiring to dodge AI" press narrative — i.e. displacement, not opt-out. Strengthens
  the cognitive/mortality stakes (Kouchekinia: involuntary job loss → ~2 yrs cognitive ageing, men 51–64,
  the overlapping demographic). VERIFIED 2026-W29 (primary PDF).
  https://crr.bc.edu/are-the-careers-of-older-workers-being-cut-short-by-ai/
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
- **Census BTOS — AI-adoption rate by sector (the adoption gradient matches the decline gradient).**
  U.S. Census Bureau Business Trends and Outlook Survey, 3 May 2026 collection wave (surfaced via a
  Bloomberg synthesis 1 Jul 2026, **verified directly at census.gov**). 🟢 (federal survey; primary
  figures). *Shows:* the **first sector-level AI-*adoption-rate* figures** in this base (distinct from
  the capability/exposure proxies elsewhere) — **Information 39.7%** and **Finance/Insurance 33.9%**
  reporting AI use, both ~**double the 19.8% national average**; Retail ~14%; very large firms in
  Information/Professional-Services/Finance reach 50–70% (employment-weighted). *Use:* the two sectors
  the project tracks *declining* on payrolls (information −342K since Nov-22; financial −107K/12mo) are
  precisely the two **adopting AI fastest** — the adoption gradient lines up with the employment
  gradient. A **sourcing upgrade**: cite census.gov adoption rates directly rather than via journalism.
  *Limits:* "used AI in the past two weeks" is a low bar (trivial vs transformative use
  undistinguished); adoption ≠ causation of the sector decline (correlational co-location). VERIFIED
  2026-W27 (primary). https://www.census.gov/library/stories/2026/05/ai-use-businesses.html
- **California AI-Unemployment Tracker (CAIT) — a new *ongoing government* attribution instrument.**
  California EDD + California Policy Lab (UCLA); launched 25 Jun 2026, first coverage wave ~2 Jul 2026.
  🟡/🟢 (first government-partnered, continuously-updating AI-attributed UI-claims dashboard;
  methodologically closer to Massenkoff & McCrory's observed-exposure measure than to capability indices;
  **but** UI-claims data — self-reported occupations, excludes non-filers/ineligible/labour-force-exiters;
  the tracker's own stated limit is "exposure ≠ causation"; administrative claims, single-state,
  preliminary — **not a standalone pillar**). *Shows (through May 2026):* **no statewide surge** in
  AI-related claims since ChatGPT's 2022 release, and no statistically significant rise in the AI-exposed
  share of claims — **but** claims from **college-educated workers in high-AI-exposure occupations** rose
  and stayed elevated, and the **SF Bay Area + information/professional-services** show a sharp, sustained
  increase since late 2022. *Use:* sits *inside* the existing synthesis (aggregate calm + selective
  high-exposure/high-education displacement) rather than overturning it — but it is a genuinely new
  **instrument** that **updates monthly**, so it becomes the project's live early-warning dashboard for
  the attribution question (unlike one-off papers). VERIFIED 2026-W27 (institutional; CPL primary report).
  https://capolicylab.org/california-ai-unemployment-tracker/
- **Ramp × Revelio Labs — firm-level AI *spending* vs headcount (the entry-level counterweight; primary
  source verified 2026-W29).** Ramp Economics Lab / Revelio Labs, "A New Look at AI's Impact on Jobs,"
  released 30 Jun 2026 (ramp.com/data/ai-jobs-impact). 🟡 (real corporate-card AI-vendor *spending*
  matched to workforce panel data across ~21,600 US firms — richer than survey or exposure proxy — **but**
  Ramp is a commercially interested fintech, and the authors flag selection: "AI adopters are not a random
  sample of employers"; correlational, not causal; lead economist calls it "early results… we will update
  over time"). *Shows:* firms in the **top third** of AI spending-per-employee grew total headcount ~**10.2%**
  and entry-level headcount ~**12%** over the two post-adoption years, while the bottom two-thirds saw no
  significant change. *Use:* the firm-level **counterweight** to the occupation-level "raised floor"
  (Stanford/ADP, PwC) — heavy-AI-adopting *firms* grew the entry rung even as AI-exposed *occupations* saw
  it raised. Different unit of analysis (firm AI-spend intensity vs occupational exposure), opposite
  entry-level valence, **unresolved** — sits in tension with Census BTOS (the fastest-adopting sectors are
  the fastest-declining on payrolls); both can hold if AI-spend marks already-fast-growing firms displacing
  slower competitors within a shrinking sector, but that reconciliation is untested. *Provenance note:* first
  folded into W27 via the Bloomberg synthesis; the primary source + figures were verified directly 2026-W29
  (sourcing upgrade). Watch for non-proprietary replication. VERIFIED 2026-W29 (primary).
  https://ramp.com/data/ai-jobs-impact
- **Macro/labour texture, June 2026** (compact 🟢-with-caveats note; details in daily logs
  2026-06-04…08). *Goldman Sachs* payroll decomposition: gross AI substitution ~25K jobs/mo,
  augmentation ~+9K, net ~−11–16K — and the offsetting "new jobs" are **data-centre construction,
  not re-employed admin workers** (proprietary model, read via journalism). *BLS May 2026:* +172K
  payrolls, U 4.3%, but **financial activities −107K/12mo** and **information −342K since Nov-22**
  persist in high-exposure sectors while growth comes from low-exposure ones (hospitality, health,
  local gov) — BLS assigns no cause. *(BLS June 2026, added W27:* +57K payrolls, U 4.2%, Apr/May revised
  down a combined 74K; information/financial-activities showed "little or no change" this month — i.e.
  **no acceleration** in the high-exposure decline. One month, no cause assigned; mild reinforcement of
  macro-calm, not a new signal.) *Dallas Fed TBOS:* 66% of TX firms use AI; 10% already cut
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
- **UN Independent International Scientific Panel on AI — Preliminary Report (PENDING PRIMARY READ,
  added 2026-W28).** United Nations; released **1 Jul 2026**; 40 scientists/experts from every region;
  **preliminary**, ahead of a full 2027 report. 🟡 (institutional evidence-based *assessment*, not
  primary research; **full report text not yet parsed** — labour framing below is from the UN press
  release + UN News + secondary coverage; flagged for a dedicated primary-text session before any 🟢
  use). *Shows (labour-relevant):* the first global, IPCC-style independent scientific assessment of AI.
  On employment it is explicitly **conditional** — AI "*will likely create new jobs*" **only with**
  "complementary investments in skills … workflows, infrastructure and labour-market institutions";
  **without** them it "risks widening inequality, displacing workers and **shifting wealth from labour
  to capital** rather than creating sustainable good jobs — those with fair compensation, **worker
  autonomy** and a reliable path to social **dignity**." Invokes the "60% of 2018 jobs are new vs 1945"
  new-jobs precedent; flags agentic AI "will soon complete tasks that currently take human programmers
  days or weeks." *Use:* institutional backing (a UN scientific panel) for two of the project's moves —
  the **new-jobs mechanism as a precondition, not a law**, and **autonomy/dignity, not just headcount**,
  as the outcome that matters (the economic–meaning decoupling in institutional language). Not a 🟢
  datum; the most citable *institutional* framing yet. **Caught 2026-W28 as a missed item** (slipped
  past every daily Jun 21–Jul 12); to be written up once the full text is read.
  https://www.un.org/independent-international-scientific-panel-ai/en/preliminary-report
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
- **ECB — employment reallocation by AI-risk gradient (wage-null).** "AI and the US labour market:
  effects on employment growth," *ECB Economic Bulletin* 4/2026 Focus (June 2026). 🟢 **with caveats**
  (ECB institutional economists; DiD with industry/COVID controls; **but exposure is capability-based
  "substitution risk," not measured deployment**, and the 2019–2025 window includes a long pre-ChatGPT
  period, so the reallocation is not cleanly GenAI-caused; primary retrieved via search; junior-
  vulnerability note from secondary). *Shows:* the **clearest DiD evidence so far that employment
  reallocation is underway** — high-risk occupations (economists, graphic designers) −4% on average,
  low-risk (electricians, teachers) +13%, a ~15pp gap; high-risk share of US employment 35%→33%, low-risk
  23%→25%; **no significant wage impact**; aggregate effect "muted so far." *Use:* reallocation is
  visible, but the declining occupations are the cognitive/creative *professional* tier and the wage-null
  beside it means the displaced are not (yet?) finding equivalent wages — reinforces, doesn't change, the
  "early reallocation without aggregate harm; loop not closing for the displaced" reading. One of the
  over-determined macro-null cluster (with Humlum & Vestergaard and Yotzov, below). VERIFIED 2026-06.
  https://www.ecb.europa.eu/press/economic-bulletin/focus/2026/html/ecb.ebbox202604_01~d9259db536.en.html
- **Humlum & Vestergaard, "Still Waters, Rapid Currents" (precise macro-null + task reorganisation).**
  NBER WP 33777 (Chicago Booth CAAI, May 2025). 🟢 **with caveats** (Danish administrative earnings/
  hours records + adoption surveys; DiD, strong identification; **single-country** — Denmark's worker
  protections / co-determination buffer effects and slow restructuring vs US/UK; admin data captures no
  quality-of-work/meaning dimension; the "rapid currents" finding is survey-based, not from the admin
  records). *Shows:* **precise null** earnings/hours effects two years post-ChatGPT (rules out effects
  larger than ~2%) — but beneath it, substantial **task reorganisation**: new AI tasks (content
  generation, AI oversight, AI integration) proliferate; adopters transition into higher-paying
  AI-relevant occupations (still "too few to move average earnings"). *Use:* the organising metaphor for
  the macro layer and the high-quality causal leg under the null — **aggregate employment stability does
  NOT mean psychological stability**, because the *tasks* reorganised away may be the competence- and
  autonomy-bearing ones (Ranjit, Lee et al., ILO WP170). The project's wedge against "if jobs hold,
  meaning is fine." VERIFIED 2026-06. https://www.nber.org/papers/w33777
- **Jiang, Park, Xiao & Zhang, "AI and the Extended Workday" (work intensification / rent capture —
  the new *time* pathway).** NBER WP 33536 (Columbia / USC, Feb 2025; SSRN:5119118). 🟢 **with caveats**
  (individual-level American Time Use Survey 2004–2023; ChatGPT shock as natural experiment; **data ends
  2023** — narrow window; **ATUS does not measure job satisfaction directly** — the "declining
  satisfaction" is a *modelled channel*, not a measured outcome; occupation-level exposure; NBER WP).
  *Shows:* higher AI occupational exposure → **longer work hours and reduced leisure** after the ChatGPT
  shock, via three channels — (1) higher marginal productivity from AI–human **complementarity**, (2)
  improved contracting efficiency from **AI-enabled monitoring**, (3) lower worker reservation utility —
  amplified in competitive markets where workers have **weak bargaining power**; productivity gains accrue
  primarily to **firms**, not to workers as reduced hours/leisure. *Use:* a **fourth "meaning-diminishing"
  pathway** beside competence (Lee et al.), autonomy (ILO WP170), and task-meaning (Ranjit) — AI can erode
  the *post-work time* in which purpose, relationships and recovery are built, **even for workers who keep
  their jobs and even where AI augments rather than automates**. The monitoring channel ties to ILO WP170;
  the rent-capture finding reinforces Falk & Tsoukalas's "two-instrument problem" (below). Resolves the
  work-hours half of the Brookings June-25 synthesis flag (the *satisfaction* half still needs a separate
  primary source — Jiang's satisfaction is modelled, not measured). VERIFIED 2026-06.
  https://www.nber.org/papers/w33536
- **Yotzov et al., "Firm Data on AI" — the employer/worker expectations gap.** NBER WP 34836 (Atlanta
  Fed, Bank of England, Bundesbank, Macquarie; Mar 2026). 🟢 **only for the pattern of expectations** —
  first representative multi-country firm survey (~6,000 CEOs/CFOs across US/UK/Germany/Australia,
  Nov 2025–Jan 2026), **but self-reported expectations, not realised outcomes**, one round, advanced-
  economy bias; **not a 🟢 anchor for job-loss claims**. *Shows:* 69% of firms actively use AI; **nine-in-
  ten executives report no employment or productivity impact over three years** (corroborating the
  macro-null); but going forward, executives forecast **−0.7% own-firm employment** over three years while
  **workers at the same firms forecast +0.5%** — a ~1.2pp **expectations gap**. *Use:* a psychological-
  preparedness dimension — workers appear **not yet to have internalised the risk their employers
  anticipate**; if the employer forecast is closer to right, displacement arrives unprepared. Pairs with
  "still waters, rapid currents." VERIFIED 2026-06. https://www.nber.org/papers/w34836

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
- **Chi et al., "Optimized but Unowned: How AI-Authored Goals Undermine the Motivation They Are Meant
  to Drive" — the ownership-erosion mechanism, pushed upstream to goal-authorship (added 2026-W30).**
  Chi, Rietsche, Göldi, Ungar & Guntuku; arXiv:2605.12344 (submitted 12 May, rev. 13 May 2026; Univ. of
  Pennsylvania / Bern Univ. of Applied Sciences). 🟢 **preregistered experiment, with caveats** (N=470;
  two-week behavioural follow-up; **preprint — not yet peer-reviewed**; single-session goal-setting task,
  not workplace field data; short horizon; US/university-adjacent sample likely). *Shows:* participants
  given **LLM-authored** personal goals (vs self-authored) ended up with objectively *better-formed* goals
  by SMART criteria (d=2.26) but reported **lower psychological ownership** (d=1.38), commitment (d=1.19)
  and perceived importance (d=1.13); at 2-week follow-up only **46.6%** had acted on ≥2 goals vs **72.8%**
  of the self-authored group. **Mediation:** psychological ownership — *not* objective goal quality —
  explains every downstream motivational/behavioural gap. **Heterogeneity:** people **low in trait
  self-efficacy** (most likely to reach for AI help) showed the **steepest** ownership erosion. *Use:* a
  **second, independent, preregistered *causal*** test of the mechanism Lee et al. (above) found for task
  *execution* — but applied to **goal-setting itself**, one level *upstream* of execution: the corrosive
  thing isn't doing the task with AI, it's the *intention* not being one's own. Strengthens the "how you
  use AI, not whether" thread with a distinct paradigm. The low-self-efficacy interaction is the notable
  wrinkle — it may **reverse** the augmentation-optimist "AI helps the least-skilled most" (Brynjolfsson
  call-center; Anthropic human-capital-enables-use) *on the ownership/meaning axis*: those least equipped
  to compensate may lose the most sense of authorship. *Limits (state honestly):* preprint, lab goal-task
  not field/workplace, 2-week horizon, no income/employment context. VERIFIED 2026-W30 (primary arXiv
  HTML v2 + abstract; ~10-week catch-up, missed by prior daily scans, grep-confirmed never previously
  logged). https://arxiv.org/abs/2605.12344
- **Broady, Dunson & Barr, "Rethinking Automation Risk: AI Applicability and Occupational Outcomes,
  2019–24" — a sub-🟢 *methodological caution*, not a displacement anchor (added 2026-W31).** Federal
  Reserve Bank of Chicago Working Paper 2026-12 (2 Jul 2026; verified from the primary PDF,
  doi.org/10.21033/wp-2026-12). 🟢 **descriptive, explicitly non-causal** (BLS occupational
  employment/wage data + O*NET, 2019–2024; the authors state the findings "do not prove that
  automation or AI caused the observed employment or wage changes" and flag DiD as future work; COVID
  sits inside the window; small occupation-level N — the "high AI applicability" group is 38
  occupations). *Shows:* **which exposure metric you pick can flip the employment sign on the same
  occupations over the same years** — on Tomlinson et al.'s (2025) Copilot-*usage*-based "AI
  applicability" scores, the most-exposed occupations *grew* **+4.05%** employment / +21.7% wages;
  on Frey & Osborne's (2017) *computerizability* risk scores, high-risk occupations *fell* **−3%**
  (moderate −6%), with wages rising **21–26% across all three risk tiers** and within-tier variance
  swamping every average. *Use (state honestly):* **do NOT cite as evidence of AI displacement or
  its absence.** Its value is a *citation-discipline* caution — every exposure-based anchor in this
  file (Stanford/ADP, ECB, Census BTOS, PwC, Massenkoff & McCrory) rests on a *construct choice*
  (usage-based vs task-based exposure), and the two can diverge in sign; name which construct is doing
  the work. The CFO Dive coverage reported the applicability figure but omitted the opposite-signed
  computerizability result in the same paper — the headline-vs-primary gap the project exists to
  catch. Revisit if the authors' promised causal (DiD) follow-up appears. VERIFIED 2026-W31 (primary
  PDF). https://doi.org/10.21033/wp-2026-12
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
  *Texture note (added 2026-W28, sub-🟢 — do not anchor alone):* a Chinese SEM survey (N=338; *Frontiers
  in Digital Health* 8:1877221, accepted 7 Jul 2026) gives this qualitative autonomy-erosion pathway a
  **testable mediator and a health outcome** — perceived algorithmic management → **frustrated work
  autonomy** → a newly-named "**workplace AI replacement anxiety**" → worse physical/mental health
  (sequential chain). Single-country, cross-sectional, self-report, no causal inference — corroborating
  texture inside WP170, not a revision; watch for a non-China replication. https://doi.org/10.3389/fdgth.2026.1877221
- **Anthropic Economic Index "Cadences" — a 🟡 self-report *counterpoint* to Lee et al. (do not
  conflate) (added 2026-W27).** Anthropic, 26 Jun 2026. 🟡 (self-report survey; single-provider;
  explicitly correlational — authors flag the confound). *Shows:* a linked survey (N≈9,700; **not
  representative** — skews computer/mathematical 30% + management 23%, active Claude users only) found
  respondents with a **higher "automation share"** of their Claude use reported **more optimistic
  expectations across all six dimensions** — pay, job security, job-finding (economic) *and* **meaning,
  autonomy, human interaction** (intrinsic). The authors state it "*is possible that this relationship
  is explained by selection.*" (Also: ~10% rated own job loss likely within 12 months; early-career
  workers reported the highest displacement anxiety.) *Use — the discipline matters:* this is the
  *opposite valence* to Lee et al. (passive/automated use *causally* reduces self-efficacy, ownership,
  felt meaning), but the two are **not necessarily in tension** — Lee et al. measures felt meaning
  *during/after a task* (a measured outcome); Cadences measures *general future-optimism* among people
  who already chose to delegate heavily (a self-reported expectation, selection-confounded). **Never
  conflate self-reported optimism about AI with a measured meaning outcome.** Logged 🟡, not 🟢; a
  caveat/counterpoint beside Lee et al./Ranjit/Giuntella, not a revision of them. VERIFIED 2026-W27.
  https://www.anthropic.com/research/economic-index-june-2026-report
- **Competence pressure from the demand side + who is least able to adapt (compact note, added
  2026-W26; sub-🟢, flagged).** Two back-filled papers extend the competence story beyond the individual
  task level. (1) **Siddiq & Zhang, "Human Capital, AI, and Labor Commoditization"** (UCLA Anderson;
  arXiv:2606.21880, Jun 2026): DiD around ChatGPT on real Upwork data (text embeddings) finds that in
  more AI-exposed categories the predictive importance of **human capital (skills, reputation) for demand
  declines** while **price rises** — the skilled-human-capital premium erodes ("commoditization"). 🟡-
  leaning (preprint; **online-freelance market**, not salaried; category-level exposure; authors' framing)
  — the **SDT-competence threat from the *demand* side**: AI can devalue distinctiveness independently of
  task substitution; pairs with PwC "raised floor" and Lee et al. The freelance channel may be an early,
  *extreme* signal. (2) **Manning & Aguirre, "How Adaptable Are American Workers…?"** (NBER WP 34705,
  Jan 2026): an adaptive-capacity index over 356 occupations finds AI exposure and adaptive capacity
  *positively* correlated overall, **but 6.1M workers (4.2%) sit in a "double-jeopardy" zone** — highly
  exposed *and* below-median adaptive capacity, concentrated in **clerical/administrative** roles. 🟡/🟢
  (**prospective** index, not outcome data; "adaptive capacity" is economic-transition, not psychological
  resilience; not peer-reviewed) — names a cohort **distinct from the young-graduate thread**: older, more
  marginal, most reliant on work's latent functions and least able to substitute them, so **the meaning
  cost likely concentrates here**. Neither a full 🟢 anchor yet; both flagged for peer review / outcome
  data. VERIFIED 2026-06 (preprints/secondary). https://arxiv.org/abs/2606.21880 ·
  https://www.nber.org/papers/w34705

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
- **The two-instrument problem — UBI doesn't correct the automation incentive (Falk & Tsoukalas).**
  "The AI Layoff Trap" (UPenn / Boston University; arXiv:2603.20617, rev. Jun 2026). 🟡 **only**
  (game-theoretic model, not empirical; **McEntire sensitivity analysis (SSRN:6592220) shows the sign/
  magnitude depend entirely on parameter choices** — under standard alternatives the model yields
  stability or under-automation, so the trap is *possible, not inevitable*). *Argues:* each firm captures
  the full cost-saving from automating a task but bears only a fraction of the demand loss it creates — a
  **demand externality** that drives an automation arms race beyond the social optimum. Of six tested
  fixes (UBI, capital-income taxes, worker equity, retraining, Coasean bargaining, Pigouvian automation
  tax), **only the automation tax** corrects the distortion. *Use:* a conceptual point for Ch.7 even
  though the quantitative result is parameter-sensitive — the *distributional* fix (UBI) and the
  *incentive* fix (automation tax) are **logically separable**; a package handling both displacement and
  meaning is necessarily multi-instrument. Pairs with Jiang et al. (firms capture the productivity rents)
  and the "two-path meaning threat." 🟡 scaffolding, not a 🟢 finding. VERIFIED 2026-06.
  https://arxiv.org/abs/2603.20617
- **The bundle hypothesis — cash + structured participation beats cash alone (WorkFREE).** "Evaluating a
  'UBI Plus' Intervention: A Needs-based Analysis of WorkFREE," *Social Indicators Research* 182(1)
  (Mar 2026). 🟡 (peer-reviewed, Max-Neef needs framework, mixed-methods; **Indian slum context** —
  INR 500–1,000/mo, 1,400 residents, dollar amounts/context not comparable to Western pilots; primary
  not retrieved). *Shows:* unconditional cash + monthly community "Plus meetings" out-performed cash-alone
  (vs the HudsonUP companion study) on **both** material and **psychological/relational** needs — cash
  alone left relational/psychological needs only partially met. *Use:* modest evidence that the missing
  ingredient is **structured social participation, not income per se** — echoes Jahoda's latent functions
  and the German RCT's purpose gain (what supplies purpose may be what cash is *bundled with*). Far from
  the OECD post-labour scenario and hard to scale; monitor for a Western replication. VERIFIED 2026-06
  (secondary). https://doi.org/10.1007/s11205-026-03806-y

---

## Gaps to fill (future 🟢 pillars to consider)

- Honest re-analysis of FIRE / early-retirement communities' wellbeing trajectories.
- Systematic re-synthesis of UBI psychological (not just financial) outcomes.
- Cross-platform: does relatedness-structure predict community resilience to AI?
