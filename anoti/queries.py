from . import models
from . import db

def new_orders(order_ids):
    """
    Returns order_ids from ``order_ids` if they don't exist in the DB
    """
    existing_orders = db.session.query(
        models.Order
    ).filter(
        models.Order.amazon_order_id.in_(order_ids)
    ).all()

    existing_order_ids = [order.amazon_order_id for order in existing_orders]

    new_orders = list(
        set(existing_orders).difference(set(order_ids))
    )
    return new_orders

