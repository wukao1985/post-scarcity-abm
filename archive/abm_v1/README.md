# Archive — ABM v1 (post-scarcity behavioural-sink simulation)

**Archived 2026-05-31. Not active. Kept intact for possible future revival.**

This is the original project: a multi-pathway agent-based model (ABM) of behavioural sink
under AI automation / post-labour displacement. It was developed and polished across ~20
adversarial-review iterations toward a JASSS submission, then **retired** when two structural
problems were judged unfixable by polishing:

1. **Circular reasoning** — the headline result was largely baked into the meaning-function
   definition rather than emerging from the model.
2. **Unfalsifiability** — it simulated a hypothetical post-labour future with no ground truth.

See `../../LESSONS.md` for the full lesson, and `../../meaning_project/MANIFESTO.md` for the
direction that superseded it.

## Why keep it
The modelling machinery is substantial and reusable. One day we may return to ABM for
research questions where it *is* the right tool (genuine emergence: contagion, networks,
tipping points) — at which point this is the starting point. The code runs (Mesa 3.5).

## What's here
- `models/` — pathway A ABM (`pathway_a_abm/`), pathway C system dynamics, pathway B (stub).
- `reports/` — the JASSS paper draft, ~20 adversarial reviews, sweep analyses, figures, audits.
- `scripts/` — sweep runners and figure generation.
- `data/` — simulation outputs (sweeps 1–6, ablations) and historical CSVs.
- `docs/` — V3 experiment design, reproduction checklist, paper↔repo map.
- `tasks/` — task tracking and review-iteration history.
- `tests/`, `Makefile`, `REPRODUCE.md` — repro infrastructure.

## To revive
The paths inside assume repo-root execution. If reactivating, either run from within
`archive/abm_v1/` or move the relevant pieces back to root. `REPRODUCE.md` documents the
original pipeline.
