#function - need to verify given number is 3 digit or not
#function - need to verify given number is even or odd

def three_digit(num):
    if num>=100 and num<=999:
        print("Given number is 3 Digit Number")
    else:
        print("Not Three Digit Number")

def even_or_odd(num):
    if num %2 ==0:
        print("Even")
    else:
        print('Odd')


three_digit(3451)
even_or_odd(7890)