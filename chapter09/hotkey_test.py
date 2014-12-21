from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest


class HotkeyTest(unittest.TestCase):

    URL = "https://rawgit.com/jeresig/jquery.hotkeys/master/test-static-05.html"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_hotkey(self):
        driver = self.driver

        shift_n_label = WebDriverWait(self.driver, 10).\
            until(expected_conditions.visibility_of_element_located((By.ID, "_Shift_n")))

        ActionChains(driver).\
            key_down(Keys.SHIFT).\
            send_keys('n').\
            key_up(Keys.SHIFT).perform()
        self.assertEqual("rgba(12, 162, 255, 1)",
                         shift_n_label.value_of_css_property("background-color"))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
