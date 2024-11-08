import psycopg2


# Connect Psycopg2 to Chinook database. connect() can take several parameters
connection = psycopg2.connect(database= "chinook")

# Build a cursor object (like a set or list. Similar to array in JS) of the database. 
# Anything that we query will become part of this object
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# Uses fetchall
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# Uses fetchall
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table. Need to use a Python string placeholder
# as neither single nor double quotes will work. Then define the string within a list
# Uses fetchone
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# Uses fetchone
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

#Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# Uses fetchall
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - CHALLENGE - select all albums with "ArtistId" #3 on the "Album" table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [3])

# Fetch the results (multiple) from the cursor
results = cursor.fetchall()

# Fetch the results (single) from the cursor
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result)