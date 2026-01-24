uname=input("Enter the username: ")
password=input("Enter the password:")

if(uname=='admin' and password=='admin'):
    print('Login Successfull')
else:
    if(uname!='admin'):
        print("Wrong Username")
    else:
        print('Wrong Password')