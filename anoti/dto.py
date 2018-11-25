from . import db
from . import models
from . import util

from datetime import datetime


def save_orders(*orders):
    for order in orders:
        db.session.add(
            amazon_order(order)
        )
    db.session.commit()


def amazon_order(order):
    """create an AmazonOrder object from an API parsed order"""
    return models.AmazonOrder(
        amazon_order_id=order.AmazonOrderId,
        is_prime = order.IsPrime == 'true',
        title=order.OrderItem.Title,
        price=float(order.OrderTotal.Amount) if 'OrderTotal' in order.keys() else None,
        number_of_items=int(order.OrderItem.ProductInfo.NumberOfItems),
        purchase_date=util.parse_amazon_datetime(order.PurchaseDate),
        order_status=order.OrderStatus,
        order_type=order.OrderType,
        ship_service_level=order.ShipmentServiceLevelCategory,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

