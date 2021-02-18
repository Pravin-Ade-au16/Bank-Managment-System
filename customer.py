import sys
class Customer:
    """customer class with bank application"""
    bank_name ="ADE Bank,(Ade Bank Bank) Vitthalwadi"
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Balance After Deposit:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds....can't perform this operation")
            sys.exit() # exist without existing rest of program
        self.balance = self.balance-amount
        print("Balance After Deposit:", self.balance)

print(" Welcome to ", Customer. bank_name) # static variable calling using class name
name = input("Enter Your Name:")
c = Customer(name)
while True:
    print("d-Deposit \nw-Withdraw \ne-exist")
    option = input("Choose your option:")
    if option == "d" or option == "D":
        amount = float(input("Enter Amount:"))
        c.deposit(amount) # method deposit calling ref var c and deposit method

    elif option == "w" or option == "W":
        amount = float(input("Enter Amount:"))
        c.withdraw(amount) # calling withdraw method

    elif option == "e" or option == "E":
        print("Thanks for Banking...have a good day!!")
        sys.exit() # means exist system without executing rest of the program.

    else:
        print("Invalid option...please choose valid option")