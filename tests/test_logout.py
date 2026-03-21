from pages.LoginPage import LoginPage

class TestLogout:
    def test_logout(self,driver_setup,pytestconfig):
        login_page = LoginPage(driver_setup)
        home = login_page.login(pytestconfig.getini("app_username"),
                                pytestconfig.getini("app_password"))
        home.logout()
        assert login_page.is_login_page()