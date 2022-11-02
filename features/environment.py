from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    context.options = webdriver.ChromeOptions()
    context.options.add_experimental_option("detach", True)
    context.options.add_argument('--no-sandbox')
    context.options.add_argument('--headless')
    context.options.add_argument('--disable-extensions')
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=context.options)
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 10)
    context.action_chain = ActionChains(context.driver)