"""
FILE I/O Intro

READ TEXT FILES IN PYTHON
Use the open builtin function. open returns a file object to you. 
A file has a lot of metadata. 

Example: 
story.txt - This short story is really short.
file = open("story.txt")
file.read()

**After you read it ONCE, it will seem as if the content has disappeared.
This is actually due to CURSOR MOVEMENT. When Python reads a file it
uses what is known as a cursor. It's like what you see when you're typing.
After a file is read, the cursor goes to the end of the file so if you try 
to read() again, it'll look like an empty string.

To move the cursor we use the SEEK method. 
file.seek(0)  # 0, takes you to the very beginning. It's like a string index
file.readline()
file.readlines()  # returns a LIST of lines
file.close()  # closes a file. Need to open() again
file.closed  # Checks whether a file is closed

If you try to read() a closed file you'll get a ValueError: I/O operation on closed file



WRITE TEXT FILES IN PYTHON
You have to use the open first. You either open and read (-r) or open and write (-w)
Example: 
with open("haiku.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!")



USE "WITH" BLOCKS WHEN READING / WRITING FILES
This is actually a more preferred method of reading/writing files with this syntax:
OPTION 1:
file = open("story.txt")
file.read()
file.close()

file.closed  # True

OPTION 2: It automatically CLOSES the file no matter if it runs or errors, etc.
with open("story.txt") as file:
    file.read()

file.closed   # True

**Behind the scenes, there is a __enter__() dunder method and any time we call a 
WITH statement, __enter__() is going to be called and it just returns the file object.
There's also a __exit__() dunder method



DESCRIBE THE DIFFERENT WAYS TO OPEN A FILE
"r" - open for reading (default). Can still use seek() afterwards
"w" - Will overwrite an existing file or create a new one. CAN CREATE A FILE.
"x" - open for exclusive creation, failing if the file already exists
"a" - open for writing, appending to the end of the file if it exists. Best to place \n 
    at the end of each line. HOwever, even seek(0) will only place at top of append,
    so append has its shortcomings. CAN CREATE A FILE.
"t" - text mode (default)
"b" - binary mode
"r+" - read and write to a file (writing based on cursor). Preferred choice if working with
    existing files, etc. DEFAULT is to automatically seek(0), so you'll start at beginning.
    AND it will overwrite whatever was there. USES EXISTING FILE.








READ CSV FILES IN PYTHON


WRITE CSV FILES IN PYTHON


JSON - JAVASCRIPT OBJECT NOTATION
"""
# file = open("story.txt")
# print(file.read())

# file.seek(0)
# file.readline()
# file.readlines  # gives you a LIST of lines


# with open("haiku.txt", "w") as file:
#     file.write("Writing files is great\n")
#     file.write("Here's another line of text\n")
#     file.write("Closing now, goodbye!")

# with open("haiku.txt", "a") as file:
#     file.write("Here's one more haiku\n")
#     file.write("What about the older one?\n")
#     file.write("Let's go check it out\n")  # adding \n at the end puts cursor on next line

# with open("haiku.txt", "a") as file:
#     file.write("\nI AM STARTING HERE FIRST\n")

# r+
# with open("haiku.txt", "r+") as file:
#     file.write("ADDED USING r+")

# with open("haiku.txt", "r+") as file:
#     file.seek(2)
#     file.write("Using r+ again but first called seek(2)\n")

# with open("haiku.txt", "r+") as file:
#     file.seek(-1)  # ValueError: negative seek position -1
#     file.write("Using r+ again but first called seek(-1)\n")

# with open("lol.txt", "w") as file:
#     file.write("haha" * 10000)

# COPY EXERCISE - Takes in a file name and a new file name and copies contents
# Alice_Original.txt and Alice_Copy.txt
# def copy(original, new):
#     with open(original) as file:
#         original_text = file.read()
#     with open(new, "w") as file:
#         file.write(original_text)

# Student's solution:
# def copy(file_name, new_file):
#     with open(file_name) as file:
#         with open(new_file, 'w') as n_file:
#             n_file.write(file.read())

# copy("Alice_Original.txt", "Alice_Copy.txt")


# COPY AND REVERSE
# def copy_and_reverse(original, new):
#     with open(original) as file:
#         # original_text = file.readlines()
#         # reversed_text = original_text[::-1]
#         # for line in :
#         # CAN I JUST USE .READ() AND THEN CONVERT TO LIST AND THEN [::-1]???
#         original_text = file.read()
#         reversed_text = original_text[::-1]
#     with open(new, "w") as file:
#         file.write(reversed_text)

# Question - Should I use a unique name for 'as file'? ('as file', 'as new_file', etc.)

#copy_and_reverse("Alice_Original.txt", "Alice_Reversed.txt")

# My 1st submission:
# def statistics(text):
#     with open(text, "r+") as file:
#         lines = file.readlines()
#         file.seek(0)
#         characters = file.read()
#         words = characters.replace('\n', ' ')  # Replace \n with ' '
#         words = words.split(' ')  # 1974. Need 2145. Problem is \n        
        
#     return {'lines': len(lines) ,'words': len(words), 'characters': len(characters)}

# My 2nd submission:
def statistics(file_name):
    with open(file_name) as file:
        text = file.read()
        lines = 

# Colt's solution w/ generator expressions
def statistics2(file_name):
    with open(file_name) as file:
        text = file.readlines()
    
    return {'lines': len(text), 
            'words': sum(len(line.split(" ")) for line in text), # This is pretty neat
            'characters': sum(len(line) for line in text)
    }


print(statistics("Alice_Original.txt"))
print(statistics2("Alice_Original.txt"))


# Student solution:
# def statistics(file):
#     with open(file) as myfile:
#         stats = myfile.read()
#         return {
#         'lines': len(stats.split('\n')),
#         'words':  len(stats.split()), 
#         'characters': len(stats)
#         }


# Another solution:
# def statistics(filename):
#     results = dict.fromkeys(["lines", "words", "characters"], 0)
#     with open(filename) as file:
#         for line in iter(lambda: file.readline(), ''):
#             results['lines'] += 1
#             results['words'] += len(line.split())
#             results['characters'] += len(line)
#     return results




