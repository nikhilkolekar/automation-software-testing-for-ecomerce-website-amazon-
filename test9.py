from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to the ChromeDriver
chrome_driver_path = r'C:\Users\HP\OneDrive\Desktop\Testing\chromedriver.exe'
driver = webdriver.Chrome(service=ChromeService(chrome_driver_path))

# Open the Amazon homepage
driver.get("https://www.amazon.in")

# Wait for the page to load completely
time.sleep(5)

# Find the search bar and search for iPhone 512GB pink
search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
search_bar.send_keys("iPhone 512GB pink")
search_bar.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(5)

try:
    # Locate the first product link in the search results
    first_product = driver.find_element(By.XPATH, "//div[@data-index='0']//h2/a")
    first_product.click()
    
    # Wait for the product page to load
    time.sleep(5)

    # Optionally, take a screenshot of the product page
    driver.save_screenshot("iphone_512gb_pink.png")
    
except Exception as e:
    print("An error occurred:", e)

# Close the browser
driver.quit()
