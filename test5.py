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

    # Type "iPhone" into the search bar
    search_query = "Apple iPhone 13 (128GB) - Midnight"
    search_bar.send_keys(search_query)

    # Press Enter to initiate the search
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    first_product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-main-slot .s-result-item h2 a"))
    )

    # Click on the first product in the search results
    first_product.click()

    # Wait for some time to observe the product page
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()










# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Set up the WebDriver (assuming you are using Chrome)
# driver = webdriver.Chrome()

# try:
#     # Open the Amazon homepage
#     driver.get("https://www.amazon.in")

#     # Wait for the search bar to be present
#     search_bar = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
#     )

#     # Type "iPhone" into the search bar
#     search_query = "Apple iPhone 13 (128GB) - Midnight"
#     search_bar.send_keys(search_query)

#     # Press Enter to initiate the search
#     search_bar.send_keys(Keys.RETURN)

#     # Wait for the search results to load
#     search_results = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".s-main-slot .s-result-item"))
#     )

#     # Click on the first product in the search results
#     first_product = search_results[0].find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
#     first_product.click()

#     # Wait for some time to observe the product page
#     time.sleep(5)

# finally:
#     # Close the browser
#     driver.quit()
