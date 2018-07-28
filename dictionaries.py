artist = {
    'first': 'Neil',
    'last': 'Young',
}

#full_name = artist['first'] + ' ' + artist['last']

# Format() solution:
# full_name = "{} {}".format(artist['first'], artist['last'])

# F-String solution:
full_name = f"{artist['first']} {artist['last']}"
print(full_name)


# Iterating over dictionaries .values()
instructor = {
    'name': 'Colt',
    'owns_dog': True,
    'num_courses': 4,
    'favorite_language': 'Python',
    'is_hilarious': False,
    44: 'my favorite number!'
}

for value in instructor.values():
    print(value)

# .keys()
for key in instructor.keys():
    print(key)

# .items()
instructor.items()
print(instructor.items())

for key, value in instructor.items():
    print(f"Key is: {key}. Value is: {value}.")

# Donations Exercise

donations = {'sam': 25.0, 'lena': 88.99, 'chuck': 13.0, 'linus': 99.5, 'stan': 150.0, 'lisa': 50.25, 'harrison': 10.0}

total_donations = 0
for value in donations.values():
    total_donations += value

print(total_donations)

# Another option using .sum()
total_donations2 = sum(donation for donation in donations.values())
print(total_donations2)

# Another advanced option using .sum()
print(sum(donations.values()))

# 'in' only checks keys in dictionaries
if 'phone' in instructor.values():
    print('There is a phone')
else:
    print('No phone!')

# Dictionary Methods
# clear
# instructor.clear()

# setdefault(key to check for, value to set if key DOES NOT EXIST)
# Good for ensuring that a key exists.
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(f'Here is spam: {spam}')
spam.setdefault('color', 'white')  # Still will be 'black' since key 'color' already exists

'''
Program that counts the number of occurrences of each letter in a string
'''

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

def count_dict(string):
    count = {letter: string.count(letter) for letter in string}
    return count

print(count_dict(message))

# count = {}
#
# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1
#
# print(count)
# pprint.pprint(count) - Nice print out view for Dictionaries





# Copy()
d = dict(a=1, b=2, c=3)
c = d.copy()
print(d, c)
c is d  # False
c == d  # True

# dict.fromkeys() -- Creates key-value pairs from comma separated values
{}.fromkeys('a', 'b')  # {'a': 'b'}
{}.fromkeys(['email'], 'unknown')  # {'email': 'unknown'}
{}.fromkeys('a', [1, 2, 3, 4, 5])  # {'a': [1, 2, 3, 4, 5]}
{}.fromkeys(range(10), 'unknown')

# .get()
instructor.get('name')  # 'Colt'

from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

[print(f'{bakery_stock[food]} left') if food in bakery_stock else print("We don't have that")
 for item in bakery_stock.keys()]

# [print(f'{bakery_stock[food]} left') if food in bakery_stock.keys() else print("We don't have that")]
# for key in bakery_stock.keys()]

print(f'Food: {food}')
print(food in bakery_stock.keys())

# Solution #1 my version:
if food in bakery_stock.keys():
    print(f'{bakery_stock[food]} left')
else:
    print("We don't have that")

# Solution #2 using .format()
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")

# Solution #3 using .get()
quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")


# dict.fromkeys Exercise Section 14, Coding Exercise 30
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"]
initial_game_state = dict.fromkeys(game_properties, 0)
print(initial_game_state)


# .pop('key') -- Removes the specified key item from dict

# .popitem() -- Removes a random key item from dict

# .update() -- dictname.update() Update keys and values in a dict with another set of key-value pairs
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)
print(second)

second['a'] = 'AMAZING'
second.update(first)
second['f'] = 6
print(second)