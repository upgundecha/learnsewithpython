from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Firefox()

def after_all(context):
    context.driver.quit()
