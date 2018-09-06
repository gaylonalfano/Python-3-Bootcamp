'''
Not working code just example:

# When we write:
@decorator
def func(*args, **kwargs):
    pass

# We're really doing:
func = decorator(func)

# When we write:
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass

# We're really doing:
func = decorator_with_args(arg)(func)

'''
from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:  # If we just did: if args[0] != val we'd get error if no args passed
                return f"First argument needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner

@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito", "ice cream", "pizza"))  # ('burrito', 'ice cream', 'pizza')
print(fav_foods("pizza", "ice cream", "burrito"))  # 'First argument needs to be ...'

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    print(num1 + num2)

print(add_to_ten(20, 5))  # First argument needs to be ...
print(add_to_ten(10, 8))  # 18

