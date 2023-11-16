import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(
    host="localhost", user="root", passwd="root", database="prostack")
# creating the cursor object
cur = myconn.cursor()
