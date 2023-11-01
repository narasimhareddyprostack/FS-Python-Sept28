class Account:
    noobject=0  #static  variable 
    def __init__(self):
        Account.noobject = Account.noobject + 1 





a1=Account()
a2=Account()
a3=Account()
a4=Account()

print(Account.noobject)