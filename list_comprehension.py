# the syntax
# [ (calc you want to do) for (interation) in (list) (conditional logic]
# [ num * 2 for num in numbers if num % 2 == 0 ]

# Examples
# nums = [1, 2, 3]
#
# print([x * 10 for x in nums])

# List comprehension
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_number = num * 2
    doubled_numbers.append(doubled_number)

print(doubled_numbers)

# String example
name = 'gaylon'

print([char.upper() for char in name])

# Another
friends = ['ashley', 'adrian', 'aaron', 'archie']

print([friend[0].upper()+friend[1:] for friend in friends])

# Used in ranges
print([num * 10 for num in range(1, 6)])

print([bool(val) for val in [0, [], '']])  # False, False, False
print([bool(val) for val in [3, [1], 'Gaylon']])


# Another
string_list = [str(num) for num in numbers]
print(string_list)  # ['1', '2', '3', '4', '5']


# List comprehension with conditional IF logic
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(evens, odds)

# List comprehension with conditional IF/ELSE logic
print([num * 2 if num % 2 == 0 else num / 2 for num in numbers])

with_vowels = 'This is so much fun!'
print(''.join(char for char in with_vowels if char not in 'aeiou'))

