"""! @file mail.py
@brief SMTP adapter that sends the contact-form message.
"""
import logging
import smtplib
import ssl
from email.message import EmailMessage

from constants import SMTP_HOST, SMTP_PORT

logger = logging.getLogger(__name__)


class SmtpMailSender:
    """! @brief Sends mail to the blog owner through Gmail over SSL."""

    def __init__(self, user: str | None, password: str | None) -> None:
        self._user = user
        self._password = password

    def send(self, subject: str, body: str) -> None:
        """! @brief Sends one message; without credentials it only logs a warning."""
        if not self._user or not self._password:
            logger.warning("Mail credentials are not configured; the message was not sent.")
            return
        message = EmailMessage()
        message["Subject"] = subject
        message["From"] = self._user
        message["To"] = self._user
        message.set_content(body)
        try:
            with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ssl.create_default_context()) as server:
                server.login(self._user, self._password)
                server.send_message(message)
        except (smtplib.SMTPException, OSError):
            logger.exception("Sending the contact message failed.")
            return
        logger.info("Contact message sent.")
