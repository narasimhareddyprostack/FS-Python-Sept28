numbers=[1,2,3,4,5,6,7,8,9,10]

def is_Odd(number):
    if number%2 !=0:
        return True
    else:
        return False
    
new_odd=list(filter(is_Odd,numbers))
print(numbers)
print(new_odd)