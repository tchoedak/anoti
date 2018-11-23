from __future__ import absolute_import
import mws
from datetime import datetime, timedelta
from . import config
from . import util
from . import queries

orders_api = mws.Orders(
    access_key=config.access_key,
    secret_key=config.secret_key,
    account_id=config.seller_id,
    region='US' or config.country_code,
)

yesterday = datetime.now() - timedelta(hours=24)

def get_order_id(order):
    return order.get('AmazonOrderId').get('value')


class Orders(object):
    def __init__(self, last_updated_after, marketplace_id):
        self.last_updated_after = last_updated_after
        self.marketplace_id = marketplace_id

    @property
    def orders(self):
        orders_ = orders_api.list_orders(
            marketplaceids=[self.marketplace_id],
            lastupdatedafter=self.last_updated_after
        ).parsed.Orders.Order
        return [orders_] if not isinstance(orders_, list) else orders_

    @property
    def structured_orders(self):
        return {get_order_id(order): order for order in self.orders}


class OrderItems(object):
    def __init__(self, amazon_order_id):
        self.amazon_order_id = amazon_order_id

    @property
    def order_items(self):
        order_items_ = (orders_api
            .list_order_items(amazon_order_id=self.amazon_order_id)
            .parsed
            .OrderItems
            .OrderItem
        )
        return order_items_


class CompleteOrders(object):

    def __init__(self, last_updated_after=yesterday, marketplace_id=config.marketplace_id):
        self.last_updated_after = last_updated_after
        self.marketplace_id = marketplace_id

    def combine_order(self, order):
        amazon_order_id = order.AmazonOrderId
        order_items = OrderItems(amazon_order_id).order_items

        order['OrderItem'] = order_items
        return order
    
    @property
    def complete_orders(self):
        orders = Orders(self.last_updated_after, self.marketplace_id).orders
        complete_orders = [self.combine_order(order) for order in orders]
        return complete_orders

