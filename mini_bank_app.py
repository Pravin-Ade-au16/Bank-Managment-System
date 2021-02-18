# Mini project
# Banking application
"""
i used Hierarchical inheritance to develop mini bank project
 Hierarchical inheritance - means inheriting properties from one class to multiple class
 which are present in same level
"""
class account:
    """ static variable - which is not vary object to object"""
    bank_name = "ADE Bank, Vitthalwadi"
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount): # instance method
        self.balance += amount

    def withdraw(self, amount):
        if self.balance-amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry,Insufficient Funds")

    def printStatement(self):
        print("Account Balance:", self.balance)

class current(account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)
    def __str__(self):
        return "{}'s Current Account with Balance:{}".format(self.name, self.balance, self.min_balance)

class saving(account):
    def __init__(self, name, balance):
        super()\
            .__init__(name, balance, min_balance=0)
    def __str__(self):
        return "{}'s saving account with Balance:{}".format(self.name, self.balance, self.min_balance)

print("Welcome to", account.bank_name)
c = saving("Pravin", 10000)
print(c)
c.deposit(5000)
c.printStatement()
c.withdraw(16000)
c.withdraw(15000)
print(c)



