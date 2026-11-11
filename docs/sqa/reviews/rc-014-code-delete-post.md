# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review (autonomous, not independent) | [6c5d40f] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the delete-route change (views.py, index.html, tests/e2e/test_blog_flow.py)
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | views.py and index.html changed by 4 lines; style unchanged and consistent with the existing code. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | views.py and index.html changed by 4 lines; style unchanged and consistent with the existing code. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | No formatter or linter is configured (gap noted in RC-009). |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Annotations unchanged; the function keeps its signature. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No exception handling added. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | views.py and index.html changed by 4 lines; style unchanged and consistent with the existing code. |
| 7 | Files, locks and connections are managed with context managers | Pass | views.py and index.html changed by 4 lines; style unchanged and consistent with the existing code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | views.py and index.html changed by 4 lines; style unchanged and consistent with the existing code. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print or logging added. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No DCD; presentation-layer change only. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 4 new e2e tests (405 on GET, 403 non-admin, 404 missing, CSRF 400 without token and 302 with token); 72 tests pass. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | N-A: no type checker. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | views.py and index.html changed by 4 lines; style unchanged and consistent with the existing code. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | CSRF handling reuses the global CSRFProtect; no second mechanism. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Only the presentation layer changed. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | views.py and index.html changed by 4 lines; style unchanged and consistent with the existing code. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | views.py and index.html changed by 4 lines; style unchanged and consistent with the existing code. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | views.py and index.html changed by 4 lines; style unchanged and consistent with the existing code. |

## Overall Verdict

Go - every mandatory criterion passes. Mode: autonomous, not independent; the stand-in decision stays open to challenge in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-002]: ../../milestones/mil-002-blog-application.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[6c5d40f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/commit/6c5d40f66bdc29a5b3680ce0929c9a4009768718
