# main.py
from Bankaccountwithclasses import BankAccount, SavingsAccount, CheckingAccount

def chatbot():
    account = BankAccount(account_number="923877")  # To start the bank account with a balance of 0
    print ('Hello! I am your personal chatbot here to help you manage your bank account')
    print('Hello! I am your personal banking chatbot here to help you manage your bank account.')
    
    # Let the user choose account type
    account_type = input("Would you like a new 'savings' or 'checking' account? ").strip().lower()
    
    if account_type == 'savings':
        interest_rate = float(input("Enter the interest rate for your Savings Account (e.g., 5 for 5%): "))
        account = SavingsAccount(account_number="HOHOHO", interest_rate=interest_rate)
        print(f"Savings Account created with an interest rate of {interest_rate}%.")

    elif account_type == 'checking':
        overdraft_limit = float(input("Enter the overdraft limit for your Checking Account (e.g., 300 for £300): "))
        account = CheckingAccount(account_number="HEHEHE", overdraft_limit=overdraft_limit)
        print(f"Checking Account created with an overdraft limit of £{overdraft_limit}.")

    else:
        print("Invalid account type. Please restart the chatbot and choose either 'savings' or 'checking'.")
        return

    # Chatbot interaction loop
    while True:
        print("\nHow may I assist you?")
        print("Available options: 'balance', 'deposit', 'withdraw', 'calculate interest' (Savings only), 'exit'")
        user_input = input("Enter your preferred action: ").strip().lower()

        # Option for balance
        if user_input == 'balance':
            print(f"Current balance: £{account.get_balance()}")

        # Option for deposit
        elif user_input == 'deposit':
            amount = input("Enter the amount you would like to deposit (no symbols like £ or $): ")
            if amount.replace('.', '', 1).isdigit():
                account.deposit(float(amount))
            else:
                print("Invalid input. Please enter a positive number.")

        # Option for withdraw
        elif user_input == 'withdraw':
            amount = input("Enter the amount you would like to withdraw (no symbols like £ or $): ")
            if amount.replace('.', '', 1).isdigit():
                account.withdraw(float(amount))
            else:
                print("Invalid input. Please enter a positive number.")


        # Option for calculating interest
        elif user_input == 'calculate interest' and isinstance(account, SavingsAccount):
            time_in_years = input("Enter the number of years to calculate interest for: ")
            if time_in_years.isdigit():
                account.calculate_interest(int(time_in_years))
            else:
                print("Invalid input. Please enter a positive integer.")

        # Option for exit
        elif user_input == 'exit':
            print("Thank you for using our services. Goodbye!")
            break

        # Otherwise invalid option
        else:
            print("Invalid option. Please choose 'balance', 'deposit', 'withdraw', 'calculate interest', or 'exit'.")

if __name__ == "__main__":
    chatbot()
