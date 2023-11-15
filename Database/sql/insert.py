import mysql.connector


try:
    dbcon = mysql.connector.connect(
        host="localhost", user="root", password="root", database="8pm")
    mycursor = dbcon.cursor()
    sql_st = ''' 
              insert into employee values(109,'kamal',45000.00,'bangalore')
             '''
    sql_st1 = '''
                insert into employee values(111,'amul',45000.00,'bangalore'),(112,'raj',535353.9,'bang')
             '''
    mycursor.execute(sql_st1)
    dbcon.commit()
    print("Data Inserted Successfully")
except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    mycursor.close()
    dbcon.close()
