# Double-Blind Compliance Audit

**Audit Date:** 2026-04-02
**Auditor:** Automated Review
**Scope:** paper_draft.md, methods_appendix.md, ODD_protocol.md

---

## Summary

| Status | Count |
|--------|-------|
| CRITICAL violations | 1 |
| Minor issues | 0 |
| Items reviewed | 3 files |

**Overall Assessment:** NOT COMPLIANT - requires remediation before submission

---

## Critical Violations

### 1. GitHub URL Contains Identifying Username

**File:** `reports/paper_draft.md`
**Line:** 474
**Section:** Data Availability

**Problematic text:**
```
All simulation code, data (6 sweeps + 2 ablation studies, 18,500 runs),
and analysis scripts are available at: https://github.com/wukao1985/post-scarcity-abm
```

**Issue:** The GitHub URL contains the username `wukao1985`, which could identify the author(s) to reviewers.

**Remediation:** Replace with anonymized placeholder:
```
All simulation code, data (6 sweeps + 2 ablation studies, 18,500 runs),
and analysis scripts are available at: [ANONYMIZED FOR REVIEW]
```

---

## Compliant Items

The following elements were checked and found compliant:

| Item | Location | Status |
|------|----------|--------|
| Author names | paper_draft.md:3 | COMPLIANT ("Anonymous Authors (under review)") |
| Author contributions | paper_draft.md:480-482 | COMPLIANT ("[Anonymized for review]") |
| Acknowledgments | paper_draft.md:476-478 | COMPLIANT (placeholder text) |
| Competing interests | paper_draft.md:484-486 | COMPLIANT (standard declaration) |
| Self-citations | All files | COMPLIANT (no identifying self-references) |
| Institutional affiliations | All files | COMPLIANT (none present) |
| Email addresses | All files | COMPLIANT (none present) |
| External URLs | methods_appendix.md, ODD_protocol.md | COMPLIANT (none present) |

---

## Items Requiring Attention (Non-Critical)

### Prior Work References

**File:** `reports/paper_draft.md`
**Line:** 78

**Text:** "The model extends prior work (V1, V2) with refined psychological dynamics..."

**Assessment:** These appear to be internal version references (model iterations) rather than previously published papers. If V1/V2 were separately published works by the same authors, this could constitute a revealing self-citation.

**Recommendation:** Confirm V1/V2 are not published papers. If they are, anonymize the reference.

---

## Files Reviewed

### paper_draft.md (524 lines)
- Scanned for: author names, GitHub/repository links, self-citations, acknowledgments, institutional affiliations, email addresses
- Violations found: 1 (GitHub URL)

### methods_appendix.md (164 lines)
- Scanned for: author names, GitHub/repository links, self-citations, acknowledgments, institutional affiliations, email addresses
- Violations found: 0
- Note: Line 163 contains "the authors' honest assessment" - standard academic language, not identifying

### ODD_protocol.md (281 lines)
- Scanned for: author names, GitHub/repository links, self-citations, acknowledgments, institutional affiliations, email addresses
- Violations found: 0

---

## Recommended Actions

1. **REQUIRED:** Remove or anonymize GitHub URL in paper_draft.md line 474
2. **OPTIONAL:** Verify V1/V2 references are not published works; anonymize if they are

---

## Audit Methodology

Patterns searched:
- GitHub/GitLab/Bitbucket URLs
- Email addresses (@domain patterns)
- Institutional keywords (university, institute, college, department)
- Acknowledgment sections
- Author/affiliation sections
- Self-citation patterns (prior work, our previous, we have shown, etc.)
- Names embedded in URLs or paths
