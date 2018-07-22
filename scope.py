# SCOPE - Where our variables can be accessed
# * Vars created in functions are scoped in that function
# **NOTE - "Keep it in the function until you write something else that relies on it too


instructor = 'Colt'  # Global scope


# def say_hello():
#     return f'Hello {instructor}'
#
#
# say_hello()


# def say_hello():
#     instructor = 'Colt'  # Scoped inside the bounds of this function ONLY.
#     return f'Hello {instructor}'
#
#
# say_hello()
#
# print(instructor)  # NameError because cannot access the var instructor


# So how to access variables that have been scoped INSIDE a function? You can RETURN them!
# Ex. Have your function return the variable 'instructor'. Then every time you call the function
# you could save it to another/new variable.

# GLOBAL SCOPE - Not defined inside a function. Generally speaking, not ideal to use global variables.
# Want to minimize the use of global variables. Note that you can reference global variables but
# if you want to modify the existing global var, you must use 'global'

# total = 0
#
# def increment():
#     total += 1
#     return total
#
# increment()  # Error! "local variable 'total' referenced before assignment"
#
# # Instead, let's reference variables (use 'global var_name') that were originally assigned on the global scope
# total = 0
#
# def increment():
#     global total  # Telling python to reference the global total variable
#     total += 1
#     return total
#
# print(increment())  # 1


# NONLOCAL - Lets us modify a parent's variables in a child (aka nested) function.
# Below, the var 'count' is not global and also not defined in inner(). Therefore, need
# to use nonlocal to modify it from within the inner() nested function.
# **Note: You won't use global or nonlocal keywords all that frequently.
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner()


#print.__doc__  # .__doc__ allows you to retrieve the text you store while documenting your functions


# using """ """
def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"


print(say_hello())

print(say_hello.__doc__)  # A simple function that...
