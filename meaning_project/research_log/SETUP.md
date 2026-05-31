# Setup — scheduling the research routines

Two routines (prompts in this folder):
- `ROUTINE_DAILY.md` — quick daily scan → `daily/YYYY-MM-DD.md`
- `ROUTINE_WEEKLY.md` — weekly synthesis → `weekly/YYYY-Www.md`, feeds `evidence_base.md` etc.

Both prompts already instruct Claude to **commit and push** (scheduled runs do not auto-commit
— it must be in the prompt). Point them at the working branch
`claude/paper-repo-review-E0GJA` (or merge to `main` and target that).

## Option A — native "Routines" (recommended; confirmed supported)
Claude Code has a native scheduler called **Routines** (research preview). Docs:
https://code.claude.com/docs/en/routines.md

Routines run autonomously on Anthropic's cloud (no machine open, no permission prompts), can
web-search and push to git. **Two important defaults to change:**
- **Network:** default "Trusted" does NOT allow web search. In the routine's environment, set
  network access to **Custom** (add the domains you want) or **Full**. Web search needs this.
- **Branch:** by default Claude can only push to `claude/`-prefixed branches — which is exactly
  our working branch `claude/paper-repo-review-E0GJA`, so **no change needed** unless you later
  move the routine to push to `main` (then enable "Allow unrestricted branch pushes").
- Commits appear under your GitHub identity. There's a per-account daily run cap.

Steps (at https://claude.ai/code/routines, or run `/schedule` in any CLI session):
1. **New routine** → name it "Daily research scan".
2. Select this repository; pick/confirm an environment, and set its **network = Full** (so web
   search works).
3. Prompt: paste the entire contents of `ROUTINE_DAILY.md`. (The prompt itself tells Claude to
   read MANIFESTO, scan, write the dated file, and `git push origin
   claude/paper-repo-review-E0GJA`.)
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
          ref: claude/paper-repo-review-E0GJA
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
