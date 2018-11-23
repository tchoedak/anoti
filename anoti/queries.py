from . import models
from . import db


def new_orders(orders):
    """
    Returns orders that haven't already been registered in the DB
    """
    order_ids = [order.amazon_order_id for order in orders]
    new_orders = (
        db.session.query(models.AmazonOrder)
        .filter(models.AmazonOrder.amazon_order_id.notin(order_ids))
    )
    return new_orders

def exists(order):
    """
    Returns True if the order exists in the DB
    """
    print(order)
    print(order.AmazonOrderId)
    order = (
        db.session.query(models.AmazonOrder)
        .filter(models.AmazonOrder.amazon_order_id == order.AmazonOrderId)
    ).first()
    if order:
        return True
    else:
        return False
