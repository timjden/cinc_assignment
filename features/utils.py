from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def wait_for_element_visibility(context, element_xpath):
    context.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, element_xpath)))

def click_element(context, element_xpath):
    wait_for_element_visibility(context, element_xpath)
    element = context.driver.find_element(By.XPATH, element_xpath)
    element.click()

def hover_element(context, element_xpath):
    wait_for_element_visibility(context, element_xpath)
    element = context.driver.find_element(By.XPATH, element_xpath)
    context.action_chain.move_to_element(element).perform()