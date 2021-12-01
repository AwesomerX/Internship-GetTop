from pages.main_page import main_page
from pages.header import Header


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = main_page(self.driver)
        self.header = Header(self.driver)