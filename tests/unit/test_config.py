"""! @file test_config.py
@brief Unit tests of the environment-based settings.
"""
import pytest

from constants import DEFAULT_DB_URI
from infrastructure.config import ConfigurationError, load_settings, normalize_db_uri

KEY = "a-secret"


@pytest.mark.parametrize(
    ("uri", "expected"),
    [
        ("postgres://u:p@host:5432/db", "postgresql+psycopg://u:p@host:5432/db"),
        ("postgresql://u:p@host/db", "postgresql+psycopg://u:p@host/db"),
        ("postgresql+psycopg://u:p@host/db", "postgresql+psycopg://u:p@host/db"),
        ("sqlite:///posts.db", "sqlite:///posts.db"),
    ],
)
def test_normalize_db_uri_maps_driverless_postgres_only(uri: str, expected: str) -> None:
    assert normalize_db_uri(uri) == expected


def test_load_settings_defaults_to_sqlite() -> None:
    settings = load_settings({"FLASK_KEY": KEY})
    assert settings["SQLALCHEMY_DATABASE_URI"] == DEFAULT_DB_URI
    assert settings["SECRET_KEY"] == KEY


def test_load_settings_normalizes_db_uri() -> None:
    settings = load_settings({"FLASK_KEY": KEY, "DB_URI": "postgres://h/db"})
    assert settings["SQLALCHEMY_DATABASE_URI"] == "postgresql+psycopg://h/db"


@pytest.mark.parametrize("environ", [{}, {"FLASK_KEY": ""}])
def test_load_settings_raises_when_secret_key_missing(environ: dict[str, str]) -> None:
    with pytest.raises(ConfigurationError):
        load_settings(environ)


def test_load_settings_omits_mail_keys_when_absent() -> None:
    settings = load_settings({"FLASK_KEY": KEY})
    assert "MAIL_USER" not in settings
    assert "MAIL_PASSWORD" not in settings


def test_load_settings_includes_mail_keys_when_present() -> None:
    settings = load_settings({"FLASK_KEY": KEY, "MAIL_USER": "me@example.com", "MAIL_PASSWORD": "pw"})
    assert settings["MAIL_USER"] == "me@example.com"
    assert settings["MAIL_PASSWORD"] == "pw"


def test_load_settings_secret_is_never_hard_coded() -> None:
    first = load_settings({"FLASK_KEY": "one"})["SECRET_KEY"]
    second = load_settings({"FLASK_KEY": "two"})["SECRET_KEY"]
    assert (first, second) == ("one", "two")
