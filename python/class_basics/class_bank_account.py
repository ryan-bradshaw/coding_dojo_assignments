class BankAccount:
    all_accounts = []
    
    def __init__(self, account_name, balance, int_rate):
        self.account_name = account_name
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    @classmethod
    def display_all(cls, accounts):
        for account in accounts:
            account.account_info()
    
    @staticmethod
    def can_withdraw(balance, amount):
        if((balance - amount) > 0):
            return True
        else:
            return False

    def check_balance(self):
        print("The current balance of this account is: " + str(self.balance))
        return self

    def deposit(self, amount):
        self.balance += amount
        print("$" + str(amount) + " has been deposited to your account")
        self.check_balance()
        return self
    
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
            print("$" + str(amount) + " has been successfully withdrawn." )
            self.check_balance()
            return self

    def transfer(self, amount, target):
        if(BankAccount.can_withdraw(self.balance, amount)):
            self.balance -= amount
            target.deposit(amount)
            print("$" + str(amount) + "has been transferred to" + target.account_name)
            self.check_balance()
            return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        else:
            print("$0.00 balance cannot accrue interest")
        return self
    
    def account_info(self):
        print("Account Owner: " + self.account_name)
        print("Interest Rate: " + str(self.int_rate * 100)+"%")
        print("Current Balance: $" + str(self.balance))

ryan_account = BankAccount("Ryan", 0, 0.10)
brandi_account = BankAccount("Brandi", 0, 0.25)

ryan_account.account_info()

ryan_account.deposit(1000).deposit(2000).deposit(3000).withdraw(500).yield_interest().check_balance()

BankAccount.display_all(BankAccount.all_accounts)