class BankAccount:
    all_accounts = []

    def __init__(self, int_rate = 0.0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${round(float(self.balance), 2)}")
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
        return self
    
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            print(f"Balance: ${round(float(account.balance), 2)}")


class User:

    def __init__(self, name, amount = 0, account_name = "checking"):
        self.username = name
        self.accounts = {}
        self.accounts[account_name] = BankAccount(0.0, amount)
    
    def open_account(self, amount, int_rate, account_name):
        if account_name in self.accounts:
            print(account_name, "already exist")
        else:
            self.accounts[account_name] = BankAccount(int_rate, amount)
    
    def close_account(self, account_name):
        if account_name not in self.accounts:
            print(account_name, "is not valid")
        elif account_name == "checking":
            print("checking is not supposed to be closed")
        else:
            del self.accounts[account_name]

    def make_deposit(self, amount, account_name = "checking"):
        # print(self.username, "make deposit before:")
        # self.display_user_balance()
        self.accounts[account_name].deposit(amount)
        # print(self.username, "make deposit after")
        # self.display_user_balance()
        return self

    def make_withdrawl(self, amount, account_name="checking"):
        # print(self.username, "make withdraw before:")
        # self.display_user_balance()
        self.accounts[account_name].withdraw(amount)
        # print(self.username, "make withdraw after:")
        # self.display_user_balance()
        return self
    
    def yield_interest(self):
        for account in self.accounts:
            self.accounts[account].yield_interest()
        return self

    def display_user_balance(self):
        for account in self.accounts:
            print(account+":")
            self.accounts[account].display_account_info()
    
    def transfer_money(self, user, amount, from_account_name="checking", to_account_name="checking"):
        print(f"{self.username} transfer {amount} to {user.username}")
        self.make_withdrawl(amount, from_account_name)
        user.make_deposit(amount, to_account_name)

claire = User("Claire", 500)
josephine = User("Josephine", 30)
anaya = User("Anaya", 250)

claire.make_deposit(25)
claire.make_deposit(17.25)
claire.make_deposit(21.29)
claire.make_withdrawl(47)
claire.display_user_balance()

josephine.make_deposit(48)
josephine.make_deposit(250000)
josephine.make_withdrawl(249999)
josephine.make_withdrawl(37)
josephine.display_user_balance()

anaya.make_deposit(3500)
anaya.make_withdrawl(45)
anaya.make_withdrawl(74.99)
anaya.make_withdrawl(258.33)
anaya.display_user_balance()

claire.transfer_money(anaya, 300)
claire.display_user_balance()
anaya.display_user_balance()

claire.open_account(300, 0.05, "savings")
#print("114 line")
claire.display_user_balance()
claire.make_deposit(3500, "savings")
#print("117")
claire.display_user_balance()
#print("119 yeild")
claire.yield_interest()
#print("212 after yeild")
claire.display_user_balance()
claire.yield_interest()
claire.display_user_balance()
claire.transfer_money(claire, 4189.5, "savings", "checking")
claire.display_user_balance()
claire.close_account("savings")
claire.display_user_balance()
claire.close_account("checking")
claire.close_account("checking2")
claire.display_user_balance()