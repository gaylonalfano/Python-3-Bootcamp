# Instructor's code (simplest solution)
# Generate the random_number
# random_number = randint(1, 10)
#
# # Collect a user's input for their guess
# usr_guess = None
#
# # Check if they guessed correct
# # Want to keep going until guess = random_number
# # While loop is preferred option when we don't know how many times
# while usr_guess != random_number:
#     # Ask for a new guess
#     usr_guess = input('Pick a number from 1 to 10: ')
#     usr_guess = int(usr_guess)
#     if usr_guess < random_number:
#         print('Too low!')
#     elif usr_guess > random_number:
#         print('Too high!')
#     else:
#         print('You won!')

# Upgraded version

import random

random_number = random.randint(1, 10)
# guess = None
guesses_taken = 0

while True:  # By using while True, don't have to initialize guess before/above while loop
    guess = input('Pick a number from 1 to 10: ')
    guess = int(guess)
    guesses_taken += 1
    if guess < random_number:
        print('Too low')
    elif guess > random_number:
        print('Too high')
    else:
        print(f'You won! You took {guesses_taken} turns.')
        play_again = input('Wanna play again? (y/n) ')
        if play_again == 'y':  # Need to generate a new number
            random_number = random.randint(1, 10)
            guess = None  # Reset the user's guess
        else:
            print('Thanks for playing!')
            break
