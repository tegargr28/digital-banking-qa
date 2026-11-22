import pytest
from automation.utils.driver_factory import create_driver


@pytest.fixture
def driver():
    browser = create_driver()
    yield browser
    browser.quit()
