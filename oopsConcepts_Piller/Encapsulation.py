class Bank_Account:
    def __init__(self,name,balance,secretKey,cvv):
        self.name=name
        self.balance=balance #public acess
        self._secretKey=secretKey #protected
        self.__cvv=cvv #private --Data Magling

acc1=Bank_Account("Phuke",150_000,999,666)

print(acc1.name, acc1.balance)
print(acc1._secretKey)
print(acc1.__cvv)