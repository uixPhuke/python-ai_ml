f=open("sample.txt","r") #file object
data=f.read()
print(data)
print(type(data))

data2=f.readline() #readline() reads one line at a time and moves the cursor to the next line
print(data2)


f.close()