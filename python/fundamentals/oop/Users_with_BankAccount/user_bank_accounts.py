class BankAccount:
    int_rate = 0.0
    balance = 0
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
    username = "Doe"
    account = None

    def __init__(self, name, amount = 0):
        self.username = name
        self.account = BankAccount(0.0, amount)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
    
    def transfer_money(self, user, amount):
        print(f"{self.username} transfer {amount} to {user.username}")
        self.make_withdrawl(amount)
        user.make_deposit(amount)

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

