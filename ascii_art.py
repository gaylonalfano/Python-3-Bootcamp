from pyfiglet import figlet_format
from termcolor import colored
#help(pyfiglet.figlet_format)


#My attempt BROKE - SEE COLT'S BELOW AS A FUNCTION:
def ascii_art(msg=input("What message do you want to print? "), color=input("What color? ")):
    accepted_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

    if color not in accepted_colors:
        color = 'magenta'

    print(colored(figlet_format(msg), color=color))


ascii_art()
#
#
# msg = pyfiglet.figlet_format(input("What message do you want to print? "))
# print(colored(msg, color=input("What color? ")))


# Colt's NO FUNCTION:
# from pyfiglet import figlet_format
# from termcolor import colored
# accepted_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
#
# msg = input("What message do you want to print? ")
# color = input("What color? ")
#
# if color not in accepted_colors:
#     color = "magenta"
#
# ascii_art = figlet_format(msg)
# colored_ascii = colored(ascii_art, color=color)
# print(colored_ascii)


# Colt's AS A FUNCTION:
# from pyfiglet import figlet_format
# from termcolor import colored
#
def print_art(msg, color):
    accepted_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

    if color not in accepted_colors:
        color = "magenta"

    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)

msg = input("What message do you want to print? ")
color = input("What color? ")
print_art(msg, color)


# Student examples:
# from pyfiglet import figlet_format as ff
# from termcolor import cprint as cp, COLORS
#
# text = input("What would you like to print? ")
# color = input("What color? ")
# cp(ff(text), color) if color in COLORS.keys() else cp(ff(text), 'magenta')