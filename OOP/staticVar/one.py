class Account:
    min_bal=500   #static

    def __init__(self,id):
        self.acc_id=id 
        Account.branchname="Marathahalli"

    def set_bal(self):
        Account.branchid=6777
    
    @classmethod
    def updateparentbrach(cls):
        cls.parentbranch='Bangalore' 
        
    @staticmethod
    def tax_cal():
        Account.tax=11

a1=Account(101)
print(a1.__dict__)  #{acc_id:101}
print(Account.__dict__)