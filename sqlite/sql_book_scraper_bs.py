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
print(books)

# Save dave to the database