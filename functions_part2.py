# Two objectives:
# Use the * and ** operator as parameters to a function and outside of a function
# Leverage dictionary and tuple unpacking to create more flexible functions

# *args -- It's a TUPLE. A special operator we can pass to functions. Gathers remaining arguments as a tuple
# This is just a PARAMETER - you can call it whatever you want but usually *args.

# def sum_all_nums(num1, num2, num3):
#     return num1 + num2 + num3
#
# print(sum_all_nums(4, 6, 9))  # But if we add more than 3, we'd like them to still be added


# Even better is to use *args
def sum_all_nums(*args):  # Need the '*' ONLY for the definition
    total = 0
    for num in args:
        total += num
    return total

# Can also add other parameters
def sum_all_nums(num1, *args):
    print(num1)
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(4, 6, 9, 4, 10))  # returns a tuple
print(sum_all_nums(4, 6))


# Another example
def ensure_correct_info(*args):
    if 'Colt' in args and 'Steele' in args:
        return 'Welcome back Colt!'  # If you use a return statement in a conditional, don't need 'else:'
    return 'Not sure who you are...'

print(ensure_correct_info([1, 2, 'hello'], 44, 'hello', False, 'Colt', 'Stee'))  # Not sure who you are...

print(ensure_correct_info(1, True, 44, 'Steele', 'Colt'))  # Welcome back Colt!


# CONTAINS_PURPLE() - contains_purple() accepts ANY NUMBER OF ARGUMENTS.
# Returns True if any arg are 'purple'.
def contains_purple(*args):
    if 'purple' in args:
        return True
    return False

print(contains_purple('a', 99, ['aaron', 'billy'], False, 1, True))  # False
print(contains_purple('a', 99, ['aaron', 'billy', 'purple'], False, 1, True))  # False
print(contains_purple('a', 99, ['aaron', 'billy'], False, 1, True, 'purple'))  # True


# SQUARE_DIGITS()
def square_digits(num):
    result = ''
    for digit in tuple(str(num)):
        result += str(int(digit) ** 2)
    return int(result)

# Another variation

print(square_digits(345))


# REPLACE_WITH_ALPHABET_POSITION(STRING)
# def alphabet_position(string):
#     alphabet = dict(zip('abcdefghijklmnopqrstuvwxyz', list(range(1, 27))))
#     positions = [alphabet[l] for l in string.lower() if l in alphabet]
#     result = ''
#     for i in positions:
#         result += str(i) + ' '
#     return result

# Better by using .join(). It can iterate over a string or list of strings
def alphabet_position(string):
    alphabet = dict(zip('abcdefghijklmnopqrstuvwxyz', list(range(1, 27))))
    positions = [str(alphabet[l]) for l in string.lower() if l in alphabet]
    return ' '.join(positions)

# Best! Uses ord('a') - 96 = 1; Also uses .isalpha() check and ' '.join()
# Also, note that you do NOT need the [] to do list comprehension if using .join(). Cool!
# Apparently this is a generator expression: https://stackoverflow.com/questions/9060653/list-comprehension-without-in-python
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

print(alphabet_position('TOOOOOoday is a great day'))



# **kwargs -- A DICT. A special operator we can pass to functions. Pronounced QWARGS
# Gathers remaining keyword arguments and stores them into a dictionary
# This is just a parameter - you can call it whatever you want!

# Could do...
# def fav_colors(colt, ruby, ethel)

# However, better is:
def fav_colors(**kwargs):
    print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(colt='purple', ruby='red', ethel='teal')
fav_colors(colt='purple', ruby='red', ethel='teal', ted='blue')
fav_colors(colt='royal deep amazing purple')
fav_colors(colt='')  # nothing returns


# Another example:
def special_greeting(**kwargs):
    if 'David' in kwargs and kwargs['David'] == 'special':
        return 'You get a special greeting, David!'
    elif 'David' in kwargs:
        return f"{kwargs['David']} David!"
    return "Not sure who this is..."

print(special_greeting(David='Hello'))  # Hello David!
print(special_greeting(Bob='hello'))  # Not sure who this is...
print(special_greeting(David='special'))  # You get a special greeting, David!
print(special_greeting(David="What's up", Gaylon='Ni hao'))  # What's up David
print(special_greeting(Bob='howdy', David='special'))  # You get a special greeting, David


# **kwargs Exercise -- COMBINE_WORDS(word, **kwargs)
def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

# Another syntax using .get()
def combine_words(word, **kwargs):
    return kwargs.get('prefix', '') + word + kwargs.get('suffix', '')

print(combine_words(word='child', suffix='ren', more='are a pain'))
print(combine_words(word='child', prefix='my', suffix='lovesme'))
print(combine_words(word='work', prefix='home'))
print(combine_words(word='child', something='ren', more='are a pain'))


# PARAMETER ORDERING
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

def display_info(a, b, *args, instructor='Colt', **kwargs):
    return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))
# [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]


# TUPLE UNPACKING - Using * as an argument: argument unpacking
# We can use * as an argument to a function to 'unpack' values
def sum_all_values(*args):
    print(args)  # it's a tuple! ([1, 2, 3, 4, 5, 6],)
    total = 0
    for num in args:
        total += num  # when passing nums, it's trying to += a LIST!
    print(total)  # Should use return but just for ease using print

# sum_all_values(1, 30, 2, 5, 6)  # 44
nums = [1, 2, 3, 4, 5, 6]
# sum_all_values(nums)  # Error since the function isn't built to accept lists

# So how do we tell the program to take everything in a list/tuple and turn them
# into individual/separate arguments for this function? Answer: Add the '*' as an argument!
sum_all_values(*nums)  # 21


# UNPACKING EXERCISE - First call count_sevens() with 1, 4, and 7. Then call it again with all
# numbers contained in nums list as individual arguments (unpack the list).

# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1, 4, 7)

result2 = count_sevens(*nums)

print(count_sevens(1, 4, 7))  # 1
print(count_sevens(*nums))  # 14



# DICTIONARY UNPACKING - Using ** as an argument to unpack dictionaries into keyword arguments
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {'first': 'Colt', 'second': 'Rusty'}

display_names(first='Charlie', second='Sue')  # Charlie says hello to Sue
#display_names(names)  # Error
display_names(**names)  # Colt says hello to Rusty


def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c)
    print('OTHER STUFF...')
    print(kwargs)

data = dict(a=1, b=2, c=3, d=55, name='Tony')

# add_and_multiply_numbers(data)  # TypeError
# add_and_multiply_numbers(**data)  # 7
add_and_multiply_numbers(**data, cat='Blue')  # 7 \n OTHER STUFF \n {'d': 55, 'name'...}



# CALCULATE() EXERCISE
'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

# def calculate(first, second, **kwargs):
#     if kwargs.get('operation') == 'add':
#         if kwargs.get('make_float') == True:
#             return f"{kwargs.get('message', 'The result is')} {float(first + second)}"
#         return f"{kwargs.get('message', 'The result is')} {int(first + second)}"
#     elif kwargs.get('operation') == 'subtract':
#         if kwargs.get('make_float') == True:
#             return f"{kwargs.get('message', 'The result is')} {float(first - second)}"
#         return f"{kwargs.get('message', 'The result is')} {int(first - second)}"
#     elif kwargs.get('operation') == 'multiply':
#         if kwargs.get('make_float') == True:
#             return f"{kwargs.get('message', 'The result is')} {float(first * second)}"
#         return f"{kwargs.get('message', 'The result is')} {int(first * second)}"
#     elif kwargs.get("operation") == 'divide':
#         if kwargs.get('make_float') == True:
#             return f"{kwargs.get('message', 'The result is')} {float(first / second)}"
#         return f"{kwargs.get('message', 'The result is')} {int(first / second)}"
#     return "Something's wrong. Not enough arguments provided."


# Instructor created another dict called operation_lookup
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 1),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    # operation_value = operation_lookup[kwargs.get('operation')]
    if kwargs.get('make_float'):
        return '{} {}'.format(kwargs.get('message', 'The result is'), float(operation_lookup[kwargs.get('operation', 'add')]))
    return '{} {}'.format(kwargs.get('message', 'The result is'), int(operation_lookup[kwargs.get('operation', 'add')]))


print(calculate(first=3, second=9, operation='add', make_float=True))
print(calculate(first=3, second=9, operation='add', make_float=False, message="You just added"))
print(calculate(first=3, second=9, operation='divide', make_float=True, message="You just divided"))
print(calculate(first=3, second=9, operation='subtract', make_float=False, message="You just subtracted"))
print(calculate(first=3, second=9, operation='multiply', make_float=True))
print(calculate(first=3, second=9, operation='multiply', make_float=True, message="You just multiplied"))