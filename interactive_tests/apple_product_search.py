# pytest -s interactive_tests/apple_product_search.py
# This test require user input either Macbook or iPhone 16

import os
from pytest_bdd import given, when, then, scenarios
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config  # Import the Config class from config.py

# Ensure the screenshots directory exists
screenshots_dir = '/screenshots'
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)

# Set up WebDriver options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set up the WebDriver (Chrome here; this can be changed based on the browser you prefer)
service = Service(
    executable_path='C:\\Users\\dhira\\Documents\\Selenium WebDriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the Apple website
driver.get("https://www.apple.com")
time.sleep(2)  # Wait for 2 seconds to allow the page to load

# Initialize WebDriverWait
wait = WebDriverWait(driver, 20)


def scroll_and_click(element):
    """Scrolls the element into view and clicks it."""
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(1)  # Optional: wait to ensure scroll is complete
    element.click()


def search_product(product_name):
    """Function to search for a product and click on it based on the user input."""
    # Wait for the search icon to be clickable and click it
    search_icon = wait.until(EC.element_to_be_clickable((By.ID, "globalnav-menubutton-link-search")))
    scroll_and_click(search_icon)

    # Wait for the search input field to be visible, then type the product name and press Enter
    search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".globalnav-searchfield-input")))
    search_input.send_keys(product_name)
    search_input.send_keys(Keys.ENTER)
    time.sleep(2)


def select_and_buy_iphone():
    """Function to select and buy iPhone 16 Pro."""
    # Wait for the 'iPhone 16 Pro and iPhone 16 Pro Max' link and click on it
    iphone_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "iPhone 16 Pro and iPhone 16 Pro Max")))
    time.sleep(2)  # Wait 2 seconds before clicking
    # Take screenshot after product search
    driver.save_screenshot(os.path.join(screenshots_dir, "iphone_search_result.png"))
    driver.execute_script("arguments[0].click();", iphone_link)

    # Click on the 'Buy' button
    buy_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Buy")))
    driver.execute_script("arguments[0].click();", buy_button)

    # Click on iPhone 16 Pro or Pro Max
    iphone_model = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#\\3Ar7\\3A_label .form-selector-title")))
    driver.execute_script("arguments[0].click();", iphone_model)

    # Click on the phone color
    iphone_color = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".colornav-item:nth-child(1) .colornav-swatch")))
    driver.execute_script("arguments[0].click();", iphone_color)

    time.sleep(2)  # Wait 2 seconds before clicking

    # Click on iPhone storage
    iphone_storage = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#\\3Are\\3A_label .form-selector-title")))
    driver.execute_script("arguments[0].click();", iphone_storage)

    # driver.execute_script("window.scrollTo(0, 0897);")

    # Click on iPhone noTradeIn_label
    iphone_noTradeIn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#noTradeIn_label .form-selector-title")))
    driver.execute_script("arguments[0].click();", iphone_noTradeIn)

    # Click on iPhone payment buy
    # Locate using data-autom attribute
    iphone_buy_label = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autom='purchaseGroupOptionfullprice_price']")))
    driver.execute_script("arguments[0].click();", iphone_buy_label)
    time.sleep(2)  # Wait 2 seconds before clicking

    # Click on iPhone carrier
    iphone_carrier = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rf-bfe-dimension-simfree")))
    driver.execute_script("arguments[0].click();", iphone_carrier)
    time.sleep(2)  # Wait 2 seconds before clicking

    # Click on iPhone apple care
    iphone_apple_care = wait.until(EC.element_to_be_clickable((By.ID, "applecareplus_58_noapplecare_label")))
    driver.execute_script("arguments[0].click();", iphone_apple_care)
    driver.execute_script("window.scrollTo(0, 3200);")
    time.sleep(3)  # Wait 3 seconds before clicking

    # Wait for the 'Add to Cart' button to be clickable and click on it
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Add to Bag']]")))
    driver.execute_script("arguments[0].click();", add_to_cart_button)

    # Take screenshot after product is added to bag
    time.sleep(2)  # Wait for the bag to update
    driver.save_screenshot(os.path.join(screenshots_dir, "iphone_added_to_bag.png"))

    # Wait for the 'Proceed' or 'Review Bag' button to be clickable and click on it
    proceed_button = wait.until(EC.element_to_be_clickable((By.NAME, "proceed")))
    driver.execute_script("arguments[0].click();", proceed_button)

    # Take screenshot of the review bag page
    time.sleep(2)  # Wait for the review bag page to load
    driver.save_screenshot(os.path.join(screenshots_dir, "iphone_review_bag.png"))

    # remove or delete added item
    iphone_delete = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autom='bag-item-remove-button']")))
    driver.execute_script("arguments[0].click();", iphone_delete)


def select_and_buy_macbook():
    """Function to select and buy MacBook Pro."""
    # Wait for the 'MacBook Pro - Apple' link and click on it
    macbook_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "MacBook Pro - Apple")))
    time.sleep(2)  # Wait 2 seconds before clicking
    # Take screenshot after product search
    driver.save_screenshot(os.path.join(screenshots_dir, "macbook_search_result.png"))
    driver.execute_script("arguments[0].click();", macbook_link)

    # Click on the 'Buy' button
    buy_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Buy")))
    driver.execute_script("arguments[0].click();", buy_button)

    tab_rb_button = wait.until(EC.element_to_be_clickable((By.ID, "tab-:rb:-2")))
    driver.execute_script("arguments[0].click();", tab_rb_button)

    css_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#panel-\\3Arb\\3A-2 .column:nth-child(2) .button")))
    driver.execute_script("arguments[0].click();", css_button)

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.NAME, "add-to-cart")))
    driver.execute_script("arguments[0].click();", add_to_cart_button)

    # Take screenshot after product is added to bag
    time.sleep(2)  # Wait for the bag to update
    driver.save_screenshot(os.path.join(screenshots_dir, "macbook_added_to_bag.png"))

    proceed_button = wait.until(EC.element_to_be_clickable((By.NAME, "proceed")))
    driver.execute_script("arguments[0].click();", proceed_button)

    # Take screenshot of the review bag page
    time.sleep(2)  # Wait for the review bag page to load
    driver.save_screenshot(os.path.join(screenshots_dir, "macbook_review_bag.png"))

    # Remove the added item
    macbook_delete = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autom='bag-item-remove-button']")))
    driver.execute_script("arguments[0].click();", macbook_delete)


# product search either with partial match or lower case or upper case
def product_to_search(input_str, target_str):
    input_str = input_str.lower()
    target_str = target_str.lower()
    return input_str in target_str or target_str in input_str


def get_valid_product_choice(max_attempts=3):
    for attempt in range(max_attempts):
        user_choice = input(
            f"Enter the product you want to search for (iPhone or Macbook) (attempt {attempt + 1}/{max_attempts}): ").strip()

        if product_to_search(user_choice, "iphone"):
            return "iphone"
        elif product_to_search(user_choice, "macbook"):
            return "macbook"
        else:
            print("Invalid input. Please enter 'iPhone' or 'MacBook'.")

    return None


# Main execution
product_choice = get_valid_product_choice()

if product_choice == "iphone":
    search_product("iPhone 16 Pro Max")
    select_and_buy_iphone()
elif product_choice == "macbook":
    search_product("MacBook Pro")
    select_and_buy_macbook()
else:
    print("Maximum attempts reached. Please try again later.")

# Close the browser
time.sleep(2)
driver.quit()
