"""! @file app_config.py
@brief Shared test configuration for create_app; the key is a test value, never used outside tests.
"""
from typing import Any

## Config every create_app call in the tests starts from.
TEST_CONFIG: dict[str, Any] = {"SECRET_KEY": "test-only-key"}
