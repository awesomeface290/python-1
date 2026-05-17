'''
from unicodedata import numeric


Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.


=============================

Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).

Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.

Output: Display the calculated simple interest.
'''


# prompt the user to enter the principal amount, interest rate, and time period 

principal = float(input("Enter the principal amount: ")) 
rate_imput = input("Enter the interest rate (in percentage): ")
rate = float(rate_imput)
time = float(input("Enter the time period (in years): "))


#calculate the simple interest below

simple_interest = (principal * rate * time) / 100

#display the output below

print("The simple interest is: ", simple_interest)