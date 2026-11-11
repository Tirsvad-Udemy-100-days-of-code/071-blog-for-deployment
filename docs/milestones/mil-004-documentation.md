# Documentation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [8bad45b] |

---

## Purpose

Decides whether S02 and S03 can understand, run and learn from the repository: README, screenshots and the three-language wiki.

## Deliverable

README from the framework template with a screenshot per lecture step, and `docs/wiki/` in English, Danish and Bahasa Malaysia explaining what each step gained.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README follows the framework template and `check-readme.sh` passes | Script exit code 0 | Criterion not met |
| 2 | Each lecture step has a screenshot in `docs/images/` used in README and wiki | Step list matches image list | Criterion not met |
| 3 | The wiki has the same pages in en, da and ms | File list check | Criterion not met |
| 4 | opengrep scan before push reports no blocking finding | Scan exit code 0 | Criterion not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The deployable application must exist to be shown |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5, success criteria 3, 4 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-13 - inside the Project Plan window (2026-11-11 to 2026-11-14); the Business Case sets no duration limit.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture lecture step screenshots | Take one screenshot per lecture step headless inside a Docker container (never on the host desktop) and store them under `docs/images/`. | No | |
| 2 | Write the README | Fill the framework README template with overview, requirements, venv setup, run, tests and the lecture steps with screenshots. | No | |
| 3 | Write the wiki in three languages | Create `docs/wiki/` pages in English, Danish (`-da`) and Bahasa Malaysia (`-ms`) explaining what each lecture step gained, with the sidebar and language lines. | No | |
| 4 | Scan with opengrep before push | Run opengrep locally before each push and fix findings. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[8bad45b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/commit/8bad45b22a1694dea060d3353738c8a1c65018a8
