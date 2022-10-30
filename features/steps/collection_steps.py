from multiprocessing.connection import wait
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

from utils import wait_for_element_visibility

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
    title_xpath = "/html/body/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/label/input"
    wait_for_element_visibility(context, title_xpath)
    title_element = context.driver.find_element(By.XPATH, title_xpath)
    context.title_text = f"{title} {random.randint(0, 1000)}"
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