# demo_list = [45, 'nap', 'budget', 17.43]
# len(demo_list)
#
#
#
# r = list(range(1, 100))
#
# for n in r:
#     print(n)


# colors = ['purple', 'red', 'orange', 'yellow', 'green', 'black']
#
# index = 0
# while index < len(colors):
# #    print(str(index) + ' color: ', colors[index])
#     print(f'{index}: {colors[index]}')
#     index += 1
#
# print('test'.upper())

correct_list = [1, 2, 3, 4]

correct_list.extend([5, 6, 7, 8])
print(correct_list)

# Removing all things from list

first_list = [1, 2, 3, 4]

first_list.clear()

print(first_list)

# pop -- remove the item at the given positin in the list and return it
# if no index is specified, removes & returns last item in the list

first_list = [1, 2, 3, 4, 5]
first_list.pop()  # 5

# remove -- removes the first item from the list whose value is x. ONLY removes FIRST item at a time.
# throws a ValueError if the item is not found
another_list = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 8]
another_list.remove(6)  # removes the first 6
print(another_list)

# index -- returns the index of the specified item in the list. Ca specify start and end.
print(another_list.index(4))
print(another_list.index(6, 6))

# count -- return the number of times x appears in list
print(another_list.count(6))

# reverse -- reverse the elements of the list in-place
another_list.reverse()
print(another_list)

# sort -- sore the items of the list in-place
another_list.sort()
print(another_list)

# join -- a STR method. Joins a list of strings together
words = ['Today', 'is', 'the', 'greatest', 'day']
print(' '.join(words))
print('Favorite phrase of the day: '.join(words))
names = ['Peter', 'Paul', 'Luke']
friends = ' is my friend. '.join(names)
print(friends)

# Create a list called instructors
instructors = []

# Add the following strings to the instructors list
# "Colt"
# "Blue"
# "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])

# Remove the last value in the list
instructors.pop()

# Remove the first value in the list
instructors.pop(0)

# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')

