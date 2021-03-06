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

# can change values with 'UPDATE'
query = "UPDATE users SET name = 'kar' WHERE id = 1"

cursor.execute(query)

db.commit()

query = "SELECT * FROM users"

cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)