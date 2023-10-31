class Account:
    def __init__(self):
        self.acc_bal = 5000 

    def get_bal(self):
        return self.acc_bal 

    def update_bal(self):
        self.acc_bal=7000

    def delete_bal(self):
        del self.acc_bal 

a1= Account()
print(a1.__dict__)
a1.delete_bal()
print(a1.__dict__)

