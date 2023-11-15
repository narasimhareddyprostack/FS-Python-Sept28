class Parent1:
    def m1(self):
        print("m1 Method- Parent1")


class Parent2:
    def m1(self):
        print("m1 Method- Parent2")


class Child(Parent1, Parent2):
    def m2(self):
        print("m3 Method- Child")


c1 = Child()
c1.m1()   # Parent1 - m1 method will execute
c1.m2()
