# Import the built-in sqlite3 module
import sqlite3

# Global constants
DATABASE_NAME = 'astronaut.db'
TABLE_NAME = 'tblAstronaut'

# Creating a database connection
connection = sqlite3.connect(DATABASE_NAME)

# Creating cursor to interact with database via the connection
cursor = connection.cursor()

# Select query
select_query = f'SELECT * FROM {TABLE_NAME}'
cursor.execute(select_query)

# Fetching all records into a list of tuples
all_astronauts = cursor.fetchall()
print('Using fetchall():')
print(all_astronauts)

# Fetching records one by one
print('Using fetchone():')
cursor.execute(select_query)
row = cursor.fetchone()
while row != None:
    print(row)
    row = cursor.fetchone()

# Closing the cursor and the connection
cursor.close()
connection.close()
