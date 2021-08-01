
# #!/usr/bin/env python
from selenium import webdriver

url = "https://www.saucedemo.com/"
user = 'standard_user'
password = 'secret_sauce'

options = webdriver.ChromeOptions()
options.add_argument("--headless") 
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')

print ('Starting the browser...')

driver = webdriver.Chrome(options=options)
print ('Starting login with ', user, ' and ', password)
driver.get(url)
driver.find_element_by_id("user-name").send_keys(user)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("login-button").click()

print("User successfully logged in")

inventory_items = driver.find_elements_by_class_name("inventory_item")
for item in inventory_items:
    title = item.find_element_by_class_name("inventory_item_name").text
    item.find_element_by_css_selector("button[class='btn btn_primary btn_small btn_inventory']").click()
    print("Adding... ", title, " to the cart")

print('Finished adding all items to the cart')

print("Go to shopping car...")
driver.find_element_by_class_name("shopping_cart_link").click()
print('on cart page')

cart_item = driver.find_elements_by_class_name("cart_item")
for item in cart_item:
    title = item.find_element_by_class_name("inventory_item_name").text
    item.find_element_by_css_selector("button[class='btn btn_secondary btn_small cart_button']").click()
    print("Removing...  ", title, " from the cart")

print('Finished removing all items in the cart')


