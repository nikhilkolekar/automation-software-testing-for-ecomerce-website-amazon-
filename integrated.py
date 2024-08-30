from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_open_amazon():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.in")
        time.sleep(5)
        print(driver.title)
    finally:
        driver.quit()

def test_click_sign_in():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.in")
        time.sleep(2)
        word_to_find = "Hello, sign in"
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{word_to_find}')]"))
        )
        element.click()
        time.sleep(5)
    finally:
        driver.quit()

def test_login_amazon():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.in")
        word_to_find = "Hello, sign in"
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{word_to_find}')]"))
        )
        element.click()
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_email_login"))
        )
        email_input.send_keys("iamnikhilkolekar@gmail.com")
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()
        time.sleep(5)
    finally:
        driver.quit()

def test_search_product(product_name):
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.in")
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_bar.send_keys(product_name)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(5)
    finally:
        driver.quit()

def test_search_and_click_product(search_query):
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.in")
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)
        first_product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-main-slot .s-result-item h2 a"))
        )
        first_product.click()
        time.sleep(5)
    finally:
        driver.quit()

def test_add_to_cart():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.in")
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_query = "software testing textbook"
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)
        first_product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-main-slot .s-result-item h2 a"))
        )
        first_product.click()
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
        )
        add_to_cart_button.click()
        try:
            no_thanks_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='proceedToRetailCheckout']"))
            )
            no_thanks_button.click()
        except:
            pass
        cart_confirmation = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "huc-v2-order-row-confirm-text"))
        )
        print(cart_confirmation.text)
        driver.get("https://www.amazon.com/gp/cart/view.html")
        cart_items = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sc-list-item-content"))
        )
        for item in cart_items:
            title = item.find_element(By.CSS_SELECTOR, ".sc-product-title").text
            print(f"Product in cart: {title}")
        time.sleep(5)
    finally:
        driver.quit()

def test_best_sellers():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.in")
        best_sellers_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Best Sellers"))
        )
        best_sellers_link.click()
        best_sellers_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "zg-ordered-list"))
        )
        best_seller_items = driver.find_elements(By.CSS_SELECTOR, ".zg-item-immersion .p13n-sc-truncate-desktop-type2")
        print("Top Best Sellers on Amazon:")
        for item in best_seller_items[:10]:
            print(item.text)
        time.sleep(5)
    finally:
        driver.quit()

def test_update_location(zip_code):
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.in")
        location_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link"))
        )
        location_icon.click()
        location_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput"))
        )
        location_input.send_keys(zip_code)
        apply_button = driver.find_element(By.CSS_SELECTOR, "#GLUXZipUpdate .a-button-input")
        apply_button.click()
        location_confirmation = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#GLUXZipConfirmationSection span"))
        )
        print("Location updated:", location_confirmation.text)
        time.sleep(5)
    finally:
        driver.quit()

def test_search_iphone_and_screenshot():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.in")
        time.sleep(5)
        search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.send_keys("iPhone 512GB pink")
        search_bar.send_keys(Keys.RETURN)
        time.sleep(5)
        try:
            first_product = driver.find_element(By.XPATH, "//div[@data-index='0']//h2/a")
            first_product.click()
            time.sleep(5)
            driver.save_screenshot("iphone_512gb_pink.png")
        except Exception as e:
            print("An error occurred:", e)
    finally:
        driver.quit()

def test_amazon_pay_balance():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.in")
        time.sleep(5)
        driver.get("https://www.amazon.in/gp/css/homepage.html?ref_=nav_em_ya_0_1_1_380")
        time.sleep(5)
        try:
            add_money_button = driver.find_element(By.XPATH, "//a[contains(@href, '/gp/sva/addmoney')]")
            add_money_button.click()
            time.sleep(5)
            driver.save_screenshot("add_money_page.png")
            amount_field = driver.find_element(By.XPATH, "//input[@id='1000']")
            amount_field.send_keys("10")
        except Exception as e:
            print("An error occurred:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_open_amazon()
    test_click_sign_in()
    test_login_amazon()
    test_search_product("laptop")
    test_search_and_click_product("Apple iPhone 13 (128GB) - Midnight")
    test_add_to_cart()
    test_best_sellers()
    test_update_location("560037")
    test_search_iphone_and_screenshot()
    test_amazon_pay_balance()
