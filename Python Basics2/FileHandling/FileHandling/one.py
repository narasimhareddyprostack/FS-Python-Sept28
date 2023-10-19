#read data.txt file and print content in console/terminal
fp=open('data.txt','r')

#data=fp.read(10)
#data=fp.readline()
data=fp.readlines()
print(data)

fp.close()