#Matthew Umana msu245

class Account:

    def __init__(self, account_num, balance):
        self.account_num = account_num
        self.balance = balance


    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def __str__(self):
        return "Acct #: " + str(self.account_num) + \
               "\nBalance: $" + str(format(self.balance, ".2f"))

def main():
    
    account1 = Account(123, 100)
    account2 = Account(456, 550)

    print(account1)
    print(account2)

    account1.deposit(5.25)
    account2.withdraw(3.27)

    print(account1)
    print(account2)

    weeks = 0

    while account1.balance < account2.balance:
        account1.deposit(10)
        account2.withdraw(7)
        weeks += 1
        
    print("Weeks =", weeks)
    print(account1)
    print(account2)

    
main()
        
