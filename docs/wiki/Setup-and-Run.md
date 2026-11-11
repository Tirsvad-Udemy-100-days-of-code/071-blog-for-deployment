# Setup and run

🌐 **English** · [Dansk](Setup-and-Run-da) · [Bahasa Melayu](Setup-and-Run-ms)

Python 3.13 or newer is needed.

Create and activate a local virtual environment, upgrade pip, install:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the tests:

```bash
python -m pytest
```

Run the blog locally (the first registered user is the administrator):

```bash
export FLASK_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
python main.py
```

Run the blog in Docker with PostgreSQL:

```bash
cp .env.example .env.docker
docker compose --env-file .env.docker up --build
```

The full list of settings is in `.env.example` of the repository.
