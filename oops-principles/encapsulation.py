"""
The first class is a bad example, 
whereas the second class is a proper example using Encapsulation 

"""


class BankAccount:
    def __init__(self, balance: int):
        self.balance = balance


account = BankAccount(0)
account.balance = -1


class EncapsulatedBankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount >= self._balance or amount <= 0:
            raise ValueError("Invalid Withdraw Amount")
        self._balance -= amount


account_1 = EncapsulatedBankAccount()
account_1.deposit(1.99)
print(account_1.balance)
account_1.withdraw(1.0)
print(account_1.balance)
account_1.withdraw(100)
