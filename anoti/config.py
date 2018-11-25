import os
from datetime import timedelta

endpoint = 'Orders'
seller_id = 'A3QF7LT0E0UZ9U'
service = "https://mws.amazonservices.com"
marketplace_id = 'ATVPDKIKX0DER'
country_code = 'US'
request_per_hour_quota = 200
access_key = os.environ.get('SELLER_CENTRAL_ACCESS_KEY_ID')
secret_key = os.environ.get('SELLER_CENTRAL_SECRET_KEY')
app = 'anoti'


TIMEDELTA_RANGE = timedelta(hours=120)
TIMEDELTA_INTERVAL = timedelta(hours=1)
