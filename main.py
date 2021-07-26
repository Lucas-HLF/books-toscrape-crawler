from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
source = requests.get(url).text

soup = BeautifulSoup(source, 'html.parser')

def find_books():
    divs = soup.find_all("article", class_="product_pod")
    books_list = []
    for div in divs:
        title = div.h3.text
        price = div.find("p", class_="price_color").text
        in_stock = div.find("p", class_="instock availability").text
        
        books_list.append({
            "Title": title,
            "Price": price.replace("Â£", "$"),
            "Available": in_stock.strip()
        })

    return books_list


def find_categories():
    categories = soup.find("ul", class_="nav-list").li.ul

    categories_list = []
    for category in categories.find_all("li"):
        categories_list.append({
            "Category": category.a.text.strip(),
            "Href": category.a['href']
        })                
    
    return categories_list

if __name__ == "__main__":
    