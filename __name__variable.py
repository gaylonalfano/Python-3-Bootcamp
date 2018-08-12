'''
A "dunder" variable. Special properties represented by __name__ variable.

When run, every Python file/module has its own __name__ variable. If the file is
the main file being run, its value is "__main__". Otherwise, its value is the file name.

***check out say_hi.py and say_sup.py for example***

Basically, the __name__ variable is set to __main__ in the main/executed file.
But, if you



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