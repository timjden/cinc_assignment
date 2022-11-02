import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from behave import given, when, then

from utils import click_element, hover_element, wait_for_element_visibility

logging.basicConfig(filename="debug.log")

@when("User clicks adjustment icon")
def step_impl(context):      
    adjustment_icon_xpath = "/html/body/div/div[2]/div/div/div[3]/div[1]/div[1]/div[1]/header/div/div/div/span/span"
    click_element(context, adjustment_icon_xpath)

@when("User hovers on Units")
def step_impl(context):
    units_xpath = "/html/body/div/div[2]/div/div/div[3]/div[1]/div[1]/div[2]/ul[1]/li[2]/span[1]"
    click_element(context, units_xpath)

@when("User clicks Metric")
def step_impl(context):
    metric_xpath = "/html/body/div/div[2]/div/div/div[3]/div[1]/div[1]/div[2]/ul[2]/li[2]/span"
    click_element(context, metric_xpath)
    time.sleep(2)

    first_value_xpath = "/html/body/div/div[2]/div/div/div[3]/div[1]/div[1]/ul/li[1]/div[1]/span/div"
    wait_for_element_visibility(context, first_value_xpath)
    first_value = context.driver.find_element(By.XPATH, first_value_xpath)
    numbers = []
    for i in first_value.text:
        if i.isdigit():
            numbers.append(i)
    logging.info(f"The first recipe amount is: {''.join(numbers)}")
    context.amount = float(''.join(numbers))

@when("User hovers on Scale")
def step_impl(context):
    scale_xpath = "/html/body/div/div[2]/div/div/div[3]/div[1]/div[1]/div[2]/ul/li[1]/span[1]/span[1]"
    hover_element(context, scale_xpath)

@when("User scales recipe X2")
def step_impl(context):
    x2_xpath = "/html/body/div/div[2]/div/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[4]/span"
    click_element(context, x2_xpath)
    time.sleep(2)

@then("Recipe amounts have been correctly scaled")
def step_impl(context):
    first_value_xpath = "/html/body/div/div[2]/div/div/div[3]/div[1]/div[1]/ul/li[1]/div[1]/span/div"
    wait_for_element_visibility(context, first_value_xpath)
    first_value = context.driver.find_element(By.XPATH, first_value_xpath)
    numbers = []
    for i in first_value.text:
        if i.isdigit():
            numbers.append(i)
    logging.info(f"The initial amount is: {context.amount}")
    logging.info(f"The X2 amount is: {''.join(numbers)}")
    assert float(''.join(numbers)) == context.amount * 2 or float(''.join(numbers)) == (context.amount * 2) + 1 or float(''.join(numbers)) == (context.amount * 2) -1