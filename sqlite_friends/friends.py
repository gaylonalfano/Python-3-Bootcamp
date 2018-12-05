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

# BAD way of inserting data:
# insert_query = "INSERT INTO friends VALUES ('Merriweather', 'Lewis', 7)"
# c.execute(insert_query)

# DYNAMIC but still BAD way of inserting data from application form that user's submit:
# BAD WAY TO INSERT DATA!!
# form_first = "Dana"   
# # You can use f"" but that's a BAD idea!" Here's a bad example:
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"
# c.execute(query)

# BETTER WAY! Dynamic and safer using '?' for values
# form_first = "Mary-Todd"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# # Then to pass in tuple containing values to be added in
# c.execute(query, (form_first,))

# BEST WAY! Usually you're passing more than one value. Usually you have a bunch
# of data coming from a form and it's already grouped. You don't have to use f-strings.
data = ("Steve", "Irwin", 9)
query = f"INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)

# 3. Commit changes
conn.commit()
# 4. Close the connection
conn.close()
