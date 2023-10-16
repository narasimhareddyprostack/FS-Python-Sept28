emp={'id':101, 'name':'rahul','loc':'wayand'}


emp['name'] = 'Rahul Gandhi'

print(emp)

emp['email'] = 'rahul@gmail.com'
print(emp)

del emp['id']

print(emp)

emp.clear()  #it removes all enties(key:values) from set.
print(emp)

del emp   #we are deleting complete dict object

print(emp)


