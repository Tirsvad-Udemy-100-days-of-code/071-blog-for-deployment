"""! @file app.py
@brief Composition root: builds the Flask app and wires the adapters into the BlogService.
"""
from typing import Any

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_wtf import CSRFProtect

from application.blog_service import BlogService
from constants import (
    APP_TITLE,
    BLOG_SERVICE_KEY,
    CONFIG_DB_URI,
    CONFIG_MAIL_PASSWORD,
    CONFIG_MAIL_USER,
    CONFIG_SECRET_KEY,
    MSG_SECRET_KEY_MISSING,
    TEST_DB_URI,
)
from infrastructure.clock import SystemClock
from infrastructure.config import ConfigurationError
from infrastructure.database import db
from infrastructure.mail import SmtpMailSender
from infrastructure.repositories import SqlCommentRepository, SqlPostRepository, SqlUserRepository
from infrastructure.security import WerkzeugPasswordHasher
from presentation.login_user import LoginUser
from presentation.views import blog


def create_app(config: dict[str, Any] | None = None) -> Flask:
    """! @brief Creates a configured application; the config dict overrides the defaults.
    @throws ConfigurationError when the config has no non-empty SECRET_KEY.
    """
    app = Flask(__name__)
    app.config[CONFIG_DB_URI] = TEST_DB_URI
    app.config.update(config or {})
    if not app.config.get(CONFIG_SECRET_KEY):
        raise ConfigurationError(MSG_SECRET_KEY_MISSING)

    db.init_app(app)
    Bootstrap5(app)
    CKEditor(app)
    CSRFProtect(app)

    service = BlogService(
        users=SqlUserRepository(db.session),
        posts=SqlPostRepository(db.session),
        comments=SqlCommentRepository(db.session),
        hasher=WerkzeugPasswordHasher(),
        clock=SystemClock(),
        mailer=SmtpMailSender(app.config.get(CONFIG_MAIL_USER), app.config.get(CONFIG_MAIL_PASSWORD)),
    )
    app.extensions[BLOG_SERVICE_KEY] = service

    login_manager = LoginManager(app)
    login_manager.login_view = "blog.login"

    @login_manager.user_loader
    def load_user(user_id: str) -> LoginUser | None:
        dto = service.get_user(int(user_id))
        return LoginUser(dto) if dto else None

    @app.context_processor
    def inject_app_title() -> dict[str, str]:
        return {"app_title": APP_TITLE}

    app.register_blueprint(blog)
    with app.app_context():
        db.create_all()
    return app
