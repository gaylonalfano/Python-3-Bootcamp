# abs('20')  # Error
#
# abs(float('20'))  # 20.0
#
# import math
#
# math.fabs()
#
# '''
# sum() - takes an iterable and an optional start. Returns the sum of start and the items of
# an iterable from LEFT to RIGHT and returns the TOTAL. Start defaults to 0.
# '''
#
# sum([1, 2, 3])
#
# sum([1, 2, 3], start=10)
# sum([1, 2, 3], start=-6)
#
#
# sum(['hi', 'there'], start='lol')  # Error. use ''.join(seq) instead
# print(''.join(['hi', 'there']))
#
#
# # Round - ndigits is omitted or is NONE. It returns the nearest INT.
#
# round(3.51323, 3)


# MAX_MAGNITUDE() - Accepts a single list of numbers. Returns the magnitude
# of the number with the largest magnitude (num that is furthest away from zero).

# def max_magnitude(nums):
#     return abs(max(nums, key=lambda num: abs(num)))

# Instructor's code/ Better:
def max_magnitude(nums):
    return max(abs(num) for num in nums)


print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]))
print(max_magnitude([-5, -1, -89]))



# SUM_EVEN_VALUES() - Accepts a variable number of arguments and return the sum of all
# arguments that are divisible by 2. If none, return 0. It accepts all the numbers as
# individual arguments!
# sum_even_values(1, 2, 3, 4, 5, 6)  # 12

def sum_even_values(*args):
    evens = []
    for num in args:
        if num % 2 == 0:
            evens.append(num)
    return sum(evens)


def sum_even_values2(*args):
    return sum(filter(lambda num: num % 2 == 0, args))


def sum_even_values3(*args):
    return sum([num if num % 2 == 0 else 0 for num in args])


print(sum_even_values(1, 2, 3, 4, 5, 6))
print(sum_even_values2(1, 2, 3, 4, 5, 6))
print(sum_even_values2(4, 2, 1, 10))
print(sum_even_values3(4, 2, 1, 10))
print(sum_even_values(1))
print(sum_even_values2(1))
print(sum_even_values3(1))



# SUM_FLOATS - Accepts a variable number of arguments (*args). Returns sum of all floats, else 0
# sum_floats(1.5, 2.4, 'awesome', [], 1)  # 3.9

def sum_floats(*args):
    return sum(filter(lambda num: type(num) == float, args))


def sum_floats2(*args):
    return sum(num for num in args if type(num) == float)

# Instructor's:
# def sum_float(*args):
#     return sum(arg for arg in args if type(arg) == float)


print(sum_floats(1.5, 2.4, 'awesome', [], 1))  # 3.9
print(sum_floats2(1.5, 2.4, 'awesome', [], 1))  # 3.9
print(sum_floats(1, 2, 3, 4, 5))  # 0
print(sum_floats2(1, 2, 3, 4, 5))  # 0