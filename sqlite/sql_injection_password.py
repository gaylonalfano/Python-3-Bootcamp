import sqlite3

conn = sqlite3.connect("/Users/gaylonalfano/Python Projects/ModernPython3Bootcamp/sqlite_friends/users.db")

# 1. Create the Cursor object
c = conn.cursor()

# 2. Execute some SQL
# You would never store password in your db as TEXT, FYI. Creating table:
# query = "CREATE TABLE users (username TEXT, password TEXT)"
# c.execute(query)

# Add some users:
# users = [
#     ('Gaylon', '&&hjn_fp'),
#     ('Colt', '2@jdn)'),
#     ('Blue', 'Meow')
# ]
# query = f"INSERT INTO users VALUES (?, ?)"
# c.executemany(query, users)

# Now for the SQL injection part:
username = input("Please enter your username: ")
password = input("Please enter your password: ")
# DON'T DO THIS! Just showing as an example:
# query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
# c.execute(query)

# A BETTER/SAFER way of doing this is like this:
query = f"SELECT * FROM users WHERE username=? AND password=?"
c.execute(query,(username,password))

result = c.fetchone()
if result:
    print("Welcome back!")
else:
    print("Failed login")

# 3. Commit your changes
conn.commit()

# 4. Close connection
conn.close()


