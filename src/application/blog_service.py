"""! @file blog_service.py
@brief The use cases of the blog: register, log in, read and manage posts, comment, contact.
"""
from application.dto import CommentDto, PostDto, UserDto
from application.ports import Clock, MailSender, PasswordHasher
from constants import ADMIN_USER_ID, CONTACT_SUBJECT
from domain.entities import Comment, Post, User
from domain.errors import (
    EmailAlreadyRegisteredError,
    InvalidCredentialsError,
    NotAuthorizedError,
    NotFoundError,
)
from domain.repositories import CommentRepository, PostRepository, UserRepository


def _user_dto(user: User) -> UserDto:
    """! @brief Maps a user entity to its DTO."""
    return UserDto(id=user.id, name=user.name, email=user.email, is_admin=user.id == ADMIN_USER_ID)


def _post_dto(post: Post) -> PostDto:
    """! @brief Maps a post entity to its DTO."""
    return PostDto(post.id, post.title, post.subtitle, post.date, post.body, post.img_url, post.author_name)


class BlogService:
    """! @brief Orchestrates the business rules; it depends only on contracts."""

    def __init__(
        self,
        users: UserRepository,
        posts: PostRepository,
        comments: CommentRepository,
        hasher: PasswordHasher,
        clock: Clock,
        mailer: MailSender,
    ) -> None:
        self._users = users
        self._posts = posts
        self._comments = comments
        self._hasher = hasher
        self._clock = clock
        self._mailer = mailer

    def register(self, email: str, password: str, name: str) -> UserDto:
        """! @brief Registers a user; the first registered user becomes the administrator."""
        if self._users.get_by_email(email) is not None:
            raise EmailAlreadyRegisteredError(email)
        user = self._users.add(User(email=email, name=name, password_hash=self._hasher.hash(password)))
        return _user_dto(user)

    def authenticate(self, email: str, password: str) -> UserDto:
        """! @brief Checks the credentials and returns the user."""
        user = self._users.get_by_email(email)
        if user is None or not self._hasher.verify(user.password_hash, password):
            raise InvalidCredentialsError()
        return _user_dto(user)

    def get_user(self, user_id: int) -> UserDto | None:
        """! @brief Returns the user with this id, or None."""
        user = self._users.get(user_id)
        return _user_dto(user) if user else None

    def get_all_posts(self) -> list[PostDto]:
        """! @brief Returns all posts."""
        return [_post_dto(p) for p in self._posts.list_all()]

    def get_post(self, post_id: int) -> PostDto:
        """! @brief Returns one post or raises NotFoundError."""
        return _post_dto(self._require_post(post_id))

    def add_new_post(self, actor: UserDto, title: str, subtitle: str, body: str, img_url: str) -> PostDto:
        """! @brief Creates a post; only the administrator may."""
        self._require_admin(actor)
        post = Post(title, subtitle, self._clock.today(), body, img_url, actor.id, actor.name)
        return _post_dto(self._posts.add(post))

    def edit_post(self, actor: UserDto, post_id: int, title: str, subtitle: str, body: str, img_url: str) -> PostDto:
        """! @brief Changes a post; only the administrator may."""
        self._require_admin(actor)
        post = self._require_post(post_id)
        post.title, post.subtitle, post.body, post.img_url = title, subtitle, body, img_url
        return _post_dto(self._posts.update(post))

    def delete_post(self, actor: UserDto, post_id: int) -> None:
        """! @brief Deletes a post; only the administrator may."""
        self._require_admin(actor)
        self._require_post(post_id)
        self._posts.delete(post_id)

    def comments_for(self, post_id: int) -> list[CommentDto]:
        """! @brief Returns the comments of a post."""
        return [CommentDto(c.id, c.text, c.author_name) for c in self._comments.list_for_post(post_id)]

    def add_comment(self, actor: UserDto, post_id: int, text: str) -> CommentDto:
        """! @brief Adds a comment of a logged-in user to an existing post."""
        self._require_post(post_id)
        saved = self._comments.add(Comment(text, actor.id, post_id, actor.name))
        return CommentDto(saved.id, saved.text, saved.author_name)

    def send_contact_message(self, name: str, email: str, phone: str, message: str) -> None:
        """! @brief Forwards the contact-form message to the owner."""
        self._mailer.send(CONTACT_SUBJECT, f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")

    def _require_post(self, post_id: int) -> Post:
        """! @brief Returns the post or raises NotFoundError."""
        post = self._posts.get(post_id)
        if post is None:
            raise NotFoundError(str(post_id))
        return post

    @staticmethod
    def _require_admin(actor: UserDto) -> None:
        """! @brief Raises NotAuthorizedError unless the actor is the administrator."""
        if not actor.is_admin:
            raise NotAuthorizedError()
