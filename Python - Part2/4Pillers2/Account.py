from Bank import Bank


class Account(Bank):

    def __init__(self, name, email, address):
        self.acc_name = name
        self.acc_email = email
        self.acc_addreess = address

    def set_mobile_no(self, mobile):
        self.mobile = mobile

    def get_mobile_no(self):
        return self.mobile

    def cal_bal(self):
        pass

    def open_account(self):
        print('account opened successfully')


# a1 = Account('rahul', 'rahul@gmail.com', 'Bangalore')
""" print(a1.__dict__) """
