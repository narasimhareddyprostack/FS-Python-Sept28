#class variable/static variable - 
class Account:
    min_bal=500  #static variable

    @classmethod
    def get_min_Bal(cls):
        return cls.min_bal 

    @classmethod
    def update_min_bal(cls):
        cls.min_bal = 700


print(Account.get_min_Bal())
Account.update_min_bal()
print(Account.get_min_Bal())
