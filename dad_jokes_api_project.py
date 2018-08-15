import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice, shuffle

while True:
    #ascii art title: Dad Joke 3000
    title = figlet_format("Dad Joke 3000")
    title = colored(title, color='yellow')
    print(title)

    #Accept user input for topic
    topic_search = input("Wanna hear something funny? Give me any topic or type 'Q' to quit and I'll tell you: ")

    if topic_search.upper() == 'Q':
        print("Thanks for listening! See you next time!")
        break
    else:
        # Search/collect API data/results
        url = "https://icanhazdadjoke.com/search"
        response = requests.get(
            url=url,
            headers={"Accept": "application/json"},
            params={"term": topic_search}
        )

        data = response.json()  # returns a DICT ['results', 'search_term', 'status', 'total_jokes', etc.]
        topic_jokes = [joke["joke"] for joke in data['results']]
        shuffle(topic_jokes)

        number_of_jokes = len(topic_jokes)

        if number_of_jokes == 0:
            print(f"Oops! I found {number_of_jokes} jokes about {topic_search}. Try a different topic.")
        elif number_of_jokes == 1:
            print(f"You're in luck! I have {number_of_jokes} joke about {topic_search}. Here it is: ")
            print(topic_jokes[0])
        else:
            print(f"I've got {number_of_jokes} jokes about {topic_search}. Here's one: ")
            print(topic_jokes.pop())
            number_of_jokes -= 1

            while number_of_jokes > 0:
                show_next_joke = input(f"Want another {topic_search} joke? I've got {number_of_jokes} left. (Y/N) ")

                if show_next_joke.upper() == 'N':
                    print("Not so funny, huh?")
                    break
                else:
                    print(topic_jokes.pop())
                    number_of_jokes -= 1
                    if number_of_jokes == 0:
                        print(f"Doh! No more {topic_search} jokes.")



'''
Possible improvements/questions:
- How to use try/except in this?
- How to try to search for the plural version (ex. 'kids' = 0 jokes; 'kid' = 4 jokes)
- Any place/reason to add a function?
- How to use .pop() and choice() together? Ex. l.pop(choice(l))
'''


# def search_topic(topic):
#     # Search/collect API data/results
#     url = "https://icanhazdadjoke.com/search"
#     response = requests.get(
#         url=url,
#         headers={"Accept": "application/json"},
#         params={"term": topic}
#     )
#     data = response.json()
#
#     while True:
#         if data['total_jokes'] == 0:
#             print(f"Oops! I found {data['total_jokes']} jokes about {topic_search}. Try a different topic.")
#             return False
#         else:
#             print(f"I've got {data['total_jokes']} jokes about {topic_search}. Here's one: ")
#             print(choice(data['results'])['joke'])
#             break
#
#
# search_topic(input("Give me a topic: "))

# ==========================
# Colt's solution:
# import requests
# from random import choice
# from pyfiglet import figlet_format
# from termcolor import colored
#
# header = figlet_format("DAD JOKE 3000!")
# header = colored(header, color='magenta')
# print(header)
#
# user_input = input("What would you like to search for? ")
# url = "https://icanhazdadjoke.com/search"
#
# # Look at API documentation > API Response Format
# res = requests.get(
#     url,
#     headers={"Accept": "application/json"},
#     params={"term": user_input}
# ).json()
#
# num_jokes = res["total_jokes"]
# results = res["results"]
# if res["total_jokes"] > 1:
#     print(f"I found {num_jokes} jokes about {user_input}. Here's one: ")
#     print(choice(results)['joke'])
# elif num_jokes == 1:
#     print(f"I found one joke about {user_input}")
#     print(results[0]['joke'])
# else:
#     print(f"Sorry, couldn't find a joke with your term: {user_input}")
#
# print(res)

# ========== Student Example with WHILE LOOP: ===========================
# import requests
# import random
#
# while True:
#     search = input("\nLet me tell you a joke! Give me a topic or Q to quit: ")
#
#     if search.upper() == "Q":
#         print("OK. See you next time.")
#         break
#     else:
#         url = "https://www.icanhazdadjoke.com/search"
#
#         response = requests.get(
#             url,
#             headers={"Accept": "application/json"},
#             params={"term": search}
#         )
#
#         data = response.json()
#         number_jokes = len(data["results"])
#
#         if number_jokes == 0:
#             print("Sorry. No jokes for that topic. Please try again.")
#         else:
#             print("I've got {} jokes about {}. Here's one:\n".format(number_jokes, search))
#             print(random.choice(data["results"])["joke"])



# ========= FUNCTIONS example ==================
# import random
# import requests
# import pyfiglet
# import termcolor
#
#
# def color():
#     ascii_msg = pyfiglet.figlet_format('Dad Joke 3000')
#     return termcolor.colored(ascii_msg, color='magenta')
#
#
# def topic_selection():
#     selection = input('Let me tell you a joke! Give me a topic: ')
#     return selection
#
#
# def selection_joke():
#     topic = topic_selection()
#     url = 'https://icanhazdadjoke.com/search'
#     json = {'accept': 'application/json'}
#     prms = {'term': topic}
#     res = requests.get(url, headers=json, params=prms)
#     selection = res.json().get('results')
#     if len(selection) > 1:
#         joke = random.choice(selection).get('joke')
#         return f'I have {len(selection)} jokes for {topic}. Here it comes one:\n{joke}'
#     elif len(selection) == 1:
#         joke = selection[0].get('joke')
#         return f'I have one joke for {topic}. Here it comes:\n{joke}'
#     return f'Sorry I don\'t have jokes for {topic}'
#
#
# print(color())
# print(selection_joke())