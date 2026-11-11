"""! @file repositories.py
@brief Storage contracts the business rules need; implemented in infrastructure.
"""
from typing import Optional, Protocol

from domain.entities import Comment, Post, User


class UserRepository(Protocol):
    """! @brief Storage of users."""

    def add(self, user: User) -> User:
        """! @brief Stores a new user and returns it with its id."""
        ...

    def get(self, user_id: int) -> Optional[User]:
        """! @brief Returns the user with this id, or None."""
        ...

    def get_by_email(self, email: str) -> Optional[User]:
        """! @brief Returns the user with this email address, or None."""
        ...


class PostRepository(Protocol):
    """! @brief Storage of posts."""

    def add(self, post: Post) -> Post:
        """! @brief Stores a new post and returns it with its id."""
        ...

    def get(self, post_id: int) -> Optional[Post]:
        """! @brief Returns the post with this id, or None."""
        ...

    def list_all(self) -> list[Post]:
        """! @brief Returns all posts, oldest first."""
        ...

    def update(self, post: Post) -> Post:
        """! @brief Saves the changes of an existing post."""
        ...

    def delete(self, post_id: int) -> None:
        """! @brief Removes a post and its comments."""
        ...


class CommentRepository(Protocol):
    """! @brief Storage of comments."""

    def add(self, comment: Comment) -> Comment:
        """! @brief Stores a new comment and returns it with its id."""
        ...

    def list_for_post(self, post_id: int) -> list[Comment]:
        """! @brief Returns the comments of a post, oldest first."""
        ...
