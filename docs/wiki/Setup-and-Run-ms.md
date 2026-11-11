# Persediaan dan jalankan

🌐 [English](Setup-and-Run) · [Dansk](Setup-and-Run-da) · **Bahasa Melayu**

Python 3.13 atau lebih baharu diperlukan.

Cipta dan aktifkan persekitaran maya setempat, naik taraf pip dan pasang:

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

Jalankan ujian:

```bash
python -m pytest
```

Jalankan blog secara setempat (pengguna pertama yang mendaftar ialah pentadbir):

```bash
export FLASK_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
python main.py
```

Jalankan blog dalam Docker dengan PostgreSQL:

```bash
cp .env.example .env.docker
docker compose --env-file .env.docker up --build
```

Senarai penuh tetapan ada dalam `.env.example` repositori.
