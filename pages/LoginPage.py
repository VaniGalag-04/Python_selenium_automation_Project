from pages.BasePage import BasePage
from pages import Locators
from pages.HomePage import HomePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self,username,password):
        self.enter_text(Locators.username_text, username)
        self.enter_text(Locators.password_text, password)
        self.click_element(Locators.login_button)
        return HomePage(self.driver)

    def get_error_msg(self):
        return self.get_msg(Locators.error_msg)

    def is_login_page(self):
        return self.is_element_present(Locators.login_button)