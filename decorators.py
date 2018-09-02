'''
DECORATORS - They are HIGHER ORDER functions. They wrap other functions and enhance their
behavior. They are examples of higher order functions and have their own syntax using "@"

Very similar to CLOSURES, but basically DECORATORS are handy since we can define/create
our own decorator function and then use @ in front of another function. In the below
case we've created a be_polite function and then we decorated "@" other functions with it.

# Just add *args and **kwargs to wrapper() to handle different function signatures:

def my_decorator(fn):
    def wrapper(*args, **kwargs):
        # do stuff with fn(*args, **kwargs)
        pass
    return wrapper

'''

# WITHOUT SYNTACTIC SUGAR - DECORATORS AS FUNCTIONS:
# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper
#
# def greet():
#     print("My name is Colt.")
#
# def rage():
#     print("I HATE YOU!")
#
# greet = be_polite(greet)  # The two funcs have no relation UNTIL this is where we start to DECORATE our function
# print(greet)  # <function be_polite.<locals>.wrapper at 0x100ea06a8> -- similar to CLOSURES
# print(greet.__name__)  # wrapper
# print(greet())  # What a pleasure to meet you! My name is Colt. Have a great day!
#
# polite_rage = be_polite(rage)
# polite_rage()


# BETTER METHOD - ADDING SYNTACTIC SUGAR WITH "@"
# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper
#
# @be_polite  # Don't need to set greet = be_polite(greet)
# def greet():
#     print("My name is Gaylon.")
#
# @be_polite  # Automatically uses the function name as the variable name (rage = be_polite(rage))
# def rage():
#     print("I HATE YOU!")
#
# print(greet.__name__)  # wrapper
# print(greet)  # <function be_polite.<locals>.wrapper at 0x104e2d6a8>
# greet()
# rage()
# print(rage.__name__)


# DIFFERENT SIGNATURES - greet() takes one argument, order takes two()
# Broken version due to different signatures:
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

# def shout(fn):
#     def wrapper(*args, **kwargs):
#         return fn(*args, **kwargs).upper()
#     return wrapper
#
# @shout
# def greet(name):
#     return f"Hello, I'm {name}!"
#
# @shout
# def order(main, side):
#     return f"Hi, I'd like the {main}, with a side of {side}, please."
#
# @shout
# def lol():
#     return "lol"
#
# # @shout
# # def poor_hearing(person):
# #     return f"{person} can you say that again?"
#
# print(greet("Aaron"))
# print(order(main='kungpao', side='salad'))  # TypeError: wrapper() takes 1 positional argument but 2 were given.
# print(order(side='burger', main='fries'))  # Can switch it all up with kwargs
# print(lol())



# SHOW_ARGS EXERCISE
from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args: {}".format(args))  # f"Here are the args: {tuple(args)}")
        print("Here are the kwargs: {}".format(kwargs))  # f"Here are the kwargs: {dict(kwargs)}")
        return fn(*args, **kwargs)
    return wrapper

@show_args
def do_nothing(*args, **kwargs):
    pass


@show_args
def do_nothing2(*args, **kwargs):
    pass

#do_nothing(1, 2, 3, a='hi', b='bye')
do_nothing2(1, [1, 2, 3], True, a='Ash', b='Gay')
