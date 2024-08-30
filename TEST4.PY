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

    # Wait for the search bar to be present
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )

    # Type the product name into the search bar
    product_name = "laptop"
    search_bar.send_keys(product_name)

    # Press Enter to initiate the search
    search_bar.send_keys(Keys.RETURN)

    # Wait for some time to observe the search results
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
