#!/usr/bin/python3

class BankAccount:
    """
    A class representing a Bank Account
    """

    def __init__(self, account_number: int, owner: str, balance: float) -> None:
        if account_number > 0:
            self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        if amount >= 0:
            self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        if amount <= self.balance and amount >= 0:
            self.balance -= amount
        else:
            print("Withdrawal Error: Invalid Amount")
    
    def get_balance(self) -> float:
        return self.balance
    
    def transfer(self, amount: float, destination: 'BankAccount') -> None:
        if amount <= self.balance and amount >= 0:
            self.balance -= amount
            destination.deposit(amount)
        else:
            print("Transfer Error: Invalid Amount")


account1 = BankAccount(1234567890, "John Smith", 1000.0)
account2 = BankAccount(2345678901, "Jane Doe", 500.0)

account1.deposit(200.0)
assert account1.get_balance() == 1200.0

account1.withdraw(300.0)
assert account1.get_balance() == 900.0

account1.transfer(500.0, account2)
assert account1.get_balance() == 400.0
assert account2.get_balance() == 1000.0

account1.withdraw(1000.0) # Withdrawal Error: Invalid Amount
assert account1.get_balance() == 400.0
