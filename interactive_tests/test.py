from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://www.apple.com/shop/buy-iphone/iphone-16-pro")

try:
    # Wait until the iPhone model element is clickable
    # iphone_model = WebDriverWait(browser, 20).until(
        # EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-autom="dimensionScreensize6_3inch"]')))
    iphone_model = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#\\3Ar7\\3A_label "
                                                                                                 ".form-selector-title")))
    # Click the element using JavaScript
    browser.execute_script("arguments[0].click();", iphone_model)
    print("Click executed successfully!")

except Exception as e:
    print(f"Error encountered: {e}")

finally:
    # Optionally take a screenshot to confirm click action
    browser.save_screenshot("after_click.png")

    # Close the browser
    browser.quit()
