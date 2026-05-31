"""
Exploratory signal check — scaffold.

PURPOSE: BEFORE committing to the full study, answer one question on a small
site: does the "motivation type x differential exodus" signal plausibly exist?

This is a LOOK, not a test. Per DESIGN.md, the real hypothesis test requires the
classifier to be frozen before outcomes are seen. This script is allowed to peek
ONLY on a small DEBUG site that will NOT be the analysis site for the paper, so we
do not contaminate the pre-registered test on Stack Overflow itself.

  ┌─────────────────────────────────────────────────────────────────────┐
  │ DISCIPLINE: findings here inform feasibility & index construction.    │
  │ They must NOT be used to tune the classifier and THEN run it on the   │
  │ same site. The frozen classifier runs on SO; exploration runs on a    │
  │ different small site. (DESIGN.md §5, §10.)                            │
  └─────────────────────────────────────────────────────────────────────┘

Planned steps (fill in once data lands):
  1. Load Users/Posts/Comments/Badges for the debug site.
  2. Build cohort (DESIGN §4): tenure >= 3mo at shock, >=5 answers in
     classification window 2021-11-30..2022-11-29.
  3. Compute the three motivation indices (DESIGN §5a) on classification window.
  4. Compute post-shock exodus (DESIGN §6) on outcome window.
  5. Crude check: do continuous indices correlate with exodus, controlling for
     log pre-shock answer volume + tenure? (descriptive, not inferential)
  6. Eyeball whether the ordering hints status>competence>relatedness.

Output: a short printed summary + a couple of diagnostic plots, so the
researcher can decide go / no-go on the full Stack Overflow pipeline.
"""
from __future__ import annotations

SHOCK_DATE = "2022-11-30"
CLASSIFY_START, CLASSIFY_END = "2021-11-30", "2022-11-29"
WASHOUT_END = "2023-01-31"
OUTCOME_START, OUTCOME_END = "2023-02-01", "2024-01-31"
PLACEBO_SHOCK_DATE = "2021-11-30"


def build_cohort(users, answers):
    """Return user_ids meeting DESIGN §4 inclusion. TODO."""
    raise NotImplementedError


def motivation_indices(answers, comments, badges, posts):
    """Return per-user (competence, status, relatedness) z-scored indices.
    Uses ONLY classification-window rows. See DESIGN §5a. TODO."""
    raise NotImplementedError


def exodus_outcome(answers):
    """Return per-user exodus time / censoring on outcome window. DESIGN §6. TODO."""
    raise NotImplementedError


def main() -> int:
    print(__doc__)
    print("Windows:")
    print(f"  shock           = {SHOCK_DATE}")
    print(f"  classify        = {CLASSIFY_START} .. {CLASSIFY_END}")
    print(f"  washout end     = {WASHOUT_END}")
    print(f"  outcome         = {OUTCOME_START} .. {OUTCOME_END}")
    print(f"  placebo shock   = {PLACEBO_SHOCK_DATE}")
    print("\nScaffold only. Implement after debug-site data is downloaded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
