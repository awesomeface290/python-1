'''
Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.

=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
'''

while True:
    char_input = input("Please input a single character: ")

    if len(char_input) == 1 and char_input.isalpha():
        char = char_input.lower()
        if char in 'aeiou':
            print(f"The character '{char_input}' is a vowel.")
        else:
            print(f"The character '{char_input}' is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabet letter.")
        continue

    repeat = input("Do you want to try again? (yes/no): ").strip().lower()
    if repeat != 'yes':
        break
    if repeat == 'no':
        print("Thank you for using the program. Goodbye!")
        break
    
    else: 
        
        if len(char_input) != 1:
            print("Invalid input. Please enter only a single character.") 
            
        else:
            print("Invalid input. Please enter a letter.") 