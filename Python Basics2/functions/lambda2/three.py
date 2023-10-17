numbers=[1,2,3,4,5,6,7,8,9,10]
odd_numbers=[]


for number in numbers:
    if number%2!=0:
        odd_numbers.append(number)

print(numbers)
print(odd_numbers)

""" map(function,seq)
filter(function,seq)
reduce(function,seq) """