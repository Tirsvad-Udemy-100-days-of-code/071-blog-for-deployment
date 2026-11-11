# 🚀 Blog for deployment

Day 71 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*: a Flask blog prepared for deployment with environment variables, gunicorn, PostgreSQL and Docker. It is written for course participants and visitors who want a readable, runnable reference.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The repository follows the lecture "Learn to Deploy Your Website": put the project under version control, move secrets into environment variables, serve the app with gunicorn through a `Procfile`, and replace SQLite with PostgreSQL. Heroku has no free plan, so the deployment target is a Docker container.

| Path | Purpose |
| --- | --- |
| `src/` | The Flask application in layers: `domain`, `application`, `infrastructure`, `presentation`, plus `constants.py` |
| `main.py` | WSGI entry point, `gunicorn main:app` |
| `tests/` | pytest suite |
| `docs/` | Project documents, wiki sources and screenshots |
| `Doxyfile` | Doxygen configuration for the source comments |

## 📋 Requirements

- Python 3.13 or newer (the language of the course project).
- `git` to clone the repository.
- Docker, only for the container deployment.
- Optional: Doxygen to build the source documentation.

## 🛠️ Setup

Create a local virtual environment in `.venv`, upgrade pip, and install the project.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## ▶️ Run

The app reads its settings from environment variables (see `.env.example`):

| Variable | Meaning |
| --- | --- |
| `FLASK_KEY` | Secret key for sessions (required) |
| `DB_URI` | Database URI; default `sqlite:///posts.db`. `postgres://` and `postgresql://` are accepted and used with psycopg 3 |
| `MAIL_USER`, `MAIL_PASSWORD` | Optional sender of the contact form |

Local run (SQLite), with the venv active:

```bash
export FLASK_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
python main.py
```

On Windows PowerShell use `$env:FLASK_KEY = (python -c "import secrets; print(secrets.token_hex(32))")`. The first registered user is the administrator and can write posts.

Production style run with gunicorn (Linux, as in the `Procfile`: `web: gunicorn main:app`):

```bash
gunicorn main:app
```

Docker with PostgreSQL (the free replacement for Heroku):

```bash
cp .env.example .env.docker      # then edit the two secrets
docker compose --env-file .env.docker up --build
```

The blog is then on <http://localhost:8000>. `psycopg` is installed next to the lecture's `psycopg-binary`, because the binary package alone does not contain the `psycopg` module.

## 🧪 Tests

```bash
python -m pytest
```

Static scan before every push (the project uses opengrep):

```bash
~/.opengrep/cli/latest/opengrep.exe scan --config auto --exclude framework --exclude .venv --error .
```

## 📄 License

See [LICENSE](./LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
