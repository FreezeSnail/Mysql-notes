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
try:
    cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
except:
    print("table users already exists")

cursor.execute("SHOW TABLES")

tables = cursor.fetchall()

for table in tables:
    print(table)


### we can also create a table with a primary key
## lets remove the user tabnle and start again with a primary key this time

cursor.execute("DROP TABLE users")

cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")

#'DESC table_name' will retrieve collum information
cursor.execute("DESC users")

print(cursor.fetchall())

## we can remove columns as well
cursor.execute("ALTER TABLE users DROP id")

cursor.execute("DESC users")

print(cursor.fetchall())

## and add columns

cursor.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

cursor.execute("DESC users")

print(cursor.fetchall())