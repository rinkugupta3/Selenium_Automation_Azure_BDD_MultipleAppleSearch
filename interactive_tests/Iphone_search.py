# To get new chrome driver https://googlechromelabs.github.io/chrome-for-testing/#stable
# used javascript.....driver.execute_script("arguments[0].click();", iphone_delete) because
# JavaScript clicks bypass the issues like....
# (Element not fully visible, Hidden by another element, special styling)
# since they directly invoke the .click() event on the element.
# pytest -s tests/Iphone_search.py

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set up the WebDriver (assuming Chrome here; this can be changed based on the browser you prefer)
service = Service(executable_path='C:\\Users\\dhira\\Documents\\Selenium WebDriver\\chromedriver.exe')  # Update with
# the actual path to chromedriver
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


# Wait for the search icon to be clickable and click it
search_icon = wait.until(EC.element_to_be_clickable((By.ID, "globalnav-menubutton-link-search")))
scroll_and_click(search_icon)

# Wait for the search input field to be visible, then type 'iPhone 16 pro max' and press Enter
search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".globalnav-searchfield-input")))
search_input.send_keys("iPhone 16 pro max")
search_input.send_keys(Keys.ENTER)

# Wait for the 'iPhone 16 pro max' link and click on it
iphone_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "iPhone 16 Pro and iPhone 16 Pro Max")))
driver.execute_script("arguments[0].click();", iphone_link)

# Click on the 'Buy' button
buy_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Buy")))
driver.execute_script("arguments[0].click();", buy_button)

# Click on iPhone 16 Pro or Pro Max
iphone_model = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#\\3Ar7\\3A_label .form-selector-title")))
driver.execute_script("arguments[0].click();", iphone_model)

# Click on the phone color
iphone_color = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".colornav-item:nth-child(1) .colornav-swatch")))
driver.execute_script("arguments[0].click();", iphone_color)

time.sleep(2)  # Wait 2 seconds before clicking

# Click on iPhone storage
iphone_storage = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#\\3Are\\3A_label .form-selector-title")))
driver.execute_script("arguments[0].click();", iphone_storage)

# driver.execute_script("window.scrollTo(0, 0897);")

# Click on iPhone noTradeIn_label
iphone_noTradeIn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#noTradeIn_label .form-selector-title")))
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

# Wait for the 'Proceed' or 'Review Bag' button to be clickable and click on it
proceed_button = wait.until(EC.element_to_be_clickable((By.NAME, "proceed")))
driver.execute_script("arguments[0].click();", proceed_button)

time.sleep(2)  # Wait 2 seconds before clicking

# remove or delete added item
iphone_delete = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autom='bag-item-remove-button']")))
driver.execute_script("arguments[0].click();", iphone_delete)

# Close the browser
time.sleep(2)  # Final wait before closing the browser
driver.quit()
