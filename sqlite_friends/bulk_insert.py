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

# To insert in bulk using executemany():
c.executemany("INSERT INTO friends VALUES (?,?,?)", people)


# 3. Commit changes
conn.commit()
# 4. Close the connection
conn.close()