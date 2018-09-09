'''
DOCTESTS - The docstring """ """ you can actually write test 
code in there as well and Python a way of parsing and running
those tests. It's not the best way of testing but is nice to 
know about. 

The catch/issue is you have to write your code is a weird way. You
have to write your code to look like it's inside a REPL.

def add(x, y):
    add together x and y

    >>> add(1, 2)  # Turns into a TEST
    3

    >>> add(8, 'hi')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    
    return x + y

NOTE you can test this out without even having to call the function
by using a special python command: python3 -m doctest -v name_of_file.py

Really finicky! Need to use single quotes in doctest ' and be careful
of spacing within lists! Or traveling whitespace after something...
BUGGY! Not first choice for testing - clutters up function code, 
lacks many features of larger testing tools, and tests are brittle.
Better is unit tests.

'''


def add(x, y):
    """
    add together x and y

    >>> add(1, 2)
    3

    >>> add(8, 'hi')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """

def sub(a, b):
    """subtract b from a
    >>> sub(2, 3)
    -1
    >>> sub(100, 200)
    -100
    """
    return a - b

# Practice the TDD method: Red, Green, Refractor
def double(values):
    """ double the values in a list

    >>> double([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return []


def say_hi():
    """
    >>> say_hi()
    'hi'
    """
    return 'hi'



