from pathlib import Path

import pytest

from automation.utils.driver_factory import create_driver

SCREENSHOTS_DIR = Path(__file__).resolve().parents[2] / "screenshots"


@pytest.fixture
def driver(request):
    browser = create_driver()
    # Expose the driver to the report hook below so a failing test can
    # be captured as evidence.
    request.node._driver = browser
    yield browser
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot to ``screenshots/`` when a test call fails.

    The screenshot is failure evidence only; it is never taken for
    passing tests and a screenshot failure never masks the real
    test result.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or report.passed:
        return
    browser = getattr(item, "_driver", None)
    if browser is None:
        return
    try:
        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        safe_name = item.name.replace("/", "_").replace("\\", "_")
        browser.save_screenshot(str(SCREENSHOTS_DIR / f"FAILED_{safe_name}.png"))
    except Exception:
        pass
