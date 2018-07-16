nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for l in nested_list:
#     for val in l:
#         print(val)

# Same as above but with list comprehension
[[print(val) for val in l] for l in nested_list]

# Another example
board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)

print([['X' if num % 2 != 0 else 'O' for num in range(1, 4)] for val in range(1, 4)])

# Let's create a blank tic-tac-toe board
ttt_board = [['*' for i in range(3)] for n in range(3)]
print(ttt_board)

# answer = [[i for i in range(0,10)] for num in range(0,10)]
