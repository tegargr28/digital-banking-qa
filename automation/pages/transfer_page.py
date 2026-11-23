from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from automation.pages.base_page import BasePage


class TransferPage(BasePage):
    """Transfer Funds form."""

    FROM_ACCOUNT = (By.ID, "fromAccountId")
    TO_ACCOUNT = (By.ID, "toAccountId")
    AMOUNT_INPUT = (By.ID, "amount")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "form input[type='submit']")

    def available_account_ids(self):
        """Account IDs offered by the Transfer Funds form.

        Both dropdowns carry the same set, and it is not every account on
        the overview: loan accounts, for example, are listed on the
        Accounts Overview but cannot be selected for a transfer.
        """
        from_select = Select(
            self.wait.until(EC.visibility_of_element_located(self.FROM_ACCOUNT))
        )
        return [
            option.get_attribute("value")
            for option in from_select.options
            if option.get_attribute("value")
        ]

    def transfer(self, from_account_id, to_account_id, amount):
        from_select = Select(
            self.wait.until(EC.visibility_of_element_located(self.FROM_ACCOUNT))
        )
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
