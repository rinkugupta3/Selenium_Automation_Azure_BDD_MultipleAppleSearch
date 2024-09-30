import logging
from typing import Any

import pytest
from selenium import webdriver

# Set up logging
log_file = 'test_results.txt'
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        logging.FileHandler('test_results.txt', mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()


# Hook to flush and close log handlers after tests
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session: Any, exitstatus: Any) -> None:
    for handler in logger.handlers:
        handler.flush()
        handler.close()


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def page(browser):
    yield browser
