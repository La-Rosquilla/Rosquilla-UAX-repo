# main.py
from banklibrary import BankAccount

def chatbot():
    account = BankAccount(account_number="923877")  # To start the bank account with a balance of 0
    print ('Hello! I am your personal chatbot here to help you manage your bank account')
    
    while True:
        print("\nHow may I be of aid?")
        print("The options availbale I can manage are: 'balance', 'deposit', 'withdraw'")
        user_input = input("Enter your preferred course of action: ").strip().lower()

        if user_input == 'balance': # If the user imputs 'balance', we must print the balance in the account
            print(account.get_balance())

        elif user_input == 'deposit': # If the user imputs 'deposit', we must create a small porgram for the user to add money
                amount = (input("Please enter the amount in pound sterling you would like to deposit (do not add special charcaters such as £, $, €): "))
                
                if amount.replace('.', '', 1).isdigit():  # A check for a valid numerical input
                    print(account.deposit(float(amount)))
                else:
                    print("Invalid input. Please enter a positive number.")

        elif user_input == 'withdraw': # If the user imputs 'withdraw', we must create a small porgram for the user to take out money
            amount = (input("Enter the amount in pound sterling you would like to withdraw (do not add special charcaters such as £, $, €): "))
            if amount.replace('.', '', 1).isdigit():  # A check for a valid numerical input
                print(account.withdraw(float(amount)))
            else:
                print("Invalid input. Please enter a positive number.")

        else:
            print("Invalid option. Please choose 'balance', 'deposit', 'withdraw', or 'exit'.")

if __name__ == "__main__":
    chatbot()