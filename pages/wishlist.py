from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pages.basepage import Page

class Wishlist(Page):

    def click_remove_this_product(self):
        self.click()
