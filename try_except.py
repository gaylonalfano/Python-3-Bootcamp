'''
In Python, it is STRONGLY encouraged to use try/except blocks to catch exceptions
when we can do something about them. Let's see what that looks like.

Most basic form:

try:
    foobar
except NameError as err:
    print(err)
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
