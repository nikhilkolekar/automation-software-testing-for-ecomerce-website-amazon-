from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
# Open Amazon website
driver.get("https://www.amazon.in")

# Wait for a few seconds to allow the page to load
time.sleep(5)

# Print the title of the page to confirm it opened correctly
print(driver.title)

# Close the browser
driver.quit()

# give a python selenium automated testing code for opening amazon website 
# in chrome and get signed in and update location pin code
# and search for software testing textbook and adding to cart and proceed buying it