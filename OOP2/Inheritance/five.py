# multi-Level Inheritance
class GrandParent:
    def m1(self):
        print("GrandParent-class : m1 method")


class Parent(GrandParent):
    def m2(self):
        print("Parent-class : m2 method")


class Child(Parent):

    def m3(self):
        print("Child-class : m3 method")


c1 = Child()
c1.m1()
c1.m2()
c1.m3()
