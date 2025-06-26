class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("Credit", amount)
        else:
            print("Deposit amount must be greater than 0")

    def _is_valid_amount(self, amount):
        return amount >= 0

    def __log_transaction(self, transaction_type, amount):
        print(
            f"Logging {transaction_type} of ${amount}. New Balance is ${self._balance}"
        )

    @staticmethod
    def is_valid_interest_rate(rate: int):
        if rate >= 0 and rate <= 5:
            return True
        return False


account = BankAccount("Alice", 500)
account.deposit(200)

# account.__log_transaction("withdraw", 300)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))
