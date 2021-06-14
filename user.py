class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def withdrawal_money(self, amount):
        self.account_balance -= amount
    def user_balance(self):
        print(f'User: {self.name}, Balance: ${self.account_balance}')
    def transfer_money(self, other_user, amount):
        self.withdrawal_money(amount)
        other_user.make_deposit(amount)

Austin = user("Austin", "merritaj@gmail.com")
Emily = user("Emily", "Emily@email.com")
Everly = user("Everly", "Everly@email.com")

Austin.make_deposit(100)
Austin.make_deposit(200)
Austin.make_deposit(10)
Austin.withdrawal_money(100)
Austin.user_balance()

Emily.make_deposit(400)
Emily.make_deposit(200)
Emily.withdrawal_money(30)
Emily.withdrawal_money(5)
Emily.user_balance()

Everly.make_deposit(1000)
Everly.withdrawal_money(100)
Everly.withdrawal_money(500)
Everly.withdrawal_money(10)
Everly.user_balance()

Austin.transfer_money(Emily,20)
Austin.user_balance()
Emily.user_balance()



# def transfer_money(self, other_user, amount)