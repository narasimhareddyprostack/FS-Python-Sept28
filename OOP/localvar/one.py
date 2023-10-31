class Test:
    a=100  #static 
    def m1(self):
        self.b=200   #instnce variable
        c=300        #local variable
        print(c)

    def m2(self):
        print(c)    #nameerror
 

t1=Test()
t1.m1()
t1.m2()