'''
Define what a module is
Import code from external modules using pip
Describe common module patterns
Use the REQUEST module to make http requests, etc.


WHY USE MODULES?
Help keep Python files small.
Ex. Imagine recreating RANDOM from scratch? Ouch.
Reuse code across multiple files by importing
A module is just a Python file!
If you have a really long file, you can group/organize things like,
putting all the apple related stuff in apples.py and bread things in
bread.py and then just import them as modules for your bake.py file.

(**see helpers.py and exercise.py**)

Built-in Modules: https://docs.python.org/3/py-modindex.html

import random

random.choice(['apple', 'banana', 'cherry', 'durian'])
random.shuffle(['apple', 'banana', 'cherry', 'durian'])

import random as ALIAS
from MODULE import * pattern

from random import choice as gimme_one, shuffle as mix_up_values
'''

# import random as rand
#
# rand.choice(['apple', 'banana', 'cherry', 'durian'])
# rand.shuffle(['apple', 'banana', 'cherry', 'durian'])


from random import choice, randint

print(choice(['apple', 'banana', 'cherry', 'durian']))
print(randint(1, 100))


# MATH()
import math
answer = math.sqrt(15129)


