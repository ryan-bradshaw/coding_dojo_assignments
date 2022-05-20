class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def current_balance(self):
        print(self.name +"'s current balance is : $" + str(self.account_balance))
        return self
    
    def make_deposit(self, amount):
        self.account_balance += amount
        print("$" + str(self.account_balance) + " has been deposited")
        self.current_balance()
        return self

    def make_withdrawal(self, amount):
        if(amount > self.account_balance):
            print("Insufficient Funds for that Withdrawal")
            self.current_balance()
            return self
        else:
            self.account_balance -= amount
            self.current_balance()
            return self

    def make_transfer(self, amount, recipient):
        if(amount > self.account_balance):
            print("Insufficient Funds for that Withdrawal")
            self.current_balance()
            return self
        if(amount < 0):
            print("Transfers must be only in positive amounts")
            return self
        else:
            self.make_withdrawal(amount)
            recipient.account_balance += amount
            print("$" + str(amount) + " has been transferred to " + recipient.name)
            return self
#-----------------------------------------
ryan = User("Ryan")
brad = User("Brad")
spencer = User("Spencer")
#-----------------------------------------
ryan.make_deposit(1000)
ryan.make_deposit(2000)
ryan.make_deposit(10000)
ryan.make_withdrawal(500)
ryan.current_balance()

brad.make_deposit(5000)
brad.make_deposit(10000)
brad.make_withdrawal(300)
brad.current_balance()

spencer.make_deposit(99999)
spencer.make_withdrawal(11111)
spencer.make_withdrawal(22222)
spencer.make_withdrawal(33333)

ryan.make_transfer(5, spencer)
ryan.current_balance()
spencer.current_balance()