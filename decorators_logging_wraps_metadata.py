"""
Typical syntax:
def my_decorator(fn):
    def wrapper(*args, **kwargs):
        # do stuff with fn(*args, **kwargs)
        pass
    return wrapper


Another tutorial example: https://www.youtube.com/watch?v=swU3c34d2NQ

from functools import wraps
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    @wraps(func)
    def log_func(*args):
        logging.info(f"Running {func.__name__} with arguments {args}")
        print(func(*args))
    return log_func

@logger  # With Decorator
def add(x, y):
    return x+y

@logger  # With Decorator
def sub(x, y):
    return x-y


# WITH DECORATOR??? Not sure with add since it's built-in...
add(3, 3)
add(4, 5)
sub(10, 5)
sub(20, 10)

# WITHOUT DECORATOR:
add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)  # 6
add_logger(4, 5)  # 9

sub_logger(10, 5)  # 5
sub_logger(20, 10)  # 10

# **NEXT** Open the file example.log to see log results

"""


# USING WRAPS TO PRESERVE METADATA - LOGGING FUNCTION DATA
# def log_function_data(fn):
#     def wrapper(*args, **kwargs):
#         """I'm a WRAPPER function"""  # This is the doc string __doc__
#         print(f"You are about to call {fn.__name__}")
#         print(f"Here's the documentation: {fn.__doc__}")
#         return fn(*args, **kwargs)
#     return wrapper
#
# @log_function_data
# def add(x,y):
#     """Adds two numbers together."""
#     return x+y
#
# print(add(10, 30))  # PROBLEM WITH ADD FUNCTION!
# print(add.__doc__)  # ALL referring to WRAPPER instead! NOT GOOD!
# print(add.__name__)
# help(add)

'''
SOLUTION - Module called functools with WRAPS FUNCTION! 
wraps is simply a function we use to wrap around our wrapper function.
It ensures that the metadata of the functions that get decorated are 
not lost by the decorator. So, for example, if you decorate @ add or len, 
you won't lose the original metadata for those functions.

from functools import wraps
# wraps preserves a function's metadata
# when it is decorated!

def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs)
        pass
    return wrapper

'''
from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I'm a WRAPPER function"""  # This is the docstring __doc__
        print(f"You are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x+y

print(add(10, 30))
print(add.__doc__)
print(add.__name__)
help(add)



