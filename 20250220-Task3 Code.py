class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Php{amount}. \nNew balance: Php{self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew Php{amount}. \nNew balance: Php{self.balance}")
    
    def display_balance(self):
        print(f"Account Balance: Php{self.balance}")

# Creating a bank account and performing transactions
account = BankAccount("010203040506", "Christianly Leuterio", 5000)
account.display_balance()
account.deposit(1000)
account.withdraw(3000)
account.withdraw(3500)
account.display_balance()