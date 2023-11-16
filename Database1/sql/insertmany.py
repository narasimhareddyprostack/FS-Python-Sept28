import mysql.connector


try:
    dbcon = mysql.connector.connect(
        host="localhost", user="root", password="root", database="8pm")
    mycursor = dbcon.cursor()
    sql_st = ''' 
              insert into employee(eid,ename,esal,eloc) values(%s,%s,%s,%s)
             '''
    data = [(102, 'Sonai', 55000.00, 'New Delhi'),
            (103, 'Priyka', 65000.00, 'Varanasi'),
            (104, 'Modi', 75000.00, 'Varanasi'),
            (105, 'Shaw', 85000.00, 'Gandhi Nagar'),
            (106, 'DK Shiva', 95000.00, 'Bangalore')
            ]
    mycursor.executemany(sql_st, [(102, 'Sonai', 55000.00, 'New Delhi'),
                                  (103, 'Priyka', 65000.00, 'Varanasi'),
                                  (104, 'Modi', 75000.00, 'Varanasi'),
                                  (105, 'Shaw', 85000.00, 'Gandhi Nagar'),
                                  (106, 'DK Shiva', 95000.00, 'Bangalore')
                                  ])
    dbcon.commit()
    print("Data Inserted Successfully")
except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    mycursor.close()
    dbcon.close()
