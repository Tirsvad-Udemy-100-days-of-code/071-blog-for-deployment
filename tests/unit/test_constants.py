"""! @file test_constants.py
@brief Checks the constants module.
"""
import constants


def test_admin_is_first_user():
    assert constants.ADMIN_USER_ID == 1


def test_default_database_is_sqlite():
    assert constants.DEFAULT_DB_URI.startswith("sqlite:///")
