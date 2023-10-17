
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)   #function call itself
    
    return result

result = factorial(6)
print(result)

""" 6*factorial(5)
6*5*factorial(4)
6*5*4*factorial(4)
6*5*4*3*factorial(2)
6*5*4*3*2*factorial(1)
6*5*4*3*2*1 """
