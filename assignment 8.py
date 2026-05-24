'''
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.

=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:

    90 and above: A
    80-89: B
    70-79: C
    60-69: D
    Below 60: F

Output: Display the calculated grade.
'''

# ask the user to enter their marks for three subjects
subject1_input = input("Please enter your marks for subject 1 (0-100): ")
subject2_input = input("Please enter your marks for subject 2 (0-100): ")
subject3_input = input("Please enter your marks for subject 3 (0-100): ")

# implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject
if (subject1_input.isdigit() and 0 <= int(subject1_input) <= 100) and \
   (subject2_input.isdigit() and 0 <= int(subject2_input) <= 100) and \
   (subject3_input.isdigit() and 0 <= int(subject3_input) <= 100):
    marks = [int(subject1_input), int(subject2_input), int(subject3_input)]
    average = sum(marks) / len(marks)

    # determine the grade based on the average
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Your average marks are: {average:.2f}")
    print(f"Your grade is: {grade}")
else:
    print("Invalid input. Please enter valid marks (between 0 and 100) for each subject.") 
repeat = input("Do you want to try again? (yes/no): ") 
if repeat.lower() == "yes":
    # You can call the function or repeat the code block here to allow the user to enter marks again
    pass # Note: The 'pass' statement is a placeholder. You can replace it with the actual code to repeat the process.
else:    print("Thank you for using the grade calculator. Goodbye!")    