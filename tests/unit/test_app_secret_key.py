"""! @file test_app_secret_key.py
@brief Tests that create_app refuses to start without a secret key and that no key is hard-coded in src/.
"""
from pathlib import Path

import pytest
from app_config import TEST_CONFIG

from infrastructure.config import ConfigurationError
from presentation import create_app

SRC_DIR = Path(__file__).resolve().parents[2] / "src"


def test_create_app_raises_without_config() -> None:
    with pytest.raises(ConfigurationError):
        create_app()


def test_create_app_raises_with_empty_secret_key() -> None:
    with pytest.raises(ConfigurationError):
        create_app({"SECRET_KEY": ""})


def test_create_app_raises_with_config_lacking_secret_key() -> None:
    with pytest.raises(ConfigurationError):
        create_app({"TESTING": True})


def test_create_app_uses_given_secret_key() -> None:
    app = create_app({**TEST_CONFIG, "TESTING": True})
    assert app.config["SECRET_KEY"] == TEST_CONFIG["SECRET_KEY"]


def test_src_has_no_hard_coded_dev_secret_key() -> None:
    offenders = [p for p in SRC_DIR.rglob("*.py") if "dev-only-secret-key" in p.read_text(encoding="utf-8")]
    assert offenders == []
