'''
raise - In Python we can also throw errors using the raise keyword. This is helpful
when creating your own kinds of exception and error messages.

raise ValueError('invalid value')
'''

# raise RandomNoNameError('yada yada')  - Needs to be a common error

# Example: Creating a module that allows people to colorize text
# Best practice is to have individual type errors (one for text, one for color)
def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    if type(color) is not str:
        raise TypeError("color must be instance of str")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    elif color not in colors:
        raise ValueError("color is invalid color")
    print(f'Printed {text} in {color}')

colorize('hello', 'red')
#colorize(23423, 'blue')  # TypeError: Text must be instance of str