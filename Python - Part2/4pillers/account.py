
from bank import Bank


class Account(Bank):

    def __init__(self, name, email):
        self.acc_name = name
        self.acc_email = email

    def open_account(self):
        print('account opened successfully')

    def cal_bal(self):
        print("Account class - cal_bal method")

Account('Rahul','rahul@gmail.com')