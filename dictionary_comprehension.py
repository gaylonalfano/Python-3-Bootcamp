# syntax
# {___ : ___ for ___ in ___}
# iterates over keys by default but can iterate over
# keys AND values using .items()

numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

# Create a DICT by starting out with a LIST
print({num: num**2 for num in [1, 2, 3, 4, 5]})

# Another way to create a DICT
str1 = 'ABC'
str2 = '123'
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)  # {'A': '1', 'B': '2', ...}

instructor = dict(name='Colt', city='san francisco', color='purple')
yelling_instructor = {k.upper(): v.upper() for k, v in instructor.items()}
print(yelling_instructor)

# Say you want to only upper case COLOR but leave name, city lower
# mine: yelling_instructor2 = {(k.upper() if k == 'color' else k.lower()): v.upper() for k, v in instructor.items()}
# instructor's:
yelling_instructor2 = {(k.upper() if k is 'color' else k): v.upper() for k, v in instructor.items()}
print(yelling_instructor2)

# Conditional logic with dictionaries
num_list = [1, 2, 3, 4]
print({num: ('even' if num % 2 == 0 else 'odd') for num in num_list})
print({num: ('even' if num % 2 == 0 else 'odd') for num in range(1, 100)})

# State Abbreviations Exercise
# Create a dict that looks like: {'CA': 'California', 'NJ': 'New Jersey', ...}
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(len(list1))}
print(answer)

# Another solution using .ZIP()
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
dict(zip(list1, list2))


# LIST TO DICTIONARY EXERCISE
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# use the person variable in your answer
# Split person into two separate lists? Don't it's best approach
# Or, some sort of nested for loops to retrieve [i][i]?
# If I use dict comprehension, the key = i[0], value = i[1]
answer2 = {person[i][0]: person[i][1] for i in range(len(person))}
print(answer2)
# Other syntax options:
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {thing[0]: thing[1] for thing in person}
#
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {k:v for k,v in person}
#
# Finally, a really simple solution.  If you have a list of pairs,
# you can very easily turn it into a dictionary using dict()
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = dict(person)



# VOWELS DICTIONARY EXERCISE
# Try to create: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
dict.fromkeys('aeiou', 0)
# Or, ...
print({k: 0 for k in 'aeiou'})

# ASCII CODES DICTIONARY
# Use chr() function
print({i: chr(i) for i in range(65, 91)})
