import pytest
from selenium import webdriver

from utils.ReadExcel import get_data, get_login_data


def pytest_addoption(parser):
    parser.addini("base_url", "App URL")
    parser.addini("excel_file", "Excel file path")
    parser.addini("sheet_name", "Login sheet name")
    parser.addini("app_username", "Login username")
    parser.addini("app_password", "Login password")

def pytest_metadata(metadata):
    metadata["Project"] = "Sauce Demo : Selenium Automation"
    metadata["Tester"] = "Vani Galag"

@pytest.fixture()
def driver_setup(pytestconfig):
    opts = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,  # Disables the "Save password?" prompt
        "profile.password_manager_enabled": False,  # Disables password manager
        "profile.password_manager_leak_detection": False  # Disables the "Change your password" pop-up
    }

    # 3. Add the preferences as an experimental option
    opts.add_experimental_option("prefs", prefs)
    #Disable Extensions : Chrome loads extensions by default which slows startup.
    opts.add_argument("--disable-extensions")
    #Disable Background Networking : Stops Chrome from calling Google services.
    #Prevents logs like:PHONE_REGISTRATION_ERROR
    opts.add_argument("--disable-background-networking")
    #Reduce Chrome Logs : This suppresses most Chrome warnings.
    opts.add_argument("--log-level=3")


    driver = webdriver.Chrome(opts)
    driver.maximize_window()
    driver.get(pytestconfig.getini("base_url"))
    yield driver
    driver.quit()

'''
Used in test_login
'''
def pytest_generate_tests(metafunc):
    login_data  = get_login_data(metafunc.config.getini("excel_file"),
                                       metafunc.config.getini("sheet_name"))
    if "valid_user" in metafunc.fixturenames:
        valid_data, _ = login_data
        metafunc.parametrize("valid_user", valid_data)

    if "invalid_user" in metafunc.fixturenames:
        _, invalid_data = login_data
        metafunc.parametrize("invalid_user", invalid_data)