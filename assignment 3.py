    # Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese.)
# ===============================
# Input: Prompt the user to enter their weight in kilograms and height in meters.
# Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
# Output: Display the calculated BMI.

# prompt the user to enter their weight in kilograms and height in meters
weight_input = input("Please enter your weight in kilograms: ")
height_input = input("Please enter your height in meters: ")

# convert the string value above to float
weight = float(weight_input)
height = float(height_input)

# calculate the BMI using the formula: BMI = Weight / (Height^2)
bmi = weight / (height ** 2)

# display the calculated bmi and provide feedback to the user based on their BMI category
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")