from selenium import webdriver
import unittest


class FrameTest(unittest.TestCase):

    URL = 'http://cookbook.seleniumacademy.com/Frames.html'

    def setUp(self)	:
        self.driver = webdriver.Firefox()
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def test_select_frame_with_id_or_name(self):
        driver = self.driver
        # activate the frame on left side using it's id attribute
        driver.switch_to.frame('left')

        # get an element from the frame on left side and verify it's contents
        left_msg = driver.find_element_by_tag_name('p')
        self.assertEquals('This is Left Frame', left_msg.text)

        # activate the Page, this will move context from frame back to the Page
        driver.switch_to.default_content()

        # activate the frame on right side using it's name attribute
        driver.switch_to.frame('right')

        # get an element from the frame on right side and verify it's contents
        right_msg = driver.find_element_by_tag_name('p')
        self.assertEquals('This is Right Frame', right_msg.text)

        # activate the Page, this will move context from frame back to the Page
        driver.switch_to.default_content()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
