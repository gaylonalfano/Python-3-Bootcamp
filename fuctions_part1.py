# What is a function?
# methods vs. functions -- all functions really.
# Function = a process for executing a task. Don't always get the same result; depends on input
# Useful way fo executing similar procedures over and over
# Some accept input and some do not.

# Why use functions?
# Stay DRY - Don't Repeat Yourself!
# Clean up and prevent code duplication
# "Abstract away" code for other users --
# imagine having to rewrite the print() function for every program you wrote
# Can also help you organize your code

def say_hi():
    print('Hi!')


say_hi()


# How to return values from functions. MUST use return. It's the output side of things
# def print_square_of_7():
#     print(7**2)
# print_square_of_7()
#
# # Have to be EXPLICIT when you want to return something out
# def square_of_7():  # Nothing happens. Similar to behavior of s = len('howdy')
#     7**2
# result = square_of_7()
# print(result)  # None is returned

# Have to use 'return' to get something out of a function
def square_of_6():
    return 6 ** 2
    print("I'm after the return")  # won't do anything since after return


result = square_of_6()
print(result)  # This outputs 36


# Keyword: return
# * It exits the function
# * Outputs whatever value is placed after the return keyword. Can use a tuple to return multiple items
# * Pops the function off of the call stack
# https://www.cs.ucsb.edu/~pconrad/cs8/topics.beta/theStack/02/

def generate_evens():
    return [i for i in range(1, 50) if i % 2 == 0]


print(generate_evens())


# How to alter functions so that they accept inputs
def add(a, b):
    return a + b


print(add(5, 1))


# Paremeters -- Vars that are passed to a function. Like placeholders that get assigned when
# you call the function. You can call parameters anything.
def multiply(first, second):  # first, second only exist in the function
    return first * second


multiply(5, 5)
multiply(2, 3)


# Naming parameters
# Not great
def print_full_name(string1, string2):
    return (f'Your full name is {string1} {string2}')


# Better
def print_full_name(first_name, last_name):
    return (f'Your full name is {first_name} {last_name}')


# Parameters vs Arguments
# Parameter = A variable in a method DEFINITION. It's a var in the declaration of a function.
# Argument = When a method is CALLED, the arguments are the data you pass into the method's parameters.
# It's the actual value of this variable that gets passed to the function.
def yell(string):
    return string.upper() + "!"


print(yell('gaylon'))


def yell(string):
    return f'{str.upper(string)}!'


print(yell('ashley'))


def yell(string):
    return f'{string.upper()}!'


# def yell(string):
#     return "{}!".format(string.upper())
# print(yell('aaron'))

# COMMON MISTAKES WHEN USING RETURN
# 1. Placing return INSIDE/TOO SOON. Return essentially ends the program
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return


# 2. Unnecessary ELSE when returning boolean values
def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:
        return False


# Better
def is_odd_number(num):
    if num % 2 != 0:
        return True  # Don't need else if TRUE since return ends function
    return False


# Coding exercise
# Without adding any new lines of code, make count_dollar_signs work as intended
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count


# HOW TO SETUP DEFAULT PARAMETERS & WHY HAVE THEM?
# * Allows you to be more defensive
# * Avoids errors with incorrect parameters
# * More readable examples
# * Defaults can be anything - functions, lists, dicts, strings, bools

# Let's make power default to 2 if no arguments passed
# making parameter power = 2
def exponent(num, power=2):
    """exponent(num, power) raises num to specified power. Power defaults to 2."""
    return num ** power

print(exponent(2, 3))  # 8
print(exponent(3, 2))  # 9
print(exponent(7))
print(exponent.__doc__)


def add(a=10, b=20):
    return a + b

print(add())  # 30
print(add(5))  # 25 (a = 5, b = 20)
print(add(1, 10))  # 11


# More complex example of default parameters
def show_information(first_name='Colt', is_instructor=False):
    if first_name == 'Colt' and is_instructor:
        return "Welcome back instructor Colt!"
    elif first_name == 'Colt':
        return "I really thought you were an instructor..."
    return f"Hello {first_name}!"

show_information()  # "I really thought..."
show_information(is_instructor=True)  # "Welcome back..."
show_information('Molly')  # Hello Molly!


# Set other functions as default parameters example
def add(a, b):
    return a + b

def math(a, b, fn=add):
    return fn(a,b)

def subtract(a, b):
    return a - b

math(2, 2)  # 4
math(2, 2, subtract)  # 0
math(2, 2, multiply)  # 4


# Coding exercise
# def speak(animal="dog"):
#     if animal == "pig":
#         return "oink"
#     elif animal == "duck":
#          return "quack"
#     elif animal == "cat":
#         return "meow"
#     elif animal == "dog":
#         return "woof"
#     else:
#         return "?"

# Another option is to use a DICT
noises = {
    "dog": "woof",
    "pig": "oink",
    "duck": "quack",
    "cat": "meow"
}

def speak(animal='dog'):
    if animal in noises.keys():
        return noises.get(animal, '?')
#  return "?"  # Can be even better using .get(animal, '?')

print(speak('duck'))
print(speak('cat'))
print(speak())

# KEYWORD ARGUMENTS - Order doesn't matter if you know the parameters
# These are different than default parameters.
# * When you define a function and use an = you are setting a default parameter
# * When you invoke a function and use an = you are making a keyword argument
