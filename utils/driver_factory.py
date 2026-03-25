from selenium import webdriver


def getchromedriver(config):
    opts = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,  # Disables the "Save password?" prompt
        "profile.password_manager_enabled": False,  # Disables password manager
        "profile.password_manager_leak_detection": False  # Disables the "Change your password" pop-up
    }

    # 3. Add the preferences as an experimental option
    opts.add_experimental_option("prefs", prefs)
    # Disable Extensions : Chrome loads extensions by default which slows startup.
    opts.add_argument("--disable-extensions")
    # Disable Background Networking : Stops Chrome from calling Google services.
    # Prevents logs like:PHONE_REGISTRATION_ERROR
    opts.add_argument("--disable-background-networking")
    # Reduce Chrome Logs : This suppresses most Chrome warnings.
    opts.add_argument("--log-level=3")

    driver = webdriver.Chrome(opts)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(config["base_url"])