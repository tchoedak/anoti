from twilio.rest import Client
from . import config


def send_text_message(message):
    client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

    for receiver_number in config.RECEIVER_NUMBER:
        message = client.messages.create(
            to=receiver_number, from_=config.ANOTI_NUMBER, body=message
        )
