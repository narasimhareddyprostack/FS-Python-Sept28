def division_check(func):
    
    def inner(a,b):
        if b==0:
            print("Can't Divide by Zero")
        else:
            return func(a,b)

    return inner



@division_check
def divide(a,b):
    print(a/b)


divide(10,5)  #2.0 
divide(10,0)  #ZerodivisionError

divide(200,10)