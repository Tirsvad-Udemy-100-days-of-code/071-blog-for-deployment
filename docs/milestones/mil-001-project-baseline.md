# Project baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decides whether the repository has the agreed skeleton (configuration, ignore rules, constants, Doxygen, venv instructions, repository metadata) so that application code can be written on it.

## Deliverable

A repository with `pyproject.toml`, Python `.gitignore`, `src/` and `tests/` skeletons, `constants.py`, `Doxyfile`, a venv section in the README, and description plus topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python >=3.13` and pytest configuration | `python -m pytest` runs (collects) without error | Criterion not met |
| 2 | `.gitignore` ignores `.venv`, `.env`, `*.db`, `.idea`, caches and `/docs/ai-prompts/` | `git check-ignore` confirms each | Criterion not met |
| 3 | `Doxyfile` exists and `doxygen Doxyfile` finishes without errors | Exit code 0 | Criterion not met |
| 4 | Repository description and topics are set | The repository API shows both | Criterion not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5, success criterion 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-11 - inside the Project Plan window (2026-11-11 to 2026-11-14); the Business Case sets no duration limit.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set the description and topics on the Gitea repository through its API so S03 sees the purpose at once. The token is read from the personal `.env`, which the project never imports. | No | |
| 2 | Configure the Python project | Add `pyproject.toml` (Python 3.13 or newer, setuptools, pytest settings, optional `dev` extra), `src/` and `tests/` packages and `constants.py` for all constants. | No | |
| 3 | Add the Python .gitignore | Ignore the venv, `.env`, SQLite files, IDE folders, caches, build output, Doxygen output and the AI prompt log, so nothing unnecessary is uploaded. | No | |
| 4 | Add the Doxyfile | Create a `Doxyfile` for `src/` so the Doxygen comments in the code build into HTML under `docs/doxygen/`. | No | |
| 5 | Document the local venv | Describe in the README how to create `.venv`, activate it and run `python -m pip install --upgrade pip` before installing. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
