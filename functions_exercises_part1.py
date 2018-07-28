# RETURN_DAY()
# Mine
'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''
days_of_the_week = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
    }


def return_day(num):
    return days_of_the_week.get(num, None)


# Instructor's:
# def return_day(num):
#     days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
#     # Check to see if num valid
#     if num > 0 and num <= len(days):
#         # use num - 1 because lists start at 0
#         return days[num-1]
#     return None
#
#
# def return_day(num):
#     try:
#         return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
#     except IndexError as e:
#         return None

# Another syntax shortcut: GREATER THAN X BUT LESS THAN Y
# if 1 <= day <= 7:
#     return days_of_week[day - 1]


# LAST_ELEMENT() - Return the last value of any list or None if list is empty
'''
last_element([1,2,3]) # 3
last_element([]) # None
'''
# My solution:
def last_element(list):  # one list parameter
    if len(list) == 0:
        return None
    return list[-1]


# Instructor's:
def last_element(l):
    if l:  # If a list has any value then it's True
        return l[-1]
    return None


# print(last_element(['Aaron', 1, 77.77, 'Matt']))
# print(last_element([]))



# NUMBER_COMPARE() - Takes two num params. If num1 > num2
'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(num1, num2):
    if num1 > num2:
        return "First is greater"
    elif num1 < num2:
        return "Second is greater"
    return "Numbers are equal"


print(number_compare(4, 1))
print(number_compare(3, 3))
print(number_compare(2, 10))



# SINGLE_LETTER_COUNT() - Two params. First is word. Second is a letter. Case sensitive. Return 0 if not found
'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
def single_letter_count(word, letter):
    return tuple(word.lower()).count(letter.lower())



# MULTIPLE_LETTER_COUNT() - One string param. Return dict w/ keys being the letters, values being count of the letter
# HARD because I forgot about DICT comprehension
'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
# def multiple_letter_count(word):
#     result = {}.fromkeys(word, word)
#     for k, v in result.items():
#         result[k] = v.count(k)
#     return result


# Instructor's using dict comprehension
def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in word}  # .count() works for STR too


# Another cool approach using dict comprehension and sets
def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in set(word)}


print(multiple_letter_count('turtle'))



# LIST_MANIPULATION() - Four params (a list, command, location and value).
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list, command, location, value=None):
    if command == "remove" and location == "end":
        return list.pop()
    elif command == "remove" and location == "beginning":
        return list.pop(0)
    elif command == "add" and location == "end":
        list.append(value)
        return list
    elif command == "add" and location == "beginning":
        list.insert(0, value)
        return list
    else:
        return "Oops, something went wrong"


sample_list = [1, 2, 4, 'gaylon', True]
sample_list2 = ['red', 'blue', 3, 11.1, True]
print(list_manipulation(sample_list, "add", "beginning", "ashley"))
print(list_manipulation([1, 2, 3, 4], "add", "end", "aaron"))
print(list_manipulation(sample_list2, "remove", "beginning"))  # 'red'



# IS_PALINDROME() - Reads the same way backward or forward, returns True or False. Ignore whitespace and capitalization

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True

'test ing'.upper().replace(" ", '')
'hannah'[:3] == 'hannah'[-1:-4:-1]  TRUE
'hannah' == 'hannah'[::-1]  TRUE
'''

def is_palindrome(x):
    x = str(x).lower().replace(" ", '')
    if x == x[::-1]:
        return True
    return False

print(is_palindrome('youare The best ever'))
print(is_palindrome(666))
print(is_palindrome("  .  "))
print(is_palindrome('hannah'))
print(is_palindrome("TAcOcat"))
print(is_palindrome("robERT"))


# FREQUENCY() - A list and a search term for parameters. The search term
# will always be a primitive value. Returns the number of times the search
# term appears in list.
'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(list, search_term):
    return list.count(search_term)



# MULTIPLY_EVEN_NUMBERS() - Accepts a list of numbers and returns the product of all even nums.
'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(list):
    total = 1
    even_only = [num for num in list if num % 2 == 0]
    for num in even_only:
        total *= num
    return total
#    even_dict = {num: num if list[num] % 2 == 0 for num in list}

# Instructor's:
def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total

print(multiply_even_numbers([2, 4, 6, 1, 3, 5, 5, 7, 2, 3]))


# CAPITALIZE() - One string. Capitalize the first letter
def capitalize(string):
    return string[0].upper() + string[1:]
#    return string.capitalize()

print(capitalize('pumpkin'))



# COMPACT() - One list. Returns a list of truthy values only
'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''
# Mine:
def compact(list):
    falsey = [None, False, 0, '', {}, []]
    truthy = [val for val in list if val not in falsey]
    return truthy


# Instructor's: WOW! if val is same as saying if True.
def compact(list):
    return [val for val in list if val]

# Another option:
# def compact(list):
#     truthy_vals = []
#     for val in list:
#         if val: truthy_vals.append(val)
#     return truthy_vals


print(compact([88, 'Archie', {}, 0, True, False, None, 1000, [1, 2, 3]]))


# INTERSECTION() - Two lists. Return only the vals that both have in common
# Use sets for a unique list of values?
def in_common(l1, l2):
    return {val for val in l1 if val in l2}  # why does True not work with sets????

# Instructor's:
def intersection(l1, l2):
    return [val for val in l1 if val in l2]

# Best:
def intersection2(l1, l2):
    return [val for val in set(l1) & set(l2)]

# Another go:
def intersection3(l1, l2):
    return list(set(l1) & set(l2))

print(in_common(['Gaylon', 4, 2, 2, 1, True, None, False, 0], [1, 'Gaylon', False, True, None, 0]))
print(intersection(['Gaylon', 4, 2, 2, 1, True, None, False, 0], [1, 'Gaylon', False, True, None, 0]))
print(intersection2(['Gaylon', 4, 2, 2, 1, True, None, False, 0], [1, 'Gaylon', False, True, None, 0]))
print(intersection3(['Gaylon', 4, 2, 2, 1, True, None, False, 0], [1, 'Gaylon', False, True, None, 0]))


# PARTITION() - A list and a callback function (returns True or False). Returns a list of lists
# where the first inner list is 'truthy' the other is 'falsey'
'''
def isEven(num):
    return num % 2 == 0

partition([1, 2, 3, 4], isEven)  # [[2, 4], [1, 3]]
'''
# This works but doesn't factor/invoke the callback function...
def partition(list, fn=True):
    result = []
    truthy = [val for val in list if val]
    falsey = [val for val in list if not val]  # Cannot directly assign result[0] = ...
#    [result[0].append(val) if val is fn else result[1].append(val) for val in list]
    result.append(truthy)
    result.append(falsey)
    return result


# Going to copy the isEven function to use as callback
def is_even(num):
    return num % 2 == 0

# Going to try to create an is_truthy() function to use
def is_truthy(item):
    return item not in [None, False, 0, '', {}, []]

# print(is_truthy(0))
# print(is_truthy(''))
# print(is_truthy([]))
# print(is_truthy(999))

print(is_truthy(['Gaylon', 0, '', True, 33, [1, 2, 3]]))


def partition2(list, fn=is_even):
    result = []
    truthy = [val for val in list if fn(val)]  # Need to use fn, not is_even
    falsy = [val for val in list if not fn(val)]
    result.append(truthy)
    result.append(falsy)
    return result


# Instructor's:
def partition3(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]


# One liner. Similar to mine:
def partition4(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


# Using .pop and .index:
def partition5(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)], l]


print(partition(['Gaylon', '', 44, True, False, None, [], {}, ['ash', 'gay', 'arch', 'aaron', 'adrian'], 0], fn=True))
print(partition2([1, 2, 1, 2, 3, 4, 5, 2, 4, 6, 7, 8, 9, 0], fn=is_even))


