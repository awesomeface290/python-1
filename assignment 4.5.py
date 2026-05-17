'''
Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.

============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
'''


import math


def get_float(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Invalid input. Please enter a numeric value.")


# input the coordinates of the two points with validation
x1 = get_float("enter x1: ")
y1 = get_float("enter y1: ")
x2 = get_float("enter x2: ")
y2 = get_float("enter y2: ")

# process the distance between the two points using the distance formula
distance = math.hypot(x2 - x1, y2 - y1)
print("The distance between the two points is:", distance)

# implament error handling to ensure that the user enters numeric values for the coordinates

try:
    x1 = float(input("enter x1: "))
    y1 = float(input("enter y1: "))
    x2 = float(input("enter x2: "))
    y2 = float(input("enter y2: "))
except ValueError:
    print("Invalid input. Please enter numeric values for the coordinates.")
    exit(1)
    
