# To get new chrome driver https://googlechromelabs.github.io/chrome-for-testing/#stable
# pytest -s tests/Macbook_search.py

import time  # Import time to use sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set up the WebDriver (assuming Chrome here; this can be changed based on the browser you prefer)
service = Service(executable_path='C:\\Users\\dhira\\Documents\\Selenium WebDriver\\chromedriver.exe')  # Update with actual path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the Apple website
driver.get("https://www.apple.com")
time.sleep(2)  # Wait for 2 seconds to allow the page to load

# Initialize WebDriverWait
wait = WebDriverWait(driver, 20)

# Wait for the search icon to be clickable and then click on it
search_icon = wait.until(EC.element_to_be_clickable((By.ID, "globalnav-menubutton-link-search")))
time.sleep(1)  # Wait 1 second before clicking
search_icon.click()

# Wait for the search input field to be visible, then type 'MacBook Pro' and press Enter
search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".globalnav-searchfield-input")))
time.sleep(1)  # Wait 1 second before typing
search_input.send_keys("MacBook Pro")
search_input.send_keys(Keys.ENTER)

# Wait for the 'MacBook Pro - Apple' link and click on it
macbook_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "MacBook Pro - Apple")))
time.sleep(2)  # Wait 2 seconds before clicking
macbook_link.click()

# Scroll the window
time.sleep(1)  # Wait before scrolling
driver.execute_script("window.scrollTo(0, 20);")

# Click on the 'Buy' button
buy_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Buy")))
time.sleep(2)  # Wait 2 seconds before clicking
buy_button.click()

# Click on the element with ID 'tab-:rb:-2'
tab_rb_button = wait.until(EC.element_to_be_clickable((By.ID, "tab-:rb:-2")))
time.sleep(2)  # Wait 2 seconds before clicking
tab_rb_button.click()

# Click on the button using the CSS selector
css_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#panel-\\3Arb\\3A-2 .column:nth-child(2) .button")))
time.sleep(2)  # Wait 2 seconds before clicking
css_button.click()

# Wait for the 'Add to Cart' button to be clickable and click on it
add_to_cart_button = wait.until(EC.element_to_be_clickable((By.NAME, "add-to-cart")))
time.sleep(2)  # Wait 2 seconds before clicking
add_to_cart_button.click()

# Wait for the 'Proceed' or 'Review Bag' button to be clickable and click on it
proceed_button = wait.until(EC.element_to_be_clickable((By.NAME, "proceed")))
time.sleep(2)  # Wait 2 seconds before clicking
proceed_button.click()

# remove or delete added item
macbook_delete = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autom='bag-item-remove-button']")))
driver.execute_script("arguments[0].click();", macbook_delete)

# Close the browser
time.sleep(2)  # Final wait before closing the browser
driver.quit()
