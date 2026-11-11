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
