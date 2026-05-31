# Setup — scheduling the research routines

Two routines (prompts in this folder):
- `ROUTINE_DAILY.md` — quick daily scan → `daily/YYYY-MM-DD.md`
- `ROUTINE_WEEKLY.md` — weekly synthesis → `weekly/YYYY-Www.md`, feeds `evidence_base.md` etc.

Both prompts already instruct Claude to **commit and push** (scheduled runs do not auto-commit
— it must be in the prompt). Point them at the working branch
`claude/paper-repo-review-E0GJA` (or merge to `main` and target that).

## Option A — native scheduling in Claude Code on the web (if available)
If the web UI (code.claude.com) offers a "schedule / recurring session / routine" option:
1. Create a scheduled session on this repo + branch.
2. Paste the contents of `ROUTINE_DAILY.md` as the prompt; set cadence = daily.
3. Create a second scheduled session; paste `ROUTINE_WEEKLY.md`; set cadence = weekly (e.g. Mon).
4. Ensure the environment's network policy allows web search, and the session may push to the
   branch.

> Note: as of this writing it is not certain the web UI exposes a native scheduler. If you
> don't see one, use Option B, which is the officially documented path.

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
