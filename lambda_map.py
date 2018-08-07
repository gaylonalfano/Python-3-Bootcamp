'''
Lambdas - Single lines. Lambda parameters: expression (return is implicit)
Can write a lambda function and save to a variable but won't do this normally.

Why use lambdas? - Most common use case is when you have some code and you
need to pass a function into another function as a parameter and you'll never
use that function again.
'''

def square(num): return num ** 2  # Can put it on one line

add = lambda a, b: a + b


square2 = lambda num: num ** 2  # Anonymous functions
print(square(9))
print(square2(3))
print(square.__name__)  # square
print(square2.__name__)  # <lambda> doesn't have a name
print(add.__name__)

add_values = lambda x, y: x + y

multiply_values = lambda x, y: x * y

print(add_values(10, 20))

print(multiply_values(10, 20))

# CUBE_A_NUMBER_LAMBDA
cube = lambda num: num **3
print(cube(3))


# MAP - A standard function that accepts at least two arguments, a function and an iterable
# Iterable is something that can be iterated over (lists, strings, dicts, sets, tuples)
# map() runs the lambda for each value in the iterable and returns a map object
# which can be converted into another data structure.

# Note: Can only iterated over once. Need to recreate it or just turn to list

nums = [2, 4, 6, 8, 10]
doubles = list(map(lambda x: x*2, nums)) # This is a map object that we can iterate over
for num in doubles:
    print(num)

print(list(doubles))


# Another example
people = ["Darcy", 'Christina', 'Dana', 'Annabel']

peeps = list(map(lambda name: name.upper(), people))
print(peeps)


# Another but with a dictionary
names2 = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele'},
    {'first': 'Blue', 'last': 'Steele'}
]

first_names = list(map(lambda x: x['first'], names2))
print(first_names)  # ['Rusty', 'Colt', 'Blue']


# Don't have to use a lambda, could create a function
def double(x): return x*2


# DECREMENT_LIST() - Accepts a list of numbers. Return a copy of the list
# where each item has been decremented by one. Use map()
def decrement_list(list_of_nums):
    return list(map(lambda x: x-1, list_of_nums))

print(decrement_list([5, 4, 3, 2, 1]))  # [4, 3, 2, 1, 0]



# TRIPLE AND FILTER() - Accepts list of numbers, filter out those not divisible by 4,
# return new list where every remaining number is tripled
'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

# Using map and filter:
def triple_and_filter(nums):
    return list(map(lambda x: x * 3, filter(lambda n: n % 4 == 0, nums)))


# Using list comprehension:
def triple_and_filter2(nums):
    return [num*3 for num in nums if num % 4 == 0]


# Student solution:
def triple_and_filter3(list_of_nums):
    return [item*3 for item in list(filter(lambda x:x%4 == 0,list_of_nums))]

print(triple_and_filter([6, 8, 10, 12]))  # 24, 36
print(triple_and_filter2([6, 8, 10, 12]))

print(triple_and_filter([1,2,3,4]))
print(triple_and_filter2([1,2,3,4]))