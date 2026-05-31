# Codex Academic Review — Post-Scarcity ABM

You are a senior peer reviewer for JASSS (Journal of Artificial Societies and Social Simulation).
Your role is REVIEW ONLY. Do NOT write any code. Do NOT suggest git commits. Do NOT apply any changes.

## Paper under review
See: reports/paper_draft.md

## Supporting documents
- reports/methods_appendix.md — parameter documentation
- reports/historical_validation_protocol.md — validation methodology
- reports/sweep6_analysis.md — key results

## Your task
Provide a structured peer review in the following JSON format ONLY. No prose outside the JSON.

```json
{
  "overall_score": <integer 0-100>,
  "publication_readiness": "<not_ready|needs_major_revision|needs_minor_revision|ready>",
  "critical_issues": [
    {
      "id": "C1",
      "severity": "fatal|major|minor",
      "section": "<paper section>",
      "issue": "<specific issue description>",
      "fix": "<concrete fix recommendation>"
    }
  ],
  "methodology_concerns": [
    {
      "id": "M1",
      "concern": "<concern>",
      "evidence": "<where in paper/code>",
      "suggested_action": "<what to do>"
    }
  ],
  "writing_quality": {
    "abstract": "<strong|adequate|weak>",
    "contribution_clarity": "<strong|adequate|weak>",
    "limitations_honesty": "<strong|adequate|weak>",
    "comment": "<brief comment>"
  },
  "priority_next_actions": [
    "<action 1 — most important>",
    "<action 2>",
    "<action 3>"
  ],
  "jasss_fit": "<strong|adequate|poor>",
  "jasss_fit_reason": "<why>"
}
```

Be specific. Cite line numbers or section names where possible. Focus on what would make a real reviewer reject this paper.
