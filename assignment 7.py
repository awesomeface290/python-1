'''
Assignment 7
Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.

===============================================
Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not.

'''

# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# Main function to get user input and determine if it's a leap year
def main():
    while True:
        try:
            year = int(input("Enter a year: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the year.")
    
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.") 
        
    # non-numeric imput error handling
if __name__ == "__main__":    main()    