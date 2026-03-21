import time

from pages.BasePage import BasePage
from pages import Locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def isHomePage(self):
        time.sleep(3)
        return self.is_element_present(Locators.product_title)

    def logout(self):
        self.click_element(Locators.menu)
        self.click_element(Locators.logout)



