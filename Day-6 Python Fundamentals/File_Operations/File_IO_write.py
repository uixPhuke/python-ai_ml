f=open("sampleWrite.txt","w") #'w' mode is used to write data to a file. If the file already exists, it will be overwritten. If the file does not exist, it will be created.
f.write("Hello, this is a sample text file.\n and me phuke ")   #write() method is used to write data to the file

f.close() #close() method is used to close the file after writing data to it. It is important to close the file to free up system resources and ensure that all data is properly saved to the file.