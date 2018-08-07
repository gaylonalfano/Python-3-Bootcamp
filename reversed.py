# [1, 2, 3, 4].reverse() is a LIST method. Does it in-place, just like sort()
# However, reversed() - takes in iterable and returns a reversed iterator object
# Can use it with strings, tuples, dicts, etc.

reversed('hello')

for char in reversed('hello world'):
    print(char)

# dlrow olleh

print("hello"[::-1])  # 'olleh'

''.join(list(reversed("hello")))  # 'olleh'

for x in reversed(range(0, 10)):
    print(x)

