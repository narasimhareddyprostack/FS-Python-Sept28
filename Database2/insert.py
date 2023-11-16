# invoke Rest API, analyze data and store into mysql table.
import requests
import mysql.connector

dbcon = None
mycur = None
try:
    dbcon = mysql.connector.connect(
        host='localhost', user='root', password='root', database='8pm')
    mycur = dbcon.cursor()

    sql_st = '''
            insert into user(uid,uname,ucity,uemail) 
            values(%s,%s,%s,%s)
          '''
    data = []
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    user_list = response.json()

    for user in user_list:
        data.append((user['id'], user['username'],
                    user['address']['city'], user['email']))

    mycur.executemany(sql_st, data)
    dbcon.commit()
    print('Data Inserted successfully')
except mysql.connector.DatabaseError as err:
    if err:
        print(err)
finally:
    if mycur:
        mycur.close()
    if dbcon:
        dbcon.close()
