from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def wait_for_element_visibility(context, element_xpath):
    context.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, element_xpath)))