from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

CORRECT_ITEM = (By.ID, 'td.product-thumbnail')


@given('Open GetTop homepage')
def open_gettop_homepage(context):
    context.app.main_page.open_main_page()


@when('Click on Mac in header')
def click_mac_in_header(context):
    context.app.header.click_product_tab()


@when('Hover over first item')
def hover_over_first_item(context):
    context.app.header.hover_over_first_item()


@when('Hover over heart icon')
def hover_over_heart_icon(context):
    context.app.header.hover_over_heart_icon()


@when('Click heart icon to add to wishlist')
def click_heart_icon(context):
    context.click()


@then('Verify that correct item is shown in wishlist')
def verify_correct_item_in_wishlist(context):
    context.driver.find_element(CORRECT_ITEM)
