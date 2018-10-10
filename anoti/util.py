from datetime import datetime

def parse_amazon_datetime(datetime_value):
    return datetime.strptime(datetime_value[:19], '%Y-%m-%dT%H:%M:%S')

