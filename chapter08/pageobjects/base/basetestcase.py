import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get('http://demo.magentocommerce.com/')

    def tearDown(self):
        # close the browser window
        self.driver.quit()
