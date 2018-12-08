import os
from datetime import timedelta

# Amazon API configuration
endpoint = 'Orders'
seller_id = 'A3QF7LT0E0UZ9U'
service = "https://mws.amazonservices.com"
marketplace_id = 'ATVPDKIKX0DER'
country_code = 'US'
request_per_hour_quota = 200
access_key = os.environ.get('SELLER_CENTRAL_ACCESS_KEY_ID')
secret_key = os.environ.get('SELLER_CENTRAL_SECRET_KEY')
app = 'anoti'


# Anoti App Configuration
TIMEDELTA_RANGE = timedelta(hours=120)
TIMEDELTA_INTERVAL = timedelta(hours=1)
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = '587'
EMAIL_USERNAME = os.environ.get('SMTP_USERNAME')
EMAIL_PASSWORD = os.environ.get('SMTP_PASSWORD')
TWILIO_ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
ANOTI_NUMBER = os.environ.get('ANOTI_NUMBER')


# Receiver Configuration
# WARNING: receiver should not have ',' in their emails or phone numbers
RECEIVER_EMAIL = os.environ.get('RECEIVER_EMAIL').split(',')
RECEIVER_NUMBER = os.environ.get('RECEIVER_NUMBER').split(',')


# Alerts Configuration
email_enabled = True
sms_enabled = True
