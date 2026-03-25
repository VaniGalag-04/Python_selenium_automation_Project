from pages.LoginPage import LoginPage

class TestLogout:
    def test_logout(self,driver_setup,config):
        login_page = LoginPage(driver_setup)
        home = login_page.login(config["app_username"],
                                config["app_password"])
        home.logout()
        assert login_page.is_login_page()