import numpy as np
import matplotlib.pyplot as plt

#Function to calculate the monthly payment
def calculate_monthly_payment(principal, annual_interest_rate, loan_term_months):
    # Convert annual interest rate to monthly and make it a decimal
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / \
                      ((1 + monthly_interest_rate) ** loan_term_months - 1)
    return monthly_payment

#Function to calculate the loan balance over time
def calculate_loan_balance(principal, monthly_payment, monthly_interest_rate, loan_term_months):
    balance_list = []
    balance = principal
    for month in range(loan_term_months):
        interest_for_month = balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_for_month
        balance -= principal_payment
        balance_list.append(balance if balance > 0 else 0)
    return balance_list

#Data to enter on Loan amount, annual interest rate, and loan term in months
principal = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
loan_term_months = int(input("Enter the loan term (in months): "))

#Calculation of the monthly payment
monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, loan_term_months)

#Calculation of the monthly interest rate
monthly_interest_rate = (annual_interest_rate / 100) / 12

#Calculate loan balance over time
balance_list = calculate_loan_balance(principal, monthly_payment, monthly_interest_rate, loan_term_months)

#Display of monthly payment
print(f"Your monthly payment is: ${monthly_payment:.2f}")

#Graph of the loan balance over time
months = np.arange(1, loan_term_months + 1)
plt.plot(months, balance_list, label='Loan Balance')
plt.title('Loan Balance Over Time')
plt.xlabel('Month')
plt.ylabel('Balance ($)')
plt.grid(True)
plt.legend()
plt.show()