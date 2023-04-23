from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from support.logger import log_method

class BaseObject:

    log = log_method()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        self.log.info(f'element {locator} is visible')
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_present(self, locator):
        self.log.info(f'element {locator} is present')
        return self.wait.until(ec.presence_of_element_located(locator))

    def is_clickable(self, locator):
        self.log.info(f'element {locator} is clickable')
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator):
        self.log.info(f'{locator} element clicked')
        self.is_clickable(locator).click()

    def enter_text(self, locator, text):
        self.log.info(f'{locator},{text} text entered')
        self.is_visible(locator).send_keys(text)

    def get_text(self, locator):
        self.log.info(f'{locator} text received')
        return self.is_visible(locator).text


