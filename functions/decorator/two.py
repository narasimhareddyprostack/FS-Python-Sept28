def outer():
    print('outer function')
    
    def inner():
        print("inner function")

    def f1():
        print("function one")
        
    return inner



inner = outer()
inner()
inner()
inner()