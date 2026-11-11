"""! @file ports.py
@brief Contracts for services outside the business: hashing, time and mail.
"""
from typing import Protocol


class PasswordHasher(Protocol):
    """! @brief Hashes and verifies passwords."""

    def hash(self, password: str) -> str:
        """! @brief Returns a salted hash of the password."""
        ...

    def verify(self, password_hash: str, password: str) -> bool:
        """! @brief Tells whether the password matches the hash."""
        ...


class Clock(Protocol):
    """! @brief Supplies the display date of a new post."""

    def today(self) -> str:
        """! @brief Returns today's date formatted for display."""
        ...


class MailSender(Protocol):
    """! @brief Sends the contact-form message to the blog owner."""

    def send(self, subject: str, body: str) -> None:
        """! @brief Sends one message."""
        ...
