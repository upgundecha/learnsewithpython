import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class CookiesTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_store_cookie(self):
        driver = self.driver
        # get the Your language dropdown as instance of Select class
        select_language = \
            Select(self.driver.find_element_by_id('select-language'))

        # check default selected option is English
        self.assertEqual('ENGLISH',
                          select_language.first_selected_option.text)
        # store cookies should be none
        store_cookie = driver.get_cookie('store')
        self.assertEqual(None, store_cookie)

         # select an option using select_by_visible text
        select_language.select_by_visible_text('French')

        # store cookie should be populated with selected country
        store_cookie = driver.get_cookie('store')['value']
        self.assertEqual('french', store_cookie)

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
