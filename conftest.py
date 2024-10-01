# conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--product-name", action="store", default=None, help="Name of the product to search"
    )


@pytest.fixture(scope="session")  # Changed to session scope
def product_name(request):
    return request.config.getoption("--product-name")

