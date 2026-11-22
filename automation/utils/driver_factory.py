"""WebDriver factory for the Digital Banking QA automation suite.

The driver is configured exclusively through ``automation.utils.config``
(which reads the environment / ``.env``):

- ``BROWSER``   -- only ``chrome`` is supported at present.
- ``HEADLESS``  -- ``true`` runs Chrome without a display (required in CI);
  ``false`` runs a visible, maximised browser for local debugging.

No browser is left running after a session: callers own the driver and
must call ``driver.quit()`` (the ``driver`` fixture in ``conftest.py``
already does this).
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from automation.utils.config import BROWSER, HEADLESS


def build_chrome_options(headless: bool = HEADLESS) -> Options:
    """Build Chrome options for the requested mode.

    Kept separate from :func:`create_driver` so the option set can be
    unit-checked without launching a browser.
    """
    options = Options()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        # Flags required for Chrome to start reliably inside CI
        # containers / runners without a real display or sandbox.
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
    else:
        options.add_argument("--start-maximized")
    return options


def create_driver(browser: str = BROWSER, headless: bool = HEADLESS):
    """Create a WebDriver instance for the configured browser."""
    if browser != "chrome":
        raise ValueError(
            f"Unsupported browser {browser!r}: only 'chrome' is supported."
        )
    return webdriver.Chrome(options=build_chrome_options(headless))
