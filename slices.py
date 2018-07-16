# from random import randint
#
# r = randint(a=1, b=200)
# print(r)
#
# print(len('aldkjaldkfjaldkfjaldjfaldj'))
# s = list('aldkjaldkfjaldkfjaldjfaldj')
# print(s)
#
# s.append('iiihhhhiiijjjj')
# print(s)

list('Gaylon')

yay = 'This is fun!'

print(yay[::-1])

# Swapping values -- For lists with 2 items? Good for shuffling cards, sorting, algorithms
names = ['James', 'Michelle', 'Gaylon']
names[0], names[1], names[2] = names[1], names[0], names[2]
print(names)

# Another exercise
multiple_of_12 = [val for val in list(range(1, 101)) if val % 12 == 0]

# Remove vowels
no_vowels = [char for char in 'amazing' if char not in 'aeiou']
