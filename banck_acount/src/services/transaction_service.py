from src.models.transaction import Transaction


class TransactionService:

    def __init__(self):
        self.transactions = []

    def deposit(self, account, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        account.balance += amount

        transaction = Transaction("DEPOSIT", amount)

        self.transactions.append(transaction)

        return account.balance

    def withdraw(self, account, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if account.balance < amount:
            raise ValueError("Insufficient balance")

        account.balance -= amount

        transaction = Transaction("WITHDRAW", amount)

        self.transactions.append(transaction)

        return account.balance

    def get_history(self):
        return self.transactions