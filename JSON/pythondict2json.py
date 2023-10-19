import json
emp_dict={'eid': 101,  
          'ename': 'Rahul', 
          'esal': 45000, 
          'avail': True,
          'discunt':None
          }

print(type(emp_dict))

emp_json=json.dumps(emp_dict)

print(emp_dict)
print(emp_json)