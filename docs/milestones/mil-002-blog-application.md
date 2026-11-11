# Blog application

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [8bad45b] |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 | Added task 6: make the delete route a POST (hardening requested in chat) | [6c5d40f] |

---

## Purpose

Decides whether the blog behaves as the lecture expects and is covered by tests before production configuration is added.

## Deliverable

A Flask application under `src/` with models, forms, routes, authentication, comments and admin-only editing, and a passing pytest suite.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Visitors can list and read posts, and add comments after logging in | pytest route tests pass | Criterion not met |
| 2 | Only the first registered user (admin) can create, edit and delete posts | Tests show 403 for other users | Criterion not met |
| 3 | Passwords are stored hashed | Test shows the stored value differs from the password | Criterion not met |
| 4 | All pytest tests pass | `python -m pytest` exit code 0 | Criterion not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The skeleton and configuration must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 and 4, success criterion 1 | [BC-001] |

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
| 1 | Create the data models | Define User, BlogPost and Comment with SQLAlchemy 2 typed mappings and the relationships between them; create tables on start. | No | |
| 2 | Create the forms | Add WTForms for register, login, comment and post (with CKEditor) with validation and CSRF protection. | No | |
| 3 | Implement authentication | Register, login and logout with Flask-Login and hashed passwords; the user with id 1 is the admin and an `admin_only` decorator guards editing. | No | |
| 4 | Implement the blog routes | Home, post page, add, edit, delete, about and contact routes with the assignment function names (`get_all_posts`, `show_post`, `add_new_post`, `edit_post`, `delete_post`, `about`, `contact`). | No | |
| 5 | Write the pytest suite | Cover models, auth, admin guard, post CRUD and comments using an in-memory SQLite database. | No | |
| 6 | Make the delete route a POST | Change `/delete/<id>` from GET to POST so a link or image on another site cannot delete a post; the index page uses a form with a CSRF token, and tests prove GET gives 405 and a POST without token gives 400. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[8bad45b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/commit/8bad45b22a1694dea060d3353738c8a1c65018a8
[6c5d40f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/commit/6c5d40f66bdc29a5b3680ce0929c9a4009768718
