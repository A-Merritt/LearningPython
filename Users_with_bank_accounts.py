class BankAccount:
	def __init__(self, name, interest_rate, balance = 0): 
        self.name = name
        self.interest_rate = interest_rate
        self.account_balance = balance
    def deposit(self, amount):
		self.account_balance += amount
		return self
	def withdraw(self, amount):
		self.account_balance -= amount
		return self
	def display_account_info(self):
		print(f'User: {self.name}, Balance: ${self.account_balance}')
		return self
    def transfer_money(self, other_user, amount):
        self.withdraw(amount)
        other_user.deposit(amount)
	def yield_interest(self):
		if self.account_balance > 0:
			self.account_balance = self.account_balance + (self.account_balance * self.interest_rate)
			print (f"You new balance after interest is {self.account_balance}!")
			return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(name, interest_rate=0.02, balance=0)
    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def display_account_info(self):
        self.account.display_account_info()
        return self
    def transfer_money(self, other_user, amount):
        self.account.transfer_money(self, other_user, amount)
        return self
    def yield_interest(self):
		self.account.yield_interest(self)
        return self

Austin = User("Austin", "austin@email.com")
Austin.deposit(100).withdraw(40).display_account_info()
Austin.account.yield_interest().display_account_info()
Austin.deposit(300)
Austin.display_account_info()
Austin.account.yield_interest().display_account_info()



	