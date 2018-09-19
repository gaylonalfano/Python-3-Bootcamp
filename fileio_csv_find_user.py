"""
KEY LEARNINGS:
I need to read up again on Try/Except statements

a = b == c syntax -- This is a boolean expression that evalues to True or False being saved to a var (a)
Could think of it like: a = (b == c).

enumerate() - https://docs.python.org/3/library/functions.html#enumerate
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which 
supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple 
containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.

list(enumerate(seasons, start=1))  # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

l1 = ["eat","sleep","repeat"]
for (count,item) in enumerate(l1):
    print count,item
    # 0 eat
    # 1 sleep
    # 2 repeat

"""


# from csv import reader

# # Trying for loop -- NOT working...
# # def find_user(first_name, last_name):
# #     with open("users.csv") as file:
# #         csv_reader = list(reader(file))
# #         for user in csv_reader:
# #             #if user[0] == first_name and user[1] == last_name:
# #             if [first_name, last_name] in user:
# #                 return user.index([first_name, last_name])
# #             return f"{first_name} {last_name} not found."

# # MY SOLUTION W/ READER Without for loop just search in list
# def find_user(first_name, last_name):
#     with open("users.csv") as file:
#         csv_reader = list(reader(file))
#         if [first_name, last_name] in csv_reader:
#             return csv_reader.index([first_name, last_name])
#         return "{} {} not found.".format(first_name, last_name)
#         #return f"{first_name} {last_name} not found."


# # ENUMERATE example student solution:
# def find_user(first, last):
#     with open("users.csv") as file:
#         users = reader(file)
#         for (index, row) in enumerate(users):
#             if row == [first, last]:
#                 return index
#         return "{} {} not found.".format(first, last)

# # COLT'S solution w/ ENUMERATE():
# import csv
 
# def find_user(first_name, last_name):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         for (index, row) in enumerate(csv_reader):
#             first_name_match = first_name == row[0]
#             last_name_match = last_name == row[1]
#             if first_name_match and last_name_match:
#                 return index
#         return "{} {} not found.".format(first_name, last_name)


# print(find_user("Colt", "Steele"))
# print(find_user("Dwayne", "Johnson"))
# print(find_user("Not", "Here"))

# with open("users.csv") as file:
#     csv_reader = list(reader(file))
#     print(['Colt', 'Steele'] in csv_reader)
#     print(csv_reader[1])


# ("FN", "Gaylon") in d.items()  # True








# DictReader attempt. Here's a sample DictReader output
'''
OrderedDict([('First Name', 'Colt'), ('Last Name', 'Steele')])
OrderedDict([('First Name', 'Dwayne'), ('Last Name', 'Johnson')])
for count, item in enumerate(csv_reader):
  print(count, item)  # 0 OrderedDict([('First Name', 'Colt'), ('Last Name', 'Steele')])
  print(item.values()) # odict_values(['Colt', 'Steele'])

'''

from csv import DictReader

def find_user2(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = DictReader(file)  # Don't have to state fieldnames?
        for count, item in enumerate(csv_reader):
            if item["First Name"] == first_name and item["Last Name"] == last_name:
                return count
            return f"{first_name} {last_name} not found."
'''
Random testing - Nothing worked really

            # print(count, item.values())
            # print(item.get("Colt", "Steele"))


            # if (first_name, last_name) in item.items():
            #     return count
            # return f"{first_name} {last_name} not found."
            #print(count, item)  # OrderedDict([('First Name', 'Colt'), ('Last Name', 'Steele')])
            #print(row["First Name"])  # Colt
            #print(row[0])
            # if (first_name, last_name) in row:
            #     return True
            # return "Not found."
'''

print(find_user2("Dwayne", "Johnson"))
print(find_user2("Colt", "Steele"))
print(find_user2("Not", "Here"))


# STUDENT'S DICTREADER ENUMERATE:
def find_user(first, last):
    with open('users.csv') as f:
        for i,r in enumerate(DictReader(f),1):
            if r['First Name'] == first and r['Last Name'] == last:
                return i
        return "{} {} not found.".format(first,last)


# STUDENT SOLUTION WITH READER AND TRY/EXCEPT:
import csv
def find_user(first_name, last_name):
    with open("users.csv", 'r') as file:
        csv_reader = list(csv.reader(file))
        try:
            result = csv_reader.index([first_name, last_name])
            return result
        except ValueError:
            return "{} {} not found.".format(first_name, last_name)