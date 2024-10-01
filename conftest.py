# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--product-name", action="store", default=None, help="Name of the product to search"
    )
    parser.addoption(
        "--headless", action="store_true", help="Run tests in headless mode."
    )


@pytest.fixture(scope="session")  # Changed to session scope
def product_name(request):
    return request.config.getoption("--product-name")


@pytest.fixture(scope='module')
def browser(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1920,1080")

    # Enable headless mode if the --headless option is set
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
