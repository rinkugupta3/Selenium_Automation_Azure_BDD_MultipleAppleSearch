"""
Project Overview: This project is a Behavior Driven Development (BDD) automation testing framework using Selenium
WebDriver and pytest-bdd for testing Apple's website functionalities. It automates the process of searching for
products, adding them to the shopping cart, taking screenshots at various steps, and removing the products from the
cart. The project is structured around feature files written in Gherkin syntax that describe the test scenarios.
More details listed in project_details.txt file
"""
# Install....pip show webdriver_manager ; pip show webdriver_manager ; pip install -r requirements.txt
# Selenium and BDD don't include interactive user input during test execution. Instead,
# we define the scenarios and their inputs in the feature file "apple_search.feature".
# The browser should not close between the MacBook Pro and iPhone tests.
# The same browser instance should be used for all scenarios
# Run test with command:
# pytest -v -s tests/test_apple_product_search_bdd_gerkin_cucumber.py --product=MacBook
# pytest -v -s tests/test_apple_product_search_bdd_gerkin_cucumber.py
# pytest -v tests/test_apple_product_search_bdd_gerkin_cucumber.py
# pytest -v -s tests/test_apple_product_search_bdd_gerkin_cucumber.py --html=reportbdd.html

import os
import sys
import time
import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config  # Import Config class
from webdriver_manager.chrome import ChromeDriverManager

# Add the project root to the Python path
sys.path.append(r'C:\Users\dhira\Desktop\Dhiraj HP Laptop\Projects\Selenium_Automation_Azure_BDD_MultipleAppleSearch')

# Load scenarios from feature file
scenarios('../features/apple_search.feature')

# Ensure the screenshots directory exists
screenshots_dir = 'C:\\Users\\dhira\\Desktop\\Dhiraj HP ' \
                  'Laptop\\Projects\\Selenium_Automation_Azure_BDD_MultipleAppleSearch\\screenshots'
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)


# Fixture for WebDriver either module or session
@pytest.fixture(scope='module')
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


@given("I am on the Apple homepage")
def open_apple_homepage(browser):
    browser.get(Config.HOMEPAGE_URL)
    time.sleep(2)


@when(parsers.parse('I search for the "{product}"'))
def search_for_product(browser, product):
    search_icon = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "globalnav-menubutton-link-search"))
    )
    search_icon.click()

    search_input = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".globalnav-searchfield-input"))
    )
    search_input.send_keys(product)
    search_input.send_keys(Keys.ENTER)
    time.sleep(2)


@then(parsers.parse('a screenshot of the search "{product}" should be taken'))
def take_search_screenshot(browser, product):
    screenshot_path = os.path.join(Config.SCREENSHOTS_DIR, f"{browser.current_url.split('/')[-1]}_search_result.png")
    browser.save_screenshot(screenshot_path)


@when(parsers.parse('I add the first "{product}" result to the bag'))
def add_product_to_bag(browser, product):
    if "MacBook Pro" in browser.title:
        select_and_buy_macbook(browser)
    elif "iPhone" in browser.title:
        select_and_buy_iphone(browser)
    else:
        raise Exception("Unknown product page")


@then('I should be able to proceed to the review bag')
def proceed_to_review_bag(browser):
    try:
        proceed_button = WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.NAME, "proceed")))
        browser.execute_script("arguments[0].click();", proceed_button)
    except TimeoutException:
        pytest.fail("Timeout while proceeding to review bag")


@then(parsers.parse('a screenshot of the reviewed "{product}" should be taken'))
def take_review_screenshot(browser, product):
    time.sleep(2)
    screenshot_path = os.path.join(Config.SCREENSHOTS_DIR, f"{browser.current_url.split('/')[-1]}_review_bag.png")
    browser.save_screenshot(screenshot_path)


@then(parsers.parse('the "{product}" should be removed or deleted from the bag'))
def remove_product_from_bag(browser, product):
    try:
        delete_button = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autom='bag-item-remove-button']"))
        )
        browser.execute_script("arguments[0].click();", delete_button)
    except TimeoutException:
        pytest.fail(f"Timeout while waiting for '{product}' to be in the bag or finding the delete button")


@then("I return to the Apple homepage")
def return_to_homepage(browser):
    try:
        apple_home_page = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.globalnav-link-apple"))
        )
        # Click the Apple home page button
        browser.execute_script("arguments[0].click();", apple_home_page)
        time.sleep(2)  # Give some time for the homepage to load
    except TimeoutException:
        # If the link is not clickable, fallback to direct navigation
        browser.get(Config.HOMEPAGE_URL)
        time.sleep(2)


@then("I close the browser")
def close_browser(browser):
    browser.quit()


def select_and_buy_iphone(browser):
    """Function to select and buy iPhone 16 Pro."""
    # Wait for the 'iPhone 16 Pro and iPhone 16 Pro Max' link and click on it
    iphone_link = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "iPhone 16 Pro and "
                                                                                             "iPhone 16 Pro Max")))
    time.sleep(2)  # Wait 2 seconds before clicking
    # Take screenshot after product search
    browser.save_screenshot(os.path.join(Config.SCREENSHOTS_DIR, "iphone_search_result.png"))
    browser.execute_script("arguments[0].click();", iphone_link)

    # Click on the 'Buy' button
    buy_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Buy")))
    browser.execute_script("arguments[0].click();", buy_button)

    # Click on iPhone 16 Pro or Pro Max
    iphone_model = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#\\3Ar7\\3A_label "
                                                                                                 ".form-selector-title")))
    browser.execute_script("arguments[0].click();", iphone_model)

    # Click on the phone color
    iphone_color = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".colornav-item:nth-child(1) .colornav-swatch")))
    browser.execute_script("arguments[0].click();", iphone_color)

    time.sleep(2)  # Wait 2 seconds before clicking

    # Click on iPhone storage
    iphone_storage = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#\\3Are\\3A_label .form-selector-title")))
    browser.execute_script("arguments[0].click();", iphone_storage)

    # browser.execute_script("window.scrollTo(0, 0897);")

    # Click on iPhone noTradeIn_label
    iphone_noTradeIn = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#noTradeIn_label .form-selector-title")))
    browser.execute_script("arguments[0].click();", iphone_noTradeIn)

    # Click on iPhone payment buy
    # Locate using data-autom attribute
    iphone_buy_label = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autom='purchaseGroupOptionfullprice_price']")))
    browser.execute_script("arguments[0].click();", iphone_buy_label)
    time.sleep(2)  # Wait 2 seconds before clicking

    # Click on iPhone carrier
    iphone_carrier = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rf-bfe-dimension"
                                                                                                   "-simfree")))
    browser.execute_script("arguments[0].click();", iphone_carrier)
    time.sleep(2)  # Wait 2 seconds before clicking

    # Click on iPhone apple care
    iphone_apple_care = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "applecareplus_58_noapplecare_label")))
    browser.execute_script("arguments[0].click();", iphone_apple_care)
    browser.execute_script("window.scrollTo(0, 3200);")
    time.sleep(3)  # Wait 3 seconds before clicking

    # Wait for the 'Add to Cart' button to be clickable and click on it
    add_to_cart_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span["
                                                                                                "text()='Add to "
                                                                                                "Bag']]")))
    browser.execute_script("arguments[0].click();", add_to_cart_button)


"""
    # Take screenshot after product is added to bag
    time.sleep(2)  # Wait for the bag to update
    browser.save_screenshot(os.path.join(Config.SCREENSHOTS_DIR, "iphone_added_to_bag.png"))

    # Wait for the 'Proceed' or 'Review Bag' button to be clickable and click on it
    proceed_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.NAME, "proceed")))
    browser.execute_script("arguments[0].click();", proceed_button)

    # Take screenshot of the review bag page
    time.sleep(2)  # Wait for the review bag page to load
    browser.save_screenshot(os.path.join(Config.SCREENSHOTS_DIR, "iphone_review_bag.png"))

    # remove or delete added item
    iphone_delete = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autom='bag"
                                                                                                  "-item-remove"
                                                                                                  "-button']")))
    browser.execute_script("arguments[0].click();", iphone_delete)
"""


def select_and_buy_macbook(browser):
    """Function to select and buy MacBook Pro."""
    # Wait for the 'MacBook Pro - Apple' link and click on it
    macbook_link = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "MacBook Pro - Apple")))
    time.sleep(2)  # Wait 2 seconds before clicking
    # Take screenshot after product search
    browser.save_screenshot(os.path.join(Config.SCREENSHOTS_DIR, "macbook_search_result.png"))
    browser.execute_script("arguments[0].click();", macbook_link)

    # Click on the 'Buy' button
    buy_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Buy")))
    browser.execute_script("arguments[0].click();", buy_button)

    tab_rb_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "tab-:rb:-2")))
    browser.execute_script("arguments[0].click();", tab_rb_button)

    css_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#panel-\\3Arb\\3A-2 .column:nth-child(2) .button")))
    browser.execute_script("arguments[0].click();", css_button)

    add_to_cart_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.NAME, "add-to-cart")))
    browser.execute_script("arguments[0].click();", add_to_cart_button)


"""
    # Take screenshot after product is added to bag
    time.sleep(2)  # Wait for the bag to update
    browser.save_screenshot(os.path.join(Config.SCREENSHOTS_DIR, "macbook_added_to_bag.png"))

    proceed_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.NAME, "proceed")))
    browser.execute_script("arguments[0].click();", proceed_button)

    # Take screenshot of the review bag page
    time.sleep(2)  # Wait for the review bag page to load
    browser.save_screenshot(os.path.join(Config.SCREENSHOTS_DIR, "macbook_review_bag.png"))

    # Remove the added item
    macbook_delete = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autom='bag"
                                                                                                   "-item-remove"
                                                                                                   "-button']")))
    browser.execute_script("arguments[0].click();", macbook_delete)
"""

"""
used code snippet to execute pytest test cases directly from the script itself, 
rather than running them separately from the command line. 
It ensures that the test code only runs when the script is executed as the main program, 
and not when it's imported as a module.
"""

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
