"""
REFERENCE from http_requests_headers.py:
import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "text/plain"})  # You won't always get plain text

headers = "Accept": "application/json"
Even better than plain text is JSON (Javascript Object Notation).
It was historically used to request JS, etc. But Python can convert
to Python code easily.

response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()  # .json() returns a DICT
print(data['joke'])
print(f"status: {data['status']}")
#print(response.text)  # Returns a STR

'''
Running .json turns it into Python so then you can use that dictionary.
It's better to request json:

"story1": "terrorist attack",
"story2": "Tiger wins Masters!"
'''

====================================================

FIRST WEB SCRAPING PROGRAM
Going to scrape a site, connect to requests, and write to CSV file

Requests + Beautiful Soup Example:
1. Scrape data into a CSV file
2. Grab all links from Rithm School blog
3. Data: store URL, anchor tag text, and a date

Blog address: https://www.rithmschool.com/blog

Order of Approach:
1. Make request
2. Get response back
3. Take the HTML we get back and send to BS
4. Navigate through that
5. Extract the info we want
6. Write to a file using CSV
"""
import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.rithmschool.com/blog")
# print(response.text)  # All the HTMl

soup = BeautifulSoup(response.text, "html.parser")  # html, "html.parser"
#print(len(soup.find_all("article")))  # 10 articles total
articles = soup.find_all("article")

# DICTWRITER version
with open("scrape_blog_data.csv", "w") as file:
    csv_writer = csv.DictWriter(file, fieldnames=["Title", "URL", "Date"])
    csv_writer.writeheader()
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow({"Title": title, "URL": url, "Date": date})

#WRITER version:
# with open("scrape_blog_data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["title", "link", "date"])
#     for article in articles:
#         a_tag = article.find("a")
#         title = a_tag.get_text()
#         url = a_tag["href"]
#         date = article.find("time")["datetime"]
#         writer.writerow([title, url, date])

    
# AFTER figuring out how to extract what you want (below),
# then work with CSV to write to new file (above).

# for article in articles:
#     # Instead of doing article.find("a") again and again, just make that into a var
#     a_tag = article.find("a")
#     # Find title
#     title = a_tag.get_text()
#     # Find href
#     url = a_tag["href"]  # Same but longer:print(article.find("a").attrs["href"])
#     # Find date
#     #print(a_tag.find_parent().find_next_sibling().attrs)
#     date = article.find("time")["datetime"]
#     print(title, url, date)
    

"""
ADVANCED CHALLENGE - Crawl through all the pages and extract the data
"""
