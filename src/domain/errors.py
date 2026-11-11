"""! @file errors.py
@brief Errors raised by the business rules of the blog.
"""


class BlogError(Exception):
    """! @brief Base class of all business errors."""


class NotFoundError(BlogError):
    """! @brief The requested post or user does not exist."""


class EmailAlreadyRegisteredError(BlogError):
    """! @brief A user with this email address already exists."""


class InvalidCredentialsError(BlogError):
    """! @brief Email or password is wrong."""


class NotAuthorizedError(BlogError):
    """! @brief The user may not perform this action."""
