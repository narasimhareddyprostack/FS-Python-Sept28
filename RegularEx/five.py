# Given email id is valid email and gmail account or not.
# greetlabs@gmail.com
# narasimha@tcs.com
import re

st = input("Enter Email id:")
pattern = "\w[a-zA-Z0-9_.]*@gmail[.]com"

match = re.fullmatch(pattern, st)
if match != None:
    print("Valid gmail Id")
else:
    print("Not Valid")
