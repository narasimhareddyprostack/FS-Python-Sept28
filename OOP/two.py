class Account:
    min_Bal=500

    def open_Account(self):
        print("Account Opened")

    def deposit_Amount(self):
        print("Amount Deposited")


a1=Account()

print(a1.min_Bal)
a1.open_Account()
a1.deposit_Amount()