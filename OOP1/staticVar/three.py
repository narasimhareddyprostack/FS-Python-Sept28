class Test:
    a=100
    
    def m1(self):
        print(Test.a)
        print(self.a)

t1=Test()

print(Test.a)
print(t1.a)
