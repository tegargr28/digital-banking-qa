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


@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.regression
def test_valid_transfer_moves_the_exact_amount(driver):
    """TRF-TC-001: a valid transfer between own accounts moves exactly the
    entered amount: source decreases and destination increases by 10.00."""
    LoginPage(driver).load(BASE_URL).login(PARABANK_USERNAME, PARABANK_PASSWORD)
    WebDriverWait(driver, 10).until(
        lambda d: "overview" in d.current_url.lower()
    )
    app_root = BASE_URL.rsplit("/", 1)[0]

    overview = AccountsOverviewPage(driver)
    before = overview.account_balances()

    # Only some accounts can take part in a transfer: the overview also
    # lists loan accounts, which the Transfer Funds form does not offer.
    # Choose the pair from the accounts the form actually offers.
    overview.go_to_transfer_funds()
    page = TransferPage(driver)
    eligible = page.available_account_ids()

    if len(eligible) < 2:
        # The shared demo data resets periodically, and after a reset the
        # demo login may hold fewer than two transfer-eligible accounts;
        # open a savings account as setup, the same approach as manual
        # session EXEC-008.
        driver.get(f"{app_root}/overview.htm")
        overview = AccountsOverviewPage(driver)
        before = overview.account_balances()
        funding = (
            max(eligible, key=lambda a: before.get(a, 0.0))
            if eligible
            else max(before, key=before.get)
        )
        overview.open_savings_account(funding)
        driver.get(f"{app_root}/overview.htm")
        overview = AccountsOverviewPage(driver)
        before = overview.account_balances()
        overview.go_to_transfer_funds()
        page = TransferPage(driver)
        eligible = page.available_account_ids()

    assert len(eligible) >= 2, (
        f"Need at least two transfer-eligible accounts, got {eligible}"
    )

    # Use the richest eligible account as the source so the transfer posts.
    from_id = max(eligible, key=lambda a: before.get(a, float("-inf")))
    to_id = next(a for a in eligible if a != from_id)

    page.transfer(from_id, to_id, f"{AMOUNT:.2f}")
    assert "Transfer Complete" in page.confirmation_text()

    driver.get(f"{app_root}/overview.htm")
    after = AccountsOverviewPage(driver).account_balances()

    assert round(before[from_id] - after[from_id], 2) == AMOUNT, (
        f"Source {from_id}: {before[from_id]} -> {after[from_id]}"
    )
    assert round(after[to_id] - before[to_id], 2) == AMOUNT, (
        f"Destination {to_id}: {before[to_id]} -> {after[to_id]}"
    )
