class Employee:
    def __init__(self,id,name):
        self.eid=id
        self.ename=name

    def set_sal(self,sal):
        self.esal=sal


a1=Employee(101,'Rahul')
a2=Employee(102,'sonia')
print(a1.__dict__)  # {eid:101, ename:"Rahul"}
print(a2.__dict__)  # {eid:102, ename:"sonia"}
a1.set_sal(45000)
a2.set_sal(55000)
print(a1.__dict__)  # {eid:101, ename:"Rahul",esal:45000}
print(a2.__dict__)  # {eid:102, ename:"sonia",esal:55000}

a1.eloc="Wayanad"
print(a1.__dict__)  # {eid:101, ename:"Rahul",esal:45000,eloc:"Wayand"}
print(a2.__dict__)  # {eid:102, ename:"sonia",esal:55000}
