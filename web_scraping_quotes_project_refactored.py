""""
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

POSSIBLE WAYS TO REFACTOR:
1. Add function for extracting pages
2. Add function for extracting bio info
3. Add function for playing game
4. Classes: Author? Hint? 
5. Add function to build/store hints


KEY LEARNINGS/QUESTIONS:
1. If calling a function that returns a value INSIDE another function, do you 
    still have to add "return"? (Ex. start_guessing() inside has select_parse that returns all_hints list)
2. Good or bad to have parameters for functions? Can become a jumbled mess: generate_hints(select_parse_author_bio(bio_request_url, extract_all_pages(url, all_extracted_data)))
"""
import requests, csv, time
from bs4 import BeautifulSoup
from random import choice, randint
from pyfiglet import figlet_format
from termcolor import colored

# CRAWL ALL PAGES
def extract_all_pages(url):
    """Sends a request and parses HTML. Crawls all pages and extracts data."""
    all_extracted_data = []
    num = 1
    while True:
        response = requests.get(url+str(num))
        quote_soup = BeautifulSoup(response.text, "html.parser")
        try:
            next_page_href = quote_soup.find(class_="next").find("a")["href"]
            next_page_number = int(next_page_href[-2:-1])
        except AttributeError:
            print(f"Scraped {str(num)} pages total...")
            break
        print(f"Scraping page {num}. Please wait...")
        extract_page(quote_soup, all_extracted_data)
        time.sleep(1)
        num += 1
    
    return all_extracted_data

# EXTRACT AUTHOR, QUOTE, BIO URL FOR SINGLE PAGE
def extract_page(quote_soup, extracted_data):
    """Extracts author, quote and bio url from one page"""
    quotes = [quote.get_text() for quote in quote_soup.select(".quote .text")]
    authors = [author.get_text() for author in quote_soup.select(".author")]
    bios_urls = [bio.find_next_sibling("a")["href"] for bio in quote_soup.select(".author")]
    for i in range(len(quotes)):
        extracted_data.append([quotes[i], authors[i], bios_urls[i]])

# EXTRACT BIO PAGE INFO AND GENERATE HINTS
def extract_bio_generate_hints(random_entry): 
    """Randomly select an entry, parse bio page and generate hints"""
    bio_url = "http://quotes.toscrape.com"
    # random_entry = choice(extract_all_pages(url, all_extracted_data))
    response = requests.get(bio_url+random_entry[2])
    bio_soup = BeautifulSoup(response.text, "html.parser")

    # Birthday hint
    birthday_hint = bio_soup.find(class_="author-born-date").get_text()
    birth_location_hint = bio_soup.find(class_="author-born-location").get_text()

    # Initials and letters in name hint
    name = bio_soup.find(class_="author-title").get_text().split(' ')
    initials_hint = name[0][0] + ' ' + name[1][0]
    fn_letters_hint = len(name[0])
    ln_letters_hint = len(name[1])

    # Description w/ name removed
    description = bio_soup.find(class_="author-description").get_text()
    description_hint = description
    name_variations = name
    name_variations.append(name[0] + ' ' + name[1])
    for variation in name_variations:
        description_hint = description_hint.replace(variation, "@"*len(variation))

    # Store all hints
    all_hints = {
        3: f"The author was born {birthday_hint} {birth_location_hint}",
        2: f"The author's initials are: {initials_hint}",
        1: f"The author's first name and last name have {fn_letters_hint} and {ln_letters_hint} letters respectively"
        #1: f"Here's the author's bio with their name removed: {description_hint}"
    }

    return all_hints  # can you return multiple things? Yes, as a tuple is one way.

    #start_guessing(random_entry, all_hints)  # Trouble with random_entry since it's choice()
    #return all_hints # since this returns here does it all return for select_parse if I don't 'return'??

def display_game_title(game_title):
    title = figlet_format(game_title)
    title = colored(title, color='cyan')
    print(title)

def start_guessing(random_entry, hints):
    """Gives user four guesses to guess correct author and displays hint after every incorrect guess"""
    number_of_guesses = 4
    print(f"You have {number_of_guesses} chances to guess the correct author of a quote.")
    print(f"Here's the quote: {random_entry[0]}")
    while number_of_guesses > 0:
        user_guess = input("Guess the author: ")
        if user_guess == random_entry[1]:
            print(f"You're right! The author is: {random_entry[1]}. Great job!")
            break
        elif number_of_guesses-1 == 0:
                print(f"Bummer! You're out of guesses. The correct answer is: {random_entry[1]}")
                break
        else:
            number_of_guesses -= 1
            print(f"That's incorrect. Here's a hint: {hints[number_of_guesses]}")

# PLAY GAME / PLAY AGAIN FUNCTION
def play_game():
    """Launches the game, scrapes data, generates hints, and offers chance to replay"""
    url = "http://quotes.toscrape.com/page/"
    display_game_title("Guess the Author")
    all_extracted_data = extract_all_pages(url)  # Returns all_extracted_data
    while True:
        wanna_play = input("Ready to play? (y/n) ")
        if wanna_play.upper() == "N":
            print("No worries! See you next time.")
            break
        else:
            random_entry = choice(all_extracted_data)
            all_hints = extract_bio_generate_hints(random_entry)
            start_guessing(random_entry, all_hints)

play_game()

#generate_hints(select_parse_author_bio(bio_request_url, extract_all_pages(url, all_extracted_data)))  # returns all_hints dict



"""
STUDENT SOLUTION WITH OOP AND CLASSES

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from random import choice
 
class Author:
 
    def __init__(self, author_tag):
        self.name = author_tag.contents[0]
        self.author_url = author_tag.find_next_sibling()['href']
        self.born = self.get_born(self.author_url)
        self.quotes = []
 
    def __repr__(self):
        return self.name
 
    def get_author_site(self, author_url):
        a_response = requests.get(urljoin(url, self.author_url))
        return BeautifulSoup(a_response.text, 'html.parser')
 
    def get_born(self, author_soup):
        a_soup = self.get_author_site(author_soup)
        return a_soup.find(class_='author-born-date').contents[0]
 
    def add_quote(self, quote_tag):
        self.quotes.append(Quote(quote_tag, self.name, self.born))
 
 
class Quote:
 
    def __init__(self, quote_tag, author, born):
        self.text = self.get_quote(quote_tag)
        self.author = author
 
    def __repr__(self):
        return self.text
 
    def get_quote(self, quote_tag):
        return quote_tag.contents[0]
 
def find_author(tag, db):
    for item in db:
        if item.name == tag:
            return item
    return None
 
def scrape_site(soup, db, url):
    quotes = soup.find_all(class_='quote')
    for q in quotes:
        author_tag = q.find(class_='author')
        quote_tag = q.find(class_='text')
        current_author = find_author(author_tag.contents[0], db)
        if current_author is None:
            current_author = Author(author_tag)
            db.append(current_author)
        current_author.add_quote(quote_tag)
 
def crawl_site(url, db):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    scrape_site(soup, quotes_db, url)
    next_button = soup.find(class_='next')
    if next_button:
        next_page = next_button.contents[1]['href']
        url = urljoin(url, next_page)
        crawl_site(url, db)
 
def print_db(db):
    for author in sorted(quotes_db, key=lambda x: x.name):
        print('-' * 80)
        print(f'\n{author.name}:\n')
        for quote in author.quotes:
            print(f'- {quote}')
 
def random_quote():
    return choice(
        tuple(quote[0] for quote in (author.quotes for author in quotes_db))
    )
 
def play():
 
    def hint(num):
        if num == 3:
            print(
                f"Here's a hint: The author was born in "
                f"{find_author(rand_quote.author, quotes_db).born}.")
        elif num == 2:
            print(
                f"Here's a hint: The author's first "
                f"name starts with {rand_quote.author[0]}")
        elif num == 1:
            print(f"Here's a hint: The author's last "
                  f"name starts with {rand_quote.author.split()[-1][0]}")
 
    def check(num):
        nonlocal guesses
        my_choice = input(f'Who said this? Guesses remaining: {guesses} ')
        if my_choice == rand_quote.author:
            print('You guessed correctly! Congratulations!')
            guesses = 0
        else:
            guesses -= 1
            hint(guesses)
 
    print("Here's a quote:\n")
    rand_quote = random_quote()
    guesses = 4
    print(f'{rand_quote}\n')
    while guesses:
        check(guesses)
    print(f"The author's name was {rand_quote.author}")
    game_input = input("Would you like to play again (y/n)? ")
    if game_input[0] == 'y':
        play()
 
quotes_db = []
url = 'http://quotes.toscrape.com'
crawl_site(url, quotes_db)
play()
print("Here's a list of every author and their quotes:\n")
print_db(quotes_db)

"""








"""  
STUDENT SOLUTION

import requests
from bs4 import BeautifulSoup
import random

quotes_list = []
page = 1
while True:
    response = requests.get(f"http://quotes.toscrape.com/page/{page}/")
    soup = BeautifulSoup(response.text, "html.parser")
    no_quotes = soup.body.contents[1].find_all(class_="col-md-8")[1].get_text()
    if "No quotes found!" in no_quotes:
        break
    else:
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            quotes_list.append([quote.find(itemprop="text").get_text(),
                                quote.find(itemprop="author").get_text(),
                                quote.find("a")["href"]])
        page += 1


def get_hint(random_quote, next_hint):
    if next_hint == 0:
        hint_response = requests.get(f"http://quotes.toscrape.com{random_quote[2]}")
        hint_soup = BeautifulSoup(hint_response.text, "html.parser")
        born = hint_soup.find(class_="author-born-date").get_text()
        born_location = hint_soup.find(class_="author-born-location").get_text()
        print(f"Here is a hint: The author was born {born}, {born_location}")
    elif next_hint == 1:
        print(f"Here is a hint: The author's first name starts with {random_quote[1][0].upper()}")
    elif next_hint == 2:
        surname = (random_quote[1].split(" ")[1][0]).upper()
        print(f"Here is a hint: The author's last name starts with {surname}")


def play_again():
    replay = input("Would you like to play again? (Y/n) > ")
    if replay.upper() == "Y":
        print("Great! Here we go again...\n")
        game()
    else:
        print("OK. See you next time.")
        exit()


def game():
    random_quote = random.choice(quotes_list)
    guesses_left = 4
    next_hint = 0
    print(f"{random_quote[0]}")
    guess = input(f"\nWho said this? Guesses remaining: {guesses_left}. > ")

    while True:
        if guess == random_quote[1]:
            print("You guessed correctly! Congratulations!")
            play_again()
        else:
            guesses_left -= 1
            if guesses_left == 0:
                print(f"You are out of guesses! The author was {random_quote[1]}")
                play_again()
            get_hint(random_quote, next_hint)
            next_hint += 1
            guess = input(f"\nWho said this? Guesses remaining: {guesses_left}. > ")


game()

"""












"""
COMPLETED BASE FUNCTIONALITY VERSION:

import requests, csv, time
from bs4 import BeautifulSoup
from random import choice, randint
from pyfiglet import figlet_format
from termcolor import colored

# Extract the quote data
title = figlet_format("Guess the Author")
title = colored(title, color='cyan')
print(title)
print("Scraping data... please wait...")

num = 1
page_request_url = "http://quotes.toscrape.com/page/"
all_quotes = []
while True:
    response = requests.get(page_request_url+str(num))
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        next_page_href = soup.find(class_="next").find("a")["href"]
        next_page_number = int(next_page_href[-2:-1])
    except AttributeError:
        print(f"Scraped {str(num)} pages total...")
        break
    quotes = [quote.get_text() for quote in soup.select(".quote .text")]
    authors = [author.get_text() for author in soup.select(".author")]
    bios_urls = [bio.find_next_sibling("a")["href"] for bio in soup.select(".author")]
    for i in range(len(quotes)):
        all_quotes.append([quotes[i], authors[i], bios_urls[i]])
    
    # print(f"Completed page {num}. Waiting 1 second before starting page {next_page_number}")
    time.sleep(1)
    num += 1

#print((choice(all_quotes)[0]))

# Create the play/play again while loop
while True:
    wanna_play = input("Ready to play? (y/n) ")
    if wanna_play.upper() == 'N':
        print("Thanks for playing! See you next time!")
        break
    else:
        # Extract hint data after random selection. See helpers below.
        random_entry = choice(all_quotes)
        bio_request_url = "http://quotes.toscrape.com"
        response = requests.get(bio_request_url+random_entry[2])
        soup = BeautifulSoup(response.text, "html.parser")

        birthday_hint = soup.find(class_="author-born-date").get_text()
        birth_location_hint = soup.find(class_="author-born-location").get_text()

        name = soup.find(class_="author-title").get_text().split(' ')
        initials_hint = name[0][0] + ' ' + name[1][0]
        fn_letters_hint = len(name[0])
        ln_letters_hint = len(name[1])

        description = soup.find(class_="author-description").get_text()
        description_hint = description
        name_variations = name
        name_variations.append(name[0] + ' ' + name[1])
        for variation in name_variations:
            description_hint = description_hint.replace(variation, "@"*len(variation))

        all_hints = {
            3: f"The author was born {birthday_hint} in {birth_location_hint}",
            2: f"The author's initials are: {initials_hint}",
            1: f"The author's first name and last name have {fn_letters_hint} and {ln_letters_hint} letters respectively"
            #1: f"Here's the author's bio with their name removed: {description_hint}"
        }

        # Guessing game logic
        number_of_guesses = 4

        print(f"You have {number_of_guesses} chances to guess the correct author of a quote.")
        print(f"Here's the quote: {random_entry[0]}")
        while number_of_guesses > 0:
            user_guess = input("Guess the author: ")
            if user_guess == random_entry[1]:
                print(f"You're right! The author is: {random_entry[1]}. Great job!")
                break
            elif number_of_guesses-1 == 0:
                    print(f"Bummer! You're out of guesses. The correct answer is: {random_entry[1]}")
                    break
            else:
                number_of_guesses -= 1
                print(f"That's incorrect. Here's a hint: {all_hints[number_of_guesses]}")

"""