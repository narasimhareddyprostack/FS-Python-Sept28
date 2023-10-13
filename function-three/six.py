#convert local variable to global 



def funcone():
    global a
    a=100


def functwo():
    print(a)


funcone()
functwo()