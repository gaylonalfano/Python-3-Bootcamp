'''
sorted - Returns a new sorted LIST from the items in iterable (tuple, list, dict, str, etc.)
You can also pass it a reverse=True argument.

Key difference between sorted and .sort() is that .sort() is a list-only method and returns the
sorted list in-place. sorted() accepts any type of iterable. Good for sorted on a key in dictionaries, etc.
'''

more_numbers = [6, 1, 8, 2]
sorted(more_numbers)  # [1, 2, 6, 8]
print(more_numbers)
print(sorted(more_numbers, reverse=True))
sorted((2, 1, 45, 23, 99))

users = [
    {'username': 'samuel', 'tweets': ['I love cake', 'I love pie']},
    {'username': 'katie', 'tweets': ["I love my cat"], "color": "purple"},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], "num": 10, "color": "green"},
    {'username': 'doggo_luvr', 'tweets': ["dogs are the best"]},
    {'username': 'guitar_gal', 'tweets': []}
]

# sorted(users)  # Error message. Need to specify on what you want to sort on
print(sorted(users, key=len))  # default is ascending
print(sorted(users, key=lambda user: user['username']))  # 'bob123', 'doggo_luvr', etc.
# Sort based off of who has the most tweets
print(sorted(users, key=lambda user: len(user['tweets']), reverse=True))  # Ascending default. 0 tweets > 2 tweets


# List of songs w/ playcount. How to sort based on playcount?
songs = [
    {'title': 'happy birthday', 'playcount': 1},
    {'title': 'Survive', 'playcount': 6},
    {'title': 'YMCA', 'playcount': 99},
    {'title': 'Toxic', 'playcount': 31}
]

print(sorted(songs, key=lambda song: song['playcount'], reverse=True))