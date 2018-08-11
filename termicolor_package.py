'''
pip syntax is:
python3 -m pip install NAME_OF_PACKAGE
'''

from termcolor import colored

# print(dir(termcolor))
# help(termcolor)

text = colored("Hi there!", color="red", on_color="on_magenta", attrs=["blink"])
print(text)
