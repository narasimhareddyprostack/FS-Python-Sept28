class Account:
    def __init__(self, name, email):
        self.acc_name = name
        self.email = email


class SA(Account):
    def __init__(self, id, name, email, amount):
        super().__init__(name, email)
        self.acc_id = id
        self.acc_bal = amount


sa1 = SA(101, 'Rahul', 'rahul@gmail.com', 50000)


class CA(Account):
    def __init__(self, id, name, email, amount):
        super().__init__(name, email)
        self.acc_id = id
        self.acc_bal = amount


ca1 = CA(102, 'Sonia', 'sonia@gmail.com', 4000)

print(sa1.__dict__)
print(ca1.__dict__)
