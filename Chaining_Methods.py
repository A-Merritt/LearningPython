class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def withdrawal_money(self, amount):
        self.account_balance -= amount
        return self
    def user_balance(self):
        print(f'User: {self.name}, Balance: ${self.account_balance}')
        return self
    def transfer_money(self, other_user, amount):
        self.withdrawal_money(amount)
        other_user.make_deposit(amount)
        return self

Austin = user("Austin", "merritaj@gmail.com")
Emily = user("Emily", "Emily@email.com")
Everly = user("Everly", "Everly@email.com")

Austin.make_deposit(100).make_deposit(200).make_deposit(10).withdrawal_money(100).user_balance()

Emily.make_deposit(400).make_deposit(200).withdrawal_money(30).withdrawal_money(5).user_balance()

Everly.make_deposit(1000).withdrawal_money(100).withdrawal_money(500).withdrawal_money(10).user_balance()

Austin.transfer_money(Emily,20).user_balance()
Emily.user_balance()