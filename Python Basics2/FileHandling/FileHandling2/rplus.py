#r+ mode: read and write data into file.
#file has data? data in the file, will not be deleted.


fp = open("data.txt",'r+')

data=fp.read()
fp.write("Hello,Good Evenig")


fp.close()

