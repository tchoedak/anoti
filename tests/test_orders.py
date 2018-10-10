import unittest
from datetime import datetime, timedelta
import requests

class TestOrders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Starting Orders Test')

    def test_get_order_ids(self):
        print('testing get_order_ids')
        from anoti.orders import Orders
        past_day_orders = Orders(last_updated_after=datetime.now() - timedelta(hours=24))
        print(past_day_orders.get_order_ids())

    def test_get_orders_since(self):
        print('testing get_orders_since')
        from anoti.orders import Orders
        past_24_hours = datetime.now() - timedelta(hours=24)
        past_day_orders = Orders(last_updated_after=past_24_hours)
        print(past_day_orders.get_orders_since(past_24_hours))

if __name__ == '__main__':
    unittest.main()
