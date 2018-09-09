# linked with tests.py
from random import choice

def eat(food, is_healthy):  # if is_healthy not an instance of bool then raise error
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a bool")
    ending = "because YOLO!"
    if is_healthy:
        ending = "because it's healthy"
    return f"I'm eating {food}, {ending}"

def nap(num_hours):
    if num_hours >= 2:
        return f"Ugh. Didn't mean to nap for {num_hours} hours"
    return f"I'm feeling refreshed after my {num_hours} hour nap"

def is_funny(person):
    if person == 'tim':  # or person IS tim
        return False
    return True  # comment out this and the test will fail

def laugh():  # returns a laughing noise lol, haha, tehehe
    return choice(('lol', 'haha', 'tehehe'))
