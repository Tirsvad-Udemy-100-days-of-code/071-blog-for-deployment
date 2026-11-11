"""! @file repositories.py
@brief SQLAlchemy implementations of the domain repository contracts.
"""
from sqlalchemy import select
from sqlalchemy.orm import Session, scoped_session

from domain.entities import Comment, Post, User
from infrastructure.models import CommentModel, PostModel, UserModel

SessionLike = Session | scoped_session[Session]


def _to_user(row: UserModel) -> User:
    """! @brief Maps a user row to an entity."""
    return User(email=row.email, name=row.name, password_hash=row.password_hash, id=row.id)


def _to_post(row: PostModel) -> Post:
    """! @brief Maps a post row to an entity, filling the author name."""
    return Post(
        title=row.title,
        subtitle=row.subtitle,
        date=row.date,
        body=row.body,
        img_url=row.img_url,
        author_id=row.author_id,
        author_name=row.author.name,
        id=row.id,
    )


def _to_comment(row: CommentModel) -> Comment:
    """! @brief Maps a comment row to an entity, filling the author name."""
    return Comment(
        text=row.text, author_id=row.author_id, post_id=row.post_id, author_name=row.author.name, id=row.id
    )


class SqlUserRepository:
    """! @brief Stores users in the users table."""

    def __init__(self, session: SessionLike) -> None:
        self._session = session

    def add(self, user: User) -> User:
        """! @brief Stores a new user and returns it with its id."""
        row = UserModel(email=user.email, name=user.name, password_hash=user.password_hash)
        self._session.add(row)
        self._session.commit()
        return _to_user(row)

    def get(self, user_id: int) -> User | None:
        """! @brief Returns the user with this id, or None."""
        row = self._session.get(UserModel, user_id)
        return _to_user(row) if row else None

    def get_by_email(self, email: str) -> User | None:
        """! @brief Returns the user with this email address, or None."""
        row = self._session.scalar(select(UserModel).where(UserModel.email == email))
        return _to_user(row) if row else None


class SqlPostRepository:
    """! @brief Stores posts in the blog_posts table."""

    def __init__(self, session: SessionLike) -> None:
        self._session = session

    def add(self, post: Post) -> Post:
        """! @brief Stores a new post and returns it with its id."""
        row = PostModel(
            title=post.title,
            subtitle=post.subtitle,
            date=post.date,
            body=post.body,
            img_url=post.img_url,
            author_id=post.author_id,
        )
        self._session.add(row)
        self._session.commit()
        return _to_post(row)

    def get(self, post_id: int) -> Post | None:
        """! @brief Returns the post with this id, or None."""
        row = self._session.get(PostModel, post_id)
        return _to_post(row) if row else None

    def list_all(self) -> list[Post]:
        """! @brief Returns all posts, oldest first."""
        rows = self._session.scalars(select(PostModel).order_by(PostModel.id)).all()
        return [_to_post(row) for row in rows]

    def update(self, post: Post) -> Post:
        """! @brief Saves the changes of an existing post."""
        row = self._session.get(PostModel, post.id)
        if row is None:
            raise LookupError(f"post {post.id} does not exist")
        row.title, row.subtitle, row.body, row.img_url = post.title, post.subtitle, post.body, post.img_url
        self._session.commit()
        return _to_post(row)

    def delete(self, post_id: int) -> None:
        """! @brief Removes a post and its comments."""
        row = self._session.get(PostModel, post_id)
        if row is not None:
            self._session.delete(row)
            self._session.commit()


class SqlCommentRepository:
    """! @brief Stores comments in the comments table."""

    def __init__(self, session: SessionLike) -> None:
        self._session = session

    def add(self, comment: Comment) -> Comment:
        """! @brief Stores a new comment and returns it with its id."""
        row = CommentModel(text=comment.text, author_id=comment.author_id, post_id=comment.post_id)
        self._session.add(row)
        self._session.commit()
        return _to_comment(row)

    def list_for_post(self, post_id: int) -> list[Comment]:
        """! @brief Returns the comments of a post, oldest first."""
        stmt = select(CommentModel).where(CommentModel.post_id == post_id).order_by(CommentModel.id)
        return [_to_comment(row) for row in self._session.scalars(stmt).all()]
