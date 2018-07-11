# Ask "How are you?" and record input
# Then just copy/print the input again

# start_game = True
# while start_game:
#     if response == magic_phrase:
#         start_game = False
#     else:
#         print(response)
#         starter = input()


response = input('How\'s it going? ')
magic_phrase = 'stop copying me'

while response != magic_phrase:
    print(response)
    response = input()
print('Ok, you win!')

# Alternative:
# while response != magic_phrase:
#     response = input(f'{response}\n')
# print('Alright already!')