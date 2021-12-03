class User:
    username = "Doe"
    balance = 0

    def __init__(self, name, amount = 0):
        self.username = name
        self.balance = amount 

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        rounded_balance = round(float(self.balance), 2)
        print(f"USER: {self.username}, BALANCE: {rounded_balance}")
    
    def transfer_money(self, user, amount):
        print(f"{self.username} transfer {amount} to {user.username}")
        self.make_withdrawl(amount)
        user.make_deposit(amount)

claire = User("Claire", 500)
josephine = User("Josephine", 30)
anaya = User("Anaya", 250)

claire.make_deposit(25).make_deposit(17.25).make_deposit(21.29).make_withdrawl(47).display_user_balance()

josephine.make_deposit(48).make_deposit(250000).make_withdrawl(249999).make_withdrawl(37).display_user_balance()

anaya.make_deposit(3500).make_withdrawl(45).make_withdrawl(74.99).make_withdrawl(258.33).display_user_balance()

claire.transfer_money(anaya, 300)
claire.display_user_balance()
anaya.display_user_balance()

