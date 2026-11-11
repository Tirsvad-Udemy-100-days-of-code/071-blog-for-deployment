"""! @file main.py
@brief WSGI entry point (gunicorn main:app).
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from infrastructure.config import load_settings  # noqa: E402  (needs src on sys.path)
from presentation import create_app  # noqa: E402

app = create_app(load_settings(os.environ))

if __name__ == "__main__":
    app.run(debug=False)
