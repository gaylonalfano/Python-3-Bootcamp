# def get_multiples(number=1, count=10):
#     for i in range(1, count+1):
#         yield number*i
#
# evens = get_multiples(2, 3)
# print(next(evens))
# print(next(evens))
# print(next(evens))
# print(next(evens))



# GET_UNLIMITED_MULTIPLES EXERCISE:
def get_unlimited_multiples(number=1):
    next_num = number
    while True:
        yield next_num
        next_num += number

# Student's example with *
# def get_unlimited_multiples(num=1):
#     next_num = 1
#     while True:
#         yield num*next_num
#         next_num += 1

fours = get_unlimited_multiples(4)
print(next(fours))
print(next(fours))
print(next(fours))
print(next(fours))