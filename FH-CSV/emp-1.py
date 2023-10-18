import csv 
fp=open('emp.csv','r')
csv_obj=csv.reader(fp)
user_List=list(csv_obj)

#print(type(csv_obj))
fp.close()
