import pytest

from src.services.account_service import AccountService


def test_create_account():

    service = AccountService()

    account = service.create_account("001", "Amine", 100)

    assert account.owner == "Amine"
    assert account.balance == 100


def test_get_account():

    service = AccountService()

    service.create_account("001", "Amine", 100)

    account = service.get_account("001")

    assert account.account_id == "001"


def test_duplicate_account():

    service = AccountService()

    service.create_account("001", "Amine", 100)

    with pytest.raises(ValueError):
        service.create_account("001", "Amine", 200)