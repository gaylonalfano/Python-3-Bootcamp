# Return heads or tails depending on a random coin toss
from random import random

def flip_coin():
    # generate random number 0-1
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())

# Another syntax:
def flip_coin():
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())