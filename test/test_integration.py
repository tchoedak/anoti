import unittest
from datetime import datetime
import requests

class TestRequest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Starting integration tests')

    def test_list_orders(self):
        from request import OrdersRequest
        dt = datetime(2018, 10, 1)
        orders = OrdersRequest(last_updated_after=dt)
        orders_request = orders.ready_request
        print(orders_request)
        r = requests.get(orders_request)

        print('Status code: {}'.format(r.status_code))
        print(r.text)
        

if __name__ == '__main__':
    unittest.main()
