import requests
from bs4 import BeautifulSoup
import time

total_products = 0
# download the html document
# with an HTTP get request
for page_number in range(1, 13):
    response = requests.get(f"https://www.scrapingcourse.com/ecommerce/page/{page_number}")

    if response.ok:
        print(f"\n\nPage Number: {page_number}\n")
        soup = BeautifulSoup(response.content, "html.parser")

        parent_element = soup.find(class_="products")
        if parent_element is not None:

            product_name = parent_element.findAll(class_="product-name")
            for name in product_name:
                print(name.getText())
                total_products+=1
            # image_url = parent_element.findAll("img")["src"]
            # price = parent_element.findAll(class_="price").getText()
            # if price is not None and image_url is not None:
            #     print(price)
            #     print(f"Image URL: {image_url}")
            # else:
            #     print("The price is not right!")
    else:
        print("Didn't Work!")


print(f"Total Products: {total_products}")