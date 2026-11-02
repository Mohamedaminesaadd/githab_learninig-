from src.models.bank_account import BankAccount


class AccountService:

    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, owner, balance=0):

        if account_id in self.accounts:
            raise ValueError("Account already exists")

        account = BankAccount(account_id, owner, balance)

        self.accounts[account_id] = account

        return account

    def get_account(self, account_id):

        if account_id not in self.accounts:
            raise ValueError("Account not found")

        return self.accounts[account_id]