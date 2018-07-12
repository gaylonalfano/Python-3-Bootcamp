# Guessing game logic. My version
from random import randint

guess = int(input("Guess a number between 1 and 10: "))
number = randint(1, 10)
play_game = input("Want to play again? (y/n) ")

while play_game == 'y':
    for guesses_taken in range(5):
        print('Guess a number between 1 and 10: ')
        guess = int(input())
        if guess < number:
            print('Too low, try again!')
    #         play_game
    #         if play_game == 'n':
    #             break
        elif guess > number:
            print('Too high, try again')
    #         play_game
    #         if play_game == 'n':
    #             break
        else:
            print('You guessed correctly! You won!')
            break
    play_game = input('Want to play again? (y/n) ')
print(f'You guessed {guess}. The number is {number}. You took {guesses_taken} guesses.')


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
# while usr_guess != random_number:  # NOTE: By doing it this way you only play once. Better is while True
#     # Ask for a new guess
#     usr_guess = input('Pick a number from 1 to 10: ')
#     usr_guess = int(usr_guess)
#     if usr_guess < random_number:
#         print('Too low!')
#     elif usr_guess > random_number:
#         print('Too high!')
#     else:
#         print('You won!')
