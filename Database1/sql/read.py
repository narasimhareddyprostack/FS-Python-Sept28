import mysql.connector
dbcon = None
try:
    dbcon = mysql.connector.connect(
        host="localhost", user="root", password="root", database="8pm")
    mycursor = dbcon.cursor()

    mycursor.execute('select * from employee')
    empdata = mycursor.fetchall()

    for emp in empdata:
        print("Employee Id:", emp[0], ":Employee Name",
              emp[1], "and Salary:", emp[2])

except mysql.connector.DatabaseError as err:
    if err:
        print("Unable to connect to Database")
        print(err)

finally:
    if mycursor:
        mycursor.close()
    if dbcon:
        dbcon.close()
