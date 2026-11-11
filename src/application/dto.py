"""! @file dto.py
@brief Data transfer objects that cross from the application to the presentation layer.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class UserDto:
    """! @brief A user as the presentation layer sees it."""

    id: int
    name: str
    email: str
    is_admin: bool


@dataclass(frozen=True)
class CommentDto:
    """! @brief A comment as the presentation layer sees it."""

    id: int
    text: str
    author_name: str


@dataclass(frozen=True)
class PostDto:
    """! @brief A post as the presentation layer sees it."""

    id: int
    title: str
    subtitle: str
    date: str
    body: str
    img_url: str
    author_name: str
