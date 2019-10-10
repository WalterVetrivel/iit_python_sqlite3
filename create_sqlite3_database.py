# Importing built-in sqlite3 module
import sqlite3

# Global constants
DATABASE_NAME = 'astronaut.db'
TABLE_NAME = 'tblAstronaut'

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

# Creating a list containing the data to be inserted into the table
# Each record is a tuple in python
astronaut_data = [
    ('Callisto', 0.1264, 101, 101, 101, 149, 149, 149),
    ('Enceladus', 0.0109, 89, 91, 102, 142, 152, 135),
    ('Europa', 0.1835, 95, 90, 100, 135, 140, 145),
    ('Ganymede', 0.1448, 79, 83, 102, 152, 149, 147),
    ('Io', 0.185, 93, 101, 89, 134, 152, 142),
    ('Mars', 0.377, 88, 87, 83, 122, 132, 142),
    ('Mercury', 0.378, 91, 88, 101, 132, 123, 149),
    ('Miranda', 0.008, 73, 83, 99, 112, 135, 147),
    ('Moon', 0.166, 92, 93, 90, 135, 140, 143),
    ('Pluto', 0.059, 88, 99, 88, 149, 149, 149),
    ('Titan', 0.143, 75, 80, 85, 110, 120, 130),
    ('Triton', 0.079, 100, 100, 100, 150, 150, 150),
    ('Venus', 0.907, 80, 90, 100, 130, 140, 150),
    ('Vesta', 0.023, 81, 83, 85, 142, 144, 146)
]
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
