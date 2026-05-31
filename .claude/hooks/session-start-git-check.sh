#!/usr/bin/env bash
# SessionStart hook: warn (never block) if the current branch is behind origin/main.
# Prevents starting work from a stale state — the cause of past orphaned divergent branches.
# Always exits 0; emits a JSON systemMessage only when there is something to say.
set +e

cd "${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null)}" 2>/dev/null || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)"

# Best-effort fetch; tolerate offline / no-remote without failing the session.
timeout 20 git fetch --quiet origin main >/dev/null 2>&1

git rev-parse --verify --quiet origin/main >/dev/null 2>&1 || exit 0

behind="$(git rev-list --count HEAD..origin/main 2>/dev/null)"
behind="${behind:-0}"

if [ "$behind" -gt 0 ] && [ "$branch" != "main" ]; then
  printf '{"systemMessage": "Branch \"%s\" is %s commit(s) behind origin/main. Consider: git pull --ff-only origin main (or rebase) before starting, to avoid divergent branches."}\n' "$branch" "$behind"
elif [ "$behind" -gt 0 ] && [ "$branch" = "main" ]; then
  printf '{"systemMessage": "Local main is %s commit(s) behind origin/main. Run: git pull --ff-only origin main before committing."}\n' "$behind"
fi
exit 0
