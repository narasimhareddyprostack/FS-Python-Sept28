class Account:
    min_bal=500   #static

    def __init__(self,id):
        self.acc_id=id 
        Account.branchname="Marathahalli"

    def set_branchId(self):
        Account.branchid=6777
    
    @classmethod
    def updateparentbrach(cls):
        cls.parentbranch='Bangalore' 
        
    @staticmethod
    def tax_cal():
        Account.tax=11

a1=Account(101)
a2=Account(102)

print(Account.__dict__)
a1.set_branchId()
a1.updateparentbrach()
a1.tax_cal()

print(Account.__dict__)

