# Loop through numbers 1-20
# for 4 and 13, print 'x is unlucky'
# for even numbers, print 'x is even'
# for odd numbers, print 'x is odd'

# My code
# for n in range(1, 21):
#     if n == 4 or n == 13:
#         print(f'{n} is unlucky')
#     elif n % 2 == 0:
#         print(f'{n} is even')
#     else:
#         print(f'{n} is odd')

# Instructor's code
# First pass was just like mine
# Then he added another option

for num in range(1, 21):
    if num == 4 or num == 13:
        state = 'unlucky'
    elif num % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{num} is {state}')
