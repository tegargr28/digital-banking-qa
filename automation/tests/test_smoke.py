import pytest

from automation.pages.home_page import HomePage
from automation.utils.config import BASE_URL


@pytest.mark.smoke
def test_parabank_homepage_loads(driver):
    page = HomePage(driver).load(BASE_URL)

    assert "ParaBank" in page.title(), (
        f"Unexpected page title: {page.title()!r}"
    )
    assert "parabank" in driver.current_url.lower()
