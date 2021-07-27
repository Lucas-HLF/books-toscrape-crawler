from bs4 import BeautifulSoup
import requests
import time


url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
source = requests.get(url).text

soup = BeautifulSoup(source, 'html.parser')


def find_books():
    books_div = soup.find_all("article", class_="product_pod")
    books_list = []
    for div in books_div:
        title = div.h3.text
        price = div.find("p", class_="price_color").text
        in_stock = div.find("p", class_="instock availability").text
        
        books_list.append({
            "Title": title,
            "Price": price.replace("Â£", "$"),
            "Stock": in_stock.strip()
        })

    return books_list


def find_categories():
    categories_items = soup.find("ul", class_="nav-list").li.ul

    categories_list = []
    for category in categories_items.find_all("li"):
        categories_list.append({
            "Category": category.a.text.strip(),
            "Href": category.a['href']
        })                
    
    return categories_list


if __name__ == "__main__":
    categories = find_categories()

    for key in categories:
        url = f"https://books.toscrape.com/catalogue/category/{key['Href'][3::]}"
        source = requests.get(url).text

        soup = BeautifulSoup(source, 'html.parser')

        books = find_books()
        print((key["Category"],
        books))
        time.sleep(10)
