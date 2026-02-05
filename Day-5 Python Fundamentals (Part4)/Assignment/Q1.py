#Q1. Create a class with attributes account BankAccount

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

# Create an object of BankAccount
account1 = BankAccount(101, "Raj", 5000)

account1.deposit(2000)
account1.withdraw(1500)
account1.check_balance()
