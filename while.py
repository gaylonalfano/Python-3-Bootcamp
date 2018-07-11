# message = input('what\'s the secret password: ')
#
# while message != 'bananas':
#     print('WRONG!')
#     message = input('what\'s the secret password: ')
# print("You are right! It is 'bananas'")

# for num in range(1, 11):
#     print(num)
#
# num = 1
#
# while num < 11:
#     print(num)
#     num += 1

from random import randint

number = 0
i = 0

while number != 5:
    number = randint(1, 10)
    i += 1
    print(number, i)