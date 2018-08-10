'''
Python Debugger (pdb) -- To set breakpoints in our code we can use pdb by inserting this line:

def function(params):
    import pdb; pdb.set_trace()  - Usually added/imported like this inside a function
    *Rest of code*

Usually placed right before something starts breaking. Allows you to see a preview of what happens before/after.


Pdb Commands:
l (list)
n (next line)
a all values
p (print)
c (continue - finishes debugging by running the rest of the code)

NOTE - If you have parameters/variable names that are any of these above COMMANDS,
then you need to type: "p [variable name]" to print the value of that var. Ex. p c #


'''

# import pdb
#
#
# first = 'First'
# second = 'Second'
# pdb.set_trace()
# result = first + second
# third = 'Third'
# result += third
# print(result)


# def add_numbers(a, b, c, d):
#     import pdb; pdb.set_trace()
#
#     return a + b + c + d
#
# add_numbers(1, 2, 3, 4)


# DIVIDE() - two params num1, num2. If you don't pass the correct amount of args
# it should say "Please provided two integers or floats". If num2 == 0, should
# raise a ZeroDivisionError, so return string "Please do not divide by zero"

def divide(num1, num2):
    try:
        return num1/num2
    except TypeError:
        print("Please provide two integers or floats")
    except ZeroDivisionError:
        print("Please do not divide by zero")


# def divide2(num1):
#     import pdb; pdb.set_trace()
#     if type(num1) != int or type(num1) != float:
#         raise TypeError("Please provide two integers or floats")
#     # elif num2 == 0:
#     #     raise ZeroDivisionError("Please do not divide by zero")
#     else:
#         print(num1)




# divide(4, 2)
# divide([], "1")
# divide(1, 0)

# divide2('1', '2')
# divide2(4, '1')
# divide2([], 0)
divide2(5)