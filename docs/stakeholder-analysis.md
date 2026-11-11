# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

The analysis names the people who decide on, use or watch this repository, so that owners, reviewers and requirements carry stable IDs. It follows the power/interest grid and maps concerns to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish Day 71 with understood, documented and deployable work |
| S02 | Udemy coursists | Course participants who share and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and README steps |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear description, topics and README, and no extra runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews every artifact.
- **Keep Informed (S02):** cannot change the project but depends on its readability and run instructions.
- **Monitor (S03):** occasional readers; they need a good first impression, nothing more.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The blog must work as in the lecture and be tested | Functionality |
| CN-002 | S01 | No secret may be committed; settings come from the environment | Supportability (configuration) |
| CN-003 | S01 | Deployment must work without a paid host | Implementation constraint |
| CN-004 | S02 | Code is readable and keeps the assignment's names | Usability |
| CN-005 | S02 | The README explains venv, install, run and test | Usability |
| CN-006 | S03 | Description, topics and README make the purpose obvious | Usability |
| CN-007 | S03 | No runtime dependencies beyond the lecture's list | Implementation constraint |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| COM-001 | Pull request on the git host | Once per milestone | Reviewed change | All milestones |
| COM-002 | README and wiki | Updated per milestone | Run steps, screenshots, lecture notes | MIL-003, MIL-004 |
| COM-003 | Repository description and topics | Once | Discoverability | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| Few dependencies (S03) against the lecture's full package list (S01, S02) | S01, S02, S03 | Install only the lecture's pinned list; add nothing else at runtime; development tools (pytest) are optional extras |
| Simple local run (S02) against production PostgreSQL (S01) | S01, S02 | SQLite default locally, `DB_URI` selects PostgreSQL |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | [BC-001] objective 1 and 4 |
| S01 | CN-002 | [BC-001] objective 2 |
| S01 | CN-003 | [BC-001] objective 3 |
| S02 | CN-004, CN-005 | [BC-001] objective 5 |
| S03 | CN-006, CN-007 | [BC-001] objective 5 |

## Sign-Off

S01, 2026-11-11 (autonomous mode: acceptance through the review record).

---

[BC-001]: ./business-case.md
