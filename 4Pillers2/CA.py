from Account import Account


class CA(Account):
    min_bal = 25000

    def __init__(self, id, name, email, address, amount):
        super().__init__(name, email, address)
        self.acc_id = id
        self.acc_bal = amount

    def cal_bal(self):
        return self.acc_bal - self.min_bal


""" ca1 = CA(201, 'Priyanka Gandi', 'priya@gmail.com', 'chennai', 70000)
print(ca1.__dict__)
print(ca1.cal_bal())
 """