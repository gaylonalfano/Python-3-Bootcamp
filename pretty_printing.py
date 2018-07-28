import pprint


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

# def count_dict(string):
#     count = {letter: string.count(letter) for letter in string}
#     return count
#
# print(count_dict(message))

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)