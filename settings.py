# In order to use MYSQL Connector, we need to import property of the mysql module

import mysql.connector 

site_title = "Premier CRUD"

# Now we have created a database we can connect to the database. To do so, se will use our MYSQL login credentials as parameters of the connect() method of the connector property of the mysql module.

# Because we are working locally, the host is localhost, XAMPP's defeault username is "root" and default password is blank. if you are using MAMP then it is required that you have a password so you will need to set one.

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "premiers"
)

# To execute SQL queries we need to create a cursor. We can set the dictionary parameter of the cursor() method to true to have rows returned as dictionaries.

mycursor = mydb.cursor(dictionary=True, buffered=True)

