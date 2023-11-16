import requests
import mysql.connector

dbcon = None
mycur = None
try:
    dbcon = mysql.connector.connect(
        host='localhost', user='root', password='root', database='8pm')
    mycur = dbcon.cursor()
    sql_st = '''
            insert into products(pid,pname,price,brand) values(%s,%s,%s,%s)
           '''
    data = []
    resp = requests.get('https://dummyjson.com/products')
    product_dict = resp.json()
    # print(type(product_dict['products']))

    for product in product_dict['products']:
        data.append((product['id'], product['title'],
                    product['price'], product['brand']))

    mycur.executemany(sql_st, data)
    dbcon.commit()
    print('Data inserted successfully')

except mysql.connector.DatabaseError as err:
    if err:
        print(err)
finally:
    if mycur:
        mycur.close()
    if dbcon:
        dbcon.close()
