class Account:

    noobjects=0  #static  variable 
   
    def __init__(self):
        Account.noobjects = Account.noobjects + 1 

    @classmethod
    def get_noofObject(cls):
        return cls.noobjects




a1=Account()
a2=Account()
a3=Account()
a4=Account()

print(Account.noobjects)
print(Account.get_noofObject())