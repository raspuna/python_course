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


ann = BankAccount(0.01, 250)
ben = BankAccount(0.02, 3000)

ann.deposit(10).deposit(20).deposit(30).withdraw(35).yield_interest().display_account_info()
ben.deposit(2500).deposit(10).withdraw(1100).withdraw(175).withdraw(643.5).withdraw(444).yield_interest().display_account_info()


BankAccount.all_balances()


