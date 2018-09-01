'''
Want to create a music beat generator. Going to use the "4-4 time" 1, 2, 3, 4, 1, 2, 3, 4..

Want a function current_beat() that always returns the current beat (essentially cycles 1-4).
Just one beat at a time.

Saw we have a another function called:
def play_kick_drum() and it plays only if current beat == 1 then play sound


'''


# How can we have it return a single number but every time a different number?
# NOT IDEAL because it prints it all at the same time basically:
# def current_beat():
#     max = 100
#     nums = (1, 2, 3, 4)
#     i = 0
#     result = []
#     while len(result) < max:
#         if i >= len(nums): i = 0
#         result.append(nums[i])
#         i += 1
#     return result
#
#
# print(current_beat())


# BETTER/BEST:
def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1

# Student's:
def current_beat2():
    while True:
        for num in (1, 2, 3, 4):
            yield num


counter2 = current_beat2()
print(next(counter2))
print(next(counter2))
print(next(counter2))
print(next(counter2))
print(next(counter2))



#My attempt:
# def current_beat():
#     nums = (1, 2, 3, 4)
#     i = 0
#     while True:
#         yield nums[i]
#         if i + 1 == len(nums):
#             i = 0
#         else:
#             i += 1


#
# counter = current_beat()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))



#
# print(next(current_beat()))
# print(next(current_beat()))
# print(next(current_beat()))
# print(next(current_beat()))
# print(next(current_beat()))

#        # i=0 if i+1 == len(nums) else i+=1
#
#
#         for n in nums:
#             yield n
#
# tune = current_beat()
# print(next(tune))
# print(next(tune))
# print(next(tune))
