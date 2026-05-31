# Does the Employment Contract, Not Just AI Substitutability, Govern Where Generative AI Hits First? A Pre-Registered Null on U.S. Self-Employed vs Salaried Workers

**Status:** Working paper / internal write-up (not submitted for publication).
**Data & code:** `contract_buffer_study/` in this repository. Pre-registration frozen 2026-05-31
in `DESIGN.md` before any post-shock employment outcome was examined.

---

## Abstract

When ChatGPT made expert text and code instantly available (30 November 2022), one online
commons — Stack Overflow — collapsed almost completely, while the broad white-collar labour
market did not visibly crater. A prominent interpretation, and the hinge of a book this study
supports, is that Stack Overflow had **no employment contract** buffering it, whereas salaried
work is protected by contractual stickiness that merely *delays* the same force — making exposed
professionals **forerunners** for everyone. A competing explanation is that Stack Overflow was
simply a **perfectly substitutable special case**. These accounts make opposite predictions when
AI exposure is held constant and only the contract buffer varies: the buffer account predicts
**no-contract** workers (unincorporated self-employed) lose employment *earlier and deeper* than
**salaried** workers in the *same* AI-exposed occupations; the substitutability account predicts
they move *together*. Using U.S. Current Population Survey basic-monthly microdata (2021-07 to
2026-04), an occupation-level generative-AI exposure index (Language-Modeling AIOE), and a
pre-registered Poisson triple-difference, **we find no support for the contract-buffer
prediction.** The triple-interaction coefficient is −2.2% per exposure standard deviation
(p = 0.21; 95% CI [−5.5%, +1.2%]), is reproduced almost exactly by a placebo shock seven months
*before* ChatGPT (−2.2%, p = 0.37), shows flat event-study pre-trends and no post-shock descent,
and is null across every robustness specification. A pre-registered dose-response across the
buffer gradient runs the *wrong* way. Notably, AI exposure produced no employment decline at all
in this window — even salaried employment in exposed occupations grew slightly — so the test is
partly under-powered for an effect the buffer account itself locates in the future. This is a
pre-registered, placebo-controlled null: through early 2026 the broad labour data do not
corroborate the claim that the absence of a contract is what makes generative AI bite first.

---

## 1. Introduction

Two facts about the first three years after ChatGPT sit in tension. Stack Overflow — the global
question-and-answer commons for programmers — lost roughly 45% of its monthly contribution within
a year and on the order of 95% by early 2026 (a near-total collapse of voluntary human
contribution). Yet the aggregate U.S. white-collar labour market has, so far, held up: through
2025–2026, employment in AI-exposed occupations has not measurably fallen, with the one robust
exception a relative decline among the very young at the entry level (Brynjolfsson et al.,
"Canaries in the Coal Mine?", using ADP payroll records).

One reading reconciles them structurally: Stack Overflow had **no employment contract**. Nobody
was paid to answer; there was no salary, notice period, severance, or organisational inertia. When
a machine could supply the asking side, nothing buffered the answering side from evaporating.
Salaried work, by contrast, carries enormous stickiness — contracts, reorganisation friction — that
slows any unwinding to a crawl, which is exactly why aggregate employment still looks calm. On this
reading the exposed professional is a **forerunner**: living, early and unbuffered, what contracts
are merely postponing for everyone else.

A competing reading concedes nothing structural about contracts: Stack Overflow collapsed because
asking a coding question and getting an answer is **almost perfectly substitutable** by a chatbot,
end to end. Most white-collar work is not substitutable that cleanly — it is tangled with judgment,
accountability, and relationships a model cannot swallow whole. If substitutability is the whole
story, Stack Overflow is not a preview of everyone's future; it is the one corner that happened to
map one-to-one onto what the machine does.

The two accounts are observationally equivalent at the aggregate level, but they diverge sharply
under a within-occupation contrast. Hold AI exposure roughly constant — compare a freelance
translator and a salaried translator, equally substitutable by the model — and vary only the
contract. If the freelancer's employment falls first and harder, the operative difference is the
**contract**, not substitutability. If the two move together, the contract is irrelevant and
substitutability governs. No prior study runs this contrast: the freelance literature (Hui et al.,
2024; "Winners and Losers of Generative AI", 2025) measures freelancer *demand* and never compares
to salaried workers in the same occupation; the salaried evidence (ADP) cannot see the no-contract
side at all. We supply the missing head-to-head on one nationally representative dataset.

We pre-registered the design — hypotheses, class and exposure definitions, estimator, window,
placebo, and decision rules — in `DESIGN.md` before examining any post-shock outcome, committing in
advance to report a null as a publishable result.

---

## 2. Data and methods

**Labour outcomes.** U.S. Census Bureau Current Population Survey **basic monthly** microdata,
2021-07 to 2026-04 (53 months; the window is entirely post-COVID-acute and on a single 2018-census
occupation basis). Months ≤ 2022-12 are read from NBER's harmonised Stata files; 2023-01 onward from
Census public-use fixed-width files. Our Census parser reproduces NBER's weighted class-of-worker
counts exactly on the 2023-11 overlap. Employment is `PEMLR ∈ {1,2}`, weighted by the final
composited person weight. The contract contrast uses class of worker (`PEIO1COW`): **no-contract =
unincorporated self-employed (7)** vs **salaried = private for-profit wage/salary (4)**; the
incorporated self-employed (6) provide a pre-registered "middle rung." Ages 18–64.

**AI exposure.** The occupation-level **Language-Modeling AIOE** (Felten, Raj & Seamans) — the
LLM-specific variant of the AI Occupational Exposure index — joined to CPS detailed occupation
(`PEIO1OCD`) through the Census 2018-occupation-to-2010-SOC crosswalk (96% of occupations matched;
base AIOE used for robustness). Exposure is z-scored across occupations.

**Estimator (frozen).** A Poisson pseudo-maximum-likelihood (PPML) triple-difference of weighted
employment counts in occupation×class×month cells:

> E[o,c,t] ~ PPML( occ×class FE + month FE + β₁·Post·Exp + β₂·Post·NoContract + β₃·Post·Exp·NoContract )

β₃ is the contract-buffer coefficient: **β₃ < 0** supports the buffer account, **β₃ = 0** (with
β₁ < 0) the substitutability account. Standard errors cluster by occupation; the panel is balanced
so that an established cell whose employment falls to zero enters as zero. The pre-registered
**placebo** is a fake shock at 2022-05 (within the AI-clean pre-ChatGPT stretch), expected to give
β₃ ≈ 0. Pre-committed robustness: base AIOE, age bands (25–54, 16+), cell-size thresholds, hours,
and an event study for dynamics.

---

## 3. Results

**The contract-buffer coefficient is null.** β₃ = −0.0220 (SE 0.0175, p = 0.21), about −2.2% per
exposure standard deviation, with a 95% confidence interval of [−5.5%, +1.2%]. The point estimate
is weakly negative — the sign H1 predicts — but indistinguishable from zero. The hypothesis that
no-contract workers in AI-exposed occupations lose employment faster than salaried workers in the
same occupations **fails its pre-registered test**.

Two results make the failure decisive rather than marginal. First, the **placebo shock** at 2022-05,
before ChatGPT existed, yields β₃ = −0.0223 (p = 0.37) — essentially identical to the real estimate.
The faint negative tilt predates ChatGPT and is therefore not a response to it (figure 2). Second,
the **event study** shows flat, non-significant pre-trends (parallel trends hold) and no
significant negative post-shock block: no no-contract penalty *emerges* after the shock (figure 1).

The surrounding coefficients explain why. **β₁ = +1.7% (p = 0.007):** employment in higher-exposure
occupations grew slightly faster after ChatGPT — through early 2026, CPS shows no AI-driven
employment decline in exposed occupations *at all*, even for salaried workers. With no visible
exposure-driven decline to begin with, there is little differential for a contract buffer to slow,
and the test is in part too early. **β₂ = −6.4% (p < 0.001):** unincorporated self-employment did
fall after 2022 — but across *all* exposure levels equally (the unwinding of the 2021 pandemic
self-employment surge), not concentrated in exposed occupations (figure 3).

**Secondary tests agree.** The early-window estimate (2022-11…2023-12) is −1.3% (p = 0.48). The
buffer-gradient prediction runs the wrong way: the *more* contract-buffered incorporated
self-employed show a *larger* exposure-related shift (−5.4%, p = 0.03) than the unincorporated
(−2.2%, p = 0.21) — incompatible with a buffer that monotonically slows AI's reach. Every robustness
specification — base AIOE, ages 25–54 and 16+, cell-size floors, and the hours margin — returns the
same small, non-significant negative with a confidence interval crossing zero (figure 2).

---

## 4. Discussion

**A null, honestly arrived at.** All pre-registered predictions failed: the primary triple
interaction is non-significant, the placebo reproduces it, the event study is flat, and the
dose-response is reversed. We resisted the tempting moves the design was frozen to prevent —
reading the −2.2% point estimate as confirmation, dropping the placebo once it matched the real
estimate, or re-binning exposure until the quartile picture (which descriptively does tilt toward
H1) reached significance. The placebo, in particular, shows that the descriptive tilt is a
pre-existing feature, not a ChatGPT effect.

**What it does and does not establish.** It does *not* refute the contract-buffer mechanism. The
estimate is imprecise (a true effect down to −5.5% per SD is inside the interval); the AI employment
shock is barely visible in CPS by 2026 even for salaried workers; and self-employed occupation is
measured with noise in thin cells. A small or still-emerging effect cannot be excluded. What the
result *does* do is fail to confirm the mechanism precisely where the supported book predicts it
should already be visible — the no-contract workforce, hit "first, fast, and unbuffered." Broad CPS
employment for unincorporated self-employed in AI-exposed occupations shows no such early,
exposure-concentrated collapse through early 2026. On this evidence the Stack Overflow collapse —
real and documented — stands more as a possibly-special, near-perfectly-substitutable case than as
the leading edge of a broad no-contract employment decline. The substitutability objection gains a
little weight; the forerunner extrapolation keeps its status as a reasoned worry, not a
demonstrated fact.

**Why the broad data may be silent.** Three reasons, none of which rescue the hypothesis but all of
which bound the null. (i) *Too early.* The buffer account itself says contract-protected employment
adjusts slowly; but it also says the *un*protected side should move fast — and even that side shows
nothing exposure-specific yet. (ii) *Margin.* CPS measures whether a self-employed person is
employed, not their earnings or hours of paid work; the freelance evidence of 20–50% *demand* drops
lives on a margin CPS cannot see for the self-employed. The contract buffer may be operating on
income, not headcount. (iii) *Measurement.* Occupation for the self-employed is self-reported and
thin; exposure is occupation-average, not task-level, so within-occupation differences in what
freelancers actually do are invisible.

---

## 5. Limitations

- **Employment, not earnings.** CPS collects no earnings for the self-employed; the outcome is
  headcount (and hours), which may miss an income-margin effect.
- **Imprecision / power.** With no visible AI employment shock in CPS by 2026, the test cannot
  distinguish a small contract-buffer effect from zero.
- **Self-employment selection.** Unincorporated self-employed differ from employees in unobserved
  ways; fixed effects absorb time-invariant differences, and the placebo and flat pre-trends support
  the design, but within-occupation task-substitutability differences between freelancers and
  employees cannot be ruled out.
- **One country, one shock, occupation-average exposure.** The 2021 self-employment surge/unwinding
  is a residual trend the placebo mitigates but cannot fully remove.

## 6. Conclusion

Holding generative-AI substitutability roughly constant and varying only the employment-contract
buffer, U.S. labour microdata through early 2026 give no significant evidence that no-contract
workers lose employment earlier or more deeply than salaried workers in the same AI-exposed
occupations. The pre-registered, placebo-controlled result is a null. The contract-buffer reading
of the Stack Overflow collapse — and the forerunner argument it supports — is not corroborated by
the broad employment data yet, and is honestly held as an unproven inference that a direct test has
so far failed to confirm.

---

## Author's note on provenance

Conducted as an independent, spare-time research project with heavy use of an AI coding assistant
for data-pipeline construction, statistical analysis, and drafting. The pre-registration was frozen
before outcome data were examined; the placebo was pre-committed; the null is reported as found.
Data and code are in this repository for full reproducibility (the Census parser is validated
against NBER to an exact match).

## References

- Brynjolfsson, E., et al. Canaries in the Coal Mine? Six Facts about the Recent Employment Effects
  of Artificial Intelligence. Stanford Digital Economy Lab (ADP payroll microdata).
- Felten, E., Raj, M., & Seamans, R. (2021). Occupational, industry, and geographic exposure to
  artificial intelligence. *Strategic Management Journal*. (AIOE; Language-Modeling variant.)
- Hui, X., Reshef, O., & Zhou, L. (2024). The Short-Term Effects of Generative Artificial
  Intelligence on Employment. arXiv:2308.05201.
- Winners and Losers of Generative AI: Early Evidence of Shifts in Freelancer Demand (2025).
  *Journal of Economic Behavior & Organization*.
- U.S. Census Bureau / NBER. Current Population Survey, basic monthly microdata.
