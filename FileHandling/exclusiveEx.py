#create Error message: FileExistsError 

fp=open('18oct.txt','x')
fp.write("exclusive creation mode for write operation")
fp.close()