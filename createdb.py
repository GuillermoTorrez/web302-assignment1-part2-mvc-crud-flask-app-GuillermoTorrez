import mysql.connector 

myuser = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

mycursor = myuser.cursor(buffered=True)

create_db = "CREATE DATABASE `premiers` "
mycursor.execute(create_db)

for database in mycursor:
    print(database)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "premiers"
)

mycursor = mydb.cursor(buffered=True)

# The Table will have a six columns
# The first wlll be a BIGINT and must use the AUTO_INCREMENT AND PRIMARY KEY statement to ensure that each row has a unique ID.
# The full_name column wich will also be a "VARCHAR" with a maximun length of 255
# The goals column wich will also be a a "VARCHAR" with a maximun length of 255
# The photo column wich will also be a "VARCHAR" with a maximun length of 255
# The birthdate column wich will also be a "DATETIME"
# The deceased wich will be a "TINYTINT" 

create_table = "CREATE TABLE `premier` (`id` BIGINT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(255), `photo` VARCHAR(255), `birthdate` DATETIME, `deceased` TINYINT(1) )"

mycursor.execute(create_table)
