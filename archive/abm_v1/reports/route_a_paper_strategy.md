# Route A Paper Strategy

This memo assumes Route A becomes the paper's primary identification repair, not a side analysis. The orthogonal sweep resolves the central methodological problem, but it also changes the substantive story. The old claim was too bundled. The new claim can be stronger if the authors state it precisely.

## A. What the Route A results mean for the paper argument

### Bottom line

Route A does **not** support the original headline in its current form: "roles outperform income support at preventing behavioural sink." What it supports is a more specific and more defensible claim:

> Under extreme post-labour displacement, resilience is driven mainly by restoration of **competence**, **contribution**, and secondarily **autonomy**; **income support** and **role participation by themselves** are nearly inert.

That is a major reframing, not a minor qualification.

### What is strengthened

- The broad "meaning channels matter more than money" argument is strengthened.
- The claim that **income alone is insufficient** is now on firmer ground than before. In the orthogonal sweep, income has only a `-0.0039` main effect on social distress (`-2.0%`) and a `-0.0172` main effect on collapse probability (`-14.3%` relative reduction from its factor-off mean), with only `+0.0035` on meaning.
- The argument that **non-economic psychosocial supports move equilibrium outcomes** is strongly supported. Competence reduces social distress by `-0.0614` (`-27.1%`), contribution by `-0.0601` (`-26.5%`), and autonomy by `-0.0268` (`-12.8%`). On collapse probability, competence is `-0.2220`, contribution `-0.2189`, and autonomy `-0.1220`.
- The bundle logic is still directionally right at a high level: the most protective interventions are those that restore latent functions of work, not just purchasing power.

### What is overturned

- The paper can no longer say or imply that **role participation itself** is the key protective mechanism. Route A shows role participation has a social-distress main effect of only `-0.0046` (`-2.3%`) and a collapse-probability main effect of only `-0.0148`.
- The old `roles_only` versus `income_only` contrast is no longer interpretable as "meaning beats money" in a clean causal sense. After orthogonalization, `rol` alone (`0.3000` distress, `99%` collapse) is almost indistinguishable from `inc` alone (`0.2972` distress, `100%` collapse), and both are close to `none` (`0.3036` distress, `100%` collapse).
- The mechanism is **not** "give people roles." It is "restore mastery, valued contribution, and self-direction." That is theoretically better and methodologically cleaner.

### How to frame the substantive conclusion now

- The paper should move from **roles vs income** to **channels of resilience under displacement**.
- The most defensible core claim is: "The protective effect previously attributed to roles is actually carried by competence and contribution, with autonomy and fairness as secondary supports."
- There is a strong structural summary in the combination rankings:
  - All top 10 lowest-distress combinations include `fairness`, `autonomy`, `competence`, and `contribution`.
  - None of the bottom 10 combinations include any of those four.
  - `income` and `role_participation` appear in only 6 of the top 10 and 4 of the bottom 10, which is exactly what "secondary or weak lever" looks like.
- The interaction structure also helps the new argument. The strongest two-way interaction is `competence × contribution` (`0.0069` on social distress; `0.4341` on collapse probability), followed by `autonomy × competence` and `autonomy × contribution`. That says the paper should emphasize **complementary latent-function bundles**, not single silver bullets.

### Implication for the original core claim

The original claim should be rewritten, not defended. A good replacement is:

> In this model, protection against behavioural sink comes much less from cash transfers or nominal role access than from institutions that preserve competence, socially valued contribution, and autonomy under mass displacement.

That preserves the paper's broader theoretical ambition while dropping the now-indefensible "roles themselves are the active ingredient" implication.

## B. Paper architecture changes needed

### Strategic recommendation

Yes: reframe the paper from **roles-vs-income** to **channels-of-resilience**.

That is the cleanest way to turn a methodological repair into a stronger contribution. If the authors keep the old framing, Route A will read like an internal contradiction. If they adopt the new framing, Route A becomes the paper's strongest result.

### Recommended revised research questions

The current RQs can be retained only partly. I would revise them to:

1. At what displacement levels does the model enter a high-risk behavioural-sink zone, and how policy-sensitive is that threshold?
2. Which latent-function channels independently reduce distress and collapse under extreme displacement?
3. Which channel combinations are complementary or synergistic?
4. How do virtual worlds, collectivism, and broader policy bundles modify resilience once the key channels are identified?

This keeps the threshold, virtual-world, and culture results, but makes Route A central rather than supplemental.

### Behavioural-sink framing

The behavioural-sink framing can stay, but it needs to shift from **loss of roles** to **loss of latent functions / need satisfaction**.

- Stronger framing: behavioural sink emerges when displacement removes the mechanisms that sustain competence, contribution, and autonomy.
- Weaker framing: behavioural sink emerges because people do not hold formal roles.

This change also helps with JASSS fit. It aligns the paper more closely with SDT and Jahoda's latent functions and less with a crude "everyone needs a job title" story.

Because aggression is already underrepresented in the model, the text should explicitly describe the system as a **withdrawal-dominated behavioural sink** driven by competence-purpose depletion. That is more precise and more defensible than leaning too heavily on role participation language.

## C. Specific section-by-section recommendations

### Abstract

The new take-home message should be:

- The orthogonal 8-factor sweep repairs a confounded bundled comparison.
- The dominant resilience channels are competence, contribution, and autonomy.
- Income support and role participation alone have little independent effect.
- Effective post-labour policy therefore requires institutions that preserve mastery, valued contribution, and self-direction, not only transfers.

Do not lead with "roles outperform income." Lead with "orthogonal decomposition reveals which channels actually matter."

### Introduction

Reframe the gap as:

- Existing debates over post-labour policy often oppose cash transfers to role restoration at too high a level of abstraction.
- The real unresolved question is which **latent functions of work** matter most for system stability once these bundles are decomposed.
- The paper contributes an ABM-based decomposition of those channels under extreme displacement.

This lets the introduction keep Jahoda, SDT, and behavioural sink, but the theoretical target becomes more exact: not "work vs money," but "which psychosocial functions of work are stabilizing?"

### Methods

Be fully explicit that Route A is a **review-driven identification repair**.

- State that the prior `income-only` versus `roles-only` comparison was bundled and therefore not suitable for isolating causal channels.
- Present Route A as a full `2^8 = 256` orthogonal factorial sweep at fixed high displacement (`95%`), `100` runs per cell.
- List the eight factors clearly.
- State that the estimands are main effects and two-way interactions, not just scenario rankings.

This is good science and will read well to reviewers. Trying to hide the repair will hurt credibility.

### Results

The results section should be restructured so Route A is the main mechanism section.

Recommended order:

1. Threshold zone and baseline system behaviour.
2. Route A main effects: a figure/table showing channel rankings for distress, collapse probability, and meaning.
3. Route A interactions: especially `competence × contribution`, then autonomy complements.
4. Policy-bundle reconstruction: map the old bundles onto the identified channels.
5. Virtual worlds and collectivism as complementary supports.

The old bundled scenario comparison should no longer carry the main causal claim. Instead:

- Use it descriptively for package performance.
- Say explicitly that bundled sweeps show what policy portfolios do in the model, while Route A identifies which channels drive those portfolio effects.

### Discussion

The discussion should pivot from "meaning beats income" to:

- competence and contribution are the principal resilience levers;
- autonomy and fairness are important secondary supports;
- income is ethically important but mechanistically weak in this model as a sink-prevention lever under extreme displacement;
- nominal participation without mastery or contribution is not enough.

That gives the paper sharper policy relevance. It suggests that viable post-labour institutions must not only distribute resources but also create structures for skill use, efficacy, recognition, and socially valued contribution.

### Existing sweeps

Most existing sweeps are still usable, but their role changes.

- Keep the displacement-threshold sweep, virtual-world sweep, collectivism sweep, and speed comparison in the main paper if space allows.
- Keep the full scenario grid as **bundle-level policy illustration**, not mechanism identification.
- Remove or demote any text that treats `roles_only` versus `income_only` as a clean causal test.
- Replace the old decoupling/ablation centerpiece with Route A.
- If space becomes tight, move some bundle comparisons and robustness tables to the supplement.

In short: old sweeps are still valuable contextual evidence, but Route A must become the mechanism backbone.

## D. Risks and opportunities

### Does the competence-dominance finding help publishability?

On balance, yes.

- It makes the paper more original. "Roles beat income" is easy to read as ideologically loaded or too coarse. "Competence and contribution dominate after orthogonal decomposition" is more novel and more analytically interesting.
- It makes the methods story better. The paper now has a clear identification correction and a cleaner mechanism result.
- It gives the discussion a stronger bridge to SDT and latent-function theory.

### Main risk

Reviewers may ask whether competence and contribution dominate because they are closer to the model's outcome construction. The paper should pre-empt this.

Two good responses are available from the current results:

- Competence and autonomy both connect to SDT-style psychological state, but competence is much larger than autonomy.
- Competence and relatedness have equal weights in the meaning index in the current model description, yet relatedness is much weaker (`-0.0116` on social distress versus `-0.0614` for competence).
- Contribution has only `0.15` weight in the meaning function yet is almost as large as competence. So the Route A ranking is not reducible to simple outcome weighting.

That argument should appear in Discussion or Limitations.

### Is role_participation being inert a problem?

It is an insight if framed correctly.

- Problematic framing: "our role-programme hypothesis failed."
- Better framing: "formal participation without mastery, autonomy, or socially valued contribution is not sufficient."

That is actually a stronger social-science claim. It says symbolic inclusion or occupied time is not enough; what matters is whether the activity restores efficacy and contribution. That is exactly the kind of mechanism clarification that reviewers often want.

### How to handle the politically sensitive income result

Do not say "income is useless." Say:

- In this model, under extreme displacement and conditional material sufficiency, income support alone is a weak lever for preventing behavioural sink.
- That does **not** mean income support is normatively unimportant or unnecessary.
- It means cash transfers are a floor, not the core resilience engine, in the model's psychosocial-collapse dynamics.

This is both more accurate and less rhetorically inflammatory.

The paper should explicitly note domains it does not model well, where income may matter more:

- poverty and consumption shocks;
- bargaining power and labour-market transitions;
- short-run stress reduction;
- health access and material hardship pathways.

That clarification is important for both fairness and reviewer resistance.

## E. Suggested new paper title and abstract

### Title options

1. **Channels of resilience in post-labour societies: an orthogonal agent-based analysis of behavioural sink**
2. **Competence, contribution, and autonomy in post-labour societies: an agent-based analysis of behavioural sink**
3. **Beyond income versus roles: latent-function channels of resilience in a post-labour agent-based model**

My recommendation is option 3 if the authors want the reframing to be explicit, or option 1 if they want the most JASSS-style neutral title.

### Draft abstract

What equilibrium states emerge when most people lose productive roles, and which interventions prevent behavioural sink? We present a stylised agent-based model of post-labour society grounded in Self-Determination Theory, latent-function accounts of work, and social contagion. Earlier scenario comparisons in the model contrasted income support with role programmes, but those bundles were structurally confounded. We therefore introduce an orthogonal eight-factor sweep at fixed high displacement (`256` combinations, `100` runs each) that separately varies income, fairness, role participation, autonomy, competence, relatedness, status, and contribution.

The decomposition changes the substantive conclusion. Competence restoration and contribution restoration are the dominant resilience channels, reducing mean social distress by `0.0614` and `0.0601` respectively and collapse probability by `0.2220` and `0.2189`. Autonomy (`-0.0268` distress; `-0.1220` collapse) and fairness (`-0.0260`; `-0.1106`) are important secondary supports. By contrast, income support (`-0.0039`; `-0.0172`) and role participation itself (`-0.0046`; `-0.0148`) have little independent effect. The strongest interaction is competence with contribution, indicating that resilience depends on complementary latent-function bundles rather than any single intervention. Existing sweeps continue to show a policy-sensitive high-displacement threshold and benefits from virtual worlds, collectivism, and multi-pillar bundles, but the orthogonal analysis shows that the protective effect previously attributed to "roles" is primarily carried by mastery, valued contribution, and self-direction. The model therefore suggests that post-labour stability depends less on cash transfers or nominal participation than on institutions that preserve competence, contribution, and autonomy under mass displacement.

## Final strategic recommendation

Do not defend the old framing. Replace it.

The strongest publishable version of this paper is no longer "roles outperform income." It is:

> Once the bundled comparison is repaired, the dominant stabilizing mechanisms are competence, contribution, and autonomy. Income support matters less as an equilibrium resilience lever than the latent functions that make people feel effective, needed, and self-directed.

That is a cleaner contribution, a better response to the confound, and a more interesting paper.
