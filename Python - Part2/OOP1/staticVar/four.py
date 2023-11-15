class Test:
    a=100   #static,
    
    def m1(self):
        print(Test.a)
        print(self.a)

    @classmethod
    def m2(cls):
        print(Test.a)
        print(cls.a)

t1=Test()

t1.m1()
t1.m2()