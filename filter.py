# ALWAYS checks whether TRUE/FALSE against the lambda function or defined function we create
# There is a lambda for each value in the iterable
# Returns filter object which can be converted into other iterables
# The object contains only the values that return true to the lambda

l = [1, 2, 3, 4]

evens = list(filter(lambda x: x % 2 == 0, l))

print(evens)


# FIRST_LETTER_A()
names = ['Gaylon', 'Aaron', 'Adrian', 'Archie', 'Ashley', 'Tom']
a_names = list(filter(lambda x: x[0].lower() == 'a', names))

print(a_names)

# Yes, we can still use list comprehension but ignoring that for a moment,
# there are lots of times you might want to extract certain things from
# a list based on a condition.


# Another filter example
users = [
    {'username': 'samuel', 'tweets': ['I love cake', 'I love pie']},
    {'username': 'katie', 'tweets': ["I love my cat"]},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo_luvr', 'tweets': ["dogs are the best"]},
    {'username': 'guitar_gal', 'tweets': []}
]

no_tweets = list(filter(lambda x: x.get('tweets') == [], users))

# Return a list of usernames for all inactive users
inactive_users = list(filter(lambda u: len(u['tweets']) == 0, users))
inactive_users2 = list(filter(lambda u: not u['tweets'], users))  # u['tweets'] will return truthy (i.e., NOT empty [])
# What if we only wanted to collect the usernames, not a full dict per user:
inactive_users3 = list(map(lambda user: user.get('username'), filter(lambda u: not u['tweets'], users)))
usernames = list(map(lambda user: user['username'].upper(), filter(lambda u: not u['tweets'], users)))
lc_version = [user['username'].upper() for user in users if not user['tweets']]

print(inactive_users)  # [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, ...]
print(no_tweets)  # [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, ...]
print(inactive_users2)  # [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, ...]
print(inactive_users3)  # ['jeff', 'bob123', 'guitar_gal']
print(usernames)  # [JEFF, BOB123, GUITAR_GAL]
print(lc_version)  # [JEFF, BOB123, GUITAR_GAL]

# BROKEN - Attempting to return a filtered list if the tweet has 'love' in it
# def love(list_of_strings):  # Return a list of booleans for each iterable in the list
# #   [True for x in list_of_strings if 'love' in list_of_strings[x] else False]
# #    return [True if 'love' in list_of_strings[val] else False for val in list_of_strings]
#     result = []
#     for i in range(len(list_of_strings)):
#         if 'love' in list_of_strings[i]:
#             result.append(True)
#         else:
#             result.append(False)
#     return result
#
#
# print(love(['I love cake', 'Today is Monday', 'I love you']))
# love_users = list(filter(lambda x: x.get('tweets')))
for user in users:
    for tweet in user['tweets']:
        if 'love' in tweet:
            print(f"Yes! Here it is: {user['tweets']}")
        else:
            print('Nope!')

# for tweet in users[0]['tweets']:
#     if 'cake' in tweet:
#         print(tweet)


# print(list(filter(lambda tweet: 'love' in tweet, users)))
# users[0]['tweets']  # ['I love cake', 'I love pie']



# COMBINING FILTER AND MAP - I 'believe' the filter() function runs first and then map()
# Return a new list with the string "Your instructor is " + each value in the array/list, but
# only if the value is less than 5 characters.
print(list(map(lambda n: "Your instructor is " + n, filter(lambda name: len(name) < 5, names))))

# Instructor's syntax:
print(list(map(lambda name: f'Your instructor is {name}',
         filter(lambda value: len(value) < 5, names))))

# Now, doing this without map/filter but with good ol' list comprehension.
# **IMPORTANT** Instructor says if you can use list comprehension, then do it!
# But need to know that lambda/map/filter, etc. exist.
your_instructor = ["Your instructor is " + name for name in names if len(name) < 5]
# Instructor's:
your_instructor2 = [f"Your instructor is {name}" for name in names if len(name) < 5]

print(your_instructor)
print(your_instructor2)


# REMOVE_NEGATIVES() - accepts a list and returns a copy of the lists with all negative numbers
# removed. Use filter(). 0 is not negative so don't filter it out.
# remove_negatives([-1, 3, 4, -99])  # [3, 4]
print(list(filter(lambda n: n >= 0, [-1, 3, 4, -99])))  # [3, 4]

def remove_negatives(l):
    return list(filter(lambda n: n >= 0, l))


print(remove_negatives([-1, 0, 4, 55, 88.8, -3, .333, -19]))  # [0, 4, 55, 88.8, 0.333]


