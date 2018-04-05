# import the db
import sqlite3

# init the connection
connection = sqlite3.connect('data.db')

# init the cursor
cursor = connection.cursor()

# create a table 
create_table = "CREATE TABLE users (id int, username text, password text)"

# execute the cursor to create the table
cursor.execute(create_table)

# create a user for teat
user = (1, 'ahmed', '123456')

# write the insert query
insert_query = "INSERT INTO users VALUES (?, ?, ?)"

# execute the cursor to insert the user
cursor.execute(insert_query, user)


# insert multible users
users = [
    (2, 'mike', '123456'),
    (3, 'john', '123456')
]

cursor.executemany(insert_query, users)


# select query
select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)
# commit the checnges
connection.commit()

# close the connection
connection.close()