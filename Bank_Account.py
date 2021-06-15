class BankAccount:
	def __init__(self, name, interest_rate, balance): 
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
	def yield_interest(self):
		if self.account_balance > 0:
			self.account_balance = self.account_balance + (self.account_balance * self.interest_rate)
			print (f"You new balance after interest is {self.account_balance}!")
			return self

Austin = BankAccount("Austin", 0.025, 100)
Emily = BankAccount("Emily", 0.05, 100)

Austin.deposit(100).deposit(200).deposit(10).withdraw(100).yield_interest().display_account_info()
Emily.deposit(2000).deposit(3000).withdraw(300).withdraw(100).withdraw(200).withdraw(50).yield_interest().display_account_info()