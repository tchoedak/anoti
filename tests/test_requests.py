import unittest
import request


class TestRequest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Starting request tests')

    def test_build_request(self):
        request_type = 'GET'
        service = 'webservices.amazon.com'
        endpoint = '/onca/xml'
        params = [
            'Service=AWSECommerceService',
            'AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE',
            'AssociateTag=mytag-20',
            'ResponseGroup=Images%2CItemAttributes%2COffers%2CReviews',
            'Operation=ItemLookup',
            'ItemId=0679722769',
            'Version=2013-08-01',
            'Timestamp=2014-08-18T12%3A00%3A00Z'
        ]

	r = request.build_request(request_type, service, endpoint, params)
        
        print(r)

	string_to_sign = (
            ('GET'
             '\nwebservices.amazon.com'
             '\n/onca/xml'
             '\nAWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20&ItemId=0679722769&Operation=ItemLookup&ResponseGroup=Images%2CItemAttributes%2COffers%2CReviews&Service=AWSECommerceService&Timestamp=2014-08-18T12%3A00%3A00Z&Version=2013-08-01'
             )
        )

	self.assertEquals(r, string_to_sign)

if __name__ == '__main__':
    unittest.main()
