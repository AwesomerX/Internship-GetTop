from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pages.basepage import Page

class Product_page(Page):

    FIRST_PRODUCT = (By.CSS_SELECTOR, 'div.product-small.has-hover.post-165')
    HEART_ICON = (By.CSS_SELECTOR, 'button.wishlist-button')

    def hover_over_first_item(self):
        lang = self.find_element(*self.FIRST_PRODUCT)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang)
        actions.perform()
        sleep(5)

    def hover_over_heart_icon(self):
        lang = self.find_element(*self.FIRST_PRODUCT)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang)
        actions.click()
        actions.perform()
        sleep(5)

    def click_heart_icon(self):
        lang = self.find_element(self.HEART_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang)
        actions.click()
        actions.perform()
        sleep(3)