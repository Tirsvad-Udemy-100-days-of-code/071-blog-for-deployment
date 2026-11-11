# Production readiness

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [8bad45b] |

---

## Purpose

Decides whether the blog can be deployed: configuration from the environment, a WSGI server, PostgreSQL and a container setup.

## Deliverable

Environment-driven configuration, `requirements.txt` with the lecture versions, `Procfile`, `Dockerfile` and `compose.yaml` with PostgreSQL, and tests of the configuration.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | No secret or connection string is hard-coded in `src/` | opengrep scan reports no secret finding | Criterion not met |
| 2 | `FLASK_KEY` and `DB_URI` are read from the environment; SQLite is only the default for `DB_URI` | Config tests pass | Criterion not met |
| 3 | `postgres://` and `postgresql://` URIs are normalised for psycopg 3 | Config test passes | Criterion not met |
| 4 | `Procfile` contains `web: gunicorn main:app` and debug is off | File content check and test | Criterion not met |
| 5 | The container image builds and serves the blog with PostgreSQL | `docker compose up` then HTTP 200 on `/` | Criterion not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The application to deploy must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2 and 3, success criterion 2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 - inside the Project Plan window (2026-11-11 to 2026-11-14); the Business Case sets no duration limit.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Read settings from environment variables | Add a config module that reads `FLASK_KEY`, `DB_URI` and the mail credentials from the environment, with SQLite as default only for the database, and set `debug=False`. | No | |
| 2 | Pin the lecture requirements | Write `requirements.txt` with the lecture versions including gunicorn and psycopg-binary, and verify it installs in a clean `.venv`. | No | |
| 3 | Add the Procfile and entry point | Create `Procfile` with `web: gunicorn main:app` and a top-level `main.py` exposing `app`. | No | |
| 4 | Add Docker and PostgreSQL | Create a `Dockerfile` and `compose.yaml` with a PostgreSQL service, as a free replacement for Heroku; normalise the database URI for psycopg. | No | |
| 5 | Test the configuration | Pytest tests for the environment handling and URI normalisation. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[8bad45b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/commit/8bad45b22a1694dea060d3353738c8a1c65018a8
