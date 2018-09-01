'''
https://hackernoon.com/the-magic-behind-python-generator-functions-bc8eeea54220

Generators are iterators and can be created two ways:
1. Generator functions (use the yield keyword)
2. Generator Expressions

Functions vs. Generator Functions

Functions - Uses RETURN, returns ONCE. when invoked, returns the return VALUE
Generator Functions - Uses YIELD, can yield MULTIPLE times. When invoked, returns a GENERATOR

YIELD keyword - RETURNS A GENERATOR! This returns the value of count and PAUSES...UNTIL next()
is called on count_up_to. It basically waits in a holding pattern until next() is called again.
When next() is called again, it will add 1 to count and go through the function/loop again, etc.

This is unique since it never stores all of the data at once, BUT it has the ability to keep track
of its state unlike a regular function where you call it once and run it again, it never remembers
what happened last time. HOWEVER, with generators each time through when you call next(), it keeps
the most recent value and stops/pauses. Then the next time next() is called, it discards the old
value and keeps the new value. It only stores ONE THING AT A TIME. Until you get the StopIteration

***THIS basically does the exact same thing as our custom COUNTER class we built where we had to add
an __init__, __iter__ and __next__ to essentially get the same thing/functionality!
We don't have to do any of that stuff behind the scenes since these generator objects
already have that code in place.

If we really need all the values, we can just return the whole list(generator)

GENERATORS VS LISTS: In terms of time, they're both really fast and it's situational.
However, in terms of memory usage/consumption, GENERATORS win hands down.

'''
# First generator function that creates a generator once we execute it:
# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count  # This will return the value of count and pause UNTIL next() is called on count_up_to
#         count += 1
#
# #print(count_up_to(5))  # <generator object count_up_to at 0x1014d7620>
#
# counter = count_up_to(5)
# print(next(counter))
#
# help(counter)  # A Generator object already has next() as a class dunder method
#
# counter2 = count_up_to(10)
# for num in counter2:
#     print(num)  # 1 - 10
#     print(hex(id(counter2)))  # all in the same memory
# # next(counter2)  # The cool thing is that it will return ONE value until we need more
# # list(counter2)
#
# # WEEK GENERATOR EXERCISE
# def week():
#     weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
#     for day in weekdays:
#         yield day
#
# first_week = week()
#
# for day in first_week:
#     print(day)
#
# def week2():
#     yield 'Monday'
#     yield 'Tuesday'
#     yield 'Wednesday'
#     yield 'Thursday'
#     yield 'Friday'
#     yield 'Saturday'
#     yield 'Sunday'



# Memory test - How generators really excel in this area:
# Fibonacci numbers/sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...
def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

print(fib_list(10))  # 10th number in the sequence [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x+y
        yield x
        count += 1

# for n in fib_list(1000000):  !! THIS WILL CONSUME MEMORY!
#     print(n)

for n in fib_gen(10):
    print(n)

for n in fib_gen(10000):
    print(n)


# GET_MULTIPLES EXERCISE
# For loop version:
def get_multiples(number=1, count=10):
    for i in range(1, count+1):
        yield number*i

evens = get_multiples(2, 3)
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))

# While loop version:
def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num


# GET_UNLIMITED_MULTIPLES EXERCISE:
def get_unlimited_multiples(number=1):
    next_num = number
    while True:
        yield next_num
        next_num += number

fours = get_unlimited_multiples(4)
print(next(fours))
print(next(fours))
print(next(fours))
print(next(fours))