employees=[{'id':101, 'name':'rahul','sal':45000},
           {'id': 102, 'name': 'sonia', 'sal': 55000},
           {'id': 103, 'name': 'priyanka', 'sal': 65000},
           {'id': 104, 'name': 'modi', 'sal': 85000}]



#print all employee ids 
#print all employee names
#print total employee salary.

for emp in employees:
    print(emp['id'])

for emp in employees:
    print(emp['name'])

total=0
for emp in employees:
    total = total + emp['sal']


print(total)