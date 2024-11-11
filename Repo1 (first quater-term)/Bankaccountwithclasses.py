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

    def withdraw(self, amount):   # A method to withdraw money from the account
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Amount Withdrawn: £{amount}. New balance: £{self.balance}.")
            else:
                print("Not enough funds to withdraw that amount.")
        else:
            print("Withdrawal amount must be a positive number.")

    def get_balance(self):  # Shows the current balance in the account
        return self.balance

    def __str__(self):      # Return a string representation of the bank account
        return f"Bank Account {self.account_number} - Balance: £{self.balance}"


# A savings account as a child class 
class SavingsAccount(BankAccount):
    def __init__(self, account_number, interest_rate):
        super().__init__(account_number)
        self.interest_rate = interest_rate  # The Interest rate in percentage

    # To calculate the interest generated over a period of time
    def calculate_interest(self, time_in_years):
        interest_generated = self.balance * (self.interest_rate / 100) * time_in_years
        print(f"Interest generated over {time_in_years} years at {self.interest_rate}%: £{interest_generated:.2f}")
        return interest_generated

    def __str__(self):
        return f"Savings Account {self.account_number} - Balance: £{self.balance}, Interest Rate: {self.interest_rate}%"


# A checking account as a child class 
class CheckingAccount(BankAccount):
    def __init__(self, account_number, overdraft_limit):
        super().__init__(account_number)
        self.overdraft_limit = overdraft_limit  # Allows the balance to become negative up to this limit

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f"Amount Withdrawn: £{amount}. New balance: £{self.balance}.")
            else:
                print("Withdrawal amount exceeds overdraft limit.")
        else:
            print("Withdrawal amount must be a positive number.")

    def __str__(self):
        return f"Checking Account {self.account_number} - Balance: £{self.balance}, Overdraft Limit: £{self.overdraft_limit}"


# An example
if __name__ == "__main__":
    # Creating a Savings Account with an interest rate of 5%
    savings_account = SavingsAccount("HOHOHO", 5)
    print(savings_account)
    savings_account.deposit(1000)
    savings_account.calculate_interest(2)  # Calculate the interest for a time of 2 years

    # Creating a Checking Account with an overdraft limit of £300
    checking_account = CheckingAccount("HEHEHE", 300)
    print(checking_account)
    checking_account.deposit(500)
    checking_account.withdraw(650)  # Should be allowed because it’s within the overdraft limit
    checking_account.withdraw(100)  # This would exceed the overdraft limit
    print(f"Final balance in Checking Account: £{checking_account.get_balance()}")