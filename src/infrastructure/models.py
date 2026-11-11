"""! @file models.py
@brief Persistence models (tables users, blog_posts, comments); mapped to domain entities by the repositories.
"""
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database import Base


class UserModel(Base):
    """! @brief Row of the users table."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(100))


class PostModel(Base):
    """! @brief Row of the blog_posts table; deleting it deletes its comments."""

    __tablename__ = "blog_posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    subtitle: Mapped[str] = mapped_column(String(250))
    date: Mapped[str] = mapped_column(String(250))
    body: Mapped[str] = mapped_column(Text)
    img_url: Mapped[str] = mapped_column(String(500))
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[UserModel] = relationship()
    comments: Mapped[list["CommentModel"]] = relationship(
        back_populates="post", cascade="all, delete-orphan", order_by="CommentModel.id"
    )


class CommentModel(Base):
    """! @brief Row of the comments table."""

    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"))
    author: Mapped[UserModel] = relationship()
    post: Mapped[PostModel] = relationship(back_populates="comments")
