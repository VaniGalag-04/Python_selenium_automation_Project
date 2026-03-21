import time

from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from utils import TestData
from utils.ReadExcel import ReadExcel


def pytest_generate_tests(metafunc):
    if "login_data" in metafunc.fixturenames:
        file_path = TestData.excel_file
        sheet_name = TestData.sheet_name
        excel = ReadExcel(file_path)
        metafunc.parametrize("login_data", excel.get_data(sheet_name))

class TestLogin:

    def test_login(self,driver_setup,login_data):
        login_page = LoginPage(driver_setup)
        # test_case,username,password,msg = login_data
        home = login_page.login(login_data[TestData.excel_username],login_data[TestData.excel_password])
        if login_data[TestData.excel_test_type] == TestData.valid_type:
            assert home.isHomePage()
        elif login_data[TestData.excel_test_type] == TestData.invalid_type:
            assert login_data[TestData.excel_msg] in login_page.get_error_msg()

