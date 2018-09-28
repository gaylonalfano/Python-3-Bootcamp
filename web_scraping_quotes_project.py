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
from random import choice, randint

# SAVED TO LIST: SCRAPE PAGE FOR QUOTES, AUTHORS, BIO URLS
# Create a function that extracts ONE page of data
# def extract_single_page(soup):
#     """Create a function that extracts ONE page of data"""
#     quotes = [quote.get_text() for quote in soup.select(".quote .text")]
#     authors = [author.get_text() for author in soup.select(".author")]
#     bios_urls = [bio.find_next_sibling("a")["href"] for bio in soup.select(".author")]
#     single_page_quotes= []
#     for i in range(len(quotes)):
#         single_page_quotes.append({
#             "quote": quotes[i],
#             "author": authors[i],
#             "bio_url": bios_urls[i]
#         })
#     return single_page_quotes


# num = 1
# request_url = "http://quotes.toscrape.com/page/"
# all_quotes = []
# while True:
#     r = requests.get(request_url+str(num))
#     soup = BeautifulSoup(r.text, "html.parser")
#     try:
#         next_page_href= soup.find(class_="next").find("a")["href"]
#         next_page_number = int(next_page_href[-2:-1])
#     except AttributeError:
#         print(f"Tried to find page {next_page_number} but only scraped {str(num)} pages total.")
#         break
#     all_quotes.append(extract_single_page(soup))
#     print(f"Completed page: {num}. Waiting 1 second to start page: {num+1}")
#     time.sleep(1)
#     num += 1

# print(all_quotes)  # Only works if I run the program... doesn't seem to store for long-term use. Ugh.
# print(len(all_quotes))  
# print(num-1)  # Should be 9 since num started at 1




# # Guessing game logic
# number_of_guesses = 4
# while number_of_guesses > 0:
#     random_quote = all_quotes[randint(0, num-1)][:2]  # num started at 1.
#     print(f"Let's play a guessing game. You have {number_of_guesses} chances to guess the correct author of a quote.")
#     print(f"Here's the quote: {random_quote}")
#     number_of_guesses -= 1


# print(extract_all_pages())
#test_list = extract_all_pages()
# print("PRINTING TEST LIST")
# print(test_list)
# all_data = []
# for page in extract_all_pages():
#     for entry in page:
#         all_data.append(entry)


# extracted_data = [entry for entry in page for page in extract_all_pages()]
# print(all_data)












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



# FUNCTION HELPER
# Function to extract_write quote, author, and bio url????
# def extract_quote_author_bio():
#     """Extract all quotes, authors, and bio URLs from a page"""

# Tried a function for the request part BUT every time I needed to access the 
# returned list of data, it always had to rerun the request.get(). Don't think this is
# necessary. Best would be to run it once and then store the data. Going to keep with
# creating a function to extract one a single page.
# def extract_all_pages():
#     """Create a function that extracts ALL pages of data"""
#     num = 1
#     request_url = "http://quotes.toscrape.com/page/"
#     all_pages_quotes_authors_bios = []
#     while True:
#         r = requests.get(request_url+str(num))
#         soup = BeautifulSoup(r.text, "html.parser")
#         try:
#             next_page_href= soup.find(class_="next").find("a")["href"]
#             next_page_number = int(next_page_href[-2:-1])
#         except AttributeError:
#             print(f"Tried to find page {next_page_number} but only scraped {str(num)} pages total.")
#             break
#         all_pages_quotes_authors_bios.append(extract_single_page(soup))
#         print(f"Completed page: {num}. Waiting 3 seconds to start page: {num+1}")
#         time.sleep(3)
#         num += 1
#     return all_pages_quotes_authors_bios



# RANDOM QUOTE HELPER
nested = [[{'quote': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'bio_url': '/author/Albert-Einstein'}, {'quote': '“It is our choices, Harry, that show what we trulyare, far more than our abilities.”', 'author': 'J.K. Rowling', 'bio_url': '/author/J-K-Rowling'}, {'quote': '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'author': 'AlbertEinstein', 'bio_url': '/author/Albert-Einstein'}, {'quote': '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'author': 'Jane Austen', 'bio_url': '/author/Jane-Austen'}, {'quote': "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", 'author': 'Marilyn Monroe', 'bio_url': '/author/Marilyn-Monroe'}, {'quote': '“Try not to become a man of success. Rather become a man of value.”', 'author': 'Albert Einstein', 'bio_url': '/author/Albert-Einstein'}, {'quote': '“It is better to be hated for what you are than to be loved for what you are not.”', 'author': 'André Gide', 'bio_url': '/author/Andre-Gide'}, {'quote': "“I have not failed. I've just found 10,000 ways that won't work.”", 'author': 'Thomas A. Edison', 'bio_url': '/author/Thomas-A-Edison'}, {'quote': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'author': 'Eleanor Roosevelt', 'bio_url': '/author/Eleanor-Roosevelt'}, {'quote': '“A day without sunshine is like, you know, night.”', 'author': 'Steve Martin', 'bio_url': '/author/Steve-Martin'}], [{'quote': "“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good partis you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”", 'author': 'Marilyn Monroe', 'bio_url': '/author/Marilyn-Monroe'}, {'quote': '“It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.”', 'author': 'J.K. Rowling', 'bio_url': '/author/J-K-Rowling'}, {'quote': "“If you can't explain it to a six year old, you don't understand it yourself.”", 'author': 'Albert Einstein', 'bio_url': '/author/Albert-Einstein'}, {'quote': "“You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.”", 'author': 'Bob Marley', 'bio_url': '/author/Bob-Marley'}, {'quote': '“I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.”', 'author': 'Dr. Seuss', 'bio_url': '/author/Dr-Seuss'}, {'quote': '“I may not have gone where I intendedto go, but I think I have ended up where I needed to be.”', 'author': 'Douglas Adams', 'bio_url': '/author/Douglas-Adams'}, {'quote': "“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite offaith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”", 'author': 'Elie Wiesel', 'bio_url': '/author/Elie-Wiesel'}, {'quote': '“It is not a lack of love, but a lack of friendship that makes unhappy marriages.”', 'author': 'Friedrich Nietzsche', 'bio_url': '/author/Friedrich-Nietzsche'}, {'quote': '“Good friends, good books, and a sleepy conscience: this is the ideal life.”', 'author': 'Mark Twain', 'bio_url': '/author/Mark-Twain'}, {'quote': '“Life is what happens to us while we are making other plans.”', 'author': 'Allen Saunders', 'bio_url': '/author/Allen-Saunders'}]]

random_page = randint(0,len(nested))  # returns int
random_entry = randint(0, random_page)  # returns int
# random_quote = random_entry["quote"]  # necessary
# nested has these layers: List>>pages>>>rows>>>>elements
# What I want is List>>rows>>>elements
# for page in range(len(nested)):
#     for row in nested[page]:
#         print(row)

unnested = [row for row in range(len(nested[page])) for page in range(len(nested))]

print(unnested)
# print(nested)
# #print(test_data[randint(0, len(test_data))][randint()])
# print(nested[0][0]["quote"])
# #print(test_data[randint(0,len(test_data))][randint(0,len(test_data[0]))]["quote"])
# print(nested[random_page][random_entry]["quote"])
