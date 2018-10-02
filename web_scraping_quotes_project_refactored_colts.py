"""
COLT'S WALKTHROUGH FOR REFACTORING - Moved the scraping portion to another file and now
we're incorporating READ CSV for the game logic.

"""
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictReader
# from web_scraping_quotes_colts_csv import scrape_quotes, write_quotes - BAD! This would scrape every time it's run!

BASE_URL = "http://quotes.toscrape.com"  # This is a CONSTANT, so should use CAPS (originally 'base_url')

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)  # converts OrderedDict to List

# read_quotes("web_scraping_colt_quotes.csv")  # For testing. Moved to bottom for final version
def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote["text"])
    print(quote["author"])  # for testing
    guess = ""
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guess remaining: {remaining_guesses} ")
        if guess.lower() == quote["author"].lower():
            print("YOU GOT IT RIGHT!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            #print(soup.body) for testing
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here's a hint: The author's last name starts with: {last_initial}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

    play_again = ''  # to start it off
    while play_again.lower() not in ('y', 'yes', 'n', 'no'):
        play_again = input("Would you like to play again (y/n)? ")
    if play_again.lower() in ('yes', 'y'):   # alternate syntax: is 'yes' or is 'y'
        #print('OK YOU PLAY AGAIN')  # Could set playing = True
        return start_game(quotes)
    else:
        print("OK, GOODBYE!")  # Could set playing = False

# Before CSV: 
# quotes = scrape_quotes()  # After adding scrape_quotes(), have to call it first
# start_game(quotes)  # After we got start_game() working, we then made a function out of scraping

# After CSV:
quotes = read_quotes("web_scraping_colt_quotes.csv")
start_game(quotes)
