class BankAccount:

    def __init__(self, account_id, owner, balance=0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance

    def get_balance(self):
        return self.balance

    def get_account_info(self):
        return {
            "account_id": self.account_id,
            "owner": self.owner,
            "balance": self.balance
        }