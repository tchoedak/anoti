from datetime import datetime
import os, logging


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


def get_logger(path='/root'):
    if not os.path.isdir(path):
        path = os.path.abspath(os.path.curdir)
    filepath = os.path.join(path, 'anoti.log')
    logger = logging.getLogger('anoti')

    handler = logging.FileHandler(filepath)
    handler.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)
    return logger


logger = get_logger()
