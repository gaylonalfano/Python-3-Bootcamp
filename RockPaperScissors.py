# Now adding a computer player (random pics)
from random import randint

player = input('Player: Enter rock, paper, or scissors: ').lower()
computer = randint(0, 2)
if computer == 0:
    computer = 'rock'
elif computer == 1:
    computer = 'paper'
else:
    computer = 'scissors'

print("...rock...\n...paper...\n...scissors...")
print('SHOOT!')

if player == computer:
    print(f'It\'s a tie! Player chose {player}. Computer chose {computer}. Play again!')
elif player == 'rock' and computer == 'scissors':
    print(f"Player chose {player}. Computer chose {computer}. Player wins!")
elif player == 'paper' and computer == 'rock':
    print(f"Player chose {player}. Computer chose {computer}. Player wins!")
elif player == 'scissors' and computer == 'paper':
    print(f"Player chose {player}. Computer chose {computer}. Player wins!")
else:
    print(f"Player chose {player}. Computer chose {computer}. Computer wins!")
