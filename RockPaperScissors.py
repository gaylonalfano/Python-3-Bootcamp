# # Now adding a computer player (random pics)
# from random import randint
#
# player = input('Player: Enter rock, paper, or scissors: ').lower()
# computer = randint(0, 2)
# if computer == 0:
#     computer = 'rock'
# elif computer == 1:
#     computer = 'paper'
# else:
#     computer = 'scissors'
#
# print("...rock...\n...paper...\n...scissors...")
# print('SHOOT!')
#
# if player == computer:
#     print(f'It\'s a tie! Player chose {player}. Computer chose {computer}. Play again!')
# elif player == 'rock' and computer == 'scissors':
#     print(f"Player chose {player}. Computer chose {computer}. Player wins!")
# elif player == 'paper' and computer == 'rock':
#     print(f"Player chose {player}. Computer chose {computer}. Player wins!")
# elif player == 'scissors' and computer == 'paper':
#     print(f"Player chose {player}. Computer chose {computer}. Player wins!")
# else:
#     print(f"Player chose {player}. Computer chose {computer}. Computer wins!")

# Updating game to include a loop that exits once someone has won 2 of 3, or 3 or 5, etc.
from random import randint

# Wrapping whole program into a big while loop
start_game = True

while start_game:

    player_wins = 0
    computer_wins = 0
    winning_score = 2  # Can change this to do your 2/3 or 3/5, etc.

    while player_wins < winning_score and computer_wins < winning_score:
        # for i in range(3):  **Don't need this FOR loop if you use WHILE
        print(f'Player: {player_wins}   Computer: {computer_wins}')
        player = input("Enter 'rock', 'paper', or 'scissors': ").lower()  # Helps with data entry validation
        if player == 'quit' or player == 'q':  # Adding a break so user can quit out
            break
        computer = randint(0, 2)
        if computer == 0:
            computer = 'rock'
        elif computer == 1:
            computer = 'paper'
        else:
            computer = 'scissors'

        print("...rock...\n...paper...\n...scissors...\nSHOOT!")

        if player == computer:
            print(f'It\'s a tie! Player chose {player}. Computer chose {computer}. Play again!')
        elif player == 'rock' and computer == 'scissors':
            print(f"Player chose {player}. Computer chose {computer}. Player wins!")
            player_wins += 1
        elif player == 'paper' and computer == 'rock':
            print(f"Player chose {player}. Computer chose {computer}. Player wins!")
            player_wins += 1
        elif player == 'scissors' and computer == 'paper':
            print(f"Player chose {player}. Computer chose {computer}. Player wins!")
            player_wins += 1
        else:
            print(f"Player chose {player}. Computer chose {computer}. Computer wins!")
            computer_wins += 1

    if player_wins > computer_wins:
        print(f'Congrats, you won! Final score: Player {player_wins} vs. Computer {computer_wins}')
        play_again = input('Want to play again? (y/n) ')
        if play_again == 'n':
            print('Thanks for playing!')
            start_game = False
    elif player_wins == computer_wins:  # only happens if we quit when it's a tie
        print('It\'s a tie! Well done to both contestants.')
        play_again = input('Want to play again? (y/n) ')
        if play_again == 'n':
            print('Thanks for playing!')
            start_game = False
    else:
        print(f'Oh no, you lost! Final score: Player {player_wins} vs. Computer {computer_wins}')
        play_again = input('Want to play again? (y/n) ')
        if play_again == 'n':
            print('Thanks for playing!')
            start_game = False
