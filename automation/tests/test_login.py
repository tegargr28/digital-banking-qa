import pytest
from selenium.webdriver.support.ui import WebDriverWait

from automation.pages.login_page import LoginPage
from automation.utils.config import (
    BASE_URL,
    PARABANK_PASSWORD,
    PARABANK_USERNAME,
)


@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.regression
def test_login_with_valid_credentials(driver):
    """AUTH-TC-001: valid demo credentials open the Accounts Overview."""
    page = LoginPage(driver).load(BASE_URL)
    page.login(PARABANK_USERNAME, PARABANK_PASSWORD)

    WebDriverWait(driver, 10).until(
        lambda d: "overview" in d.current_url.lower()
    )
    assert "Accounts Overview" in driver.page_source


@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.xfail(
    reason=(
        "BUG-001: ParaBank web login accepts an invalid password and opens "
        "the Accounts Overview instead of rejecting the login "
        "(observed 2026-11-23; see Bug Reports in test-cases.xlsx). "
        "The REST API rejects the same credentials correctly."
    ),
    strict=False,
)
def test_login_with_invalid_password_is_rejected(driver):
    """AUTH-TC-002: a wrong password is rejected with an error message."""
    page = LoginPage(driver).load(BASE_URL)
    page.login(PARABANK_USERNAME, "definitely-wrong-password")

    error = page.error_text()
    assert "could not be verified" in error.lower(), (
        f"Unexpected login error message: {error!r}"
    )
    assert "overview" not in driver.current_url.lower()
