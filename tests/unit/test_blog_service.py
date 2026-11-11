"""! @file test_blog_service.py
@brief Unit tests of the BlogService use cases with in-memory fakes.
"""
import pytest
from fakes import (
    FakeClock,
    FakeCommentRepository,
    FakeHasher,
    FakeMailer,
    FakePostRepository,
    FakeUserRepository,
)

from application.blog_service import BlogService
from application.dto import UserDto
from domain.errors import (
    EmailAlreadyRegisteredError,
    InvalidCredentialsError,
    NotAuthorizedError,
    NotFoundError,
)


class Setup:
    """! @brief A service plus the fakes behind it."""

    def __init__(self) -> None:
        self.users = FakeUserRepository()
        self.comments = FakeCommentRepository()
        self.posts = FakePostRepository(self.comments)
        self.mailer = FakeMailer()
        self.service = BlogService(
            self.users, self.posts, self.comments, FakeHasher(), FakeClock(), self.mailer
        )


@pytest.fixture
def env() -> Setup:
    return Setup()


@pytest.fixture
def admin(env: Setup) -> UserDto:
    return env.service.register("admin@example.com", "secret", "Admin")


@pytest.fixture
def reader(env: Setup, admin: UserDto) -> UserDto:
    return env.service.register("reader@example.com", "pw", "Reader")


def test_register_makes_first_user_admin(admin: UserDto) -> None:
    assert admin.is_admin is True


def test_register_second_user_is_not_admin(reader: UserDto) -> None:
    assert reader.is_admin is False


def test_register_rejects_duplicate_email(env: Setup, admin: UserDto) -> None:
    with pytest.raises(EmailAlreadyRegisteredError):
        env.service.register("admin@example.com", "x", "Other")


def test_register_stores_password_hashed(env: Setup, admin: UserDto) -> None:
    stored = env.users.get(admin.id)
    assert stored is not None
    assert stored.password_hash != "secret"
    assert stored.password_hash == FakeHasher().hash("secret")


def test_authenticate_returns_user_for_correct_password(env: Setup, admin: UserDto) -> None:
    assert env.service.authenticate("admin@example.com", "secret") == admin


def test_authenticate_rejects_wrong_password(env: Setup, admin: UserDto) -> None:
    with pytest.raises(InvalidCredentialsError):
        env.service.authenticate("admin@example.com", "wrong")


def test_authenticate_rejects_unknown_email(env: Setup) -> None:
    with pytest.raises(InvalidCredentialsError):
        env.service.authenticate("nobody@example.com", "x")


def test_get_user_returns_none_for_unknown_id(env: Setup) -> None:
    assert env.service.get_user(99) is None


def test_add_new_post_by_admin_is_listed_with_date_and_author(env: Setup, admin: UserDto) -> None:
    post = env.service.add_new_post(admin, "T", "S", "<p>b</p>", "http://img")
    assert env.service.get_all_posts() == [post]
    assert (post.date, post.author_name) == ("January 02, 2026", "Admin")


def test_add_new_post_rejected_for_non_admin(env: Setup, reader: UserDto) -> None:
    with pytest.raises(NotAuthorizedError):
        env.service.add_new_post(reader, "T", "S", "b", "i")


def test_edit_post_changes_fields_for_admin(env: Setup, admin: UserDto) -> None:
    post = env.service.add_new_post(admin, "T", "S", "b", "i")
    edited = env.service.edit_post(admin, post.id, "T2", "S2", "b2", "i2")
    assert (edited.title, edited.subtitle, edited.body, edited.img_url) == ("T2", "S2", "b2", "i2")


def test_edit_post_rejected_for_non_admin(env: Setup, admin: UserDto, reader: UserDto) -> None:
    post = env.service.add_new_post(admin, "T", "S", "b", "i")
    with pytest.raises(NotAuthorizedError):
        env.service.edit_post(reader, post.id, "x", "x", "x", "x")


def test_edit_post_missing_raises_not_found(env: Setup, admin: UserDto) -> None:
    with pytest.raises(NotFoundError):
        env.service.edit_post(admin, 42, "x", "x", "x", "x")


def test_delete_post_rejected_for_non_admin(env: Setup, admin: UserDto, reader: UserDto) -> None:
    post = env.service.add_new_post(admin, "T", "S", "b", "i")
    with pytest.raises(NotAuthorizedError):
        env.service.delete_post(reader, post.id)
    assert len(env.service.get_all_posts()) == 1


def test_delete_post_removes_post_for_admin(env: Setup, admin: UserDto) -> None:
    post = env.service.add_new_post(admin, "T", "S", "b", "i")
    env.service.delete_post(admin, post.id)
    assert env.service.get_all_posts() == []


def test_delete_post_missing_raises_not_found(env: Setup, admin: UserDto) -> None:
    with pytest.raises(NotFoundError):
        env.service.delete_post(admin, 7)


def test_get_post_missing_raises_not_found(env: Setup) -> None:
    with pytest.raises(NotFoundError):
        env.service.get_post(1)


def test_add_comment_appears_in_comments_for_post(env: Setup, admin: UserDto, reader: UserDto) -> None:
    post = env.service.add_new_post(admin, "T", "S", "b", "i")
    env.service.add_comment(reader, post.id, "nice")
    assert [(c.text, c.author_name) for c in env.service.comments_for(post.id)] == [("nice", "Reader")]


def test_add_comment_on_missing_post_raises_not_found(env: Setup, reader: UserDto) -> None:
    with pytest.raises(NotFoundError):
        env.service.add_comment(reader, 5, "hi")


def test_send_contact_message_forwards_details_to_mailer(env: Setup) -> None:
    env.service.send_contact_message("Ann", "ann@example.com", "123", "Hello")
    (subject, body), = env.mailer.sent
    assert "Ann" in body and "ann@example.com" in body and "123" in body and "Hello" in body
    assert subject
