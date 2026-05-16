with open("sample.txt","r") as f: #with statement is used to open the file and automatically close it after the block of code is executed. It is a good practice to use with statement when working with files to ensure that the file is properly closed even if an error occurs.
    data=f.read()
    print(data)
    print(type(data))
    print(len(data))

