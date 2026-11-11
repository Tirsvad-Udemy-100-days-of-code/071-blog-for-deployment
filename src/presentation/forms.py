"""! @file forms.py
@brief WTForms forms of the blog.
"""
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import URL, DataRequired, Optional, Regexp

from constants import EMAIL_PATTERN

## Simple address check; the Email validator would need the extra email_validator package.
EMAIL_CHECK = Regexp(EMAIL_PATTERN, message="Invalid email address.")


class RegisterForm(FlaskForm):
    """! @brief Sign-up form."""

    email = EmailField("Email", validators=[DataRequired(), EMAIL_CHECK])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    """! @brief Log-in form."""

    email = EmailField("Email", validators=[DataRequired(), EMAIL_CHECK])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


class CommentForm(FlaskForm):
    """! @brief Comment form shown under a post."""

    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


class PostForm(FlaskForm):
    """! @brief Form to create or edit a post."""

    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = URLField("Blog Image URL", validators=[Optional(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class ContactForm(FlaskForm):
    """! @brief Contact-us form."""

    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), EMAIL_CHECK])
    phone = StringField("Phone Number", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")
