"""! @file test_sql_repositories.py
@brief Integration tests of the SQLAlchemy repositories, hasher and mail sender against in-memory SQLite.
"""
import logging
from collections.abc import Iterator

import pytest
from flask import Flask

from domain.entities import Comment, Post, User
from infrastructure.clock import SystemClock
from infrastructure.database import db
from infrastructure.mail import SmtpMailSender
from infrastructure.repositories import SqlCommentRepository, SqlPostRepository, SqlUserRepository
from infrastructure.security import WerkzeugPasswordHasher
from presentation import create_app


@pytest.fixture
def app() -> Iterator[Flask]:
    application = create_app({"TESTING": True})
    with application.app_context():
        yield application


@pytest.fixture
def seeded() -> tuple[SqlUserRepository, SqlPostRepository, SqlCommentRepository, int]:
    users = SqlUserRepository(db.session)
    user = users.add(User("a@example.com", "Ann", "hash"))
    return users, SqlPostRepository(db.session), SqlCommentRepository(db.session), user.id


def test_user_repository_roundtrip_by_id_and_email(app: Flask) -> None:
    users = SqlUserRepository(db.session)
    saved = users.add(User("a@example.com", "Ann", "hash"))
    assert saved.id == 1
    assert users.get(saved.id) == saved
    assert users.get_by_email("a@example.com") == saved


def test_user_repository_returns_none_when_missing(app: Flask) -> None:
    users = SqlUserRepository(db.session)
    assert users.get(5) is None
    assert users.get_by_email("none@example.com") is None


def test_post_repository_fills_author_name(app: Flask, seeded: tuple) -> None:
    _, posts, _, uid = seeded
    saved = posts.add(Post("T", "S", "D", "B", "I", uid))
    assert saved.author_name == "Ann"
    assert posts.get(saved.id) == saved
    assert posts.list_all() == [saved]


def test_post_repository_update_changes_fields(app: Flask, seeded: tuple) -> None:
    _, posts, _, uid = seeded
    saved = posts.add(Post("T", "S", "D", "B", "I", uid))
    saved.title, saved.body = "New", "NB"
    updated = posts.update(saved)
    assert (posts.get(saved.id).title, updated.body) == ("New", "NB")


def test_post_repository_update_missing_post_raises(app: Flask, seeded: tuple) -> None:
    _, posts, _, uid = seeded
    with pytest.raises(LookupError):
        posts.update(Post("T", "S", "D", "B", "I", uid, id=99))


def test_deleting_post_deletes_its_comments(app: Flask, seeded: tuple) -> None:
    _, posts, comments, uid = seeded
    post = posts.add(Post("T", "S", "D", "B", "I", uid))
    other = posts.add(Post("T2", "S", "D", "B", "I", uid))
    comments.add(Comment("c1", uid, post.id))
    comments.add(Comment("c2", uid, other.id))
    posts.delete(post.id)
    assert posts.get(post.id) is None
    assert comments.list_for_post(post.id) == []
    assert [c.text for c in comments.list_for_post(other.id)] == ["c2"]


def test_delete_missing_post_does_nothing(app: Flask, seeded: tuple) -> None:
    _, posts, _, _ = seeded
    posts.delete(123)
    assert posts.list_all() == []


def test_comment_repository_lists_oldest_first_with_author_name(app: Flask, seeded: tuple) -> None:
    _, posts, comments, uid = seeded
    post = posts.add(Post("T", "S", "D", "B", "I", uid))
    comments.add(Comment("first", uid, post.id))
    comments.add(Comment("second", uid, post.id))
    listed = comments.list_for_post(post.id)
    assert [(c.text, c.author_name) for c in listed] == [("first", "Ann"), ("second", "Ann")]


def test_hasher_hash_differs_from_password_and_verifies() -> None:
    hasher = WerkzeugPasswordHasher()
    hashed = hasher.hash("secret")
    assert hashed != "secret"
    assert hashed.startswith("pbkdf2:sha256")
    assert hasher.verify(hashed, "secret") is True
    assert hasher.verify(hashed, "other") is False


def test_hasher_uses_new_salt_each_time() -> None:
    hasher = WerkzeugPasswordHasher()
    assert hasher.hash("secret") != hasher.hash("secret")


def test_system_clock_returns_formatted_date() -> None:
    assert len(SystemClock().today().split()) == 3


def test_mail_sender_without_credentials_logs_warning_and_sends_nothing(
    caplog: pytest.LogCaptureFixture,
) -> None:
    with caplog.at_level(logging.WARNING):
        SmtpMailSender(None, None).send("s", "b")
    assert "not configured" in caplog.text
