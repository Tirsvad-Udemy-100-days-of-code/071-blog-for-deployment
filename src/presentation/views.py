"""! @file views.py
@brief HTTP views of the blog; they call the BlogService and pass DTOs to templates.
"""
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar, cast

from flask import Blueprint, abort, current_app, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.wrappers import Response

from application.blog_service import BlogService
from application.dto import PostDto, UserDto
from constants import (
    BLOG_SERVICE_KEY,
    DEFAULT_POST_IMAGE,
    HTTP_FORBIDDEN,
    HTTP_NOT_FOUND,
    MSG_BAD_CREDENTIALS,
    MSG_EMAIL_TAKEN,
    MSG_LOGIN_REQUIRED,
    MSG_MESSAGE_SENT,
)
from domain.errors import EmailAlreadyRegisteredError, InvalidCredentialsError, NotAuthorizedError, NotFoundError
from presentation.forms import CommentForm, ContactForm, LoginForm, PostForm, RegisterForm
from presentation.login_user import LoginUser
from presentation.sanitizer import sanitize_html

blog = Blueprint("blog", __name__)

P = ParamSpec("P")
R = TypeVar("R")


def _service() -> BlogService:
    """! @brief Returns the BlogService wired by the composition root."""
    return cast(BlogService, current_app.extensions[BLOG_SERVICE_KEY])


def _actor() -> UserDto:
    """! @brief Returns the application-layer view of the logged-in user."""
    return cast(LoginUser, current_user).dto


def admin_only(view: Callable[P, R]) -> Callable[P, R]:
    """! @brief Answers 403 unless the current user is the administrator."""

    @wraps(view)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        if not getattr(current_user, "is_admin", False):
            abort(HTTP_FORBIDDEN)
        return view(*args, **kwargs)

    return wrapper


def _post_or_404(post_id: int) -> PostDto:
    """! @brief Returns the post or answers 404."""
    try:
        return _service().get_post(post_id)
    except NotFoundError:
        abort(HTTP_NOT_FOUND)


@blog.route("/")
def get_all_posts() -> str:
    """! @brief Home page listing every post."""
    return render_template("index.html", all_posts=_service().get_all_posts(), default_image=DEFAULT_POST_IMAGE)


@blog.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id: int) -> str | Response:
    """! @brief Shows a post with its comments; logged-in users may comment."""
    post = _post_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash(MSG_LOGIN_REQUIRED)
            return redirect(url_for("blog.login"))
        _service().add_comment(_actor(), post_id, sanitize_html(form.comment_text.data or ""))
        return redirect(url_for("blog.show_post", post_id=post_id))
    return render_template(
        "post.html",
        post=post,
        form=form,
        comments=_service().comments_for(post_id),
        default_image=DEFAULT_POST_IMAGE,
    )


@blog.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post() -> str | Response:
    """! @brief Creates a post (administrator only)."""
    form = PostForm()
    if form.validate_on_submit():
        _service().add_new_post(
            _actor(),
            form.title.data or "",
            form.subtitle.data or "",
            sanitize_html(form.body.data or ""),
            form.img_url.data or DEFAULT_POST_IMAGE,
        )
        return redirect(url_for("blog.get_all_posts"))
    return render_template("make-post.html", form=form, is_edit=False)


@blog.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id: int) -> str | Response:
    """! @brief Edits a post (administrator only)."""
    post = _post_or_404(post_id)
    form = PostForm(title=post.title, subtitle=post.subtitle, img_url=post.img_url, body=post.body)
    if form.validate_on_submit():
        try:
            _service().edit_post(
                _actor(),
                post_id,
                form.title.data or "",
                form.subtitle.data or "",
                sanitize_html(form.body.data or ""),
                form.img_url.data or DEFAULT_POST_IMAGE,
            )
        except NotAuthorizedError:
            abort(HTTP_FORBIDDEN)
        return redirect(url_for("blog.show_post", post_id=post_id))
    return render_template("make-post.html", form=form, is_edit=True)


@blog.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id: int) -> Response:
    """! @brief Deletes a post and its comments (administrator only)."""
    try:
        _service().delete_post(_actor(), post_id)
    except NotFoundError:
        abort(HTTP_NOT_FOUND)
    return redirect(url_for("blog.get_all_posts"))


@blog.route("/about")
def about() -> str:
    """! @brief About page."""
    return render_template("about.html")


@blog.route("/contact", methods=["GET", "POST"])
def contact() -> str:
    """! @brief Contact page; a valid submission is mailed to the owner."""
    form = ContactForm()
    if form.validate_on_submit():
        _service().send_contact_message(
            form.name.data or "", form.email.data or "", form.phone.data or "", form.message.data or ""
        )
        flash(MSG_MESSAGE_SENT)
    return render_template("contact.html", form=form)


@blog.route("/register", methods=["GET", "POST"])
def register() -> str | Response:
    """! @brief Registers a user and logs them in."""
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = _service().register(form.email.data or "", form.password.data or "", form.name.data or "")
        except EmailAlreadyRegisteredError:
            flash(MSG_EMAIL_TAKEN)
            return redirect(url_for("blog.login"))
        login_user(LoginUser(user))
        return redirect(url_for("blog.get_all_posts"))
    return render_template("register.html", form=form)


@blog.route("/login", methods=["GET", "POST"])
def login() -> str | Response:
    """! @brief Logs a user in."""
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = _service().authenticate(form.email.data or "", form.password.data or "")
        except InvalidCredentialsError:
            flash(MSG_BAD_CREDENTIALS)
        else:
            login_user(LoginUser(user))
            return redirect(url_for("blog.get_all_posts"))
    return render_template("login.html", form=form)


@blog.route("/logout")
def logout() -> Response:
    """! @brief Logs the current user out."""
    logout_user()
    return redirect(url_for("blog.get_all_posts"))
