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

#can use 'ORDER BY' to sort the results of a query
# default to ascending or using 'DESC' to descend

query = "SELECT * FROM users ORDER BY name"

cursor.execute(query)
records = cursor.fetchall()

for record in records:
    print(record)

query = "SELECT * FROM users ORDER BY name DESC"

cursor.execute(query)
records = cursor.fetchall()

for record in records:
    print(record)