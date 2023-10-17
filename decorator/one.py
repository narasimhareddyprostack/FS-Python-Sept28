def outer():
    print('outer function')
    
    def inner():
        print("inner function")

    inner()
    inner()



outer()

#execute inner function, outside a function?
#return function ref, and call