# given mobile is indian mobile number or not?
# 6,7,8,9 and 10 digit number
# [6-9]\d{9}
import re
number = input('Enter Mobile Number')

match = re.fullmatch("[6-9]\d{9}", number)

if match != None:
    print("Given number is Valid indian Mobile Number")
else:
    print("Not Valid Mobile Number")
