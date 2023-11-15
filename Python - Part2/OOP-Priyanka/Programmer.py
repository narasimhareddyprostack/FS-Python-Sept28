from Employee import Employee
class Programmer(Employee):
    total_leaves=10

    def __init__(self, name, id, desgn, level, lreq):
        super().__init__(name, id)
        self.emp_desgn=desgn
        self.emp_level=level
        self.emp_lreq=lreq
    
    def cal_leaves(self):
        if(self.total_leaves>0):
            print("Leave granted")
            self.total_leaves=self.total_leaves-self.emp_lreq
            print("leaves remaining", self.total_leaves )
        
    
cl1=Programmer("Harry",40,"WebDeveloper",9, 2)
print(cl1.__dict__)
cl1.cal_leaves()