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
#         result[k] = tuple(v).count(k)
#     return result


# Instructor's using dict comprehension
def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in word}  # .count() works for STR too

print(multiple_letter_count('absolutely'))




