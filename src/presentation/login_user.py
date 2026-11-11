"""! @file login_user.py
@brief Adapter that lets Flask-Login work with the application's UserDto.
"""
from flask_login import UserMixin

from application.dto import UserDto


class LoginUser(UserMixin):
    """! @brief The logged-in user as Flask-Login sees it."""

    def __init__(self, dto: UserDto) -> None:
        self._dto = dto

    def get_id(self) -> str:
        """! @brief Returns the id Flask-Login stores in the session."""
        return str(self._dto.id)

    @property
    def name(self) -> str:
        """! @brief Display name of the user."""
        return self._dto.name

    @property
    def is_admin(self) -> bool:
        """! @brief Tells whether the user is the blog administrator."""
        return self._dto.is_admin

    @property
    def dto(self) -> UserDto:
        """! @brief The application-layer view of the user."""
        return self._dto
