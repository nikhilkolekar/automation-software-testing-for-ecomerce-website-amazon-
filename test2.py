from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (assuming you are using Chrome)
driver = webdriver.Chrome()

try:
    # Open a webpage (replace 'your_website_url' with the actual URL)
    driver.get("https://www.amazon.in")

    # Wait for the page to load
    time.sleep(2)

    # Define the word to find
    word_to_find = "Hello, sign in"

    # Locate the element containing the word (using XPath here, adjust as needed)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{word_to_find}')]"))
    )

    # Click on the element
    element.click()

    # Wait for some time to observe the result of the click
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
