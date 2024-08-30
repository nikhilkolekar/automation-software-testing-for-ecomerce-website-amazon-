from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# Set up the WebDriver
chrome_driver_path = r'C:\Users\HP\OneDrive\Desktop\Testing\chromedriver.exe'  # Update this path
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open Amazon website
    driver.get("https://www.amazon.in")
    
    # Sign in
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "nav-link-accountList"))
    )
    sign_in_button.click()
    
    email = "mpavan.km@gmail.com"  # Update with your email
    password = "Pavan@662001"  # Update with your password
    
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ap_email"))
    )
    email_input.send_keys(email)
    
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ap_password"))
    )
    password_input.send_keys(password)
    
    sign_in_submit = driver.find_element(By.ID, "signInSubmit")
    sign_in_submit.click()
    
    # Update location with pin code
    location_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link"))
    )
    location_icon.click()
    
    location_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput"))
    )
    zip_code = "560037"  # Example ZIP code
    location_input.send_keys(zip_code)
    
    apply_button = driver.find_element(By.CSS_SELECTOR, "#GLUXZipUpdate .a-button-input")
    apply_button.click()
    
    # Confirm location update
    location_confirmation = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#GLUXZipConfirmationSection span"))
    )
    print("Location updated:", location_confirmation.text)
    
    # Search for software testing textbook
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_query = "Software Engineering: A Practitioner's Approach | 9th Edition"
    search_bar.send_keys(search_query)
    search_bar.send_keys(Keys.RETURN)
    
    # Add the first textbook to the cart
    first_product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-main-slot .s-result-item h2 a"))
    )
    first_product.click()
    
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
    )
    add_to_cart_button.click()
    
    # Handle optional pop-ups
    try:
        no_thanks_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='proceedToRetailCheckout']"))
        )
        no_thanks_button.click()
    except:
        pass
    
    # Proceed to checkout
    proceed_to_checkout = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "hlb-ptc-btn-native"))
    )
    proceed_to_checkout.click()
    
    # Wait for some time to observe the result
    time.sleep(5)
    
finally:
    # Close the browser
    driver.quit()
