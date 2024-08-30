from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (assuming you are using Chrome)
driver = webdriver.Chrome()

try:
    # Open the Amazon homepage
    driver.get("https://www.amazon.in")

    # Wait for the location icon to be present
    location_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link"))
    )

    # Click on the location icon to open the location setting modal
    location_icon.click()

    # Wait for the location input field to be present
    location_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput"))
    )

    # Enter the ZIP code into the location input field
    zip_code = "560037"  # Example ZIP code
    location_input.send_keys(zip_code)

    # Click on the 'Apply' button to set the location
    apply_button = driver.find_element(By.CSS_SELECTOR, "#GLUXZipUpdate .a-button-input")
    apply_button.click()

    # Wait for the location confirmation message
    location_confirmation = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#GLUXZipConfirmationSection span"))
    )

    # Print the confirmation message
    print("Location updated:", location_confirmation.text)

    # Wait for some time to observe the result
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
