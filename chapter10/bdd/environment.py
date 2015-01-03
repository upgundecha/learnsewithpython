from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.quit()
