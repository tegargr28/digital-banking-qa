from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from automation.pages.base_page import BasePage


def _parse_money(text):
    cleaned = text.replace("$", "").replace(",", "").strip()
    if cleaned.startswith("(") and cleaned.endswith(")"):
        cleaned = "-" + cleaned[1:-1]
    return round(float(cleaned), 2)


class AccountsOverviewPage(BasePage):
    """Accounts Overview: the account table shown after login."""

    ACCOUNT_TABLE = (By.ID, "accountTable")
    ACCOUNT_ROWS = (By.CSS_SELECTOR, "#accountTable tbody tr td a")
    TRANSFER_FUNDS_LINK = (By.LINK_TEXT, "Transfer Funds")
    OPEN_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")
    NEW_ACCOUNT_TYPE = (By.ID, "type")
    NEW_ACCOUNT_FROM = (By.ID, "fromAccountId")
    OPEN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "form input[type='submit']")

    def account_balances(self):
        """Return {account_id: balance} for every row of the overview table.

        The demo populates the table asynchronously and unreliably: it can
        render with no rows at all, or with only some of the rows, and fill
        in the rest a moment later. A single read can therefore be empty or
        partial, so read repeatedly until two consecutive reads agree on a
        non-empty table, and only then trust the result.
        """
        self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_TABLE)
        )
        last = {}

        def stable_balances(driver):
            nonlocal last
            current = self._read_balances_once()
            if current and current == last:
                return current
            last = current
            return False

        return WebDriverWait(self.driver, 20).until(stable_balances)

    def _read_balances_once(self):
        table = self.driver.find_element(*self.ACCOUNT_TABLE)
        balances = {}
        for row in table.find_elements(By.CSS_SELECTOR, "tbody tr"):
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) < 2:
                continue  # total row has a different cell layout
            link = cells[0].find_elements(By.TAG_NAME, "a")
            if not link:
                continue
            account_id = link[0].text.strip()
            balances[account_id] = _parse_money(cells[1].text)
        return balances

    def open_savings_account(self, from_account_id):
        """Open a SAVINGS account funded from an existing account.

        Used as test setup when the shared demo login currently holds a
        single account and a transfer test needs two (the demo data resets
        periodically; the same setup was used in manual session EXEC-008).
        """
        self.wait.until(
            EC.element_to_be_clickable(self.OPEN_ACCOUNT_LINK)
        ).click()
        type_select = Select(
            self.wait.until(EC.visibility_of_element_located(self.NEW_ACCOUNT_TYPE))
        )
        type_select.select_by_value("1")  # 0 = CHECKING, 1 = SAVINGS
        # The funding-account dropdown is populated asynchronously; wait
        # until the funding account is actually among its options.
        WebDriverWait(self.driver, 20).until(
            lambda d: str(from_account_id)
            in [
                option.get_attribute("value")
                for option in Select(
                    d.find_element(*self.NEW_ACCOUNT_FROM)
                ).options
            ]
        )
        Select(self.driver.find_element(*self.NEW_ACCOUNT_FROM)).select_by_value(
            str(from_account_id)
        )
        self.driver.find_element(*self.OPEN_ACCOUNT_BUTTON).click()
        self.wait.until(lambda d: "Account Opened" in d.page_source)
        return self

    def go_to_transfer_funds(self):
        self.wait.until(
            EC.element_to_be_clickable(self.TRANSFER_FUNDS_LINK)
        ).click()
        return self
