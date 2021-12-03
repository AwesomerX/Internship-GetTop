from pages.mainpage import Mainpage
from pages.header import Header


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = Mainpage(self.driver)
        self.header = Header(self.driver)
