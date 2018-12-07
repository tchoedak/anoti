from twilio.rest import Client
from . import config


def send_text_message(message):
    client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        to=config.RECEIVER_NUMBER,
        from_=config.ANOTI_NUMBER,
        body=message
    )

