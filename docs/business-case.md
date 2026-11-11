# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Executive Summary

Day 71 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" teaches how to take a Flask blog from a laptop to the internet. This project delivers that assignment as a readable, runnable repository: the blog application, its production configuration (environment variables, gunicorn, a Procfile, PostgreSQL) and a container-based deployment, because the course host Heroku has no free plan. Each lecture step is documented with a screenshot in the README and a three-language wiki (English, Danish, Bahasa Malaysia) that explains what was learned.

## Methodological and Standards Foundation

The work follows the SQA and QC framework mounted at `framework/`: artifacts are reviewed against their QC checklist and every criterion is tagged with an ISO/IEC 25010:2023 characteristic. Python code follows the `coding-conventions` skill and the layering of the `clean-architecture` skill. The deployment follows the twelve-factor practice of configuration in the environment.

## Problem Statement

A course participant has a working Flask blog that only runs in debug mode on one machine with a SQLite file and a secret key written in the source. Such a blog cannot be shared, would lose its data on a hosted file system and leaks its secrets if pushed to a public repository. Other participants and GitHub visitors have no clean reference solution to compare against.

## Business Opportunity

A deployable blog with environment-driven configuration, a production web server and a production database lets the participant complete the lecture, publish the result and give other participants and visitors a reference they can run in minutes.

## Objectives

1. Deliver the Day 71 blog (posts, registration, login, comments, admin-only editing) as a Flask application under `src/`.
2. Read every setting that is sensitive or environment specific from environment variables, with a safe local default for the database only.
3. Provide `Procfile`, gunicorn and PostgreSQL support and a Docker based deployment that replaces the paid Heroku host.
4. Provide a pytest suite under `tests/` that passes on Python 3.13 or newer.
5. Document setup in a local `.venv`, the run and test commands, and each lecture step with a screenshot in README and wiki (en, da, ms).

## Scope

### In Scope

- The blog application, its tests and Doxygen comments with a `Doxyfile`.
- `pyproject.toml`, `requirements.txt` (versions of the lecture), `.gitignore`, `Procfile`, `Dockerfile` and a compose file with PostgreSQL.
- README from the framework template and a wiki in en, da, ms.
- Repository description and topics on the git host.

### Out of Scope

- Signing up to or deploying on a commercial host (Heroku, Render); the container setup stands in.
- Downloading the course's starting archive; the application is written from the lecture description.
- A working contact-form mailer beyond reading its credentials from the environment.

## Expected Benefits

### Tangible Benefits

- A repository that runs after four commands (venv, upgrade pip, install, run).
- A passing automated test suite and a clean static scan before every push.

### Intangible Benefits

- Understanding of version control, configuration through the environment, WSGI servers and production databases.
- A reusable reference for other course participants.

## Strategic Alignment

The project supports the participant's learning goal (finish the 100 Days of Code bootcamp with documented, reviewable work) and the practice of delivering every exercise through the same plan-first, reviewed process.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Tests pass | 100% of pytest tests pass on Python 3.13 | `python -m pytest` exit code 0 |
| 2 | No secrets in source | 0 hard-coded secrets | opengrep scan reports 0 blocking findings |
| 3 | Run instructions work | App starts from a fresh `.venv` in 4 commands | Manual run following README |
| 4 | Lecture steps documented | Each lecture step has 1 screenshot in README and in 3 wiki languages | Count of screenshots in `docs/images/` against the step list |
| 5 | Wiki languages | 3 languages with the same page set | File list of `docs/wiki/` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| A pinned package version (SQLAlchemy 2.1.0b1) does not install or behave as expected | App cannot start | Test in a clean venv; record any deviation in the README |
| Secrets from `.env` leak into the repository | Credential exposure | `.env` is ignored, never read by the project, opengrep scan before each push |
| Screenshots taken on the host desktop disturb the user | Lost control of mouse and keyboard | Take them headless inside a Docker container (`framework/process/gui-testing.md`) |
| Translations contain errors | Misleading wiki pages | English is authoritative; translations follow page by page and are reviewed by the author |

## Assumptions

- S01 is Product Owner, developer and reviewer; in autonomous mode the AI acts as stand-in reviewer and records that.
- Python 3.13 or newer, Docker and the git host are available on the author's machine.
- The Day 69/70 blog features are the baseline of the Day 71 application.

## Constraints

- Source in `src/`, tests in `tests/`, documents in `docs/`.
- Runtime dependencies are limited to the packages of the lecture's `requirements.txt`.
- Constants live in `constants.py`; Doxygen comments in source.
- Work is delivered by branch and pull request, one per milestone.

## Cost–Benefit Assessment

A qualitative assessment is justified because this is a learning project with no revenue: the cost is the author's time, the benefit is skill and a shareable reference.

| Costs | Benefits |
| --- | --- |
| Author time for code, tests, documents and three wiki languages | A complete, reviewed reference solution of the lecture |
| Docker and CI minutes | Safe, repeatable deployment without a paid host |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer: finishes and understands the lecture |
| S02 | Udemy course participants: readable, runnable code with the assignment's names and README steps |
| S03 | GitHub viewers: clear description, topics and README, no extra runtime dependencies |

## Recommendation

Proceed — the scope is small, the risks have mitigations and the result is useful to all three stakeholders.
