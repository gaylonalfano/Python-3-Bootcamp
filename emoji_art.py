# print("\U0001f600") will give you the emoji graphic
# Need to use both a for loop and a while loop
# Can try nested loops. Also remember can multiply a string if needed.

# for x in range(3):
#     for i in range(1, 11):  # Don't forget to start at 1
#         print("\U0001f600" * i)

# count = 1
#
# while count < 11:
#     print("\U0001f600" * count)
#     count += 1


# # Instructor's code (wonky alternative w/o str multiplication):
# for num in range(1, 11):
#     count = 1
#     smileys = ""
#     while count <= num:
#         smileys += "\U0001f600"
#         count += 1
#     print(smileys)


# Pyramid option (*need to use odd numbers 1, 3, 5):

# count = 1
# smiley = "\U0001f600"
# space = " "
# spaces = 20
#
# while count < spaces:
#     print(f'{count * smiley}')
#     count += 2


spaces = 20
smiley = "\U0001f600"
space = " "
count = 1
for x in range(spaces, 0, -2):
    print(f'{x * space}{smiley * count}')
    count += 2
    # for i in range(1, spaces):  # Don't forget to start at 1
    #     print("\U0001f600" * i)


# Student example:
# x = 10
# y=1
# while y <= 10:
#     print(y * "\U0001f600")
#     y +=1
# print(10 * "\U0001f600" + "????")
# while x >=0:
#     print(x * "\U0001f600")
#     x -=1


'testing'.