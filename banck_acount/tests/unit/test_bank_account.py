import pytest
from src.models.bank_account import BankAccount

def test_deposit():
    account = BankAccount("Amine", 100)

    account.deposit(50)

    assert account.balance == 150


def test_deposit_negative_amount():
    account = BankAccount("Amine", 100)

    with pytest.raises(ValueError):
        account.deposit(-50)