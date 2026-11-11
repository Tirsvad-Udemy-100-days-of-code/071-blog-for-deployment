"""! @file test_main_entrypoint.py
@brief Integration tests of the WSGI entry point (main.py) and the Procfile.
"""
import importlib
import sys
from pathlib import Path

import pytest
from flask import Flask

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def main_app(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Flask:
    monkeypatch.setenv("FLASK_KEY", "test-secret")
    monkeypatch.setenv("DB_URI", f"sqlite:///{(tmp_path / 'posts.db').as_posix()}")
    monkeypatch.syspath_prepend(str(ROOT))
    monkeypatch.delitem(sys.modules, "main", raising=False)
    module = importlib.import_module("main")
    monkeypatch.delitem(sys.modules, "main", raising=False)
    app = module.app
    assert isinstance(app, Flask)
    return app


def test_main_exposes_app_with_debug_off(main_app: Flask) -> None:
    assert main_app.debug is False
    assert main_app.config["SECRET_KEY"] == "test-secret"


def test_main_app_serves_index(main_app: Flask) -> None:
    assert main_app.test_client().get("/").status_code == 200


def test_importing_main_without_secret_key_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    from infrastructure.config import ConfigurationError

    monkeypatch.delenv("FLASK_KEY", raising=False)
    monkeypatch.syspath_prepend(str(ROOT))
    monkeypatch.delitem(sys.modules, "main", raising=False)
    with pytest.raises(ConfigurationError):
        importlib.import_module("main")


def test_procfile_starts_gunicorn_on_main_app() -> None:
    assert (ROOT / "Procfile").read_text(encoding="utf-8").strip() == "web: gunicorn main:app"
