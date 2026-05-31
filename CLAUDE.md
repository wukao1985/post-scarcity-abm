# CLAUDE.md — project guide

This repository hosts a lifelong inquiry into **human meaning in the post-AI / post-labour
era**, plus the empirical studies and archived work that feed it.

> New session? Read `meaning_project/SYNTHESIS.md` (the living layered overview of everything
> we understand), then `meaning_project/MANIFESTO.md` and `STYLE.md`, then `LESSONS.md`. They
> carry the current state of knowledge, the north star, the writing voice, and the hard-won
> lessons. The repo is the long-term memory — Claude's own memory resets each session.

## Structure

- **`meaning_project/`** — the active hub. Medium writing (bilingual, English-led) on
  post-labour meaning. Three-layer honesty method (🟢 empirical / 🟡 analogical / 🔴
  normative-design, never blurred). Contains MANIFESTO, evidence_base, idea_pool, concepts,
  STYLE, and `articles/`.
- **`so_sdt_study/`** — a completed, pre-registered, placebo-controlled empirical study of
  Stack Overflow contributors after ChatGPT. Result: an honest null. Reusable as a 🟢
  "load-bearing pillar" / case study in the writing. Fully reproducible.
- **`archive/abm_v1/`** — the original post-scarcity behavioural-sink ABM, retired (circular +
  unfalsifiable) but kept intact for possible future revival when ABM is the right tool.

## Working norms

- **Honesty first.** Never present 🟡/🔴 claims as 🟢. State limitations in the open. When
  citing studies, cite what they actually showed — verify from primary text, not search
  summaries. This is the project's only real capital.
- **Falsifiability for empirical work.** Pre-register before seeing outcomes; freeze designs;
  use placebos/controls; let the data win even when it kills the hypothesis.
- **Commit & push** meaningful progress to the working branch so the repo stays the reliable
  memory.

## Per-article workflow
See `meaning_project/STYLE.md`. Briefly: `articles/<slug>/brief.md` → optional 🟢 analysis/
figure → `draft.md` → polish against STYLE + honesty rules → publish, record URL.

## Stack (for empirical pillars)
Python: pandas, numpy, scipy, statsmodels (PHReg for survival), matplotlib. Data via public
sources (e.g. Stack Exchange Data Explorer). Keep analyses reproducible from committed scripts.
