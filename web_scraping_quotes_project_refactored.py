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
"""
import requests, csv, time
from bs4 import BeautifulSoup
from random import choice, randint
from pyfiglet import figlet_format
from termcolor import colored

# CRAWL ALL PAGES
# url = "http://quotes.toscrape.com/page/"
# all_extracted_data = []
def extract_all_pages(url, all_extracted_data):
    """Sends a request and parses HTML. Crawls all pages and extracts data."""
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
def extract_bio_generate_hints(): 
    """Randomly select an entry, parse bio page and generate hints"""
    bio_url = "http://quotes.toscrape.com"
    random_entry = choice(extract_all_pages(url, all_extracted_data))
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
        3: f"The author was born {birthday_hint} in {birth_location_hint}",
        2: f"The author's initials are: {initials_hint}",
        1: f"The author's first name and last name have {fn_letters_hint} and {ln_letters_hint} letters respectively"
        #1: f"Here's the author's bio with their name removed: {description_hint}"
    }

    start_guessing(random_entry, all_hints)  # Trouble with random_entry since it's choice()
    #return all_hints # since this returns here does it all return for select_parse if I don't 'return'??

# PLAY GAME / PLAY AGAIN FUNCTION
def start_game():
    """Launches the game and scrapes for quote, author, and bio url data"""
    display_game_title("Guess the Author")
    extract_all_pages(url, all_extracted_data)  # Returns all_extracted_data
    #start_guessing(extract_all_pages(url, all_extracted_data))

def display_game_title(game_title):
    title = figlet_format(game_title)
    title = colored(title, color='cyan')
    print(title)

# def play_again():
#     while True:
#         wanna_play = input("Ready to play? (y/n) ")
#         if wanna_play.upper() == 'N':
#             print("Thanks for playing! See you next time!")
#             break


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


url = "http://quotes.toscrape.com/page/"
all_extracted_data = []

# Lauch the game and extract quote, author, bio url data
print(start_game()) # None

print(f"PRINTING ALL EXTRACTED DATA: {all_extracted_data}")

#select_parse_author_bio(bio_request_url, all_extracted_data)  # returns all_hints dict

#generate_hints(select_parse_author_bio(bio_request_url, extract_all_pages(url, all_extracted_data)))  # returns all_hints dict


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