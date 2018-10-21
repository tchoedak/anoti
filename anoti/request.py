import requests
import config
from datetime import datetime, timedelta
from collections import OrderedDict


def sign(string, secret, digest='hex'):
    import hashlib
    import hmac
    import base64

    secret = bytes(secret, 'utf-8')
    message = bytes(string, 'utf-8')
    hash_ = hmac.new(secret, message, hashlib.sha256)
    if digest == 'hex':
        return hash_.hexdigest()
    elif digest == 'base64':
        return base64.b64encode(hash_.digest()).decode()


def build_request(request_type, service, endpoint, params):
    ordered_params = sorted([param.encode('utf-8') for param in params])
    to_sign_params = '&'.join([param for param in ordered_params])
    r = '\n'.join([line for line in (request_type, service, endpoint, to_sign_params)])
    return r


def access():
    keys = {'AWSAccessKeyId': config.access_key}
    return keys


class OrdersRequest(object):

    _timestamp_format = '%Y-%m-%dT%H:%M:%S'

    def __init__(self, action='ListOrders', last_updated_after=None):
        self.action = action
        self.marketplace_id = config.marketplace_id
        self.fulfillment_channel = 'FBA'
        self.last_updated_after = last_updated_after
        self.timestamp = datetime.now().isoformat()
        self.seller_id = config.seller_id
        self.signature = None
        self.signature_method = 'HmacSHA256'
        self.signature_version = '2'
        self.version = '2013-09-01'
        self.service = 'mws.amazonservices.com'
        self.endpoint = config.endpoint
        self.request_type = 'GET'
        self.access_key = config.access_key

    @property
    def ready_request(self):
        _keys = []
        _url = self.signed_request
        return _url

    def create_signature(self, url):
        to_sign = 'GET\r\n'
        to_sign += self.service + '\r\n'
        to_sign += '/' + self.endpoint
        to_sign += '/' + self.version + '\r\n'
        to_sign += url
        print("To Sign URL is: ")
        print(to_sign)
        print('--EOF')
        return sign(to_sign, config.secret_key)

    @property
    def signed_request(self):
        signature = self.create_signature(self.built_request)
        _keys = OrderedDict()
        _keys.update({'Signature': signature})
        _url = self.built_request + self.to_url(_keys)
        return _url

    @property
    def params_url(self):
        # just params
        pass

    @property
    def built_request(self):
        _keys = OrderedDict()
        _keys.update(
            {
                'Action': self.action,
                'FulfillmentChannel.Channel.1': self.fulfillment_channel,
                'LastUpdatedAfter': self.last_updated_after,
                'MarketplaceId.Id.1': self.marketplace_id,
                'SellerId': self.seller_id,
                'SignatureMethod': self.signature_method,
                'SignatureVersion': self.signature_version,
                'Timestamp': self.timestamp,
                'Version': self.version,
            }
        )
        _url = self.base_url + self.to_url(_keys)
        return _url

    def to_url(self, keys):
        return ''.join(['&{}={}'.format(key, keys[key]) for key in keys])

    def to_keys(self, url):
        # '&lname=choedak&fname=tenzin' : {'lname': 'choedak', 'fname': 'tenzin'}
        keys = {}
        for kv in url.split('&'):
            if kv:
                key, val = kv.split('=')
                keys[key] = val
        return keys

    @property
    def base_url(self):
        _base_url = 'https://{service}/{endpoint}/{version}?AWSAccessKeyId={access_key}'
        return _base_url.format(
            service=self.service,
            endpoint=self.endpoint,
            version=self.version,
            access_key=self.access_key,
        )
