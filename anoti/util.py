from datetime import datetime


def parse_amazon_datetime(datetime_value):
    return datetime.strptime(datetime_value[:19], '%Y-%m-%dT%H:%M:%S')


def is_empty(value):
    if value[:1] == '\n':
        return True
    else:
        return False


def is_marker(value):
    if value == 'value':
        return True
    else:
        return False


def parse(message):
    parsed = dict()
    for key, val in message.items():
        if isinstance(val, dict) and is_marker(key):
            parsed[key] = val['value']
        elif isinstance(val, dict):
            parsed.update(parse(val))
    return parsed
