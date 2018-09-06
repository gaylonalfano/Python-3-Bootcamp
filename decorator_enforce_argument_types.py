'''
ENFORCING TYPES AND ATTEMPTS TO CONVERT IF NO MATCH
This is handy/Pythonic since if you can try to convert
a float to an int and continue the program, then great


ENFORCING FIRST ARGUMENT
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
# def ensure_first_arg_is(val):
#     def inner(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != val:  # If we just did: if args[0] != val we'd get error if no args passed
#                 return f"First argument needs to be {val}"
#             return fn(*args, **kwargs)
#         return wrapper
#     return inner

# Note that this isn't maybe the best implementation of this but it's a good example
def enforce(*types):
    def decorator(f):  # inner
        def new_func(*args, **kwargs):  # wrapper
            # Convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))  # Feel free to have more elaborate
            return f(*newargs, **kwargs)
        return new_func  # wrapper
    return decorator  # inner


@enforce(str, int)  # types
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)  # Could use int but it would lose decimal data
def divide(a, b):
    print(a/b)

'''
Breakdown of how this works:
types - str, int
args -- So when zip(args, types) you get ("hello", str) ('3', int)

Then, newargs will append these pairs BUT by calling type(arg) 
e.g., str("hello") = "hello";  int("3") = 3

So, newargs will look like this: ["hello", 3]
Next, we pass f(*newargs, **kwargs) which essentially CHANGES what
is passed by then adding/using @enforce!

Originally this is passed:                "hello", "3"
But with f(*NEWARGS, **kwargs) it's now:  ["hello", 3]
'''

repeat_msg("hello", "5")  # hello, hello, ...
divide(1,2)  # 0.5
divide("1", "4")  # 0.25
