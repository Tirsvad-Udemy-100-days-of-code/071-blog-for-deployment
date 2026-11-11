# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [8bad45b] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's cross-artifact traceability can be measured. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | RC-001 |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | RC-002 |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | MIL-001 to MIL-004 | RC-003 |
| MIL-001 | MIL | en | it | [PP-001] | `src/`, `tests/` (baseline) | RC-004 |
| MIL-002 | MIL | en | it | [PP-001] | `src/`, `tests/` (application) | RC-005 |
| MIL-003 | MIL | en | it | [PP-001] | deployment files | RC-006 |
| MIL-004 | MIL | en | it | [PP-001] | README, wiki | RC-007 |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | MIL-002 | - | pytest suite | Covered |
| CN-002 | MIL-003 | - | opengrep scan | Covered |
| CN-003 | MIL-003 | - | docker compose run | Covered |
| CN-004 | MIL-002 | - | review of code | Covered |
| CN-005 | MIL-001, MIL-004 | - | manual run of README | Covered |
| CN-006 | MIL-001, MIL-004 | - | repository API check | Covered |
| CN-007 | MIL-003 | - | requirements review | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | none | none found | - | Closed | - |

## Coverage Notes

No ADR, TP, DM, UC or design artifacts exist: the tasks are technical. `-` in Upstream means foundational.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[8bad45b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/commit/8bad45b22a1694dea060d3353738c8a1c65018a8
