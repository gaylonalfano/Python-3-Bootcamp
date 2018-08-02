# max - Returns the largest item in an iterable or the largest of two or more arguments

max(3, 67, 99)  # 99
max('c', 'd', 'a')  # d
max([3, 4, 1, 2])  # 4
max([1, 2, 3, 4])  # 4
max('awesome')  # 'w'
max({1: 'a', 3: 'c', 2: 'b'})  # 3

nums = [40, 32, 6, 5, 10]
max(nums)  # 40
min(nums)  # 5
max("hello world")  # 'w'
min("hello world")  # ' '
max((3, 5, 23, 65))  # 65

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']

print(min(names))  # Arya
print(min(len(name) for name in names))

# What if I wanted the name "Tim" for min, or "Olivander" for max?
print(max(names, key=lambda name: len(name)))  # Olivander

# Find the song that has the least number of plays. Return song
songs = [
    {'title': 'happy birthday', 'playcount': 1},
    {'title': 'Survive', 'playcount': 6},
    {'title': 'YMCA', 'playcount': 99},
    {'title': 'Toxic', 'playcount': 31}
]

# This is how to find max playcount through for loop
# max_playcount = 0
# for song in songs:
#     if song['playcount'] > max_playcount:
#         max_playcount = song['playcount']
# print(max_playcount)


# This by using max/min functions:

max(songs, key=lambda s: s['playcount'])
min(songs, key=lambda song: song['playcount'])['title']  # 'happy birthday'

# User question/solution using sorted():
sorted_songs = sorted(songs, key=lambda song: song['playcount'])

for song in sorted_songs:
    print(f"{song['title']}: {song['playcount']}")


# EXTREMES() - using min/max - accepts iterable and returns a tuple containing the min and max elements.
# extremes([1,2,3,4,5])  # (1, 5)
# extremes([99, 25, 30, -7])  # (-7, 99)
# extremes("alcatraz")  # ('a', 'z')
def extremes(i):
    return min(i), max(i)

print(extremes([1,2,3,4,5]))
print(extremes("alcatraz"))




