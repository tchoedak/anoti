import os
from datetime import timedelta
import bugsnag
import click


class Key(object):
    def __init__(self, key, required=False, prompt=None):
        self.key = key
        self.required = required
        self.required_str = f'{"REQUIRED" if required else "Optional"}'
        self.prompt = (
            f'{self.required_str}: {prompt}'
            if prompt
            else f'{self.required_str}: Please enter your {key}'
        )


class Config(object):

    PATH = os.path.join(os.path.expanduser('~'), '.anoti')

    def __init__(self):
        self.config = {}
        self.keys = [
            Key(
                'SELLER_CENTRAL_ACCESS_KEY_ID',
                required=True,
                prompt='Please enter your AWS Access Key ID',
            ),
            Key(
                'SELLER_CENTRAL_SECRET_KEY',
                required=True,
                prompt='Please enter your AWS Secret Key',
            ),
            Key('SELLER_ID', required=True),
            Key('MWS_AUTH_TOKEN'),
            Key('EMAIL_HOST'),
            Key('EMAIL_PORT'),
            Key('SMTP_USERNAME'),
            Key('SMTP_PASSWORD'),
            Key('TWILIO_NUMBER'),
            Key('TWILIO_ACCOUNT_SID'),
            Key('TWILIO_AUTH_TOKEN'),
            Key('RECEIVER_NUMBER'),
            Key('RECEIVER_EMAIL'),
            Key('BUGSNAG_API_KEY'),
        ]

        try:
            self.load_config()
        except FileNotFoundError:
            self.build_config()
            self.load_config()

    def load_config(self):
        with open(self.PATH, 'r') as f:
            self.config.update(
                {
                    line.split('=')[0]: line.split('=')[1]
                    for line in f.read().splitlines()
                }
            )

    def build_config(self):
        with open(self.PATH, 'wb') as f:
            for key in self.keys:
                self.put(f, key.key, click.prompt(key.prompt))

    def get(self, key):
        return self.config.get(key)

    def put(self, file_, key, val):
        file_.write(f'{key}={val}')


config = Config()


# Amazon API configuration
app = 'anoti'
endopoint = 'Orders'
service = 'https://mws.amazonservices.com'
marketplace_id = 'ATVPDKIKX0DER'
country_code = 'US'
request_per_hour_quota = 200
access_key = config.get('SELLER_CENTRAL_ACCESS_KEY_ID')
secret_key = config.get('SELLER_CENTRAL_SECRET_KEY')
seller_id = config.get('SELLER_ID')
mws_auth_token = config.get('MWS_AUTH_TOKEN')


# Anoti App Configuration
TIMEDELTA_RANGE = timedelta(hours=2)  # app will view orders updated in the last 2 hours
TIMEDELTA_INTERVAL = timedelta(hours=1)
EMAIL_HOST = config.get('EMAIL_HOST')
EMAIL_PORT = config.get('EMAIL_PORT')
EMAIL_USERNAMAE = config.get('SMTP_USERNAME')
EMAIL_PASSWORD = config.get('SMTP_PASSWORD')
ANOTI_NUMBER = config.get('TWILIO_NUMBER')
TWILIO_ACCOUNT_SID = config.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = config.get('TWILIO_AUTH_TOKEN')  # was AUTH_TOKEN


# Receiver Configuration
RECEIVER_EMAIL = config.get('RECEIVER_EMAIL')
if RECEIVER_EMAIL:
    RECEIVER_EMAIL = RECEIVER_EMAIL.split(',')
RECEIVER_NUMBER = config.get('RECEIVER_NUMBER')
if RECEIVER_NUMBER:
    RECEIVER_NUMBER = RECEIVER_NUMBER.split(',')

BUGSNAG_API_KEY = config.get('BUGSNAG_API_KEY')

BUGSNAG_ENABLED = BUGSNAG_API_KEY is not None

email_enabled = (
    SMTP_USERNAME is not None
    and SMTP_PASSWORD is not None
    and RECEIVER_EMAIL is not None
)

sms_enabled = (
    TWILIO_NUMBER is not None
    and TWILIO_ACCOUNT_SID is not None
    and RECEIVER_NUMBER is not None
)


if BUGSNAG_ENABLED:
    # setup bugsnag logging
    bugsnag.configure(
        api_key=os.environ.get('BUGSNAG_API_KEY'),
        project_root=os.path.abspath(os.path.dirname(__file__)),
    )
