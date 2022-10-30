from multiprocessing.connection import wait
import time
import random
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

from utils import click_element, hover_element, wait_for_element_visibility

logging.basicConfig(filename="debug.log")

# Scenario Outline: Add a Collection

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
    dashboard_title_xpath = "/html/body/div/div[2]/div[1]/div/div/header/h1"
    wait_for_element_visibility(context, dashboard_title_xpath)
    dashboard_title_element = context.driver.find_element(By.XPATH, dashboard_title_xpath)
    assert dashboard_title_element.text == "Dashboard"

@when("User clicks Collections tab")
def step_impl(context):
    collection_tab_xpath = "/html/body/div/div[2]/div[1]/div/div/ul/li[3]"
    wait_for_element_visibility(context, collection_tab_xpath)
    collection_tab_element = context.driver.find_element(By.XPATH, collection_tab_xpath)
    collection_tab_element.click()

@when("User adds a new Collection")
def step_impl(context):
    add_a_collection_xpath = "/html/body/div/div[2]/div[2]/div/div/div/p/span"
    wait_for_element_visibility(context, add_a_collection_xpath)
    add_a_collection_element = context.driver.find_element(By.XPATH, add_a_collection_xpath)
    add_a_collection_element.click()

@when("User enters a title: {title}")
def step_impl(context, title):
    logging.info(f"Adding Collection with title: {title}")
    title_xpath = "/html/body/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/label/input"
    wait_for_element_visibility(context, title_xpath)
    title_element = context.driver.find_element(By.XPATH, title_xpath)
    context.title_text = f"{title} {random.randint(0, 1000)}" # There is a bug on the website that does not allow adding a Collection with same name as a deleted Collection
    title_element.send_keys(context.title_text)

@when("User clicks Save")
def step_impl(context):
    save_xpath = "/html/body/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/ul[2]/li/button"
    wait_for_element_visibility(context, save_xpath)
    save_element = context.driver.find_element(By.XPATH, save_xpath)
    save_element.click()

@then("A new Collection is added")
def step_impl(context):
    collection_xpath = "/html/body/div/div[2]/div[2]/div/div/div/div[2]/header/h2"
    wait_for_element_visibility(context, collection_xpath)
    collection_element = context.driver.find_element(By.XPATH, collection_xpath)
    assert collection_element.text == context.title_text

@then("Delete the Collection")
def step_impl(context):
    delete_xpath = "/html/body/div/div[2]/div[2]/div/div/div/div[2]/header/div/div/span[2]"
    yes_delete_xpath = "/html/body/div/div[2]/div[2]/div/div/div[2]/div/div/div/ul[2]/li/button"
    wait_for_element_visibility(context, delete_xpath)
    delete_element = context.driver.find_element(By.XPATH, delete_xpath)
    delete_element.click()
    wait_for_element_visibility(context, yes_delete_xpath)
    yes_delete_element = context.driver.find_element(By.XPATH, yes_delete_xpath)
    yes_delete_element.click()

# Scenario Outline: Add a Recipe to a Collection

@given("A Collection with title: {title}, exists")
def step_impl(context, title):
    context.execute_steps(f"""
        Given User is on the Dashboard page
        When User clicks Collections tab
        When User adds a new Collection
        When User enters a title: {title}
        When User clicks Save
        Then A new Collection is added
    """)

@when("User clicks Explore")
def step_impl(context):
    explore_xpath = "/html/body/div/div[1]/div/nav/div/ul/li/a"
    click_element(context, explore_xpath)

@when("User clicks a Recipe")
def step_impl(context):
    recipe_xpath = "/html/body/div/div[2]/div[2]/div/div/ul/li[1]/div/div[1]/a"
    wait_for_element_visibility(context, recipe_xpath)
    recipe_element = context.driver.find_element(By.XPATH, recipe_xpath)
    context.recipe_title = recipe_element.text
    click_element(context, recipe_xpath)

@when("User clicks kebab icon")
def step_impl(context):
    kebab_xpath = "/html/body/div/div[2]/div/div/header/div/div/div[1]/div[2]/div/div[4]/span"
    click_element(context, kebab_xpath)

@when("User hovers on Add to collection")
def step_impl(context):
    add_to_collection_xpath = "/html/body/div/div[2]/div/div/header/div/div/div[1]/div[2]/div/div[4]/div/ul/li[1]/span[1]"
    hover_element(context, add_to_collection_xpath)

@then("Collection with title: {title}, is present")
def step_impl(context, title):
    collection_xpath = "/html/body/div/div[2]/div/div/header/div/div/div[1]/div[2]/div/div[4]/div/div/ul/li[2]"
    wait_for_element_visibility(context, collection_xpath)
    collection_element = context.driver.find_element(By.XPATH, collection_xpath)
    assert collection_element.text == context.title_text

@when("User clicks title: {title}")
def step_impl(context, title):
    collection_xpath = "/html/body/div/div[2]/div/div/header/div/div/div[1]/div[2]/div/div[4]/div/div/ul/li[2]"
    click_element(context, collection_xpath)

@when("User clicks profile icon")
def step_impl(context):
    profile_icon_xpath = "/html/body/div/div[1]/div/nav/ul/li[4]/div/span/span"
    click_element(context, profile_icon_xpath)

@when("User clicks Dashboard")
def step_impl(context):
    dashboard_xpath = "/html/body/div/div[1]/div/nav/ul/li[4]/div/ul/li[1]/a"
    click_element(context, dashboard_xpath)

@then("Recipe is visible in Collection")
def step_impl(context):
    recipe_xpath = "/html/body/div/div[2]/div[2]/div/div/div/ul/li/div/div[1]/a"
    wait_for_element_visibility(context, recipe_xpath)
    recipe_element = context.driver.find_element(By.XPATH, recipe_xpath)
    logging.info(f"Recipe title is {context.recipe_title}")
    logging.info(f"Recipe title on Dashboard is: {recipe_element.text}")
    assert recipe_element.text == context.recipe_title

# Scenario Outline: User can add a Collection with the same name as a deleted Collection

@when("User enters a specific title: {title}")
def step_impl(context, title):
    logging.info(f"Adding Collection with title: {title}")
    title_xpath = "/html/body/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/label/input"
    wait_for_element_visibility(context, title_xpath)
    title_element = context.driver.find_element(By.XPATH, title_xpath)
    context.specific_title_text = title
    title_element.send_keys(context.specific_title_text)

@when("User adds a Collection with title: {title}")
def step_impl(context, title):
    context.execute_steps(f"""
    When User clicks Collections tab
    When User adds a new Collection
    When User enters a specific title: {title}
    When User clicks Save
    """)

@then("Error: {error_message}, does not appear")
def step_impl(context, error_message):
    message_xpath = "/html/body/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul/li"
    wait_for_element_visibility(context, message_xpath)
    message_element = context.driver.find_element(By.XPATH, message_xpath)
    assert message_element.text != error_message