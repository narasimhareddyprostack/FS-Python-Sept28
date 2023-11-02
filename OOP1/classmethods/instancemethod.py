class Account:

    def set_account_Id(self,id):
        self.acc_id=id 

    def get_account_Id(self):
        return self.acc_id

a1=Account()
a2=Account()

a1.set_account_Id(1101)
a2.set_account_Id(1102)
print(a1.get_account_Id())
print(a2.get_account_Id())