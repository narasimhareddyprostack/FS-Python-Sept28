class Accout:
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name 
        self.acc_bal=amount
        print('inside Account class const')

    def open_Account(self):
        print('account opened')
        
    def cal_bal(self):
        pass

a1=Accout(101,'rahul',6000)
a2=Accout(101,'Sonia',7000)
a1.open_Account()
a2.open_Account()
a1.open_Account()
a1.open_Account()