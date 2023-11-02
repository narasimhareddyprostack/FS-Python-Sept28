class Parent:
    def __init__(self):
        print("Parent Class -constructor")

    def m1(self):
        print("Parent class - m1 method")


class Child(Parent):
    def __init__(self):
        super().__init__()
        super().m1()
        print("Child Class -constructor")


Child()
