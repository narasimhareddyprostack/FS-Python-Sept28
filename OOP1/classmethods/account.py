class Account:
    counter = 0  # static

    def __init__(self, id, name):
        Account.counter = Account.counter+1


Account(101, 'Rahul')
Account(102, 'Sonia')
Account(103, 'Priyanka')
Account(104, 'Modi')


print("No of Object", Account.counter)
