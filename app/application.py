from pages.mainpage import Mainpage
from pages.header import Header
from pages.product_page import Product_page
from pages.wishlist import Wishlist


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = Mainpage(self.driver)
        self.header = Header(self.driver)
        self.product_page = Product_page(self.driver)
        self.wishlist = Wishlist(self.driver)
