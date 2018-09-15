'''
File I/O - Writing to CSV files

WRITE USING LISTS:
writer - creates a writer object for writing to CSV. Use the writerow method.

from csv import writer
with open("fighters.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])



WRITE USING DictWriter:
DictWriter - creates a writer object for writing using dictionaries
fieldnames - kwarg for the DictWriter specifying headers
writeheader - method on a writer to write header row
writerow - method on a writer to write a row based on a dictionary

from csv import DictWriter
with open("example.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move: "Hadouken"
    })




'''

# from csv import writer
# with open("cats.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Blue", 3])
#     csv_writer.writerow(["Kitty", 1])

from csv import writer, DictWriter
with open("cats.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Garfield",
        "Breed": "Orange Tabby",
        "Age": 10
    })

# Another example want to convert fighters cm to feet
# Want to read from fighters and then create a new file with inches
# Need to pass the cm value to the cm_to_in function and write that 
# into the new file
from csv import DictReader, DictWriter

def cm_to_in(cm):  # Better would be to validate the argument
    return round(float(cm) * 0.393701, 2)

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    with open("fighters_inches.csv", "w") as file:
        csv_writer = DictWriter(file, fieldnames=["Name", "Country", "Height (in inches)"])
        csv_writer.writeheader()
        for fighter in csv_reader:
            csv_writer.writerow({
                "Name": fighter["Name"],
                "Country": fighter["Country"],
                "Height (in inches)": cm_to_in(fighter["Height (in cm)"])
            })



# ADD_USER EXERCISE - Function add_user(fn, ln) and adds that user to 
# a users.csv file with headers "First Name" and "Last Name"
# My solution:
from csv import DictReader, DictWriter

def add_user(first_name, last_name):
    with open("users.csv", "a") as file:
        csv_writer = DictWriter(file, fieldnames=["First Name", "Last Name"])
        #csv_writer.writeheader()  # necessary if existing file w/ headers? NOPE!
        csv_writer.writerow({
            "First Name": first_name,
            "Last Name": last_name
        })

# Used open("w"), writeheader() and add_user(Colt) to create users.csv file
#add_user("Colt", "Steele")  

# After file was created with Colt and headers, changed to open("a") and no header()
#add_user("Dwayne", "Johnson")

# Colt's solution with WRITER (lists)
# import csv

# def add_user(first_name, last_name):
#     with open("users.csv", "a") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow([first_name, last_name])


# PRINT_USERS - Prints out all first and last names in the users.csv file
# from csv import DictReader

# def print_users():
#     with open("users.csv") as file:
#         csv_reader = DictReader(file, fieldnames=["First Name", "Last Name"])
#         next(csv_reader)  # In order to skip printing the headers
#         for user in csv_reader:
#             #print(f"{user['First Name']} {user['Last Name']}")  # Watch "'"s!
#             print("{} {}".format(user["First Name"], user["Last Name"]))

# print_users()

# Using reader instead DictReader
from csv import reader

def print_users():
    with open("users.csv") as file:
        csv_reader = reader(file)
        next(csv_reader)  # skip headers
        for user in csv_reader:
            print("{} {}".format(user[0], user[1]))

print_users()