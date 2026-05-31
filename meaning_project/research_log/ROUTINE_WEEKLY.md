# Routine prompt — WEEKLY digest

Paste this as the prompt for the weekly scheduled run (e.g. Monday). It synthesises the week's
daily scans into something durable, and feeds the project's permanent files.

---

You are maintaining the research log for a lifelong project on **human meaning in the post-AI /
post-labour era**. Today is the weekly synthesis.

**First, load context:**
1. Read `meaning_project/MANIFESTO.md` (niche + three-layer honesty method 🟢/🟡/🔴).
2. Read this week's `meaning_project/research_log/daily/*.md` entries.
3. Read the last 2–3 `meaning_project/research_log/weekly/*.md` (avoid repetition; track
   running threads).
4. Read `meaning_project/evidence_base.md`, `idea_pool.md`, `concepts.md`.

**Then do a slightly broader sweep** than the daily scans — catch anything the dailies missed
this week (new papers, reports, notable essays) on the same themes. Web search; primary
sources; verify what each actually shows.

**Synthesise — this is the point of the weekly run.** Don't just list; connect. What's the
week's throughline? Did anything shift the picture? Where do the new items sit in the
🟢/🟡/🔴 frame? Be honest when the week was quiet.

**Write** `meaning_project/research_log/weekly/YYYY-Www.md` (ISO week), format:

```
# Weekly digest — YYYY-Www (dates)

## The week in one paragraph
What, if anything, moved. Honest — "a quiet week" is a valid answer.

## Notable items
- **[Title]** — source. 🟢/🟡/🔴. What it shows. Significance for the meaning niche.

## Running threads
- Ongoing storylines worth tracking across weeks (e.g. UBI evidence accumulating, an
  occupation visibly affected, a policy debate developing).

## Watchlist (the analogy breakpoints)
- What is being automated (muscle → routine cognition → judgment/creativity)?
- Speed vs society's adjustment timescale?
- Does the 'new jobs appear' mechanism still hold (or does AI do the new jobs too)?
Note any real-world movement on these this week.

## Feeds into the project
- evidence_base: <any genuine 🟢 anchors to add — and DO add them to evidence_base.md>
- idea_pool: <any article ideas — and DO add them to idea_pool.md, tagged by claim type>
- concepts: <any pattern that strengthens/challenges a coinage in concepts.md>
```

**Then actually update the permanent files** when warranted: append new 🟢 anchors to
`evidence_base.md`, new ideas to `idea_pool.md`, notes to `concepts.md`. (These updates are
the compounding value — the digest is the staging area, these files are the asset.)

**Finally, commit and push** (mandatory):
```
git add meaning_project/
git commit -m "research log: weekly digest YYYY-Www (+ evidence_base/idea_pool updates)"
git push origin <the working branch>
```

**Honesty rules (non-negotiable):** mark claims 🟢/🟡/🔴; never inflate certainty; cite what
sources show, not headlines; a quiet week is reported as a quiet week. The goal is a
trustworthy, compounding knowledge base — not the appearance of activity.
