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
    return(f'Your full name is {string1} {string2}')
# Better
def print_full_name(first_name, last_name):
    return(f'Your full name is {first_name} {last_name}')


# Parameters vs Arguments
# Parameter = A variable in a method DEFINITION. It's a var in the declaration of a function.
# Argument = When a method is CALLED, the arguments are the data you pass into the method's parameters.
# It's the actual value of this variable that gets passed to the function.


