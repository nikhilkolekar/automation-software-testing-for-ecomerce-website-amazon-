from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# Specify the path to the ChromeDriver
chrome_driver_path = r'C:\Users\HP\OneDrive\Desktop\Testing\chromedriver.exe'
driver = webdriver.Chrome(service=ChromeService(chrome_driver_path))

# Open the Amazon homepage
driver.get("https://www.amazon.in")

# Wait for the page to load completely
time.sleep(5)

# Navigate to the Amazon Pay balance page via URL
# Note: The exact URL may vary. This example uses a commonly used URL.
driver.get("https://www.amazon.in/gp/css/homepage.html?ref_=nav_em_ya_0_1_1_380")

# Wait for the page to load completely
time.sleep(5)

try:
    # Attempt to find and click the "Add Money" button
    add_money_button = driver.find_element(By.XPATH, "//a[contains(@href, '/gp/sva/addmoney')]")
    add_money_button.click()
    
    # Wait for the Add Money page to load
    time.sleep(5)

    # Optionally, take a screenshot of the Add Money page
    driver.save_screenshot("add_money_page.png")

    # Optionally, find input fields to enter the amount (do not proceed with actual transaction)
    amount_field = driver.find_element(By.XPATH, "//input[@id='1000']")
    amount_field.send_keys("10")  # Example amount

    # Do not automate the following step for security reasons:
    # submit_button = driver.find_element(By.XPATH, "//input[@name='submit']")
    # submit_button.click()
except Exception as e:
    print("An error occurred:", e)

# Close the browser
driver.quit()
