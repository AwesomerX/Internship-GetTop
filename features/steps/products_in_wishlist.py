from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@given('Open GetTop homepage')
def open_gettop_homepage(context):
    context.driver.get('https://gettop.us/')


@when('Click on Mac in header')
def click_mac_in_header(context):
    context.driver.find_element(By.CSS_SELECTOR, 'li.menu-item-468.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-468.has-dropdown').click()

@when('Hover over first item')
def hover_over_first_item(context):
    context.app.header.hover_over_first_item()


@when('Hover over heart icon')
def hover_