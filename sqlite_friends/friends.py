import sqlite3

# Create the database and store to a variable (conn, c, connection)
# Interact with database with this connection
conn = sqlite3.connect("my_friends.db")

# Creating a table using a Python Cursor object. A Cursor is like a temporary
# workspace for SQL command. Pattern is:
# 1. Create the Cursor object
c = conn.cursor()
# 2. Execute some SQL
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# 3. Commit changes
conn.commit()
# 4. Close the connection
conn.close()
