'''
def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:  # If we just did: if args[0] != val we'd get error if no args passed
                return f"First argument needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner

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

****Breakdown of how the above works:
types - str, int
args -- So when zip(args, types) you get ("hello", str) ('3', int)

Then, newargs will append these pairs BUT by calling type(arg)
e.g., str("hello") = "hello";  int("3") = 3

So, newargs will look like this: ["hello", 3]
Next, we pass f(*newargs, **kwargs) which essentially CHANGES what
is passed by then adding/using @enforce!

Originally this is passed:                "hello", "3"
But with f(*NEWARGS, **kwargs) it's now:  ["hello", 3]

===========

@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"

'''

from functools import wraps
from time import sleep


def delay(time):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(time, fn.__name__))
            sleep(time)
            return fn(*args, **kwargs)
        return wrapper
    return inner

@delay(5)
def say_hi():
    return "hi"


print(say_hi())

'''
Hello Ethan,

Thanks for the question.

You should put all the wrapping code inside the wrapper function.

When we wrap the say_hi function with the delay function, we are actually calling the inner function with say_hi passed as an argument. That means that the inner function will run when we run our python .py script, even without calling say_hi() explicitly. If you put your timer code outside of the wrapper, it will run on .py script load regardless of the fact that we are potentially not even calling the say_hi() function. It can pass the tests because they are testing things on script load, but you could run into issues otherwise.

You want to put that code inside the wrapper function, which gets returned from the executed inner function. The wrapper function that gets returned is not immediately ran, but it's waiting for us to run it with say_hi()

Please let me know if you have any more questions.

'''