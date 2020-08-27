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

### Selecting data

query = "SELECT * FROM users"

## retrive records from table
cursor.execute(query)

records = cursor.fetchall()

for record in records:
    print(record)

## Lets get a column

query = "SELECT user_name FROM users"

cursor.execute(query)

usernames = cursor.fetchall()

for name in usernames:
    print(name)


## Multiple columns
query = "SELECT name, user_name FROM users"

cursor.execute(query)

usernames = cursor.fetchall()

for name in usernames:
    print(name)