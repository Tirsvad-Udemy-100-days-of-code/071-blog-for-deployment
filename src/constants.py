"""! @file constants.py
@brief All constants of the blog; no other module defines magic values.
"""

## Name of the environment variable that holds the Flask secret key.
ENV_SECRET_KEY = "FLASK_KEY"
## Name of the environment variable that holds the database URI.
ENV_DB_URI = "DB_URI"
## Name of the environment variable that holds the contact-form sender address.
ENV_MAIL_USER = "MAIL_USER"
## Name of the environment variable that holds the contact-form sender password.
ENV_MAIL_PASSWORD = "MAIL_PASSWORD"
## Local development database used when DB_URI is not set.
DEFAULT_DB_URI = "sqlite:///posts.db"
## Id of the user who is the blog administrator (the first registered user).
ADMIN_USER_ID = 1
## Application title shown in the page header.
APP_TITLE = "Blog for deployment"
## Subject of the e-mail sent from the contact form.
CONTACT_SUBJECT = "New message from the blog"
## Date format used for the display date of a post.
POST_DATE_FORMAT = "%B %d, %Y"
## Image used when a post has no image address.
DEFAULT_POST_IMAGE = "https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=1200"
## Password hashing method.
PASSWORD_HASH_METHOD = "pbkdf2:sha256"
## Length of the random salt of a password hash.
PASSWORD_SALT_LENGTH = 8
## SMTP server used for the contact form.
SMTP_HOST = "smtp.gmail.com"
## SMTP-over-SSL port.
SMTP_PORT = 465
## Database used by the app factory when its config gives none.
TEST_DB_URI = "sqlite:///:memory:"
## Secret key used when the config gives none (development and tests only).
DEV_SECRET_KEY = "dev-only-secret-key"
## Flask config keys read by the app factory.
CONFIG_SECRET_KEY = "SECRET_KEY"
CONFIG_DB_URI = "SQLALCHEMY_DATABASE_URI"
CONFIG_MAIL_USER = "MAIL_USER"
CONFIG_MAIL_PASSWORD = "MAIL_PASSWORD"
## Key under which the BlogService is stored in app.extensions.
BLOG_SERVICE_KEY = "blog_service"
## HTTP status codes used by the views.
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
## Tags allowed in the HTML body of a post.
ALLOWED_TAGS = frozenset(
    {"p", "br", "strong", "b", "em", "i", "u", "s", "ul", "ol", "li", "blockquote",
     "h1", "h2", "h3", "h4", "a", "img", "pre", "code", "span", "div", "hr"}
)
## Attributes allowed on those tags.
ALLOWED_ATTRIBUTES = frozenset({"href", "src", "alt", "title"})
## Tags whose whole content is dropped, not only the tag.
DROPPED_CONTENT_TAGS = frozenset({"script", "style", "iframe", "object", "embed"})
## Tags without a closing tag.
VOID_TAGS = frozenset({"br", "img", "hr"})
## URL schemes allowed in href and src.
ALLOWED_URL_SCHEMES = frozenset({"http", "https", "mailto"})
## Flash message texts.
MSG_EMAIL_TAKEN = "You've already signed up with that email, log in instead!"
MSG_BAD_CREDENTIALS = "Invalid email or password."
MSG_LOGIN_REQUIRED = "You need to log in or register to comment."
MSG_MESSAGE_SENT = "Your message was sent."
## Pattern a valid email address must match (no extra dependency needed).
EMAIL_PATTERN = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
