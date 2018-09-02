'''
Beginning of Decorators section. But first a review of Higher Order Functions
Ex. @classmethod is a decorator but first...

HIGHER ORDER FUNCTION - Just a function that either returns anothr function
or accepts one or more functions as an argument(s).

CLOSURES - An inner function that remembers and has access to vars in the local
scope in which it was created EVEN AFTER the outer function has finished executing!
In simple terms, when you've nested functions where the outer function
returns an inner function, and you save that to a variable. A CLOSURE closes over
the free variables from their environment (e.g., message from below 2nd example).


TUTORIAL: https://www.youtube.com/watch?v=swU3c34d2NQ

See example:

def outer_func():
    message = "Hi"

    def inner_func():
        print(message)

    return inner_func  # Notice no () so it won't execute

my_func = outer_func()

my_func()  # Hi

print(my_func)  # <function outer_func.<locals>.inner_func at 0x101010aji>
print(my_func.__name__)  # inner_func !! Now I can execute this variable my_func just like a function!



# NOW ADDING PARAMETERS TO OUR FUNCTIONS:

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func  # Notice no () so it won't execute

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')


'''
# ONE TYPE OF BASIC HIGHER ORDER FUNCTION - Passing functions as args
def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total


def square(x):
    return x**2

def cube(x):
    return x**3

print(sum(3, square))  # 1 2 3 > 1 + 4 + 9 = 14
print(sum(3, cube))


# NESTED FUNCTIONS INSIDE ONE ANOTHER
from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg

    result = get_mood() + person
    return result

print(greet("Toby"))


# RETURN FUNCTIONS FROM OTHER FUNCTIONS
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHA', 'lol', 'tehehe'))
        return l

    return get_laugh  # Returning ENTIRE get_laugh function!

laugh = make_laugh_func()
print(laugh())



# INNER FUNCTIONS CAN ACCESS OUTER FUNCTION SCOPE
# CLOSURES - https://www.youtube.com/watch?v=swU3c34d2NQ
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(("HAHAHA", 'lol', 'tehehe'))
        return f"{laugh} {person}"

    return get_laugh  # Returns the func WITHOUT executing it!

laugh_at = make_laugh_at_func("Linda")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())


'''
Return func vs. Return func()


Michael — Teaching Assistant  · 6 months ago 
Hi Stefan,

make_laugh_func  returns get_laugh , which is a variable that points to that function. So when you assign laugh = make_laugh_func() , the laugh  variable points another function called get_laugh .

When you add parentheses to get_laugh , this invokes the function. So if you return get_laugh() , it returns whatever the result of get_laugh  is, because the function runs before your return statement. 

The TypeError  then comes from adding the parentheses tolaugh  : you're trying to invoke it like a function, but it has already resolved to a string ( TypeError  arises whenever you call a string like a function). Try printing laugh to see what the value is. 

If you return get_laugh  without the parentheses, your laugh  variable can still be pointing to the function, but it has not yet been invoked. Then you invoke it whenever you want.

Hopefully this wasn't too confusing!



'''