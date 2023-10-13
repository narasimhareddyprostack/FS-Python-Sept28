a=100               #global

def funcone():
    b=200   #local variable , scope is with in the func


def functwo():
    a=20
    print(a+b)

funcone()
functwo()
