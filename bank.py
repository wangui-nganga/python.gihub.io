class Account:
    def __init__(self,account_number,account_name,balance=0):
        self.account_number = int(account_number)
        self.account_name = account_name
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance:{self.balance}"
        else:
            return"Deposit amount must be positive"

    def withdraw(self,amount):
        if amount > 0 <=self.balance:
            self.balance -= amount
            return f"Withdrawing {amount}. New balance:{self.balance}"
        else:
            return"Withdraw amount must be positive"

    def check_balance(self):
        return f"current balance:{self.balance}"


account1 = Account("657","Missy",20000)
account2 = Account("123","Sissy",100)
print(account1.check_balance())
print(account2.check_balance())
print(account1.deposit(500))
print(account2.withdraw(2000))
print(account1.withdraw(2000))
print(account1.withdraw(200))