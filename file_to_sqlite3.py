# Importing built-in sqlite3 module
import sqlite3

# Global constants
DATABASE_NAME = 'astronaut.db'
TABLE_NAME = 'tblAstronaut'
FILE_NAME = 'astronaut_data.txt'

# Creating a database connection
print(f'Connecting to {DATABASE_NAME}')
connection = sqlite3.connect(DATABASE_NAME)

# Creating cursor to interact with database via the connection
cursor = connection.cursor()

# Drop the table 'tblAstronaut' if it exists (to create a fresh table each time the code is run)
print(f'Dropping table {TABLE_NAME} if exists')
drop_query = f'DROP TABLE IF EXISTS {TABLE_NAME}'
print(f'Running query: {drop_query}')
cursor.execute(drop_query)

# Creating an empty table named 'tblAstronaut' with the following fields:
# Destination, MassMultiplier, CrewToolWeight1, CrewToolWeight2, CrewToolWeight3,
# MSToolWeight1, MSToolWeight2, MSToolWeight3
print(f'Creating table {TABLE_NAME}')
create_table_query = f'''
    CREATE TABLE {TABLE_NAME}
    (
        Destination TEXT NOT NULL PRIMARY KEY,
        MassMultiplier REAL,
        CrewToolWeight1 INTEGER,
        CrewToolWeight2 INTEGER,
        CrewToolWeight3 INTEGER,
        MSToolWeight1 INTEGER,
        MSToolWeight2 INTEGER,
        MSToolWeight3 INTEGER
    )
'''
print(f'Running query: {create_table_query}')
cursor.execute(create_table_query)
print(f'Table created')

# Reading data from file
with open(FILE_NAME, mode='r') as data_file:
    astronaut_data = [tuple([entry for entry in line.strip().split(',')]) for line in data_file.readlines()]
    
print(f'Astronaut Data: {astronaut_data}')

# Inserting the data into the sqlite3 database (the tblAstronaut table)
print(f'Inserting astronaut data into {TABLE_NAME}')
insert_query = f'INSERT INTO {TABLE_NAME} VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
print(f'Running query: {insert_query}')
cursor.executemany(insert_query, astronaut_data)
print(f'Inserted {cursor.rowcount} rows into {TABLE_NAME}')

# Commit changes to the database
# Commit is very important, if it's not done, the data will not be saved to the database
print(f'Committing changes to {DATABASE_NAME}')
connection.commit()
print('Commit successful')

# Closing the cursor and the connection
print('Closing the connection')
cursor.close()
connection.close()
print('Done.')
