#read 'n'  of emp and data from user, print in emp.csv 

import csv 

fp=open('emp.csv','w',newline="")
csv_ojb=csv.writer(fp)
#prepare csv header 
csv_ojb.writerow(["eid","ename","esal"])

n=int(input("Enter Number of employees:"))

for i in range(n):
    eid = input("Enter Eid:")
    ename =input("Enter Employee Name:")
    esal = input("Enter Employee Salary:")

    csv_ojb.writerow([eid,ename,esal])

