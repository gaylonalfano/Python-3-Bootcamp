# Beautiful Soup book scraper version following Colt's Scraping to DB
import sqlite3
import requests
from bs4 import BeautifulSoup

# Request the URL
response = requests.get("http://books.toscrape.com/catalogue/category/books/history_32/index.html")
# Initialize BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# Extract the data we want (title, price, rating)
books = soup.find_all("article")
for book in books:
    # Get the title:
    # title = book.find("h3").find("a")["title"]
    # # Get the price:
    # price = book.select(".price_color")[0].get_text()  # Â£54.23
    # # Replace/get rid of the currency symbols and convert to float:
    # price = float(price.replace("Â","").replace("£",""))
    # Get the review. It's hard because it's a class within a class
    # Create a dict to help convert str rating to int:
    ratings = {"Five": 5, "Four": 4, "Three": 3, "Two": 2, "One": 1, "Zero": 0}
    # If you don't add [0] after .select()[0], then you get an error
    # since it's trying to get_text() on a LIST instead of the element.
    paragraph = book.select(".star-rating")[0]
    # Retrieve the STR rating ('Five', 'Four', etc.)
    str_rating = paragraph.get_attribute_list("class")[1]
    int_rating = ratings[str_rating]
    print(int_rating) # 5, 1, 1, ...
    #print(title, price)

# print(books)

# Save dave to the database