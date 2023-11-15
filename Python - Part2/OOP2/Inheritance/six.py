class Parent1:
    def m1(self):
        print("m1 Method- Parent1")


class Parent2:
    def m2(self):
        print("m2 Method- Parent1")


class Child(Parent1, Parent2):
    def m3(self):
        print("m3 Method- Parent1")


c1 = Child()
c1.m1()
c1.m2()
c1.m3()
