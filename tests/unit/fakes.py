"""! @file fakes.py
@brief In-memory fakes of the repository and port contracts for unit tests.
"""
from dataclasses import replace

from domain.entities import Comment, Post, User


class FakeUserRepository:
    """! @brief Users kept in a dict."""

    def __init__(self) -> None:
        self.items: dict[int, User] = {}

    def add(self, user: User) -> User:
        saved = replace(user, id=len(self.items) + 1)
        self.items[saved.id] = saved
        return saved

    def get(self, user_id: int) -> User | None:
        return self.items.get(user_id)

    def get_by_email(self, email: str) -> User | None:
        return next((u for u in self.items.values() if u.email == email), None)


class FakePostRepository:
    """! @brief Posts kept in a dict; also removes comments on delete like the real one."""

    def __init__(self, comments: "FakeCommentRepository | None" = None) -> None:
        self.items: dict[int, Post] = {}
        self._next_id = 1
        self._comments = comments

    def add(self, post: Post) -> Post:
        saved = replace(post, id=self._next_id)
        self._next_id += 1
        self.items[saved.id] = saved
        return saved

    def get(self, post_id: int) -> Post | None:
        return self.items.get(post_id)

    def list_all(self) -> list[Post]:
        return list(self.items.values())

    def update(self, post: Post) -> Post:
        self.items[post.id] = post
        return post

    def delete(self, post_id: int) -> None:
        self.items.pop(post_id, None)
        if self._comments is not None:
            self._comments.items = [c for c in self._comments.items if c.post_id != post_id]


class FakeCommentRepository:
    """! @brief Comments kept in a list."""

    def __init__(self) -> None:
        self.items: list[Comment] = []

    def add(self, comment: Comment) -> Comment:
        saved = replace(comment, id=len(self.items) + 1)
        self.items.append(saved)
        return saved

    def list_for_post(self, post_id: int) -> list[Comment]:
        return [c for c in self.items if c.post_id == post_id]


class FakeHasher:
    """! @brief Reversible fake hash so tests can see that plain text is never stored."""

    def hash(self, password: str) -> str:
        return f"hashed::{password[::-1]}"

    def verify(self, password_hash: str, password: str) -> bool:
        return password_hash == self.hash(password)


class FakeClock:
    """! @brief Clock with a fixed date."""

    def today(self) -> str:
        return "January 02, 2026"


class FakeMailer:
    """! @brief Remembers the messages it was asked to send."""

    def __init__(self) -> None:
        self.sent: list[tuple[str, str]] = []

    def send(self, subject: str, body: str) -> None:
        self.sent.append((subject, body))
