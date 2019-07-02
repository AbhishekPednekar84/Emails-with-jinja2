import smtplib
import ssl
from news_scraper import scrape_render
from email.message import EmailMessage
from constants import (
    SUBJECT,
    PASSWORD,
    PORT,
    RECIPIENTS,
    SENDER_EMAIL,
    SMTP_SERVER,
    TEMPLATE,
)


def _send_email(template):
    msg = EmailMessage()
    msg["Subject"] = SUBJECT
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENTS
    msg["Cc"] = " "
    msg["Bcc"] = " "
    msg.add_alternative(template, subtype="html")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as smtp_ssl:
        smtp_ssl.login(SENDER_EMAIL, PASSWORD)
        smtp_ssl.send_message(msg)


if __name__ == "__main__":
    html_template = scrape_render(TEMPLATE)
    _send_email(html_template)
