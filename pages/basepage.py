class Page:



    def __init__(self, driver):
        self.driver = driver
        self.base_url = ('https://gettop.us/')

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, page_address=''):
        self.driver.get(f'{self.base_url}{page_address}')

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)