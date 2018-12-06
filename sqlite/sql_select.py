import sqlite3, os

#print(os.getcwd())
#os.chdir("/Users/gaylonalfano/Python Projects/ModernPython3Bootcamp/sqlite_friends")
conn = sqlite3.connect("/Users/gaylonalfano/Python Projects/ModernPython3Bootcamp/sqlite_friends/my_friends.db")
# 1. Create the Cursor object
c = conn.cursor()
# 2. Execute some SQL. But for SELECT, we get something back!
# We can choose to do something with what's returned (iterate, convert to list, etc.)
# c.execute("SELECT * FROM friends WHERE first_name = 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
#print(c)  # <sqlite3.Cursor object at 0x104e...>
# Iterate over the Cursor:
# for result in c:
#     print(result)

# To fetch one result using .fetchone():
# print(c.fetchone())

# To convert the results into a Python list, use fetchall():
print(c.fetchall())  # [('Steve', 'Irwin', 9), ('Roald', 'Amundsen', 5), ...]

# To convert results to a list and specify the number to return using fetchmany(size):
# print(c.fetchmany(3))

# 3. Commit changes
conn.commit()
# 4. Close the connection
conn.close()