
# #!/usr/bin/env python
from selenium import webdriver
from datetime import datetime

url = "https://www.saucedemo.com/"
user = 'standard_user'
password = 'secret_sauce'

options = webdriver.ChromeOptions()
options.add_argument("--headless") 
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')

log_arr = []
log_file = 'selenium_log.txt'

def log(logtext):
    time = datetime.now().strftime("%Y-%m-%dT%H:%M:%SK")
    print(logtext+' '+time)
    log_arr.append(logtext+time)

log('Starting the browser...')

driver = webdriver.Chrome(options=options)

log('Starting login with '+user+' and '+password)

driver.get(url)
driver.find_element_by_id("user-name").send_keys(user)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("login-button").click()

log("User successfully logged in")

inventory_items = driver.find_elements_by_class_name("inventory_item")
for item in inventory_items:
    title = item.find_element_by_class_name("inventory_item_name").text
    item.find_element_by_css_selector("button[class='btn btn_primary btn_small btn_inventory']").click()
    log("Adding... "+title+" to the cart")

log('Finished adding all items to the cart')

log("Go to shopping car...")
driver.find_element_by_class_name("shopping_cart_link").click()
log('on cart page')

cart_item = driver.find_elements_by_class_name("cart_item")
for item in cart_item:
    title = item.find_element_by_class_name("inventory_item_name").text
    item.find_element_by_css_selector("button[class='btn btn_secondary btn_small cart_button']").click()
    log("Removing...  "+title+" from the cart")

log('Finished removing all items in the cart')

with open(log_file, "a+") as file:
    for line in log_arr:
        file.write("".join(line)+"\n")
