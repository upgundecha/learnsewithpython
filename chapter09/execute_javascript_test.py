from selenium import webdriver
import unittest


class ExecuteJavaScriptTest (unittest.TestCase):
    def setUp(self)	:
        self.driver = webdriver.Firefox()

    def test_execute_java_script(self):
        driver = self.driver
        driver.get("http://www.google.com")

        title = driver.execute_script("return document.title")
        self.assertEquals("Google", title)

        all_links = driver.\
            execute_script("var links = document.getElementsByTagName('A'); return links.length")
        self.assertEquals(len(all_links), 49)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
