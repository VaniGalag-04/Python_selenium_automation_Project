import pytest

from utils import driver_factory
from utils.ReadExcel import get_data, get_login_data

'''
This registers a new config key for pytest
which is present in pytest.ini
'''
def pytest_addoption(parser):
    parser.addini("config_path", "File containing path to config file")

'''
 metadata fields in test reports
'''
def pytest_metadata(metadata):
    metadata["Project"] = "Sauce Demo : Selenium Automation"
    metadata["Tester"] = "Vani Galag"

# conftest.py

'''
Helper function
storing data inside pytest config object
- Read JSON once
- Cache it
- Reuse everywhere (hooks + fixtures)
'''
def load_config(config):
    #skips loading again
    if not hasattr(config, "_json_data"):
        path = config.getini("config_path")
        import json
        with open(path) as f:
            config._json_data = json.load(f)
    return config._json_data

@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver_setup")
        if driver:
            driver.save_screenshot("failure.png")

@pytest.fixture()
def driver_setup(config):
    driver = driver_factory.getchromedriver(config)
    yield driver
    driver.quit()

'''
Used in test_login
'''
def pytest_generate_tests(metafunc):
    if "valid_user" in metafunc.fixturenames or "invalid_user" in metafunc.fixturenames:
        config_data = load_config(metafunc.config)
        login_data  = get_login_data(config_data["excel_file"],
                                           config_data["sheet_name"])
    if "valid_user" in metafunc.fixturenames:
        valid_data, _ = login_data
        metafunc.parametrize("valid_user", valid_data, ids=[f"{u[0]}" for u in valid_data])

    if "invalid_user" in metafunc.fixturenames:
        _, invalid_data = login_data
        metafunc.parametrize("invalid_user", invalid_data, ids=[f"{u[2]}" for u in invalid_data])