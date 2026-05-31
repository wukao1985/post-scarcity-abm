# Style Guide — voice & Medium conventions

So drafts come out aligned with the author's voice. Update as the voice develops.

## Voice
- **Calibrated, not breathless.** This project's whole brand is honesty about uncertainty. No
  hype, no doom-porn, no false confidence. Where we don't know, say so — that *is* the value.
- **Thinking out loud, but rigorous.** Essay register: a smart, curious person reasoning
  carefully in public. Personal, first-person, but every claim earns its place.
- **Convey the claim type in words, not labels.** Readers should *feel* which sentences are
  data, which are inference, which are the author's values — but **never via 🟢/🟡/🔴 emoji or
  tags in the prose.** That's scaffolding showing; it reads as affected and interrupts. Instead,
  let the language carry it: "that is a measured result, not a hunch" (data); "this is reasoning,
  but it's reasoning — I have little hard evidence here" (inference); "this is my counsel, not my
  finding" (values). The 🟢/🟡/🔴 markers live ONLY in the back-office files (SYNTHESIS,
  evidence_base, RESEARCH_TODO, research-note footers) as an internal index — never in reader-
  facing prose. The one allowed exception: the methodology may be *named and explained in words*
  once (e.g. the epilogue's three-way recap) — as content, still without emoji.
- **Steelman before you counter.** Engage the strongest version of opposing views.
- **Concrete over abstract.** Anchor with real studies, real cases, real numbers from
  `evidence_base.md`. Avoid the airy futurism that makes this genre cheap.

## Honesty rules (non-negotiable — see MANIFESTO)
- Never present 🟡/🔴 as 🟢.
- State the limitations of your own evidence in the piece, not just privately.
- When citing a study, cite what it *actually* showed, not the headline. (Verify from primary
  text — search summaries lie. Lesson from the SO lit review.)
- It's fine — good, even — to say "I changed my mind" or "I was wrong."

## Medium craft
- **Title + subtitle:** concrete, curiosity-driven, no clickbait that the piece can't cash.
- **Open with a hook** (a question, a surprising real fact, a tension) — earn the first 30s.
- **Subheads every ~300–400 words.** Scannable. One idea per section.
- **Length:** typically 1,200–2,500 words. Long enough to be substantive, short enough to
  finish. The methodology/pillar pieces can run longer.
- **One clear takeaway** per piece, stated plainly somewhere.
- **Figures/tables welcome** when they carry real information (we can generate them).
- **End with the honest edge:** what this doesn't settle, what you're watching next.
- **Citations:** link inline; a short "sources / further reading" list at the end is fine.

## Per-article workflow (in `articles/<slug>/`)
1. `brief.md` — angle, claim-type spine, target takeaway, which evidence_base anchors.
2. (if needed) a small analysis / figure as a 🟢 pillar.
3. `draft.md` — the piece.
4. polish pass against this guide + honesty rules.
5. on publish: mark ✅ in idea_pool, note the Medium URL in the article folder.
