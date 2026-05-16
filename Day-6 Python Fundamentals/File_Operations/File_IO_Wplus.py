f=open("samplePlus.txt","r+") #'r+' mode is used to read and write data to a file. If the file does not exist, it will raise a FileNotFoundError. If the file exists, it allows you to read and write data to the file.

f.write("New")    #write() method is used to write data to the file
data=f.read() #read() method is used to read data from the file. It reads the entire file and returns it as a string.
print(data)
f.close() #close() method is used to close the file after reading and writing data to it. It is important to close the file to free up system resources and ensure that all data is properly saved to the file.