'''
all - Return True if all elements of the iterable are truthy (or if the iterable is empty)
'''

all([0, 1, 2, 3,])  # False

all([char for char in 'eio' if char in 'aeiou'])  # True

all([num for num in [4, 2, -1, 10, 6, 8] if num % 2 == 0])  # False

# Do all first letters start with 'c'?
people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina']
print(all(name for name in people if name[0].lower() == 'c'))  # True

# Alternative syntax... pretty neat!
# Just the simple list comprehension returns a list of True or False values
# [name[0] == 'C' for name in people]  # [True, True, True, True, True]
print(all(name[0] == 'C' for name in people))

nums = [2, 60, 26, 18]
all(num % 2 == 0 for num in nums)  # True


'''
any - Returns True if ANY element of the iterable is truthy. If the iterable
is empty, returns False.
'''
any([0, 1, 2, 3, 4])  # True

any([val for val in [1, 2, 3] if val > 2])  # True

any([val for val in [1, 2, 3] if val > 5])  # False

any([num % 2 == 1 for num in nums])  # False

# Could also write it like this:
# for person in people:
#     if person[0] != 'C':
#         return False....

'''
GENERATOR EXPRESSIONS - "Basically, use a generator expresssion if all you're doing is iterating ONCE.
If you want to store and use the generated results, then you're probably better off with a list comprehension."
See stackoverflow "Generator Expressions vs. List Comprehension"
'''
print((x*2 for x in range(256)))  # Returns <generator object>
print([x*2 for x in range(256)])  # List Comp

# Example to show memory size between genexpr and listcomp
import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_expr = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List comprehension: {list_comp} bytes")  # 9024 bytes
print(f"Generator expression: {gen_expr} bytes")  # 88 bytes!!!!


# IS_ALL_STRINGS() - accepts single iterable and returns True if it contains ONLY strings
# isinstance(1, str) = False
# isinstance('stuff', str)  # True
# isinstance(1, int)  # True
def is_all_strings(l):
    return all(isinstance(i, str) == True for i in l)

# Instructor's gen expr using type(i) == str
def is_all_strings2(lst):
    return all(type(l) == str for l in lst)

# # Instructor's list comp:
# def is_all_strings(lst):
#     return all([type(l) == str for l in lst])


print(is_all_strings(['a', 'b', 'c', 4]))  # False
print(is_all_strings(['', 'gaylon', 'lkjlkj', '33333']))  # True
print(is_all_strings2(['a', 'b', 'c', 4]))  # False
print(is_all_strings2(['', 'gaylon', 'lkjlkj', '33333']))  # True