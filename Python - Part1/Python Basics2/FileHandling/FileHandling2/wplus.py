#w+ : write and read operation.

st = "Hello,Good Evening!"
fp=open('stex.txt','w+')

fp.write(st)

data=fp.read()

print(data)

fp.close()