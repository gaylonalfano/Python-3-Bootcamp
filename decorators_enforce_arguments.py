'''

# ENSURING ARGUMENTS WITH DECORATORS - Want to enforce certain restrictions
on arguments. For example:
-Prevent a function from being called with any keyword arguments
-Prevent any numerical args
-Prevent certain types of args
-Ensure certain args exist
-Ensure that the first argument is something

*Unrelated - why have to add print()  https://www.udemy.com/the-modern-python3-bootcamp/learn/v4/t/lecture/9376712


'''

from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! Sorry :(")
        return fn(*args, **kwargs)  # Could just not pass **kwargs here
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"Hi there, {name}")

greet("Tony")
#greet(name="Tony")  # Raise ValueError

# DOUBLE_RETURN - Accepts func and returns another func. @double_return
# should decorate a function by returning two copies of the inner functions
# return value inside of a list.
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
        # Alternative syntax:
        # val = fn(*args, **kwargs)
        # return [val, val]
    return wrapper

@double_return
def sub(x, y):
    return x - y

@double_return
def morning_greet(name):
    return "G'morning, {}".format(name)

print(sub(16, 5))
print(morning_greet("Archie"))



# ENSURE_FEWER_THAN_THREE_ARGS
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) >= 3:
            return "Too many arguments!"
        return fn(*args, **kwargs)
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

print(add_all())
print(add_all(1))
print(add_all(1,2))
print(add_all(1,2,3))
print(add_all(1,2,3,4))



# ONLY_INTS - Onlly invoked if ALL args are integers
def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if all(type(arg) == int for arg in args):
            return fn(*args, **kwargs)
        return "Please only invoke with integers."
    return wrapper

'''
WHAT ABOUT CHECKING **KWARGS?
Yes, but what about **kwargs, Žarko? Your solution doesn't work if the user passes non-int keyword arguments into the decorated func, e.g:

add(x="1", y="2") 

Hello Goran,

Thanks for the question.

The task of this particular exercise is to handle function argument types, but if you wanted to check keyword arguments, you could also loop over them inside the inner function:

for key, value in kwargs.items():
    print(type(value))
Click here to see an SO answer. Based on that, you can write logic that will also check kwargs values and their types (you also need alter the add function to accept **kwargs).

subject = obj.subject
body = obj.body
for key, value in kwargs.items():
    subject = subject.replace('[%s]' % key.toupper(), value)
    body = body.replace('[%s]' % key.toupper(), value)

return (subject, body, obj.is_html)

Hope that helps! Let us know what you come up with.

'''



@only_ints
def sub(x, y):
    return x - y

print(sub(10, 3))  # 7
print(sub('gaylon', 3))  # "Please only invoke..."
print(sub(x=15, y=10))  # Is x and y args or kwargs when entered like this?
print()


# Colt's solution w/ ANY():
# def only_ints(fn):
#     @wraps(fn)
#     def inner(*args, **kwargs):
#         if any([arg for arg in args if type(arg) != int]):
#             return "Please only invoke with integers."
#         return fn(*args, **kwargs)
#     return inner

'''
Alt solution:
def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            new_args = []
            for i in args:
                i = int(i)
                new_args.append(i)
            new_args = tuple(new_args)
            return fn(*new_args, **kwargs)
        except ValueError as err:
            raise err
    return wrapper
'''


# ENSURE_AUTHORIZED EXERCISE - Accepts a func and returns another func.
# The func passed should have kwarg of 'role' = 'admin', otherwise 'Unauthorized'
def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('role') == 'admin':
            return fn(*args, *kwargs)
        return "Unauthorized"
    return wrapper

@ensure_authorized
def show_secrets(*args, **kwargs):
    return f"Shh! Don't tell about {args}!"

print(show_secrets(a='b'))
print(show_secrets(role='admin'))
print(show_secrets(role='anybody'))

