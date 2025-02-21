# import necessary libraries

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import csv



# set up chrome driver

service = Service()

options = webdriver.ChromeOptions()

options.add_argument("--headless=new")

driver = webdriver.Chrome(service=service, options=options)



# navigate to the target webpage

driver.get("https://www.scrapingcourse.com/javascript-rendering")



# wait for the product grid to load

WebDriverWait(driver, 10).until(

    EC.presence_of_all_elements_located(

        (By.CSS_SELECTOR, "#product-grid .product-item")

    )

)



# extract product details

products = []

items = driver.find_elements(By.CSS_SELECTOR, "#product-grid .product-item")

for item in items:

    name = item.find_element(By.CSS_SELECTOR, ".product-name").text.strip()

    price = item.find_element(By.CSS_SELECTOR, ".product-price").text.strip()

    image_url = item.find_element(By.CSS_SELECTOR, ".product-image").get_attribute(

        "src"

    )

    products.append({"name": name, "price": price, "imageUrl": image_url})



# specify the CSV headers
headers = ["name", "price", "imageUrl"]

# write the extracted data to a CSV file
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(products)

print("CSV file written successfully.")



# close the driver

driver.quit()
