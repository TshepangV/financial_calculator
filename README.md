# financial_calculator
-**When you run finance_calculators.py, it will prompt the user to choose between calculating an investment or a bond repayment.
Depending on the user's choice, it will execute the corresponding calculation function (calculate_investment() or calculate_bond()).
Invalid inputs are handled with appropriate error messages and recursive function calls (in the case of incorrect interest type selection).**

# Import Required Modules
-**Import the math module at the top of the file.**

# The Main Program Logic
-**Display a menu to the user to choose between 'investment' and 'bond'.
Handle user input to allow flexible casing (i.e., accept 'Investment', 'investment', etc.)**

#Investment Function
-**Prompt the user for deposit amount, interest rate, investment period, and interest type (simple or compound).
Perform the calculation based on the chosen interest type and display the result.**

#Bond Function
-**Prompt the user for house value, interest rate, and repayment period in months.
Calculate the monthly repayment amount using the provided formula and display the result.**

#Execute 
-**Call the main() function to start the program.**

#formulars
-**The total amount when  simple  interest  is  applied  is  calculated  as follows: A = P(1 + r * t)
The total amount when compound interest is applied is calculated as follows: A = P(1 + r) ^ t

●     ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
●     ‘P’ is the amount that the user deposits.
●     ‘t’ is the number of years that the money is being invested for.
●     ‘A’ is the total amount once the interest has been applied.**
