'''
Colt's refactored version using CSV. Doesn't want to write to CSV each time game is run.
I actually wrote to CSV the first time I started building this app. Here's my old code:

# SAVED TO CSV: SCRAPE PAGE FOR QUOTES, AUTHORS, BIO URLS. WORKS.
# num = 1
# with open("web_scraping_quotes.csv", "a") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Quote", "Author", "BioURL"])
#     request_url = "http://quotes.toscrape.com/page/"
#     while True:
#         r = requests.get(request_url+str(num))
#         soup = BeautifulSoup(r.text, "html.parser")
#         try:
#             next_page_href= soup.find(class_="next").find("a")["href"]
#             next_page_number = int(next_page_href[-2:-1])
#         except AttributeError:
#             print("Looks like you've reached the last page. Total number of pages is: " + str(num))
#             break
#         quotes = [quote.get_text() for quote in soup.select(".quote .text")]
#         authors = [author.get_text() for author in soup.select(".author")]
#         bios_urls = [bio.find_next_sibling("a")["href"] for bio in soup.select(".author")]
#         for i in range(len(quotes)):
#             csv_writer.writerow([quotes[i], authors[i], bios_urls[i]])
        
#         print(f"Completed page: {num}. Waiting 3 seconds to start page: {num+1}")
#         time.sleep(3)
#         num += 1

'''
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

quotes = scrape_quotes()
# After we scrape, we then need to write quotes to CSV file
with open("web_scraping_colt_quotes.csv", "w") as file:
    csv_writer = DictWriter(file, fieldnames=["text", "author", "bio-link"])
    csv_writer.writeheader()
    for quote in quotes:
        csv_writer.writerow(quote)