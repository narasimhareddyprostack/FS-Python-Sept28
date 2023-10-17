from functools import reduce

marks=[35,36,37,38,39]

result=reduce(lambda a,b:a+b,marks)

print(result)

