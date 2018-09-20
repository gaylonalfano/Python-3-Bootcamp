"""
UPDATE_USERS EXERCISE - Two columns: First Name, Last Name

Takes an old first name and old last name , new first name, new last name
and updates the users.csv file. 

Here are some FIND_USERS() METHODS:
# MY SOLUTION W/ READER Without for loop just search in list
def find_user(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = list(reader(file))
        if [first_name, last_name] in csv_reader:
            return csv_reader.index([first_name, last_name])
        return "{} {} not found.".format(first_name, last_name)
        #return f"{first_name} {last_name} not found."


# ENUMERATE example student solution:
def find_user(first, last):
    with open("users.csv") as file:
        users = reader(file)
        for (index, row) in enumerate(users):
            if row == [first, last]:
                return index
        return "{} {} not found.".format(first, last)

# MY SOLUTION DICTREADER ENUMERATE
def find_user2(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = DictReader(file)  # Don't have to state fieldnames? No! Default 1st row
        for count, item in enumerate(csv_reader):
            if item["First Name"] == first_name and item["Last Name"] == last_name:
                return count
            return f"{first_name} {last_name} not found."

# STUDENT'S DICTREADER ENUMERATE:
def find_user(first, last):
    with open('users.csv') as f:
        for i,r in enumerate(DictReader(f),1):
            if r['First Name'] == first and r['Last Name'] == last:
                return i
        return "{} {} not found.".format(first,last)


Handy dict reference: https://docs.python.org/3/library/stdtypes.html#dict
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e


KEY LEARNINGS:
Can't nest WITH statements if working on the same file. Need to read and store into a var.


"""
# UPDATE_USERS - Need to use read and write???
import csv

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as file:
        csv_reader = list(csv.DictReader(file))
    with open("users.csv", "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=["First Name", "Last Name"])
        csv_writer.writeheader()
        users_updated = 0
        for row in csv_reader:
            if row["First Name"] == old_first and row["Last Name"] == old_last:
                csv_writer.writerow({"First Name": new_first, "Last Name": new_last}) 
                users_updated += 1
            else:
                csv_writer.writerow({"First Name": row["First Name"], "Last Name": row["Last Name"]})

        return "Users updated: {}.".format(users_updated)   #f"Users updated: {users_updated}."

#print(update_users('Gaylon', 'Alfano', "Aaron", "Anthony"))
print(update_users('Not', 'Here', "Still Not", "Here"))


# COLT'S SOLUTION USING READER/WRITER:
import csv
 
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users updated: {}.".format(count)


# STUDENT SOLUTION DICTREADER/DICTWRITER
from csv import DictReader, DictWriter
 
def update_users(old_first, old_last, new_first, new_last):
    count = 0
    with open("users.csv") as f:
        data = list(DictReader(f))
        for row in data:
            if row["First Name"] == old_first and row["Last Name"] == old_last:
                row["First Name"], row["Last Name"] = new_first, new_last
                count += 1
    with open("users.csv", "w", newline="") as file:
        headers = ("First Name", "Last Name")
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow({
                "First Name": row["First Name"],
                "Last Name": row["Last Name"]
            })
    return "Users updated: {}.".format(count)






# ======= BELOW are my broken attempts ========

# def update_users(old_first, old_last, new_first, new_last):
#     with open("users.csv", "r+") as file:
#         csv_reader = csv.DictReader(file)  # fieldnames=Defaults to first row
#         #csv_writer = csv.DictWriter(file, fieldnames=["First Name", "Last Name"])
#         #print(list(csv_reader))  # [('First Name', 'Colt'), ('Last Name', 'Steele')]
#         # Need to open with "w" or "r+" to update?
#         users_updated = 0
#         for row in csv_reader:
#             if row["First Name"] == old_first and row["Last Name"] == old_last:
#                 row['First Name'] = new_first
#                 row["Last Name"] = new_last
#                 # row["First Name"] = csv_writer.writerow({"First Name": new_first}) - This appends at end with linebreak
#                 # row["Last Name"] = csv_writer.writerow({"Last Name": new_last})
#                 users_updated += 1
#         return f"Users updated: {users_updated}."
            

# def update_users(old_first, old_last, new_first, new_last):
#     with open("users.csv") as file:
#         csv_reader = csv.DictReader(file)
#         with open("users.csv", "w") as file:
#             csv_writer = csv.DictWriter(file, fieldnames=["First Name", "Last Name"])
#             users_updated = 0
#             for row in csv_reader:
#                 if row["First Name"] == old_first and row["Last Name"] == old_last:
#                     csv_writer.writerow({"First Name": new_first, "Last Name": new_last}) 
#                     users_updated += 1
#                 else:
#                     csv_writer.writerow({"First Name": old_first, "Last Name": old_last})
#             return f"Users updated: {users_updated}."



