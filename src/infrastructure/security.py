"""! @file security.py
@brief Password hashing adapter built on Werkzeug.
"""
from werkzeug.security import check_password_hash, generate_password_hash

from constants import PASSWORD_HASH_METHOD, PASSWORD_SALT_LENGTH


class WerkzeugPasswordHasher:
    """! @brief Salted pbkdf2 password hashing."""

    def hash(self, password: str) -> str:
        """! @brief Returns a salted hash of the password."""
        return generate_password_hash(password, method=PASSWORD_HASH_METHOD, salt_length=PASSWORD_SALT_LENGTH)

    def verify(self, password_hash: str, password: str) -> bool:
        """! @brief Tells whether the password matches the hash."""
        return check_password_hash(password_hash, password)
