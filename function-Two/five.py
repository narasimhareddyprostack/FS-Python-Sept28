#how to invoke inner function, out side the function.

def outer():
    def inner():
        print("Inner Function")

    #return 100,200  (100,200)
    #return "Hello,GE"  Hello,GE
    return inner
inner_fun_ref=outer()
inner_fun_ref()
inner_fun_ref()

