import sqlite3
conn = sqlite3.connect("my_friends.db")
# 1. Create the Cursor object
c = conn.cursor()

# 2. Execute some SQL
people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)
]
# To iterate and insert one by one:
# for person in people:
#     insert that one person

# To insert in bulk using executemany() but can only insert
#c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# To insert AND do something else with each record:
average = 0
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    average += person[2]
print(average/len(people))
    


# 3. Commit changes
conn.commit()
# 4. Close the connection
conn.close()