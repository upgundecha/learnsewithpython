import unittest
from pages.homepage import HomePage
from base.basetestcase import BaseTestCase


class SearchProductTest(BaseTestCase):
    def testSearchForProduct(self):
        homepage = HomePage(self.driver)
        search_results = homepage.search.searchFor('earphones')
        self.assertEqual(3, search_results.product_count)
        product = search_results.open_product_page('MADISON EARBUDS')
        self.assertEqual(product.name, 'MADISON EARBUDS')
        self.assertEqual(product.price, '$35.00')
        self.assertEqual(product.stock_status, 'IN STOCK')

if __name__ == '__main__':
    unittest.main(verbosity=3)
