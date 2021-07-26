from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/catalogue/page-1.html"
source = requests.get(url).text

soup = BeautifulSoup(source, 'html.parser')

divs = soup.find_all("article", class_="product_pod")

for div in divs:
    title = div.h3.text
    price = div.find("p", class_="price_color").text
    in_stock = div.find("p", class_="instock availability").text
    print(dict({
        "Title": title,
        "Price": price.replace("Â£", "$"),
        "Available": in_stock.strip()
    }))

categories = soup.find("ul", class_="nav-list").li.ul

category_list = []
for category in categories.find_all("li"):
    category_list.append(category.text.strip())

print(dict({
    "Categories": [category_items for category_items in category_list]
}))

