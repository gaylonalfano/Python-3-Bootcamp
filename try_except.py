'''
In Python, it is STRONGLY encouraged to use try/except blocks to catch exceptions
when we can do something about them. Let's see what that looks like.

Most basic form:

try:
    foobar
except NameError as err:
    print(err)
'''


'''
WHEN TO USE TRY/EXCEPT VS. RAISE:

You would want to use try-except when you want to try running a code that may or may not cause an error, 
and you want to catch that error in the except block and add some additional logic that needs to get run 
if the error does get triggered. In this exercise, we are just returning messages to the user which explain 
what went wrong and that only numbers can be used/no zero for division. Really important difference is that 
if you don't raise an error within try-except, the code under the blocks can continue running, the script 
doesn't necessarily need to stop like when using raise alone. It's also considered a cleaner approach to
 try executing a potentially error-prone code and catching those errors if they happen.

raise can be used with try-except, where you can raise a custom error for the user, for example. It can also
 be used alone for your own errors, when you want to check a value of something and if it isn't what you except, 
 you can just directly throw an error to the user and stop the script.

So, try is used to execute code that might raise an Exception that you're expecting. Instead of stopping 
the program, you can catch the exception and deal with it in your code. Also, finally can be really useful 
in the combination, see here. The important point is that it doesn't have to stop the execution, the code 
below try-except can keep running - you can set some values in the except block which will then make the 
code below works differently, and adapt to the error that got triggered in the try block.

Read more here: https://stackoverflow.com/questions/40182944/difference-between-raise-try-and-assert

Please let me know if you have any more questions.

Regards,
Zarko
'''





# try:
#     foobar
# except:
#     print("PROBLEM!")
# print("after the try")


# def get(d, key):
#     try:
#         return d[key]
#     except KeyError:
#         return (f'{key} is not in {d.keys()}')
#
#
#
# d = {"name": "Ricky", 'address': 'shanghai', 'color': 'purple'}
# #d["city"]  # KeyError if you don't add to dict
# print(get(d, 'name'))  # Ricky
# print(get(d, 'city'))  # None



'''
Common use for when you are accepting user input.
try:
except:
else: The else block is only executed if the code in the try doesn't raise an exception. 
finally:  Runs no matter what. Good for closing database connections or a file.
'''
# while True:
#     try:
#         num = int(input('please enter a number: '))  # 10
#     except ValueError:
#         print('That\'s not a number!')  # Runs if a problem
#     else:
#         print("Good job, you entered a number!")
#         break
#     finally:
#         print("Runs no matter what!")  # Problem or no problem it will run!
#
# print("Rest of game logic runs!")

# try:
#     num = int(input('please enter a number: '))  # 10
# except:
#     print('That\'s not a number!')  # Runs if a problem
# else:
#     print("I'm in the ELSE!")  # 10
# finally:
#     print("Runs no matter what!")  # Problem or no problem it will run!


def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:  # Can combined multiple Errors using a TUPLE (ZeroDivisionError, TypeError) as err:
        print('do not divide by zero please')
    except TypeError as err:  # can add 'as err'
        print(f'{a} and {b} must be ints or floats')
        print(err)
    # else:
    #     print(f"{a} divided by {b} is {result}")


#print(divide(1, 2))
print(divide(1, 'a'))
#print(divide(1, 0))
