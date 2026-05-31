# Setup — scheduling the research routines

Two routines (prompts in this folder):
- `ROUTINE_DAILY.md` — quick daily scan → `daily/YYYY-MM-DD.md`
- `ROUTINE_WEEKLY.md` — weekly synthesis → `weekly/YYYY-Www.md`, feeds `evidence_base.md` etc.

Both prompts already instruct Claude to **commit and push** (scheduled runs do not auto-commit
— it must be in the prompt). **They push directly to `main`** — the daily/weekly log is the
project's long-term memory and belongs on the trunk. The prompts `git fetch` + `pull --ff-only`
before committing so a run never starts from a stale state and never spawns a parallel branch.
(History lesson: earlier runs each pushed to their own `claude/…` branch and drifted apart,
producing three conflicting same-day logs that had to be merged by hand. Pushing to `main`
avoids that.)

## Option A — native "Routines" (recommended; confirmed supported)
Claude Code has a native scheduler called **Routines** (research preview). Docs:
https://code.claude.com/docs/en/routines.md

Routines run autonomously on Anthropic's cloud (no machine open, no permission prompts), can
web-search and push to git. **Two important defaults to change:**
- **Network:** default "Trusted" does NOT allow web search. In the routine's environment, set
  network access to **Custom** (add the domains you want) or **Full**. Web search needs this.
- **Branch — IMPORTANT:** by default Claude can only push to `claude/`-prefixed branches. These
  routines push to **`main`**, so you MUST enable **"Allow unrestricted branch pushes"** in the
  routine's environment, or the push will be rejected. (If you'd rather not, change the two
  prompts back to a single fixed branch — but then merge it to `main` regularly so logs don't
  drift; the whole point of targeting `main` is to avoid that drift.)
- Commits appear under your GitHub identity. There's a per-account daily run cap.

Steps (at https://claude.ai/code/routines, or run `/schedule` in any CLI session):
1. **New routine** → name it "Daily research scan".
2. Select this repository; pick/confirm an environment, and set its **network = Full** (so web
   search works).
3. Prompt: paste the entire contents of `ROUTINE_DAILY.md`. (The prompt itself tells Claude to
   read MANIFESTO, scan, write the dated file, and `git push origin main` after a
   `pull --ff-only`.) Enable **"Allow unrestricted branch pushes"** so the push to `main` works.
4. Trigger: **Schedule → daily**. Create.
5. Repeat for a second routine "Weekly research digest": prompt = `ROUTINE_WEEKLY.md`,
   Schedule → weekly (e.g. Monday).

That's it — the prompts already contain the commit+push step (Routines do NOT auto-commit).

## Option B — GitHub Actions cron (documented, robust)
Docs: https://docs.claude.com/en/docs/claude-code/github-actions

Add a secret `ANTHROPIC_API_KEY` (repo → Settings → Secrets → Actions). Then add a workflow
like `.github/workflows/research-routine.yml`:

```yaml
name: research-routine
on:
  schedule:
    - cron: '0 13 * * *'    # daily 13:00 UTC
    - cron: '0 14 * * 1'    # weekly Monday 14:00 UTC
  workflow_dispatch: {}       # allow manual runs
permissions:
  contents: write             # needed to commit/push
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 0          # full history so the prompt's pull --ff-only works
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          # pick the prompt file by day: weekly on Mondays, daily otherwise
          prompt_file: ${{ github.event.schedule == '0 14 * * 1' && 'meaning_project/research_log/ROUTINE_WEEKLY.md' || 'meaning_project/research_log/ROUTINE_DAILY.md' }}
          allowed_tools: "WebSearch,WebFetch,Bash,Read,Write,Edit"
```

(Exact `claude-code-action` input names may evolve — check the docs link above. The key pieces:
checkout the branch, give the API key, pass the prompt file, allow web + git tools, grant
`contents: write` so the push in the prompt succeeds.)

## Cadence chosen
Daily scan + weekly digest. Daily keeps you current; weekly compounds it into the permanent
files (`evidence_base.md`, `idea_pool.md`). Most days will be "nothing substantive" — that is
by design; the prompts forbid padding.
