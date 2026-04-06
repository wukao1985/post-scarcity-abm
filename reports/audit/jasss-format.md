# JASSS Format Compliance Audit

**Document:** Post-Labor Behavioral Sink ABM Paper Submission
**Audit Date:** 2026-04-02
**Status:** READ-ONLY AUDIT

---

## Executive Summary

| Check | Status | Finding |
|-------|--------|---------|
| Abstract word count | **FAIL** | 368 words (target: 150-250) |
| ODD protocol completeness | **PARTIAL** | Missing explicit "Patterns" subsection |
| Reference format consistency | **PARTIAL** | Minor APA inconsistencies |

---

## 1. Abstract Word Count Analysis

### Requirement
JASSS and most social simulation journals require abstracts between **150-250 words** to ensure concise summary of research contributions.

### Current State
- **Measured word count:** 368 words
- **Excess:** 118-218 words over limit
- **Location:** `reports/paper_draft.md`, lines 11-25

### Issue Details
The abstract attempts to summarize all five major findings with quantitative details. While comprehensive, this exceeds standard limits. The abstract includes:
- Model framing (1 paragraph)
- Five numbered findings with numerical values
- A caveat paragraph with validation gaps
- An italicized limitation note

### Recommendation
Reduce to 200-220 words by:
1. Condensing the five findings into 2-3 key takeaways
2. Moving specific numerical values (e.g., "sink index of ~0.52") to the main text
3. Removing the inline limitation note (keep in Discussion)

---

## 2. ODD Protocol Completeness

### Requirement
Per Grimm et al. (2020), the ODD protocol requires **seven elements** across three sections:

| # | Element | Required |
|---|---------|----------|
| 1 | Purpose **and Patterns** | Yes |
| 2 | Entities, State Variables, and Scales | Yes |
| 3 | Process Overview and Scheduling | Yes |
| 4 | Design Concepts (11 sub-elements) | Yes |
| 5 | Initialization | Yes |
| 6 | Input Data | Yes |
| 7 | Submodels | Yes |

### Current State (`reports/ODD_protocol.md`)

| Element | Present | Notes |
|---------|---------|-------|
| Purpose | **YES** | Clearly stated with 5 research questions |
| **Patterns** | **NO** | Not explicitly documented |
| Entities, State Variables, Scales | **YES** | Complete with state variable table |
| Process Overview and Scheduling | **YES** | Sequential ordering documented |
| Design Concepts | **YES** | All 11 sub-elements present |
| Initialization | **YES** | 7-step procedure documented |
| Input Data | **YES** | States "no external input" |
| Submodels | **YES** | Mathematical specifications included |

### Missing: Patterns Subsection

Per ODD standard, Section 1 should include "Patterns" — the observable patterns the model is designed to reproduce or explain. Current ODD lists research questions but not target patterns.

**Expected patterns to document:**
1. Phase transition at ~80-90% displacement (threshold effect)
2. Archetype distribution shifts (Productive → Beautiful One → Withdrawn → Collapsed)
3. Intervention ordering effects (bundle > single interventions)
4. Collectivism-moderated sink severity

### Design Concepts Completeness Check

| Sub-element | Present | Location |
|-------------|---------|----------|
| Basic Principles | **YES** | Section 4.1 (SDT, contagion, behavioral sink) |
| Emergence | **YES** | Section 4.2 |
| Adaptation | **YES** | Section 4.3 |
| Objectives | **YES** | Section 4.4 |
| Learning | **YES** | Section 4.5 |
| Prediction | **YES** | Section 4.6 |
| Sensing | **YES** | Section 4.7 |
| Interaction | **YES** | Section 4.8 |
| Stochasticity | **YES** | Section 4.9 |
| Collectives | **YES** | Section 4.10 |
| Observation | **YES** | Section 4.11 |

---

## 3. Reference Format Consistency

### Requirement
JASSS follows standard academic citation practices. Most ABM papers in JASSS use APA-style references.

### Current State
19 references in `reports/paper_draft.md` (lines 430-468)

### Issues Found

#### Issue 3.1: Incomplete Author Lists
```
Grimm, V., et al. (2020). The ODD Protocol...
```
**Problem:** APA 7th edition requires listing up to 20 authors. Using "et al." in the reference list is non-standard.

**Should be:**
```
Grimm, V., Railsback, S. F., Vincenot, C. E., Berger, U., Gallagher, C.,
DeAngelis, D. L., ... & Ayllón, D. (2020). The ODD Protocol...
```

#### Issue 3.2: Inconsistent Publisher Formatting

**Books with location:**
- None present

**Books without location (APA 7 compliant):**
- `Crown Business` (line 432)
- `WW Norton & Company` (line 436)
- `Princeton University Press` (lines 440, 464)
- `Cornell University Press` (line 456)
- `Sage` (line 458)
- `Cambridge University Press` (lines 460, 462)
- `Penguin UK` (line 468)

**Verdict:** Publisher formatting is consistent (APA 7 style, no location required).

#### Issue 3.3: Journal Title Formatting

All journal titles use italics consistently: **PASS**

Examples:
- `*Cambridge Journal of Regions, Economy and Society*`
- `*Scientific American*`
- `*American Journal of Sociology*`

#### Issue 3.4: Page Number Formatting

All page ranges use hyphens consistently: **PASS**

Examples:
- `29-44`, `3-30`, `702-734`

#### Issue 3.5: DOIs Missing

No DOIs are included in any reference. While not strictly required, DOIs improve citation reliability and are increasingly expected.

**Recommendation:** Add DOIs for all references where available.

### Reference Format Summary

| Check | Status |
|-------|--------|
| Author format | **PARTIAL** - "et al." in reference list |
| Year format | **PASS** |
| Title capitalization | **PASS** |
| Journal italics | **PASS** |
| Volume/issue format | **PASS** |
| Page numbers | **PASS** |
| Book publishers | **PASS** |
| DOIs | **MISSING** (optional but recommended) |

---

## 4. Additional JASSS Requirements

### 4.1 Keywords
**Present:** Yes (line 5)
```
post-labor displacement, behavioral sink, self-determination theory,
agent-based modeling, role substitution, social cohesion, universal basic income
```
**Status:** PASS (7 keywords, appropriate for topic)

### 4.2 Data Availability Statement
**Present:** Yes (lines 472-474)
**Status:** PASS (includes GitHub repository URL)

### 4.3 Code Availability
**Present:** Yes (same as data availability)
**Status:** PASS

### 4.4 Author Contributions
**Present:** Yes (line 482, anonymized)
**Status:** PASS for review

### 4.5 Competing Interests
**Present:** Yes (line 486)
**Status:** PASS

---

## 5. Recommendations Summary

### Critical (Must Fix)
1. **Reduce abstract to 150-250 words** — currently 118+ words over limit

### Important (Should Fix)
2. **Add "Patterns" subsection to ODD protocol** — required by Grimm et al. (2020)
3. **Expand Grimm et al. author list** — "et al." not standard in reference lists

### Optional (Nice to Have)
4. Add DOIs to references where available
5. Consider adding ORCID identifiers for authors (post-review)

---

## Appendix: Files Audited

| File | Purpose | Lines |
|------|---------|-------|
| `reports/paper_draft.md` | Main submission | ~524 |
| `reports/ODD_protocol.md` | Model description | ~281 |

---

*Audit performed as READ-ONLY review. No files modified.*
