#read emp.json data from json, print all employee names
import json 

fp=open('emp.json','r')

employees=json.load(fp)
print(employees)
#print all employee names, or print emp id 





for emp in employees:
    #print(emp['name'])
    print(emp['id'])

