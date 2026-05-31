# LESSONS.md

Errors and learnings. Read at the start of every session.

## Biggest lesson: polishing ≠ fixing the foundation
The original post-scarcity ABM was polished across ~20 adversarial-review iterations but
never fixed two structural diseases: (1) **circular reasoning** — the headline result was
baked into the meaning-function definition, not discovered; (2) **unfalsifiability** — it
simulated a hypothetical post-labour future with no ground truth. No amount of prose polish,
sensitivity tables, or referee rounds can rescue an unfalsifiable design. Falsifiability must
be built in *before* writing code. (Pivot recorded 2026-05-30; old ABM kept for history.)

## Method follows the question, not the reverse
Don't pick a tool (ABM, LLM-town) then hunt for a problem. Ask first: is the finding I want
"derivable" (then it's circular) or "emergent / empirical"? The pivot to a falsifiable,
data-anchored study (so_sdt_study) came from asking what could actually be *refuted*.

## Verify prior work from primary text before claiming novelty
Search-agent summaries were wrong/imprecise (e.g. conflated two same-author papers). Reading
all four closest papers in full changed the novelty positioning and saved us from duplicating
Li & Kim / Shan & Qiu.

## Pre-registration + placebo actually work — let them kill your hypotheses
In so_sdt_study, freezing the classifier before outcomes, and pre-committing a placebo, did
their job: H1 was rejected, an eye-catching "reversal" turned out to be noise (interaction
p=0.52), and H3's causal claim was killed by a placebo that reproduced the effect one year
before ChatGPT existed. Three tempting cheats were declined (redefining "status" post-hoc to
save H1; writing up the noise reversal; skipping the placebo). The result is an honest null.

## Behavioural proxies measure disposition, not reaction
The deepest methodological lesson: behavioural traces on a platform capture *stable
propensities* far better than *shock-induced change*. Relatedness types comment more by
temperament — so any time window (including the placebo) shows it. To test a psychological
*reaction* to a shock, you need an instrument that captures reaction (e.g. LLM-coded content
signals), not behaviour that mostly reflects who people already are.
