# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-003]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of config, entry point and tests; deployment files checked by running them
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | config.py and main.py follow PEP 8 casing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | normalize_db_uri, load_settings, ConfigurationError state purpose. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | No formatter or linter configured (gap noted in RC-009); two imports in main.py carry a justified noqa E402 because src must be on sys.path first. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All new functions annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | Missing FLASK_KEY raises ConfigurationError; no swallowed exception. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults. |
| 7 | Files, locks and connections are managed with context managers | Pass | No files or connections opened in the new code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Docstrings in Doxygen form. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print; secrets are never logged or hard-coded (test checks it). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No DCD; config belongs to the infrastructure layer. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 15 new tests (68 in total) including Procfile content and import of main with a tmp SQLite DB; container run verified against PostgreSQL 16 (HTTP 200, tables created). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | N-A: no type checker configured. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | psycopg==3.3.3 added next to psycopg-binary: the binary wheel has no psycopg module (found by the container failing with ModuleNotFoundError). Deviation from the lecture list, needed at runtime. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Environment variable names and scheme strings are in constants.py only. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | config.py in infrastructure imports only constants and the standard library. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | load_settings takes a Mapping, so tests need no real environment. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Config in infrastructure; entry point main.py at the root as the Procfile requires. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File names English and valid. |

## Overall Verdict

Go - every mandatory criterion passes. Mode: autonomous, not independent; the stand-in decision stays open to challenge in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-003]: ../../milestones/mil-003-production-readiness.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
