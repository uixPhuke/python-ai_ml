class BankAccount:
    def __init__(self,name,balance,secretKey,cvv,atmPIN):
        self.name=name
        self.balance=balance #public acess
        self._secretKey=secretKey #protected
        self.__cvv=cvv #private --Data Magling
        self.__atmPIN=atmPIN

    def get_Cvv(self): #getter
            return self.__cvv
    
    def set_Cvv(self,newCvv):  #Setter--->to set new Value
         self.__cvv=newCvv

acc1=BankAccount("Phuke",150_000,999,666,808)

print(acc1.name, acc1.balance)
print(acc1._secretKey)
#print(acc1.__cvv) Not possible to access outside the class
acc1.set_Cvv(292)#new Cvv Assigned
print(acc1.get_Cvv())#getter

#one more method is there to access private data
print(acc1._BankAccount__atmPIN)




#