import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

@given("User is on the home page")
def step_impl(context):
    driver.get("https://www.cinc.kitchen/")
    page_title = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/div/div[1]/h1")
    assert page_title.text == "Recipes just got better."

@when("User clicks Log In")
def step_impl(context):
    login_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/nav/ul/li/span")
    login_button.click()

@then("Log in dialog pops up")
def step_impl(context):
    login_dialog = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/div/div/header/h2")
    assert login_dialog.text == "Log in"

@when("User enters username: {username}")
def step_impl(context, username):
    username_field = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/div/div/form/ul[2]/li[1]/div/div/label/input")
    username_field.send_keys(username)

@when("User enters password: {password}")
def step_impl(context, password):
    password_field = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/div/div/form/ul[2]/li[2]/div/div/label/input")
    password_field.send_keys(password)

@when("User clicks Log in button")
def step_impl(context):
    login_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/div/div/form/ul[2]/li[4]/button")
    login_button.click()

@then("User is logged in")
def step_impl(context):
    dashboard_title = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/header/h1")
    assert dashboard_title.text == "Dashboard"
    driver.close()