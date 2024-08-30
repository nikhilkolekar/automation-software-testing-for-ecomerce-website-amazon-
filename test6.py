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

    # Type "software testing textbook" into the search bar
    search_query = "software testing textbook"
    search_bar.send_keys(search_query)

    # Press Enter to initiate the search
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load and locate the first product link
    first_product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-main-slot .s-result-item h2 a"))
    )

    # Click on the first product in the search results
    first_product.click()

    # Wait for the product page to load
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
    )

    # Click the "Add to Cart" button
    add_to_cart_button.click()

    # Optional: Handle any pop-ups or additional steps (e.g., protection plans)
    # For example, handle the "No thanks" button if a warranty pop-up appears
    try:
        no_thanks_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='proceedToRetailCheckout']"))
        )
        no_thanks_button.click()
    except:
        pass  # If no pop-up appears, proceed

    # Wait for the cart confirmation to ensure the product was added
    cart_confirmation = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "huc-v2-order-row-confirm-text"))
    )

    # Print confirmation text
    print(cart_confirmation.text)

    # Navigate to the cart page
    driver.get("https://www.amazon.com/gp/cart/view.html")

    # Wait for the cart page to load and display the cart items
    cart_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sc-list-item-content"))
    )

    # Print out the product titles in the cart
    for item in cart_items:
        title = item.find_element(By.CSS_SELECTOR, ".sc-product-title").text
        print(f"Product in cart: {title}")

    # Wait for some time to observe the cart
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
