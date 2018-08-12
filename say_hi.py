'''
Here's what happens you import something:
1. Tries to find the module (if it doesn't find it, it throws an error).
2. But if found, it runs the code inside of the module being imported

So, in the example with say_hi and say_sup, when you import say_sup into the say_hi file,
it will run the code in the say_sup module FIRST, which has a say_sup() function call.

If you want to prevent this code from running, then here's the trick to ignore code
on import:

if __name__ == "__main__":
    # this code will only run
    # if the file is the main file!

Ex. Modify the say_sup.py file and add this code to call the function:
if __name__ == "__main__":
    say_sup()
'''

from say_sup import say_sup

def say_hi():
    print(f"Hi! My __name__ is {__name__}")

say_hi()
say_sup()  # Get 3 outputs IF you don't add if __name__ == "__main__" in say_sup.py
# Sup! My __name__ is say_sup
# Hi! My __name__ is __main__
# Sup! My __name__ is say_sup