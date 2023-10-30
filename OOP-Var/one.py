class Account:
    min_bal=500   #static variable
    def __init__(self,id,name):
        self.acc_id=id
        self.acc_name=name
    def open_Account(self):
        self.acc_bal = 200
    @classmethod 
    def get_Min_Bal(cls):
        pass
    @staticmethod
    def cal_interest():
        tax=5

a1=Account(101,'Rahul')
a2=Account(102,'Sonia')

print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)

