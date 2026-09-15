class bank_account():
    def __init__(self,account_holder_name,account_number,balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance


        print(f"ACCOUNT BALANCE: {self.balance}")

        print()

    def deposit(self,amount):
        if amount <= 500:
            print("account balance less than 500")
            return
        self.balance += amount
        print(f"deposit amount: {amount}")
        print(f" Current amount:{self.balance}")

        print()

    def withdraw(self,amount):
        if amount <= 0:
            print("account balance less than 0")
            return
        self.balance -= amount
        print(f"withdraw amount: {amount}")
        print(f"Current amount: {self.balance}")

        print()

    def check_balance(self):
        print(f"Current balance is {self.balance}")

    print()

    def profile_info(self):
        print(f"account name: {self.account_holder_name}")
        print(f"account number: {self.account_number}")
        print(f"balance: {self.balance}")



b=bank_account("mahadeer",12345678,5000)
b.deposit(3000)
b.withdraw(1000)
b.check_balance()
print()
print("===== Account Info =====")
b.profile_info()