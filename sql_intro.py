#1. import sqlite module to be able to use a database
import sqlite3

#2. the connect method creates?starts our database
connect = sqlite3.connect()

#3. the cursor variable creates a new object that lets us send objects to our database
cursor = connect.cursor()

#4. we need to create a schema (structure) for our data
cursor.execute('''(
    CREATE TABLE compers(
    id INTERGER PRIMARY computers,
    model TEXT,
    color TEXT,
    hasWebCam BOOL, 
               )''')

cursor.execute('''
    INJSERT INTO COMPUTERS(model,color,hasWebcam,memory,price)
    values('apple m4'')