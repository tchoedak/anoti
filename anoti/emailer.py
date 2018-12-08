import smtplib
from .config import (
    EMAIL_USERNAME,
    EMAIL_PASSWORD,
    EMAIL_HOST,
    EMAIL_PORT,
    RECEIVER_EMAIL,
)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_order_message(message):
    server = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)

    for receiver_email in RECEIVER_EMAIL:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = 'You have new Amazon Orders!'

        body = MIMEText(message, 'html')

        msg.attach(body)
        server.send_message(msg)

        del msg
