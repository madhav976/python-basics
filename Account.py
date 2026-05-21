class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return "Transaction Successful"
        return "Insufficient Balance"

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)


account = SavingsAccount("Rahul", 10000, 5)

print(account.get_balance())

account.deposit(2000)
print(account.get_balance())

print(account.withdraw(5000))
print(account.get_balance())

account.add_interest()
print(account.get_balance())
