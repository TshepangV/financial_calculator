#Reviewed By Toufique Mahlangu on 09-July-2024
import math
def main():
    print("Welcome to the Financial(bond and investment) Calculator program!")
    print("Choose either 'investment' or 'bond' from the menu below:")
    print("1. Investment")
    print("2. Bond")
    
    choice = input("Please enter your selection(1 or 2): ").strip().lower()
    
    if choice == '1':
        investment()
    elif choice == '2':
        calculate_bond()
    else:
        print("Invalid input. Please enter 'investment' or 'bond'.")
        main()


def investment():
    amount = float(input("Enter the amount of money you are depositing: "))

    rate = float(input("Enter the interest rate-use two decimals: ")) / 100
    period = int(input("Enter the number of years you plan to invest for: "))
    
    type = input("Do you want 'simple' or 'compound' interest? ").strip().lower()
    
    if type == 'simple':
        total_amount = amount * (1 + rate * period)
    elif type == 'compound':
        total_amount = amount * math.pow((1 + rate), period)
    else:
        print("Invalid input. Please enter 'simple' or 'compound'.")
        investment()
        return
    
    print(f"Your investment will be worth R {total_amount:.2f} after {period} years.")


def calculate_bond():
    house_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the interest rate: ")) / 100
    months = int(input("Enter the number of months to repay the bond: "))
    
    monthly_interest_rate = rate / 12
    
    monthly_repayment = (monthly_interest_rate * house_value) / (1 - math.pow((1 + monthly_interest_rate), -months))
    
    print(f"You will have to repay R {monthly_repayment:.2f} per month for {months} months.")
    
if __name__ == "__main__":
    main()
