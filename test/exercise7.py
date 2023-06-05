# Write a Python class called BankAccount with methods for depositin,
# withdrawing and checkin the account balance.


class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Welcome to Team-International Bank")
    #Metodo para despositar
    def deposit(self):
        amount=float(input("Enter amount for deposit"))
        self.balance += amount
        print("\n Amount deposited is :",amount)
    #Metodo para extraer
    def withdraw(self):
        amount = float(input("Enter amount to retired"))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You retire:",amount)
        else:
            print("\n Insufficiente money in account.")
    
    def display(self):
        print("\n Money Avaible in account is: ", self.balance)


test_account = Bank_Account()

test_account.deposit()
test_account.display()
