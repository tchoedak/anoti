import smtplib
from . config import (
    EMAIL_USERNAME,
    EMAIL_PASSWORD,
    EMAIL_HOST,
    EMAIL_PORT,
    RECEIVER_EMAIL
)


def send_order_message(message):
    server = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)

    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USERNAME
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = 'You have new Amazon Orders!'

    msg.attach(message)
    server.send_message(msg)

    del msg
