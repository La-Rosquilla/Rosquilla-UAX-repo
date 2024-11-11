class BankAccount:

    def __init__(self, account_number):   # The bank account must start with a unique number and a default balance of 0
        self.account_number = account_number
        self.balance = 0  

    def deposit(self, amount):   # A way to deposit money into the account
        if amount > 0:
            self.balance += amount
            print(f"Deposited: £{amount}. New balance: £{self.balance}.")
        else:
            print("Deposited amount has to be greater than 0.")

    def withdraw(self, amount):   # A method to withdraw money from teh account
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Amount Withdrawn: £{amount}. New balance: £{self.balance}.")
            else:
                print("Not enough funds to withdraw that amount.")
        else:
            print("Withdrawal amount must be a positive number.")

    def get_balance(self):  # Shoes the current balance in the account
        return self.balance

    def __str__(self):      # Return a string representation of the bank account
        return f"Bank Account {self.account_number} - Balance: £{self.balance}"


if __name__ == "__main__":
    account = BankAccount("923877")  # Create an account number ("923877")
    print(account)  # Account details must be printed
    
    account.deposit(500)  # An attempt to deposit £500
    account.withdraw(300)  # An attempt to withdraw £300
    print(f"Final balance: £{account.get_balance()}")  # Display of the final balance
