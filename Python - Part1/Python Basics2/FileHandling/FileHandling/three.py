fp=open("one.txt", 'w')

print(fp.name)
print(fp.mode)
print(fp.readable())
print(fp.writable())
print(fp.closed)
fp.close()

print(fp.closed)