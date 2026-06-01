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
  - Meta-analyses: cash → small positive subjective-wellbeing (d≈0.13), larger on
    depression/anxiety, often not sustained post-program.
  - **Synthesis:** money reliably buys *relief from material stress*, not *meaning/purpose*.
    This is the project's most important recurring 🟢 result.

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

## Deaths of despair (the 🟢 floor for the "how bad" chapter)

- **Case & Deaton** (2015 onward; *Deaths of Despair and the Future of Capitalism*, 2020).
  "Deaths of despair" = suicide + drug/alcohol poisoning + alcoholic liver disease. *Shows:*
  rising mortality among **middle-aged, non-college-educated white Americans** (45–54); 1998–2017
  overdose deaths up >4×, alcoholic liver disease +~50%, suicide +~37%; they attribute it to loss
  of employment, security, mobility — i.e. work-and-meaning erosion, not just income. *Limits
  (state honestly):* correlational, heavily confounded (opioid supply, healthcare, specific
  demographic/era); shows the stakes are mortal, does NOT prove a future post-work society repeats
  it. VERIFIED 2026-05.

## Relatedness / care as AI-resistant (direct test of "can AI supply mattering?")

- **"People prefer human empathy even when AI says the same thing"** (9 experiments, >6,000
  participants; 2025). *Shows:* identical LLM-written responses are rated **more empathic,
  supportive, and emotionally satisfying when labelled "human" than when labelled "AI"**; a
  one-sentence AI disclosure *reduces* felt empathy; people will wait longer for a human reply.
  This is a **direct 🟢 test** of Q3's open question ("can virtual/AI supply *mattering*?") — and
  the answer leans no: the value of care depends partly on a *human* being its source. Anchors
  Ch.6's relatedness path and Q7. VERIFIED 2026-05.

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

---

## Gaps to fill (future 🟢 pillars to consider)

- Honest re-analysis of FIRE / early-retirement communities' wellbeing trajectories.
- Systematic re-synthesis of UBI psychological (not just financial) outcomes.
- Cross-platform: does relatedness-structure predict community resilience to AI?
