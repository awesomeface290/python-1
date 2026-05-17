'''
Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.

============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
'''

import math

def get_coordinate(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a numeric value.")

x1 = get_coordinate("Enter the x-coordinate of the first point: ")
y1 = get_coordinate("Enter the y-coordinate of the first point: ")
x2 = get_coordinate("Enter the x-coordinate of the second point: ")
y2 = get_coordinate("Enter the y-coordinate of the second point: ")

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between the two points is: {distance}")

# challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.
try:
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))
    print("Coordinates of the first point are valid.")
except ValueError:
    print("Invalid input. Please enter numeric values for the coordinates.")    