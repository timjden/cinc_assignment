from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    context.options = webdriver.ChromeOptions()
    context.options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=context.options)
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 10)