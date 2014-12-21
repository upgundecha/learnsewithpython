from selenium import webdriver
from time import gmtime, strftime
import unittest


class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://demo.magentocommerce.com/")

    def test_register_new_user(self):
        driver = self.driver

        # click on Log In link to open Login page
        driver.find_element_by_link_text("ACCOUNT").click()
        driver.find_element_by_link_text("My Account").click()

        # get the Create Account button
        create_account_button = \
            driver.find_element_by_link_text("CREATE AN ACCOUNT")

        # check Create Account button is displayed and enabled
        self.assertTrue(create_account_button.is_displayed() and
                        create_account_button.is_enabled())

        # click on Create Account button. This will displayed new account
        create_account_button.click()

        # check title
        self.assertEquals("Create New Customer Account", driver.title)

        # get all the fields from Create an Account form
        first_name = driver.find_element_by_id("firstname")
        last_name = driver.find_element_by_id("lastname")
        email_address = driver.find_element_by_id("email_address")
        password = driver.find_element_by_id("password")
        confirm_password = driver.find_element_by_id("confirmation")
        news_letter_subscription = driver.find_element_by_id("is_subscribed")
        submit_button = driver.\
            find_element_by_xpath("//button[@title='Register']")

        # check maxlength of first name and last name textbox
        self.assertEqual("255", first_name.get_attribute("maxlength"))
        self.assertEqual("255", last_name.get_attribute("maxlength"))

        # check all fields are enabled
        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and
                        email_address.is_enabled() and
                        news_letter_subscription.is_enabled() and
                        password.is_enabled() and confirm_password.is_enabled()
                        and submit_button.is_enabled())

        # check Sign Up for Newsletter is unchecked
        self.assertFalse(news_letter_subscription.is_selected())

        user_name = "user_" + strftime("%Y%m%d%H%M%S", gmtime())

        # fill out all the fields
        first_name.send_keys("Test")
        last_name.send_keys(user_name)
        news_letter_subscription.click()
        email_address.send_keys(user_name + "@example.com")
        password.send_keys("tester")
        confirm_password.send_keys("tester")

        # click Submit button to submit the form
        submit_button.click()

        # check new user is registered
        self.assertEqual("Hello, Test " + user_name + "!",
                         driver.find_element_by_css_selector("p.hello > strong").text)
        driver.find_element_by_link_text("ACCOUNT").click()
        self.assertTrue(driver.find_element_by_link_text("Log Out").is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
