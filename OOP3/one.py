class Account:

    def __init__(self):
        pass

    def m1(self):
        pass

    @classmethod
    def m2(cls):
        pass

    @staticmethod
    def m3():
        pass
    
    @abstractmethod
    def m4(self):
        pass


print(Account().m1())
