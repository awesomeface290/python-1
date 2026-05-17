'''
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.

=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle to the user. 
''' 

# Get user input for length and width

input_length = input("Enter the length of the rectangle: ")
input_width = input("Enter the width of the rectangle: ")  

# Convert the input to float and handle potential errors
try:
    length = float(input_length)
    width = float(input_width)

    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

    area = length * width
    print(f"The area of the rectangle is: {area}")
except ValueError as e:
    print("Invalid input:", e)


processing = "Calculate the area of the rectangle using the formula: Area = Length * Width."
print(processing)   

output = "Display the calculated area of the rectangle to the user."
print(output)   

error_handling = "Implement error handling to ensure that the length and width entered by the user are positive numbers."
print(error_handling)