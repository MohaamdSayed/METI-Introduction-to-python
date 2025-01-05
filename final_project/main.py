import os
import json
from tabulate import tabulate
from datetime import datetime
from enum import Enum


class AccountType(Enum):
    SAVINGS = "Savings"
    CHECKING = "Checking"


class BankAccount:

    def __init__(self, account_holder_name: str, account_type: AccountType,
                 account_number: int, account_balance: float):
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.account_number = account_number
        self.account_balance = account_balance
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account_balance += amount
        self.transactions.append({
            "type":
            "Deposit",
            "amount":
            amount,
            "date":
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "balance_after":
            self.account_balance
        })

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.account_balance:
            raise ValueError("Insufficient funds.")
        self.account_balance -= amount
        self.transactions.append({
            "type":
            "Withdrawal",
            "amount":
            amount,
            "date":
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "balance_after":
            self.account_balance
        })

    def to_dict(self):
        return {
            "account_holder_name": self.account_holder_name,
            "account_type": self.account_type.value,
            "account_number": self.account_number,
            "account_balance": self.account_balance,
            "transactions": self.transactions
        }

    @staticmethod
    def from_dict(data):
        account = BankAccount(data["account_holder_name"],
                              AccountType(data["account_type"]),
                              data["account_number"], data["account_balance"])
        account.transactions = data["transactions"]
        return account


# File path configuration
current_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(current_file_path)
file_name = "accounts.json"
FILEPATH = os.path.join(current_file_dir, file_name)


# Functions to handle file operations
def write_data(accounts: list):
    with open(FILEPATH, "w") as file:
        json.dump([account.to_dict() for account in accounts], file, indent=4)


def read_data():
    if not os.path.exists(FILEPATH):
        return []
    with open(FILEPATH, "r") as file:
        data = json.load(file)
        return [BankAccount.from_dict(account) for account in data]


# Utility functions
def print_accounts(accounts: list):
    if not accounts:
        print("No accounts available.")
        return False
    rows = []
    for i, account in enumerate(accounts, 1):
        rows.append([
            i, account.account_holder_name, account.account_type.value,
            account.account_number, f"{account.account_balance:.2f}"
        ])
    table = tabulate(
        rows,
        headers=["Index", "Holder Name", "Type", "Account Number", "Balance"],
        tablefmt="fancy_grid",
        colalign=("center", "center", "center", "center", "center"
                  )  # Center-align all columns
    )
    print(table)
    return True


def add_account(accounts: list):
    try:
        name = input("Enter account holder name: ")
        if not name.strip():
            raise ValueError("Name cannot be empty.")

        account_type = input(
            f"Enter account type ({'/'.join(t.value for t in AccountType)}): ")
        if account_type not in [t.value for t in AccountType]:
            raise ValueError("Invalid account type.")

        number = int(input("Enter account number: "))
        if number <= 0:
            raise ValueError("Account number must be positive.")

        balance = float(input("Enter initial balance: "))
        if balance < 0:
            raise ValueError("Balance must be non-negative.")

        account = BankAccount(name, AccountType(account_type), number, balance)
        accounts.append(account)
        write_data(accounts)
        print("Account added successfully.")
    except Exception as e:
        print(f"Error: {e}")


def delete_account(accounts: list):
    if not print_accounts(accounts):
        return
    try:
        index = int(input("Enter the index of the account to delete: ")) - 1
        if index < 0 or index >= len(accounts):
            raise IndexError("Invalid index.")
        deleted = accounts.pop(index)
        write_data(accounts)
        print(f"Account '{deleted.account_holder_name}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")


def deposit_to_account(accounts: list):
    if not print_accounts(accounts):
        return
    try:
        index = int(
            input("Enter the index of the account to deposit into: ")) - 1
        if index < 0 or index >= len(accounts):
            raise IndexError("Invalid index.")
        amount = float(input("Enter the amount to deposit: "))
        accounts[index].deposit(amount)
        write_data(accounts)
        print("Deposit successful.")
    except Exception as e:
        print(f"Error: {e}")


def withdraw_from_account(accounts: list):
    if not print_accounts(accounts):
        return
    try:
        index = int(
            input("Enter the index of the account to withdraw from: ")) - 1
        if index < 0 or index >= len(accounts):
            raise IndexError("Invalid index.")
        amount = float(input("Enter the amount to withdraw: "))
        accounts[index].withdraw(amount)
        write_data(accounts)
        print("Withdrawal successful.")
    except Exception as e:
        print(f"Error: {e}")


# Main menu
def main():
    accounts = read_data()
    while True:
        print("1. Add Account")
        print("2. Delete Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. View Accounts")
        print("6. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                add_account(accounts)
            case "2":
                delete_account(accounts)
            case "3":
                deposit_to_account(accounts)
            case "4":
                withdraw_from_account(accounts)
            case "5":
                print_accounts(accounts)
            case "6":
                print("Exiting...")
                break
            case _:
                print("Invalid choice.")
        print("\n")


if __name__ == "__main__":
    main()
