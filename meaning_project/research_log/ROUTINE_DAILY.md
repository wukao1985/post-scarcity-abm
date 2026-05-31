# Routine prompt — DAILY scan

Paste this as the prompt for the daily scheduled run (Claude Code web routine, or a GitHub
Actions cron job — see `SETUP.md`). It is intentionally strict about curation: most days there
is nothing genuinely new, and saying so is correct.

---

You are maintaining the research log for a lifelong project on **human meaning in the post-AI /
post-labour era**. Today is a routine daily scan.

**First, load context (do not skip):**
1. Read `meaning_project/MANIFESTO.md` (the niche, and the three-layer honesty method:
   🟢 empirical / 🟡 analogical / 🔴 normative-design — never blur them).
2. Skim `meaning_project/evidence_base.md` and the last ~7 files in
   `meaning_project/research_log/daily/` so you do NOT re-report things already logged.

**Then scan for genuinely new, relevant developments (last ~24–48h)** across:
- AI's measured effect on labour, jobs, wages, occupational exposure (new studies/data).
- UBI / cash-transfer experiments and their **psychological / wellbeing / meaning** outcomes.
- Meaning of work, Self-Determination Theory, deaths of despair, retirement/FIRE, loneliness,
  status, purpose — anything bearing on meaning when work recedes.
- Serious futures/policy thinking on post-labour society (think-tanks, notable essays).
- Major AI capability milestones **only insofar as they change the labour/meaning picture**.

Use web search. Prefer primary sources (papers, preprints, official reports) over hot takes.
**Do not trust headlines — note what a source actually shows.**

**Curate hard.** Include an item only if it is (a) genuinely new since the last logs AND
(b) relevant to the meaning niche. Aim for 0–4 items. **If nothing substantive: say so in one
line and stop — do not pad.**

**Write** `meaning_project/research_log/daily/YYYY-MM-DD.md` (today's date), format:

```
# Daily scan — YYYY-MM-DD

## Items
- **[Title]** — source (link). 🟢/🟡/🔴. One sentence on what it actually shows (not the
  headline). Why it matters for the meaning project. If it's a 🟢 anchor worth keeping,
  add "→ candidate for evidence_base". If it sparks a piece, add "→ idea: <one line>".

## Watchlist movement
- (optional) any of the tracked variables that moved — see MANIFESTO §analogy breakpoints:
  what is being automated, speed vs adjustment, whether the 'new jobs' mechanism holds.

## Note
- One line: overall read of the day, or "nothing substantive new today."
```

**Finally, commit and push to `main`** (this is mandatory — the run is wasted otherwise).
The daily log belongs on `main` (the project's long-term memory); do NOT create a new branch.
Sync first so you never commit from a stale state (this is what caused orphaned parallel logs
before):
```
git fetch origin main
git checkout main && git pull --ff-only origin main
git add meaning_project/research_log/
git commit -m "research log: daily scan YYYY-MM-DD"
git push origin main
```
If the daily file for today already exists (a run earlier today), APPEND/merge your items into
it rather than overwriting. If nothing new, still commit the short "nothing substantive" entry so
the cadence is recorded.

**Honesty rules (non-negotiable):** mark every item 🟢/🟡/🔴; never upgrade a claim's
certainty; cite what the source shows, not its headline; if you couldn't verify something,
say so. Quality and honesty over volume.
