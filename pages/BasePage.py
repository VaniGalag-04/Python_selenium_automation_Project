from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()


    def enter_text(self, locator, text):
        if text is not None:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.send_keys(text)
            # self.driver.find_element(*locator).send_keys(text)

    def is_element_present(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def get_msg(self, locator):
        return self.driver.find_element(*locator).text