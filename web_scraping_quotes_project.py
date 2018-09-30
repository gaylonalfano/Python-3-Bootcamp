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



POSSIBLE WAYS TO REFACTOR:
1. Add function for extracting pages
2. Add function for extracting bio info
3. Add function for playing game
4. Classes: Author? Hint? 
5. Add function to build/store hints
"""
import requests, csv, time
from bs4 import BeautifulSoup
from random import choice, randint

# Extract the quote data
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
        print(f"Tried to find page {next_page_number} but only scraped {str(num)} pages total.")
        break
    quotes = [quote.get_text() for quote in soup.select(".quote .text")]
    authors = [author.get_text() for author in soup.select(".author")]
    bios_urls = [bio.find_next_sibling("a")["href"] for bio in soup.select(".author")]
    for i in range(len(quotes)):
        all_quotes.append([quotes[i], authors[i], bios_urls[i]])
    
    print(f"Completed page {num}. Waiting 1 second before starting page {next_page_number}")
    time.sleep(1)
    num += 1

#print((choice(all_quotes)[0]))

# Create the play/play again while loop
while True:
    wanna_play = input("Want to play a 'Guess the Quote' game? (y/n) ")
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


# EXTRACT HINT DATA HELPER
# r = requests.get("http://quotes.toscrape.com/author/Albert-Einstein")
# soup = BeautifulSoup(r.text, "html.parser")
# # author's birthday and location:
# #print(soup.select(".author-born-date"))
# birthday_hint = soup.find(class_="author-born-date").get_text()
# birth_location_hint = soup.find(class_="author-born-location").get_text()
# # author's initials:
# #name = soup.find(class_="author-title").get_text()
# #print(name)
# name = soup.find(class_="author-title").get_text().split(' ')
# #print(name)
# initials_hint = name[0][0], name[1][0]
# #print(initials_hint[0], initials_hint[1])
# #number of letters in authors name
# fn_letters_hint = len(name[0])
# ln_letters_hint = len(name[1])
# #print(fn_letters_hint, ln_letters_hint)

# WORKS BUT TRICKY. BETTER IS REPLACE() replace name in description - using lists and split() and join()
# description = soup.find(class_="author-description").get_text()
# description_split = description.split(' ')
# #print(description_split)
# description_hint = []
# for i in description_split:
#     if i in name:
#         description_hint.append('%'*len(i))
#     else:
#         description_hint.append(i)
# # list comp version of description_hint
# description_hint = ['%'*len(i) if i in name else i for i in description_split]
# description_hint_text = " ".join(description_hint)
# print(description_hint_text)

# BETTER/CLEANER: replace name in description - using replace(), no lists
# description = soup.find(class_="author-description").get_text()
# description_hint = description
# name_variations = name
# name_variations.append(name[0] + ' ' + name[1])
# #print(name_variations)
# #print(description.replace("Einstein", "@"*len("Einstein")))  # This works for Einstein
# for variation in name_variations:
#     description_hint = description_hint.replace(variation, "@"*len(variation))

# #print(description_hint)
# #print(description)

# # Now store all the hints
# all_hints = {
#     "birthday": birthday_hint,
#     "birth_location": birth_location_hint,
#     "initials": initials_hint,
#     "first_name_letters": fn_letters_hint,
#     "last_name_letters": ln_letters_hint,
#     "description": description_hint
# }
    











# RANDOM QUOTE FROM LIST
test_data = [['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'Albert Einstein', '/author/Albert-Einstein'], ['“It is ourchoices, Harry, that show what we truly are, far more than our abilities.”', 'J.K. Rowling', '/author/J-K-Rowling'], ['“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'Albert Einstein', '/author/Albert-Einstein'], ['“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'Jane Austen', '/author/Jane-Austen'], ["“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", 'Marilyn Monroe', '/author/Marilyn-Monroe'], ['“Try not to become a man of success. Rather become a man of value.”', 'Albert Einstein', '/author/Albert-Einstein'], ['“It is better to be hated for what you are than to be loved for what you are not.”', 'André Gide', '/author/Andre-Gide'], ["“I have not failed. I've just found 10,000 ways that won't work.”", 'Thomas A. Edison', '/author/Thomas-A-Edison'], ["“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'Eleanor Roosevelt', '/author/Eleanor-Roosevelt'], ['“A day without sunshine is like, you know, night.”', 'Steve Martin', '/author/Steve-Martin'], ["“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. Butjust remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn'tmean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”", 'Marilyn Monroe', '/author/Marilyn-Monroe'], ['“It takesa great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.”', 'J.K. Rowling', '/author/J-K-Rowling'], ["“If you can't explain it to a six yearold, you don't understand it yourself.”", 'Albert Einstein', '/author/Albert-Einstein'], ["“You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let herknow when she makes you mad, and miss her when she's not there.”", 'Bob Marley', '/author/Bob-Marley'], ['“I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.”', 'Dr. Seuss', '/author/Dr-Seuss'], ['“I may not have gone where I intended to go, but I think I have ended up where I needed to be.”', 'Douglas Adams', '/author/Douglas-Adams'], ["“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”", 'Elie Wiesel', '/author/Elie-Wiesel'], ['“It is not a lack of love, but a lack of friendship that makes unhappy marriages.”', 'Friedrich Nietzsche', '/author/Friedrich-Nietzsche'], ['“Good friends, good books, and a sleepy conscience: this is the ideal life.”', 'Mark Twain', '/author/Mark-Twain'], ['“Life is what happens to us while we are making other plans.”', 'Allen Saunders', '/author/Allen-Saunders'], ['“I love you without knowing how, or when, or from where. I love you simply, without problems or pride: I love you in this way because I do not know any other way of loving but this, in which there is no I or you, so intimate that your hand upon mychest is my hand, so intimate that when I fall asleep your eyes close.”', 'Pablo Neruda', '/author/Pablo-Neruda'], ['“For every minute you are angry you lose sixty seconds of happiness.”', 'Ralph Waldo Emerson', '/author/Ralph-Waldo-Emerson'], ['“If you judge people, you have no time to love them.”', 'Mother Teresa', '/author/Mother-Teresa'], ['“Anyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.”', 'Garrison Keillor', '/author/Garrison-Keillor'], ['“Beauty is in the eye of the beholder and it may be necessary from time to time to give a stupid or misinformed beholder a black eye.”', 'Jim Henson', '/author/Jim-Henson'], ['“Today you are You, that is truer than true. There is no one alive who is Youer than You.”', 'Dr. Seuss', '/author/Dr-Seuss'], ['“If you want your children to be intelligent, read them fairy tales. If youwant them to be more intelligent, read them more fairy tales.”', 'Albert Einstein', '/author/Albert-Einstein'], ['“It is impossible to live without failing at something, unless youlive so cautiously that you might as well not have lived at all - in which case, you fail by default.”', 'J.K. Rowling', '/author/J-K-Rowling'], ['“Logic will get you from A to Z; imagination will get you everywhere.”', 'Albert Einstein', '/author/Albert-Einstein'], ['“One good thing about music, when it hits you, you feel no pain.”', 'Bob Marley', '/author/Bob-Marley'], ["“The more that you read, the more things you will know. The more that you learn, the more places you'll go.”", 'Dr. Seuss', '/author/Dr-Seuss'], ['“Of course it is happening inside your head, Harry, but why on earth should that mean that it is not real?”', 'J.K. Rowling', '/author/J-K-Rowling'], ['“The truth is, everyone is going to hurt you. You just got to find the ones worth suffering for.”', 'Bob Marley', '/author/Bob-Marley'], ['“Not all of us can do great things. But we can do small things with great love.”', 'MotherTeresa', '/author/Mother-Teresa'], ['“To the well-organized mind, death is but the next great adventure.”', 'J.K. Rowling', '/author/J-K-Rowling'], ["“All you need is love. But a little chocolate now and then doesn't hurt.”", 'Charles M. Schulz', '/author/Charles-M-Schulz'], ["“We read to know we're not alone.”", 'William Nicholson', '/author/William-Nicholson'], ['“Any fool can know. The point is to understand.”', 'Albert Einstein', '/author/Albert-Einstein'], ['“I have always imagined that Paradise will be a kind of library.”', 'JorgeLuis Borges', '/author/Jorge-Luis-Borges'], ['“It is never too late to be what you might have been.”', 'George Eliot', '/author/George-Eliot'], ['“A reader lives a thousand lives before he dies, said Jojen. The man who never reads lives only one.”', 'George R.R. Martin', '/author/George-R-R-Martin'], ['“You can never get a cup of tea large enough or a book long enough to suit me.”', 'C.S. Lewis', '/author/C-S-Lewis'], ['“You believe lies so you eventually learn to trust no one but yourself.”', 'Marilyn Monroe', '/author/Marilyn-Monroe'], ['“If you can make a woman laugh, you can make her do anything.”', 'Marilyn Monroe', '/author/Marilyn-Monroe'], ['“Life is like riding a bicycle. To keep your balance, you must keep moving.”', 'Albert Einstein', '/author/Albert-Einstein'], ['“The real lover is the man who can thrill you by kissing your forehead or smiling into your eyes or just staring into space.”', 'Marilyn Monroe', '/author/Marilyn-Monroe'], ["“A wise girl kisses but doesn't love, listens but doesn't believe, and leaves before she is left.”", 'Marilyn Monroe', '/author/Marilyn-Monroe'], ['“Only in the darkness can you see the stars.”', 'Martin Luther King Jr.', '/author/Martin-Luther-King-Jr'], ['“It matters not what someone is born, but what they grow to be.”', 'J.K. Rowling', '/author/J-K-Rowling'], ['“Love does not begin and end the way we seem to think it does. Love is a battle, love is a war; love is a growing up.”', 'James Baldwin', '/author/James-Baldwin'], ['“There is nothing I would not do for those who are really my friends. I have no notion of loving people by halves, it is not my nature.”', 'Jane Austen', '/author/Jane-Austen'], ['“Do one thing every day that scares you.”', 'Eleanor Roosevelt', '/author/Eleanor-Roosevelt'], ['“I am good, but not an angel. I do sin, but I am not the devil. I am just a small girl in a big world trying to find someone to love.”', 'Marilyn Monroe', '/author/Marilyn-Monroe'], ['“If I were not a physicist, I wouldprobably be a musician. I often think in music. I live my daydreams in music. I see my life in terms of music.”', 'Albert Einstein', '/author/Albert-Einstein'], ['“If you only readthe books that everyone else is reading, you can only think what everyone else is thinking.”', 'Haruki Murakami', '/author/Haruki-Murakami'], ['“The difference between genius and stupidity is: genius has its limits.”', 'Alexandre Dumas fils', '/author/Alexandre-Dumas-fils'], ["“He's like a drug for you, Bella.”", 'Stephenie Meyer', '/author/Stephenie-Meyer'],['“There is no friend as loyal as a book.”', 'Ernest Hemingway', '/author/Ernest-Hemingway'], ['“When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.”', 'Helen Keller', '/author/Helen-Keller'], ["“Life isn't about finding yourself. Life is about creating yourself.”", 'George Bernard Shaw', '/author/George-Bernard-Shaw'], ["“That's the problem with drinking, I thought, as I poured myself a drink. If something bad happens you drink in an attempt to forget; if something good happens you drink in order to celebrate; and if nothing happens you drink to make something happen.”", 'Charles Bukowski', '/author/Charles-Bukowski'], ['“You don’t forget the face of the person who was your last hope.”', 'Suzanne Collins', '/author/Suzanne-Collins'], ["“Remember, we're madly in love, so it's all right to kissme anytime you feel like it.”", 'Suzanne Collins', '/author/Suzanne-Collins'], ['“To love at all is to be vulnerable. Love anything and your heart will be wrung and possibly broken. If you want to make sure of keeping it intact you must give it to no one, not even an animal. Wrap it carefully round with hobbies and little luxuries; avoid all entanglements. Lock it up safe in the casket or coffin of your selfishness. But in that casket, safe, dark, motionless, airless, it will change. It will not be broken; it will become unbreakable, impenetrable, irredeemable. To love is to be vulnerable.”', 'C.S. Lewis', '/author/C-S-Lewis'], ['“Not all those who wander are lost.”', 'J.R.R. Tolkien', '/author/J-R-R-Tolkien'], ['“Do not pity the dead, Harry. Pity the living, and, above all those who live without love.”', 'J.K. Rowling', '/author/J-K-Rowling'], ['“There is nothing to writing. All you do is sit down at a typewriter and bleed.”', 'Ernest Hemingway', '/author/Ernest-Hemingway'], ['“Finish each day and be done with it. You have done what you could. Some blunders and absurdities no doubt crept in; forget them as soon as you can. Tomorrow is a new day. You shall begin it serenely and with too high a spirit to be encumbered with your old nonsense.”', 'Ralph Waldo Emerson', '/author/Ralph-Waldo-Emerson'], ['“I have never let my schooling interfere with my education.”', 'Mark Twain', '/author/Mark-Twain'], ["“I have heard there are troubles of more than one kind. Some come from ahead and some come from behind. But I've bought a big bat. I'm all ready you see. Now my troubles are going to have troubles with me!”", 'Dr. Seuss', '/author/Dr-Seuss'], ['“If I had a flower for every time I thought of you...I could walk through my garden forever.”', 'Alfred Tennyson', '/author/Alfred-Tennyson'], ['“Some people never go crazy. What truly horrible lives they must lead.”', 'Charles Bukowski', '/author/Charles-Bukowski'], ['“The trouble with having an open mind, of course, isthat people will insist on coming along and trying to put things in it.”', 'Terry Pratchett', '/author/Terry-Pratchett'], ['“Think left and think right and think low and think high. Oh, the thinks you can think up if only you try!”', 'Dr. Seuss', '/author/Dr-Seuss'], ["“What really knocks me out is a book that, when you're all done reading it, you wish the author that wrote it was a terrific friend of yours and you could call him up on the phone whenever you felt like it. That doesn't happen much, though.”", 'J.D. Salinger', '/author/J-D-Salinger'], ['“The reason I talk to myself is because I’m the only one whose answers I accept.”', 'George Carlin', '/author/George-Carlin'], ["“You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one.”", 'John Lennon', '/author/John-Lennon'], ['“I am free of all prejudice. I hate everyone equally. ”', 'W.C. Fields', '/author/W-C-Fields'], ["“The question isn't who is going to let me; it's who is going to stop me.”", 'Ayn Rand', '/author/Ayn-Rand'], ["“′Classic′ - a book which people praise and don't read.”", 'Mark Twain', '/author/Mark-Twain'], ['“Anyone who has never made a mistake has never tried anything new.”', 'Albert Einstein', '/author/Albert-Einstein'], ["“A lady's imagination is very rapid; it jumps from admiration to love, from love to matrimony in a moment.”", 'Jane Austen', '/author/Jane-Austen'], ['“Remember, if the time should come when you have to make a choice between what is right and what is easy, remember what happened to a boy who was good, and kind, and brave, because he strayed across thepath of Lord Voldemort. Remember Cedric Diggory.”', 'J.K. Rowling', '/author/J-K-Rowling'], ['“I declare after all there is no enjoyment like reading! How much sooner one tires of any thing than of a book! -- When I have a house of my own, I shall be miserable if I have not an excellent library.”', 'Jane Austen', '/author/Jane-Austen'], ['“There are few people whom I really love, and still fewer of whom I think well. The more I see of the world, the more am I dissatisfied with it; and every day confirms my belief of the inconsistency ofall human characters, and of the little dependence that can be placed on the appearance of merit or sense.”', 'Jane Austen', '/author/Jane-Austen'], ['“Some day you will be old enough to start reading fairy tales again.”', 'C.S. Lewis', '/author/C-S-Lewis'], ['“We are not necessarily doubting that God will do the best for us; we are wondering how painful the best will turn out to be.”', 'C.S. Lewis', '/author/C-S-Lewis'], ['“The fear of death follows from the fear of life. A man who lives fully is prepared to die at any time.”', 'Mark Twain', '/author/Mark-Twain'], ['“A lie can travel half way around the world while the truth is putting on its shoes.”', 'Mark Twain', '/author/Mark-Twain'], ['“I believe in Christianity as I believe that the sun has risen: not only because I see it, but because by it I see everything else.”', 'C.S. Lewis', '/author/C-S-Lewis']]

# print(choice(test_data))  
# print(choice(test_data[0]))  # Incorrect. This pulls a random item from a list (q, a, b)
# print(choice(test_data)[0])  # this gets a random quote















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






# FUNCTION HELPER - MEH. NOT WORKING.
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




# RANDOM QUOTE HELPER -- CRASH AND BURN
# nested = [[{'quote': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'bio_url': '/author/Albert-Einstein'}, {'quote': '“It is our choices, Harry, that show what we trulyare, far more than our abilities.”', 'author': 'J.K. Rowling', 'bio_url': '/author/J-K-Rowling'}, {'quote': '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'author': 'AlbertEinstein', 'bio_url': '/author/Albert-Einstein'}, {'quote': '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'author': 'Jane Austen', 'bio_url': '/author/Jane-Austen'}, {'quote': "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", 'author': 'Marilyn Monroe', 'bio_url': '/author/Marilyn-Monroe'}, {'quote': '“Try not to become a man of success. Rather become a man of value.”', 'author': 'Albert Einstein', 'bio_url': '/author/Albert-Einstein'}, {'quote': '“It is better to be hated for what you are than to be loved for what you are not.”', 'author': 'André Gide', 'bio_url': '/author/Andre-Gide'}, {'quote': "“I have not failed. I've just found 10,000 ways that won't work.”", 'author': 'Thomas A. Edison', 'bio_url': '/author/Thomas-A-Edison'}, {'quote': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'author': 'Eleanor Roosevelt', 'bio_url': '/author/Eleanor-Roosevelt'}, {'quote': '“A day without sunshine is like, you know, night.”', 'author': 'Steve Martin', 'bio_url': '/author/Steve-Martin'}], [{'quote': "“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good partis you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”", 'author': 'Marilyn Monroe', 'bio_url': '/author/Marilyn-Monroe'}, {'quote': '“It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.”', 'author': 'J.K. Rowling', 'bio_url': '/author/J-K-Rowling'}, {'quote': "“If you can't explain it to a six year old, you don't understand it yourself.”", 'author': 'Albert Einstein', 'bio_url': '/author/Albert-Einstein'}, {'quote': "“You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.”", 'author': 'Bob Marley', 'bio_url': '/author/Bob-Marley'}, {'quote': '“I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.”', 'author': 'Dr. Seuss', 'bio_url': '/author/Dr-Seuss'}, {'quote': '“I may not have gone where I intendedto go, but I think I have ended up where I needed to be.”', 'author': 'Douglas Adams', 'bio_url': '/author/Douglas-Adams'}, {'quote': "“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite offaith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”", 'author': 'Elie Wiesel', 'bio_url': '/author/Elie-Wiesel'}, {'quote': '“It is not a lack of love, but a lack of friendship that makes unhappy marriages.”', 'author': 'Friedrich Nietzsche', 'bio_url': '/author/Friedrich-Nietzsche'}, {'quote': '“Good friends, good books, and a sleepy conscience: this is the ideal life.”', 'author': 'Mark Twain', 'bio_url': '/author/Mark-Twain'}, {'quote': '“Life is what happens to us while we are making other plans.”', 'author': 'Allen Saunders', 'bio_url': '/author/Allen-Saunders'}]]

# random_page = randint(0,len(nested))  # returns int
# random_entry = randint(0, random_page)  # returns int
# # random_quote = random_entry["quote"]  # necessary
# # nested has these layers: List>>pages>>>rows>>>>elements
# # What I want is List>>rows>>>elements
# # for page in range(len(nested)):
# #     for row in nested[page]:
# #         print(row)

# # unnested = [row for row in range(len(nested[page])) for page in range(len(nested))]

# # print(unnested)
# # print(nested)
# # #print(test_data[randint(0, len(test_data))][randint()])
# # print(nested[0][0]["quote"])
# # #print(test_data[randint(0,len(test_data))][randint(0,len(test_data[0]))]["quote"])
# # print(nested[random_page][random_entry]["quote"])
