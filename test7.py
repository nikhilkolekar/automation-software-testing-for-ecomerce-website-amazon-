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

    # Wait for the 'Best Sellers' link to be present
    best_sellers_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Best Sellers"))
    )

    # Click on the 'Best Sellers' link
    best_sellers_link.click()

    # Wait for the 'Best Sellers' page to load
    best_sellers_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zg-ordered-list"))
    )

    # Find and print the titles of the top products listed in the 'Best Sellers' section
    best_seller_items = driver.find_elements(By.CSS_SELECTOR, ".zg-item-immersion .p13n-sc-truncate-desktop-type2")
    
    print("Top Best Sellers on Amazon:")
    for item in best_seller_items[:10]:  # Limiting to top 10 items
        print(item.text)

    # Wait for some time to observe the result
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
