import mysql.connector as mysql
import os


from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('SQL_HOS')
USER = os.getenv('SQL_USER')
PASS = os.getenv('SQL_PASS')

#use the 'connect()'method to coonect to the database

db = mysql.connect(
    host = HOST,
    user = USER,
    passwd = PASS,
    database = "testing"
)

cursor = db.cursor()


###Adding a row
#define a query
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"

#put values in to a variable
values = ("Hafeez", "hafeez")

#run the query
cursor.execute(query, values)

#use 'commit()' to finalize changes
db.commit()

print(cursor.rowcount, "record inserted")


### Adding multiple rows

values = [
    ("jim", "j"),
    ("kim", "k"),
    ("lim", "l"),
    ("mim", "m")
]

## use 'exectuemany()' to insert multiple values
cursor.executemany(query, values)

db.commit()

print(cursor.rowcount, "records inserted")