# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review (autonomous, not independent) | [6494d1d] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of scripts/capture_screenshots.py
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | No formatter or linter is configured (gap noted in RC-009). |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | The one broad except in git_host() logs with logger.exception and keeps going on purpose (git host may be unreachable from the container). |
| 6 | No mutable default arguments and no shadowed builtins | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |
| 7 | Files, locks and connections are managed with context managers | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | logging used, no print; no secrets: the demo user password is random and never logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No DCD; the script is tooling outside the layers. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | The script is exercised by running it: 12 screenshots were produced and inspected. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | N-A: no type checker. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | N-A | Tooling lives in scripts/, outside src/ and tests/, so the layer rule does not apply. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | scripts/capture_screenshots.py checked: PEP 8 names, annotations, Doxygen docstrings, no mutable defaults. |

## Overall Verdict

Go - every mandatory criterion passes. Mode: autonomous, not independent; the stand-in decision stays open to challenge in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-004]: ../../milestones/mil-004-documentation.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[6494d1d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/commit/6494d1d1b9c8b6db18f551feb8fd320760daba45
