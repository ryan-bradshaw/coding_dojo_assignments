#----------------------------------------------------------------------
#       User Class
#----------------------------------------------------------------------
class User:

    all_users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.all_users.append(self)
        self.accounts = {}
    
    def show_accounts(self):
        for account in self.accounts:
            print(account)
    
    def new_account(self, account_name):
        self.accounts[account_name] = BankAccount(0, int_rate = 0.10)
        return self
    
    def withdraw_funds(self, account_name, amount):
        self.accounts[account_name].withdraw(amount)
        return self

    def deposit_funds(self, account_name, amount):
        self.accounts[account_name].deposit(amount)
        return self

    def transfer_funds(self, account_name, amount, target):
        self.accounts[account_name].transfer(amount, target)
        return self

    def account_balance(self, account_name):
        self.accounts[account_name].account_info()
        return self
#----------------------------------------------------------------------
#       BankAccount Class
#----------------------------------------------------------------------
class BankAccount:

    all_accounts = []

    def __init__(self, balance = 0, int_rate= 0.10):
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
            print("$" + str(amount) + " has been successfully withdrawn.")
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
        # print("Account: " + self.account_name)
        print("Interest Rate: " + str(self.int_rate * 100)+"%")
        print("Current Balance: $" + str(self.balance))
#----------------------------------------------------------------------
#       TESTING
#----------------------------------------------------------------------
ryan = User("Ryan", "ryan@testing.com")
ryan.new_account("checking")
# print(ryan.accounts["checking"].check_balance())
ryan.deposit_funds("checking", 1000)
ryan.account_balance("checking")
