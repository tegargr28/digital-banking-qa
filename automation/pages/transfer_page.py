from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from automation.pages.base_page import BasePage


class TransferPage(BasePage):
    """Transfer Funds form."""

    FROM_ACCOUNT = (By.ID, "fromAccountId")
    TO_ACCOUNT = (By.ID, "toAccountId")
    AMOUNT_INPUT = (By.ID, "amount")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "form input[type='submit']")

    def _stable_option_values(self, locator):
        """Option values of a select element, read once they stop changing.

        The form's dropdowns are populated asynchronously: the select is
        visible before its options arrive, so reading them immediately
        can return an empty or partial list. Poll until two consecutive
        reads agree on a non-empty list.
        """
        self.wait.until(EC.visibility_of_element_located(locator))
        last = None

        def read(driver):
            nonlocal last
            select = Select(driver.find_element(*locator))
            values = [
                option.get_attribute("value")
                for option in select.options
                if option.get_attribute("value")
            ]
            if values and values == last:
                return values
            last = values
            return False

        return WebDriverWait(self.driver, 20).until(read)

    def available_account_ids(self):
        """Account IDs offered by the Transfer Funds form, once loaded."""
        return self._stable_option_values(self.FROM_ACCOUNT)

    def transfer(self, from_account_id, to_account_id, amount):
        self._stable_option_values(self.FROM_ACCOUNT)
        from_select = Select(self.driver.find_element(*self.FROM_ACCOUNT))
        from_select.select_by_value(str(from_account_id))
        Select(self.driver.find_element(*self.TO_ACCOUNT)).select_by_value(
            str(to_account_id)
        )
        amount_input = self.driver.find_element(*self.AMOUNT_INPUT)
        amount_input.clear()
        amount_input.send_keys(str(amount))
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        return self

    def confirmation_text(self):
        self.wait.until(lambda d: "Transfer Complete" in d.page_source)
        return self.driver.page_source
