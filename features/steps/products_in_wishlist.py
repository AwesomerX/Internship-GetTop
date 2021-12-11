from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


PRODUCT = (By.ID, 'td.product-thumbnail')
PRODUCT_NAME = (By.CSS_SELECTOR, 'td.product-name')
WISHLIST = (By.CSS_SELECTOR, 'h1.uppercase.mb-0')
SHARE = (By.CSS_SELECTOR, 'div.yith-wcwl-share.social-icons.share-icons.share-row')

# Given

@given('Open GetTop homepage')
def open_gettop_homepage(context):
    context.app.main_page.open_main_page()
 #   context.app.main_page.


# When

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


@when('Verify product is in wishlist')
def verify_product_in_wishlist(context):
    context.driver.find_element(PRODUCT_NAME)


@when('Verify correct product in wishlist')
def verify_correct_product_in_wishlist(context):
    context.driver.find_element(PRODUCT)




# Then

@then('Verify correct product in wishlist')
def verify_correct_product_in_wishlist(context):
    context.driver.find_element(PRODUCT)


@then('Click the remove this product button')
def click_remove_product_button(context):
    context.driver.find_element(By.ID, 'a.remove.remove_from_wishlist').click()


@then('Verify that product is removed from wishlist')
def verify_product_removed_from_wishlist(context):
    context.driver.find_element(By.ID, 'div.message-container.container.success-color.medium-text-center')


@then('Click on product in wishlist')
def click_on_product(context):
    context.driver.find_element(PRODUCT)


@then('Verify user is redirected to the correct product page')
def verify_correct_product_page(context):
    context.driver.find_element(PRODUCT_NAME)


@then('Verify redirect to wishlist page')
def verify_redirect_to_wishlist(context):
    context.driver.find_element(WISHLIST)


@then('Verify social logos shown on wishlist page')
def verify_social_logos_present(context):
    context.driver.find_element(SHARE)



