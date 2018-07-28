# Tuple = ordered collection or grouping of items but are immutable!
# and tuples are faster than lists.
# Can use tuples as keys in DICT
from typing import Tuple

numbers = (1, 2, 3, 4, 5)  # Cannot update/change

x = (1, 2, 3)
print(3 in x)
x[0]

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
for month in months:
    print(month)

# Print months out in backward order using while loop
i = len(months) - 1  # 11
while i >= 0:
    print(months[i])
    i -= 1

locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4195): "San Francisco Office"
}

print(locations[(37.7749, 122.4195)])

# .items() returns tuples for dictionaries

# Looping with tuples
for loc in locations.values():  # returns VALS
    print(loc)

for k, v in locations.items():  # returns KEYS, VALS
    print(k, v)

for k, v in locations:  # returns KEYS
    print(k, v)

# Tuple methods
# tuple([list of values]) -- Converts a list into a tuple
# .count() -- Returns the number of times a value appears in a tuple
print(months.count('Dec'))

# .index() -- Returns the index at which a value is found in a tuple
t = (1, 2, 3, 3, 3)
t.index(1)  # 0
# t.index(5)  # ValueError: tuple.index(x): x not in tuple
t.index(3)  # 2 -- only the first matching index is returned

# Nested tuples and slicing
nums = (1, 2, 3, (4, 5), 6, 7)
nums[0]
nums[3]  # (4, 5)
nums[3][1]  # 4
nums[0: 4: 2] # (1, 3)



# SETS -- Collections of data. Formal mathematical sets. Sort of like a dict/list combo
# Do not have duplicate values. It's all UNIQUE data
# Elements in sets aren't ordered
# You cannot access items in a set by index
# Used for: When you need to keep track of a collection of elements,
# but you don't care about ordering, keys, or values and duplicates
# SETS don't seem to work with values that equal boolean "True" - odd... "False" works...
# See function exercises part 1 - INTERSECTION()

# Creating .set()
s = set({1, 2, 3, 4, 5, 5, 5, 'a', 'b', 23.3334})  # {1, 2, 3, 4, 5}
s = set({1, 4, 5})
# Creates a set w/ the same values as above
s = {1, 4, 5}
4 in s  # True
8 in s  # False
# Can use for loops
for thing in s:
    print(thing)

# One common use for sets is to convert a list that has duplicates into a set using .set()
# Then you can convert that unique set back into a list so you end up with a list of unique values
registrants_cities = ['austin', 'houston', 'dallas', 'austin', 'georgetown', 'houston', 'houston']
print(set(registrants_cities))
print(len(set(registrants_cities)))
print(len(registrants_cities))

# Set Methods
# add -- Way to add items
cities = {'LA', 'Dallas', 'NYC', 'Chicago', 'Austin', 'Houston', 'Austin', 'Seattle', 'LA'}
print(len(cities))

# remove - removes a value from the set and returns a KeyError if the value is not found

# discard -- if you need to avoid KeyErrors then use .discard()

# copy -- makes a duplicate but are NOT identical
h = set({1, 2, 3})
another_h = h.copy()
print(another_h)
print(another_h is h)  # False

# clear -- removes all the contents of set

# Set Math -- intersection, symmetric_difference, union
math_students = {'matthew', 'helen', 'prashant', 'james', 'aparna'}
biology_students = {'jane', 'matthew', 'charlotte', 'mesut', 'oliver', 'james'}
# Now want to generate a set of all students but w/o duplicates. Use union
print(math_students | biology_students)
# Or, want a set of students who are in both sets (intersection)
print(math_students & biology_students)


# TUPLES AND SETS EXERCISE
# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers_ = (1, 2, 3, 4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value: Tuple[int] = (1,)

# 3 - Given the following variable:
values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
print(static_values)

# 4 - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]
# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)