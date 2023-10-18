#read csv file, and display user names
import csv 
fp=open('emp.csv','r')
csv_obj=csv.reader(fp)
users=list(csv_obj)

for user in users:
    print(user[3])



fp.close()
