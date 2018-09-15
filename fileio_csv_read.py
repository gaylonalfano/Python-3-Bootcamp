"""
File I/O - Reading CSV files
Two ways covered in this tutorial:
1. reader - lets you iterate over rows of the CSV as lists. READER OBJECT.
Gets exhausted/used up after calling it once! It's an iterator so if you 
go over it once, it can't call next() anymore.
    
2. DictReader - lets you iterate over rows of the CSV as OrderedDicts. It's a 
special collection in Python. It's also an iterator so can only iterate once!
This (I believe) is part of the Pandas DF structure...

3. **KWARGS - Other Delimiters - Readers accept a delimiter kwarg in case your data
isn't spearated by commas. 

Example: kwargs
from csv import reader
with open("example.csv") as file:
    csv_reader = reader(file, delimiter="|")
    for row in csv_reader:
        # each row is a list
        print(row)



Example: reader
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        # each row is a LIST!
        print(row)


Example: DictReader
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # each row is an OrderedDict!
        print(row)
"""

from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader)  # This starts on the rows AFTER the headers
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")
#         # each row is a LIST!
#         #print(row)

# If you wanted to keep the headers and use it:
# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)  # Returns a list of lists: [['Name', 'Country', 'Height'],['Ryu',...]]

from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # each row is an OrderedDict!
        print(row['Name'])  # See below
'''
OrderedDict([('Name', 'Ryu'), ('Country', 'Japan'), ('Height (in cm)', '175')])
OrderedDict([('Name', 'Ken'), ('Country', 'USA'), ('Height (in cm)', '175')])
OrderedDict([('Name', 'Chun-Li'), ('Country', 'China'), ('Height (in cm)', '165')])
OrderedDict([('Name', 'Guile'), ('Country', 'USA'), ('Height (in cm)', '182')])
...
'''
