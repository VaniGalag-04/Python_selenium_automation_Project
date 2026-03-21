from pages.Locators import password_text
from pages.LoginPage import LoginPage
from utils import TestData


class TestLogout:
    def test_logout(self,driver_setup):
        login_page = LoginPage(driver_setup)
        home = login_page.login(TestData.app_username, TestData.app_password)
        home.logout()
        assert login_page.is_login_page() is True