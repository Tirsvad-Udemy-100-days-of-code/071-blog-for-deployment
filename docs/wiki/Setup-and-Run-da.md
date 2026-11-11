# Opsætning og kørsel

🌐 [English](Setup-and-Run) · **Dansk** · [Bahasa Melayu](Setup-and-Run-ms)

Python 3.13 eller nyere er nødvendig.

Opret og aktivér et lokalt virtuelt miljø, opgradér pip og installér:

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

Kør testene:

```bash
python -m pytest
```

Kør bloggen lokalt (den første oprettede bruger er administrator):

```bash
export FLASK_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
python main.py
```

Kør bloggen i Docker med PostgreSQL:

```bash
cp .env.example .env.docker
docker compose --env-file .env.docker up --build
```

Den fulde liste over indstillinger står i `.env.example` i repositoriet.
