from __future__ import absolute_import
import mws
from . import config
from . import util

orders_api = mws.Orders(
    access_key=config.access_key,
    secret_key=config.secret_key,
    account_id=config.seller_id,
    region='US' or config.country_code
)

def get_order_id(order):
    return order.get('AmazonOrderId').get('value')

class Orders(object):

    def __init__(self, last_updated_after, marketplace_id=None):
        self.api = orders_api
        self.marketplace_id = marketplace_id or config.marketplace_id
        self.last_updated_after = last_updated_after
        orders = self.api.list_orders(
            marketplaceids=[self.marketplace_id],
            lastupdatedafter=last_updated_after
        ).parsed.Orders.Order
        self.orders = [orders] if not isinstance(orders, list) else orders
        self.structured_orders = {get_order_id(order): order for order in self.orders}

    def get_order_ids(self):
        return [get_order_id(order) for order in self.orders]

    def get_orders_since(self, since):
        return [
            order for order in self.orders if util.parse_amazon_datetime(
                order.get('PurchaseDate').get('value')
            ) >= since
        ]

