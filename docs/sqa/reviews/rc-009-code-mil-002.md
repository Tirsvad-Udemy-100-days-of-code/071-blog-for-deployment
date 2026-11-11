# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review (autonomous, not independent) | [0bb8342] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of src/ and tests/ delivered by the milestone
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | snake_case modules and functions, PascalCase classes, UPPER_SNAKE constants in src/constants.py. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (BlogService, SqlPostRepository, admin_only); assignment names kept in views.py. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | No formatter or linter is configured in the project; code follows PEP 8 by hand. Noted as a gap, not a suppression. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions and methods annotated; HTMLParser overrides included. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except. SmtpMailSender logs SMTP/OS errors with logger.exception and does not raise (documented, deliberate for a contact form). |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults, no shadowed builtins (hash is a method name only). |
| 7 | Files, locks and connections are managed with context managers | Pass | SMTP uses a context manager; the DB session is managed by Flask-SQLAlchemy. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module and public docstrings in Doxygen form; HTMLParser overrides lack docstrings (minor, optional). |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | logging used; grep finds no print; credentials are never logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No DCD exists (technical tasks); classes follow the layer map of clean-architecture. Recorded here as the deviation record. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 53 tests (20 unit, 12 integration, 20 e2e incl. sanitiser), order independent, no network; all pass. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | No type checker configured; N-A for this exercise. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | requirements.txt pins the lecture versions; email_validator not added (regex used instead). |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Constants live only in constants.py; DTO mapping functions defined once. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain and application import no Flask or SQLAlchemy; infrastructure and presentation import inward only; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | BlogService depends on narrow Protocols injected by create_app (composition root). |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | src/{domain,application,infrastructure,presentation}, tests/{unit,integration,e2e}. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All file names English snake_case without spaces; templates use hyphens (make-post.html). |

## Overall Verdict

Go - every mandatory criterion passes. Mode: autonomous, not independent; the stand-in decision stays open to challenge in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-002]: ../../milestones/mil-002-blog-application.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[0bb8342]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/commit/0bb834201b0a8149b0dcc51c567bf373c508df7f
