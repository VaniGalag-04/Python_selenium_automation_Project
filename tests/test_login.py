from pages.LoginPage import LoginPage

class TestLogin:

    def test_valid_login(self,driver_setup,valid_user):
        login_page = LoginPage(driver_setup)
        username,password = valid_user
        home = login_page.login(username,password)
        assert home.isHomePage()

    def test_invalid_login(self,driver_setup,invalid_user):
        login_page = LoginPage(driver_setup)
        username, password, msg = invalid_user
        home = login_page.login(username, password)
        assert msg in login_page.get_error_msg()