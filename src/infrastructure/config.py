"""! @file config.py
@brief Reads the deployment settings from environment variables into the app config.
"""
from collections.abc import Mapping
from typing import Any

from constants import (
    CONFIG_DB_URI,
    CONFIG_MAIL_PASSWORD,
    CONFIG_MAIL_USER,
    CONFIG_SECRET_KEY,
    DB_SCHEME_POSTGRES,
    DB_SCHEME_POSTGRESQL,
    DB_SCHEME_POSTGRESQL_PSYCOPG,
    DEFAULT_DB_URI,
    ENV_DB_URI,
    ENV_MAIL_PASSWORD,
    ENV_MAIL_USER,
    ENV_SECRET_KEY,
    MSG_SECRET_KEY_MISSING,
)


class ConfigurationError(Exception):
    """! @brief A required deployment setting is missing (an environment concern, not a business rule)."""


def normalize_db_uri(uri: str) -> str:
    """! @brief Maps a driverless PostgreSQL URI to the psycopg 3 driver; other URIs are unchanged."""
    for scheme in (DB_SCHEME_POSTGRES, DB_SCHEME_POSTGRESQL):
        if uri.startswith(scheme):
            return DB_SCHEME_POSTGRESQL_PSYCOPG + uri[len(scheme):]
    return uri


def load_settings(environ: Mapping[str, str]) -> dict[str, Any]:
    """! @brief Builds the create_app config from the environment; raises ConfigurationError without a secret key."""
    secret_key = environ.get(ENV_SECRET_KEY)
    if not secret_key:
        raise ConfigurationError(MSG_SECRET_KEY_MISSING)
    settings: dict[str, Any] = {
        CONFIG_SECRET_KEY: secret_key,
        CONFIG_DB_URI: normalize_db_uri(environ.get(ENV_DB_URI) or DEFAULT_DB_URI),
    }
    for env_name, config_key in ((ENV_MAIL_USER, CONFIG_MAIL_USER), (ENV_MAIL_PASSWORD, CONFIG_MAIL_PASSWORD)):
        value = environ.get(env_name)
        if value:
            settings[config_key] = value
    return settings
