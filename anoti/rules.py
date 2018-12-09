from . import queries


def is_status(order, status):
    return order.OrderStatus == status


def is_new(order):
    """
    order must not already be in the DB
    """
    return queries.exists(order) == False


def is_pending(order):
    """
    Order must be in pending status
    """
    return is_status(order, 'Pending')


def is_shipped(order):
    """
    Order must be in shipped status
    """
    return is_status(order, 'Shipped')


rules = [is_new]
