# Bank Account System

A simple Python program that simulates basic bank account operations using object-oriented programming — deposits, withdrawals, balance checks, and account profile display.

## Features
- Create an account with holder name, account number, and starting balance
- Deposit funds (with a minimum deposit check)
- Withdraw funds (with a basic validation check)
- Check current balance
- Display full account profile info

## How It Works
The `bank_account` class models a bank account with:
- `deposit(amount)` – adds funds to the balance
- `withdraw(amount)` – removes funds from the balance
- `check_balance()` – prints the current balance
- `profile_info()` – prints the account holder's name, account number, and balance

## Usage
```
python bank_account.py
```
Example output:
ACCOUNT BALANCE: 5000
deposit amount: 3000
Current amount:8000
withdraw amount: 1000
Current amount: 7000
Current balance is 7000

===== Account Info =====
account name: mahadeer
account number: 12345678
balance: 7000


## Requirements
- Python 3.x (no external libraries needed)

## Possible Improvements
- Fix the `deposit()` check — currently it *rejects* deposits of 500 or less, which reads more like a minimum deposit rule than a balance check; the message text could be clearer
- Add a check in `withdraw()` to prevent withdrawing more than the current balance
- Rename the class to `BankAccount` (PascalCase) to follow Python naming conventions
- Add transaction history logging
- Add multiple account support instead of one hardcoded account

