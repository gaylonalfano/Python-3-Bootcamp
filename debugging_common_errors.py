# Checkout documentation on Built-in Errors

'''
SyntaxError - Occurs when Python encounters incorrect syntax (something it doesn't parse).
Usually due to typos or not knowing Python well enough

def first:  # SyntaxError

None = 1  # SyntaxError

return  # SyntaxError
'''


'''
NameError - Occurs when a variable is not defined, i.e. it hasn't been assigned.

'''


'''
TypeError - Occurs when an operation or function is applied to the wrong type. 
Python cannot interpret an operation on two data types. Also occurs when
missing arguments. 

len(5)  # TypeError: object of type 'int' has no len()

"awesome" + []  # TypeError: cannot concatenate 'str' and 'list' objects
4 + "4"  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

3 + 's'
len(2.4)

def add(a, b):
    return a+b
add(1)  # TypeError: add() missing 1 required positional argument: 'b'
'''


'''
IndexError - Occurs when you try to access an element in a list using an invalid index.
i.e., one that is outside the range of the list or string.

list = ['hello']
list[2]  # IndexError: string index out of range
'''


'''
ValueError - Occurs when a built-in operation or function receives an argument that has
the right type but an inappropriate value.

int('foo')  # ValueError: invalid literal for int() with base 10: 'foo'

**Note that the above isn't a TypeError because int() does accept str. Hhowever, it's a 
ValueError because the str 'foo' cannot be converted to a number.
'''


'''
KeyError - Occurs when a dictionary does not have a specific key. Similar to an
IndexError for a list.

d = {}
d['foo']  # KeyError: 'foo'
'''


'''
AttributeError - This occurs when a variable does not have an attribute.

"awesome".foo  # AttributeError: 'str' object has no attribute 'foo'
[1, 2, 3].hello()  # AttributeError: 'list' object has no attribute 'hello'

'''