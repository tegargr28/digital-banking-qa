import pytest
from selenium.webdriver.support.ui import WebDriverWait

from automation.pages.accounts_overview_page import AccountsOverviewPage
from automation.pages.login_page import LoginPage
from automation.pages.transfer_page import TransferPage
from automation.utils.config import (
    BASE_URL,
    PARABANK_PASSWORD,
    PARABANK_USERNAME,
)

AMOUNT = 10.00


@pytest.mark.ui
@pytest.mark.regression
def test_valid_transfer_moves_the_exact_amount(driver):
    """TRF-TC-001: a valid transfer between own accounts moves exactly the
    entered amount: source decreases and destination increases by 10.00."""
    LoginPage(driver).load(BASE_URL).login(PARABANK_USERNAME, PARABANK_PASSWORD)
    WebDriverWait(driver, 10).until(
        lambda d: "overview" in d.current_url.lower()
    )

    overview = AccountsOverviewPage(driver)
    before = overview.account_balances()
    if len(before) < 2:
        # The shared demo data resets periodically and the demo login
        # currently holds a single account; open a second one as setup,
        # the same approach as manual session EXEC-008.
        overview.open_savings_account(next(iter(before)))
        app_root = BASE_URL.rsplit("/", 1)[0]
        driver.get(f"{app_root}/overview.htm")
        overview = AccountsOverviewPage(driver)
        before = overview.account_balances()
    assert len(before) >= 2, f"Need at least two accounts, got {before}"

    # Use the richest account as the source so the transfer can post.
    from_id = max(before, key=before.get)
    to_id = next(a for a in before if a != from_id)

    overview.go_to_transfer_funds()
    page = TransferPage(driver).transfer(from_id, to_id, f"{AMOUNT:.2f}")
    assert "Transfer Complete" in page.confirmation_text()

    app_root = BASE_URL.rsplit("/", 1)[0]
    driver.get(f"{app_root}/overview.htm")
    after = AccountsOverviewPage(driver).account_balances()

    assert round(before[from_id] - after[from_id], 2) == AMOUNT, (
        f"Source {from_id}: {before[from_id]} -> {after[from_id]}"
    )
    assert round(after[to_id] - before[to_id], 2) == AMOUNT, (
        f"Destination {to_id}: {before[to_id]} -> {after[to_id]}"
    )
