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


# Other approach with only 1 file open at a time
from csv import reader, writer
with open("fighters.csv") as file:
    csv_reader = reader(file)
    # data converted to list and saved to variable
    fighters = [[s.upper() for s in row] for row in csv_reader]  # Not best but it's simple

# 2nd file: SCREAM version of fighter.csv
with open("screaming_fighters.csv", "w") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)

# Colt's nested with statements solution:
from csv import reader, writer
with open("fighters.csv") as file:
    csv_reader = reader(file)  # data never converted to list
    with open("screaming_fighters.csv", "w") as new_file:
        csv_writer = writer(new_file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])

# My NESTED attempt:
from csv import reader, writer
with open("fighters.csv") as file:
    csv_reader = reader(file)
    with open("screaming_fighters.csv", "w") as new_file:
        csv_writer = writer(new_file)
        fighters = [[trait.upper() for trait in fighter] for fighter in csv_reader]  # Not best.
        for fighter in fighters:
           csv_writer.writerow(fighter)


