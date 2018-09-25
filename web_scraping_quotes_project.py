"""
Web Scraping Project
Introduction
In this project you'll be building a quotes guessing game. When run, your program will scrape a website for a collection of quotes. Pick one at random and display it. The player will have four chances to guess who said the quote. After every wrong guess they'll get a hint about the author's identity.

Requirements
Create a file called `scraping_project.py` which, when run, grabs data on every quote from the website http://quotes.toscrape.com
You can use `bs4` and `requests` to get the data. For each quote you should grab the text of the quote, the name of the person who said the quote, and the href of the link to the person's bio. Store all of this information in a list.
Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
After each incorrect guess, the number of guesses remaining will decrement. If the player gets to zero guesses without identifying the author, the player loses and the game ends. If the player correctly identifies the author, the player wins!
After every incorrect guess, the player receives a hint about the author. 
For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell the player the author's birth date and location.
The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the author's last name, the number of letters in one of the names, etc.
When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. If no, the program is complete.

REFERENCES FROM BLOG SCRAPING PROGRAM:

STUDENT SOLUTION TRY/EXCEPT WHILE LOOP
import requests
from bs4 import BeautifulSoup
from csv import writer
 
num = 1
with open('blog_data.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow(['Title', 'URL', 'Date'])
        while True:
                response = requests.get('https://www.rithmschool.com/blog?page='+str(num)) #returns response code/ .text returns html               
                soup = BeautifulSoup(response.text, 'html.parser')
                try:
                        pageNo = int(soup.find(class_='page current').get_text())
                except AttributeError:
                        print('You have reached the last page. Total no. of pages = ' + str(num-1))
                        break
                articles = soup.find_all('article')
                for i in articles:
                        a_tag = i.find('a')
                        title = a_tag.get_text()
                        url = a_tag['href']
                        date = i.find('time')['datetime']
                        csv_writer.writerow([title, url, date])
                                
                num += 1

KEY LEARNINGS:
1. soup.select(".class tag")  # List of all matches! Ex. soup.select(".pagination a")
2. pages[0].get("href") OR pages[0]["href"]  # /blog?page=n
3. time.sleep(10) to delay between requests
4. Call a function in another function: range(1, get_total_pages()+1)
5. soup.select("article a") returns a list of 25 articles on the site, regardless of pages...not sure why
6. Can open two files at once:  with open(file1) as fsock1, open(file2, 'a') as fsock2:
7. Don't always try to refactor as you go... sometimes get stuck and don't complete functionality
8. Where/how should I utilize functions in this?

"""

import requests, csv, time
from bs4 import BeautifulSoup

# SAVED TO LIST: SCRAPE PAGE FOR QUOTES, AUTHORS, BIO URLS
num = 1
with open("web_scraping_quotes.csv", "a") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Quote", "Author", "BioURL"])
    request_url = "http://quotes.toscrape.com/page/"
    while True:
        r = requests.get(request_url+str(num))
        soup = BeautifulSoup(r.text, "html.parser")
        try:
            next_page_href= soup.find(class_="next").find("a")["href"]
            next_page_number = int(next_page_href[-2:-1])
        except AttributeError:
            print("Looks like you've reached the last page. Total number of pages is: " + str(num))
            break
        quotes = [quote.get_text() for quote in soup.select(".quote .text")]
        authors = [author.get_text() for author in soup.select(".author")]
        bios_urls = [bio.find_next_sibling("a")["href"] for bio in soup.select(".author")]
        for i in range(len(quotes)):
            csv_writer.writerow([quotes[i], authors[i], bios_urls[i]])
        
        print(f"Completed page: {num}. Waiting 3 seconds to start page: {num+1}")
        time.sleep(3)
        num += 1

# Can I create a function where you pass 'soup' and it then generates
# quotes, authors, bios, etc.?





# SAVED TO CSV: SCRAPE PAGE FOR QUOTES, AUTHORS, BIO URLS
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


# QUOTES HELPER
# r = requests.get("http://quotes.toscrape.com")
# soup = BeautifulSoup(r.text, "html.parser")

# GOOD. Page numbers next page
# print(soup.find(class_="next").find("a")["href"])  # /page/2/
# next_page_href = soup.find(class_="next").find("a")["href"]
# next_page_number = int(next_page_href[-2:-1])
# print(next_page_number)

# GOOD. Quotes
# print(soup.select(".quote .text"))
# quotes = [quote.get_text() for quote in soup.select(".quote .text")]
# print(quotes[0])
# for q in quotes:
#     print(q)

# GOOD. Authors
# print(soup.find(class_="author").get_text())
# print(soup.select(".author"))
# print(soup.find_all(class_="author"))
#authors = [author.get_text() for author in soup.select(".author")]
#print(authors[0])
# for author in authors:
#     print(author.get_text())

# GOOD. Author Bio URL
# bios = soup.select(".author a")  - won't work since a isn't descendent of author
# about = soup.select(".author")
# for a in about:
#     print(a.find_next_sibling("a")["href"])
# bios_urls = [bio.find_next_sibling("a")["href"] for bio in soup.select(".author")]
# print(bios_urls[0])
# test = soup.find_all(class_="author")
# for t in test:
#     print(t.find_next_sibling("a")["href"])

# Function to extract_write quote, author, and bio url????
# def extract_quote_author_bio():
#     """Extract all quotes, authors, and bio URLs from a page"""