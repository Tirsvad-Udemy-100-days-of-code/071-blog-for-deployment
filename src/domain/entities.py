"""! @file entities.py
@brief Plain business entities; they know nothing about frameworks or databases.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """! @brief A registered blog user."""

    email: str
    name: str
    password_hash: str
    id: Optional[int] = None


@dataclass
class Post:
    """! @brief A blog post written by the administrator."""

    title: str
    subtitle: str
    date: str
    body: str
    img_url: str
    author_id: int
    author_name: str = ""
    id: Optional[int] = None


@dataclass
class Comment:
    """! @brief A comment of a user on a post."""

    text: str
    author_id: int
    post_id: int
    author_name: str = ""
    id: Optional[int] = None
