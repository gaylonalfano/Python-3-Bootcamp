'''
You can import from you own code too. The syntax is the same as before.
import from the name of the Python file.

Ex.

file1.py contains:
def fn():
    return "do some stuff"

def other_fn():
    return "do some other stuff"


file2.py contains:
import file1

file1.fn()  # 'do some stuff'

file1.other_fn()  # 'do some other stuff'
'''