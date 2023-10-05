from sys import argv

argv_Values = argv[1:]

sum = 0

for value in argv_Values:
    sum =sum+int(value) 

print(sum)