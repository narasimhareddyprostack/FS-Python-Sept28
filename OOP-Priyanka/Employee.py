from Company import Company
class Employee(Company):
    def __init__(self, name, id):
        self.emp_name=name
        self.emp_id=id

    def login(self):
        print(" logged in")

    def logout(self):
        print(" logged out")
    
    def cal_leaves(self):
        print("employee class cal_leaves method")
    
    def set_no(self, no):
        self.no=no
    
    def get_no(self):
        return self.no
e1=Employee("ABC", 24)
e1.login()
e1.set_no(99567)
num=e1.get_no()
print(num)
