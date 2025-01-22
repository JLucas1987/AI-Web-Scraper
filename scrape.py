from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the product page
driver.get('https://www.mscdirect.com/product/123456789')

# Extract the Brand
brand = driver.find_element(By.CSS_SELECTOR, '.product-brand').text

# Extract the title
title = driver.find_element(By.CSS_SELECTOR, '.product-title').text

# Extract the MSC product #
msc_product_number = driver.find_element(By.CSS_SELECTOR, '.product-number').text

# Extract the Manufacturer model #
manufacturer_model_number = driver.find_element(By.CSS_SELECTOR, '.manufacturer-model-number').text

# Extract the price
price = driver.find_element(By.CSS_SELECTOR, '.product-price').text

# Extract the quantity available
quantity_available = driver.find_element(By.CSS_SELECTOR, '.product-availability').text

# Print the extracted information
print(f"Brand: {brand}")
print(f"Title: {title}")
print(f"MSC product #: {msc_product_number}")
print(f"Manufacturer model #: {manufacturer_model_number}")
print(f"Price: {price}")
print(f"Quantity available: {quantity_available}")

# Close the browser
driver.quit()
