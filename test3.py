from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (assuming you are using Chrome)
driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

   

    # Define the word to find
word_to_find = "Hello, sign in"

    # Locate the element containing the word (using XPath here, adjust as needed)
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{word_to_find}')]"))
    )

    # Click on the element
element.click()

try:
    # Open the Amazon login page
   

    # Wait for the email input field to be present
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ap_email_login"))
    )

    # Enter the email
    email_input.send_keys("iamnikhilkolekar@gmail.com")

    # Find the continue button and click it
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "continue"))
    )
    continue_button.click()

    # Wait for some time to observe the result of the click
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
