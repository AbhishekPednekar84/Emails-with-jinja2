import os

SMTP_SERVER = "smtp.gmail.com"
PORT = 465
SENDER_EMAIL = os.environ.get("EMAIL_USER")
PASSWORD = os.environ.get("EMAIL_PASS")
SUBJECT = "Top News Headlines"
RECIPIENTS = [" "]
TEMPLATE = "email.html"
