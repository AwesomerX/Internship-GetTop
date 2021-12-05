from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pages.basepage import Page


class Header(Page):
    PRODUCT_TABS = (By.CSS_SELECTOR, 'ul.header-nav-main.nav-left.nav-uppercase')
    MAC_TAB = (By.CSS_SELECTOR, 'li.menu-item-468.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-468.has-dropdown')
    IPHONE_TAB = (By.CSS_SELECTOR, 'li.menu-item-469.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-469.has-dropdown')
    IPAD_TAB = (By.CSS_SELECTOR, 'li.menu-item-470.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-470.has-dropdown')
    WATCH_TAB = (By.CSS_SELECTOR, 'li.menu-item-471.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-471.has-dropdown')
    ACCESSORIES_TAB = (By.CSS_SELECTOR, 'li.menu-item-472.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-472.has-dropdown')


    def click_product_tab(self):
        self.click(*self.MAC_TAB)





