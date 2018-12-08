# Beautiful Soup book scraper version following Colt's Scraping to DB
import sqlite3
import requests
from bs4 import BeautifulSoup


def scrape_books(url):
    '''Scrape the url for books'''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        # Store in tuple
        book_data = (get_title(book), get_price(book), get_rating(book))
        # Store to all_books list:
        all_books.append(book_data)
    # Call save_books function to store in database:
    save_books(all_books)

def save_books(all_books):
    '''Connects to database and performs a bulk insert'''
    # 1. Establish connection to db
    connection = sqlite3.connect("/Users/gaylonalfano/Python Projects/ModernPython3Bootcamp/sqlite/books.db")
    # 2. Create cursor object
    c = connection.cursor()
    # 3. Execute some SQL
    # If running this often, better to just first create db/table outside of Python:
    c.execute('''CREATE TABLE books 
        (title TEXT, price REAL, rating INTEGER)''')
    query = "INSERT INTO books VALUES (?,?,?)"
    c.executemany(query, all_books)
    # 4. Commit your changes
    connection.commit()
    # 5. Close connection to db
    connection.close()

def get_title(book):
    return book.find("h3").find("a")["title"]

def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("Â","").replace("£",""))

def get_rating(book):
    ratings = {"Five": 5, "Four": 4, "Three": 3, "Two": 2, "One": 1, "Zero": 0}
    paragraph = book.select(".star-rating")[0]
    str_rating = paragraph.get_attribute_list("class")[1]
    int_rating = ratings[str_rating]
    return int_rating

# Now we call the functions to scrape and store:
scrape_books("http://books.toscrape.com/catalogue/category/books/history_32/index.html")

# BELOW IS SPAGHETTI CODE. ABOVE IS REFACTORED VERSION.

# # Request the URL
# response = requests.get("http://books.toscrape.com/catalogue/category/books/history_32/index.html")
# # Initialize BeautifulSoup
# soup = BeautifulSoup(response.text, "html.parser")
# # Extract the data we want (title, price, rating)
# books = soup.find_all("article")
# for book in books:
#     # Get the title:
#     title = book.find("h3").find("a")["title"]
#     # Get the price:
#     price = book.select(".price_color")[0].get_text()  # Â£54.23
#     # Replace/get rid of the currency symbols and convert to float:
#     price = float(price.replace("Â","").replace("£",""))
#     # Get the review. It's hard because it's a class within a class
#     # Create a dict to help convert str rating to int:
#     ratings = {"Five": 5, "Four": 4, "Three": 3, "Two": 2, "One": 1, "Zero": 0}
#     # If you don't add [0] after .select()[0], then you get an error
#     # since it's trying to get_text() on a LIST instead of the element.
#     paragraph = book.select(".star-rating")[0]
#     # Retrieve the STR rating ('Five', 'Four', etc.)
#     str_rating = paragraph.get_attribute_list("class")[1]
#     int_rating = ratings[str_rating]
#     print(int_rating) # 5, 1, 1, ...
#     #print(title, price)

# Save dave to the database