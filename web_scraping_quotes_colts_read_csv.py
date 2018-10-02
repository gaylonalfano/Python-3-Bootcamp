# Now for simply READING the CSV results

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

#all_quotes = []  # During refactoring, moved to inside scrape_quotes()
BASE_URL = "http://quotes.toscrape.com"  # This is a CONSTANT, so should use CAPS (originally 'base_url')
#url = "/page/1"  # During refactoring, moved to inside scrape_quotes()

def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        print(f"Now scraping {BASE_URL}{url}...")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
        next_button = soup.find(class_="next")
        url = next_button.find("a")["href"] if next_button else None  # Neat one liner
        sleep(2)
    return all_quotes


# After we scrape, we then need to write quotes to CSV file
# This now works. But we can refactor so that we don't scrape every time. But before that, 
# let's create a new function write_quotes()

def write_quotes(quotes):
    with open("web_scraping_colt_quotes.csv", "w") as file:
        csv_writer = DictWriter(file, fieldnames=["text", "author", "bio-link"])
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)