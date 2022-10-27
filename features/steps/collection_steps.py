import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

@given("User is logged in as username: {username}, password: {password}")
def step_impl(context, username, password):
    context.execute_steps(f"""
    Given User is on the Home page
    When User clicks Log In
    Then Log in dialog pops up
    When User enters username: {username}
    When User enters password: {password}
    When User clicks Log in button
    Then User is logged in
    """)

@given("User is on the Dashboard page")
def step_impl(context):
    pass

@when("User clicks Collections tab")
def step_impl(context):
    pass

@when("User adds a new Collection")
def step_impl(context):
    pass

@then("A new Collection is added")
def step_impl(context):
    pass