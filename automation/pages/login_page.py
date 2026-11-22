from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from automation.pages.base_page import BasePage


class LoginPage(BasePage):
    """Customer Login form on the ParaBank home page."""

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Log In']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.error")

    def load(self, base_url):
        return self.open(base_url)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def error_text(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return element.text
