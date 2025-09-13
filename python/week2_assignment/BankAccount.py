class Bank_Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

if ( __name__ == "__main__" ):
    account1 = Bank_Account("123456", "Alice", 1000)
    print(f"Account Holder: {account1.account_holder}")
    print(f"Initial Balance: ${account1.get_balance():.2f}")
    account1.deposit(500)
    print(f"Balance after deposit: ${account1.get_balance():.2f}")
    account1.withdraw(200)
    print(f"Balance after withdrawal: ${account1.get_balance():.2f}")           
        