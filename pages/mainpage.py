from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.basepage import Page


class Mainpage(Page):
        def open_main_page(self):
            self.open_page()

