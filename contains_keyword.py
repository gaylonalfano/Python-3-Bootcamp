# CONTAINS_KEYWORD() - Accepts any number of string arguments. Returns True if any keywords found,
# Otherwise it returns False. Import module keyword and method iskeyword.
import keyword

# def contains_keyword(*strings):
#     if True in (keyword.iskeyword(x) for x in strings):
#         return True
#     return False


# Student BEST solution:
# any() will stop once on FIRST truthy value
def contains_keyword(*strings):
    return any(keyword.iskeyword(x) for x in strings)


# Colt's:
# def contains_keyword(*args):
#     for item in args:
#         if keyword.iskeyword(item): return True
#     return False

#
# import random
#
#
# def sample_generator(number):
#     n = 0
#     while n < number:
#         print("Inside generator: " + str(n))
#         yield random.choice([True, False])
#         n += 1
#
#
# print(any(sample_generator(100)))



print(contains_keyword('hello', 'goodbye'))
print(contains_keyword('def', 'haha', 'lol', 'chicken', 'alaska'))
print(contains_keyword('four', 'for', 'if'))