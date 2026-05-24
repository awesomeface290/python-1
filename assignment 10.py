'''
Challenge: Implement error handling to ensure that the user enters a positive integer for the age.

==================================
Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:

    Under 18: Minor
    18-65: Adult
    Above 65: Senior citizen

Output: Display the category based on the entered age.

'''

# ask the user to enter their age
age_input = input("Please enter your age: ") 

# implement error handling to ensure that the user enters a positive integer for the age
if age_input.isdigit() and int(age_input) > 0:
    age = int(age_input)
    
    # classify the age into different categories
    if age < 18:
        print("You are a Minor.")
    elif 18 <= age <= 65:
        print("You are an Adult.")
    else:
        print("You are a Senior citizen.")
        
else:
    print("Invalid input. Please enter a positive integer for the age.") 
    
repeat = input("Do you want to try again? (yes/no): ")
if repeat.lower() == "yes":
    # ask the user to enter their age again
    age_input = input("Please enter your age: ") 

    # implement error handling to ensure that the user enters a positive integer for the age
    if age_input.isdigit() and int(age_input) > 0:
        age = int(age_input)
        
        # classify the age into different categories
        if age < 18:
            print("You are a Minor.")
        elif 18 <= age <= 65:
            print("You are an Adult.")
        else:
            print("You are a Senior citizen.")
            
    else:
        print("Invalid input. Please enter a positive integer for the age.") 
if not repeat.lower() == "yes":
    print("Thank you for using the age classifier. Goodbye!")   
    
    