import csv

fp=open("user.csv",'w',newline="")
csv_obj=csv.writer(fp)
csv_obj.writerow(["username","email","location"])



csv_obj.writerow(["rahul","rahul@gmail.com","Wayanad"])
csv_obj.writerow(["sonia","sonia@gmail.com","Noida"])
csv_obj.writerow(["print","priyanka@gmail.com","chennai"])

fp.close()