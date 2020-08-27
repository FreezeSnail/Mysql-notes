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
    passwd = PASS
)

print(db) # will give a connector object if successful

## need an instance of the 'cursor' class to execute SQL statements
cursor = db.cursor()

#can use the 'execute()' method to compile and run SQL statements

##create a new db
#will throw an error is already created
try:
    cursor.execute("CREATE DATABASE testing")
except:
    print("the database testing already exists")

### lets see all the available databases
cursor.execute("SHOW DATABASES")

## 'fetchall()' will return all rows from the last executed statement
databases = cursor.fetchall() # in this case it will give all the databases present

print(databases) # print the rows


