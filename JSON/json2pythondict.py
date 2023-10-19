import json 

emp_json =''' { "eid":101, "ename":"Rahul","esal":45000,"avail":true} '''


emp_dict = json.loads(emp_json)
print(emp_json)
print(emp_dict)