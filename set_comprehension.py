print({x ** 2 for x in range(10)})  # set
print({x: x ** 2 for x in range(10)})  # now it's a DICT! Notice the ':'

{char.upper() for char in 'hello'}  # {'H', 'E', 'L', 'O'}

string = 'hello'


# Function that takes a given string that returns True or False if it has all the vowels
def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5

