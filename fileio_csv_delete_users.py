"""
DELETE_USERS - Takes a fn,ln and deletes that user if a match. Returns count of Users deleted: n.


Here is my update_users() solution for reference:
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

        return "Users updated: {}.".format(users_updated)

"""
import csv

# Reader/Writer
def delete_users(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = list(csv.reader(file))  # gotta have list() if you don't nest with statements!
    with open("users.csv", "w") as file:
        csv_writer = csv.writer(file)  # Must use writer? A: Yes, otherwise just empties the file
        users_deleted = 0
        for row in csv_reader:
            if row[0] == first_name and row[1] == last_name:
                row.clear()
                users_deleted += 1
            else:
                #row[0], row[1] = row[0], row[1]  # Doesn't work without .writerow
                csv_writer.writerow(row)  

        return "Users deleted: {}.".format(users_deleted)

print(delete_users("Gaylon", "Alfano"))



# DictReader/DictWriter:
def delete_users(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = list(csv.DictReader(file, fieldnames=["First Name", "Last Name"]))
    with open("users.csv", "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=["First Name", "Last Name"])
        # csv_writer.writeheader() - Not necessary since else: writerow(row) below
        users_deleted = 0
        for row in csv_reader:
            #print(row.values())  # odict_values(['Gaylon', 'Alfano'])
            if row["First Name"] == first_name and row["Last Name"] == last_name:
                del row["First Name"]  # Not needed!
                del row["Last Name"]  # Not needed!
                users_deleted += 1
            else:
                csv_writer.writerow(row)
        
        return "Users deleted: {}.".format(users_deleted)

print(delete_users("Gaylon", "Alfano"))

"""
CARRIAGE RETURN (CR) AND LINE FEED (LF) NOTES:
I also had this solution but there is one thing to be aware of:

On top of a Carriage Return (CR) by default csv adds a Line Feed (LF) to each row in this example. 
So when you import the same file again it gets butchered.

Instead add the newline parameter with an empty string to the open() function:

    with open("users.csv", "w", newline="") as file: 

That way, only Carriage Returns are added after each row is written.
"""


# COLT'S SOLUTION W/ READER/WRITER:
# import csv
 
# def delete_users(first_name, last_name):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         rows = list(csv_reader)
 
#     count = 0
#     with open("users.csv", "w") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         for row in rows:
#             if row[0] == first_name and row[1] == last_name:
#                 count += 1  # !!! DON'T NEED TO ADD row.clear()!!!??
#             else:
#                 csv_writer.writerow(row)
 
#     return "Users deleted: {}.".format(count)



