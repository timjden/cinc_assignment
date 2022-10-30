import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from behave import given, when, then

from utils import wait_for_element_visibility

logging.basicConfig(filename="debug.log")

@given("User is on the Home page")
def step_impl(context):
    context.driver.get("https://www.cinc.kitchen/")
    try:
        logging.info("Looking for home page title...")
        page_title_xpath = "/html/body/div/div[2]/div[1]/div/div/div/div[1]/h1"
        wait_for_element_visibility(context, page_title_xpath)
        page_title = context.driver.find_element(By.XPATH, page_title_xpath)
        logging.info("Found home page title")
    except:
        logging.info("Couldn't find home page title, logging out...")
        profile_icon_xpath = "/html/body/div/div[1]/div/nav/ul/li[4]/div"
        profile_icon = context.driver.find_element(By.XPATH, profile_icon_xpath)
        profile_icon.click()
        log_out_xpath = "/html/body/div/div[1]/div/nav/ul/li[4]/div/ul/li[6]/a"
        log_out = context.driver.find_element(By.XPATH, log_out_xpath)
        log_out.click()
        cinc_xpath = "/html/body/div/div[1]/div/nav/div/div/a/img"
        wait_for_element_visibility(context, cinc_xpath)
        cinc = context.driver.find_element(By.XPATH, cinc_xpath)
        cinc.click()
    
    page_title_xpath = "/html/body/div/div[2]/div[1]/div/div/div/div[1]/h1"
    wait_for_element_visibility(context, page_title_xpath)
    page_title = context.driver.find_element(By.XPATH, page_title_xpath)
    assert page_title.text == "Recipes just got better."

@when("User clicks Log In")
def step_impl(context):
    login_button_xpath = "/html/body/div/div[1]/div/nav/ul/li/span"
    wait_for_element_visibility(context, login_button_xpath)
    login_button = context.driver.find_element(By.XPATH, login_button_xpath)
    login_button.click()

@then("Log in dialog pops up")
def step_impl(context):
    login_dialog_xpath = "/html/body/div/div[1]/div[2]/div/div/div/div/header/h2"
    wait_for_element_visibility(context, login_dialog_xpath)
    login_dialog = context.driver.find_element(By.XPATH, login_dialog_xpath)
    assert login_dialog.text == "Log in"

@when("User enters username: {username}")
def step_impl(context, username):
    username_field_xpath = "/html/body/div/div[1]/div[2]/div/div/div/div/form/ul[2]/li[1]/div/div/label/input"
    wait_for_element_visibility(context, username_field_xpath)
    username_field = context.driver.find_element(By.XPATH, username_field_xpath)
    username_field.send_keys(username)

@when("User enters password: {password}")
def step_impl(context, password):
    password_field_xpath = "/html/body/div/div[1]/div[2]/div/div/div/div/form/ul[2]/li[2]/div/div/label/input"
    wait_for_element_visibility(context, password_field_xpath)
    password_field = context.driver.find_element(By.XPATH, password_field_xpath)
    password_field.send_keys(password)

@when("User clicks Log in button")
def step_impl(context):
    login_button_xpath = "/html/body/div/div[1]/div[2]/div/div/div/div/form/ul[2]/li[4]/button"
    wait_for_element_visibility(context, login_button_xpath)
    login_button = context.driver.find_element(By.XPATH, login_button_xpath)
    login_button.click()

@then("User is logged in")
def step_impl(context):
    dashboard_title_xpath = "/html/body/div/div[2]/div[1]/div/div/header/h1"
    wait_for_element_visibility(context, dashboard_title_xpath)
    dashboard_title_element = context.driver.find_element(By.XPATH, dashboard_title_xpath)
    assert dashboard_title_element.text == "Dashboard"