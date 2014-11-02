from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest


class DoubleClickTest (unittest.TestCase):

    URL = "https://rawgit.com/upgundecha/learnsewithpython/master/pages/DoubleClickDemo.html"

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_double_click(self):
        driver = self.driver
        driver.get(self.URL)
        message = driver.find_element_by_id("message")

        # verify color is Blue
        self.assertEqual("rgba(0, 0, 255, 1)",
                         message.value_of_css_property("background-color"))

        ActionChains(self.driver).double_click(message).perform()

        # verify Color is Yellow
        self.assertEqual("rgba(255, 255, 0, 1)",
                         message.value_of_css_property("background-color"))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
