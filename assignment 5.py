'''
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.

=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
'''

# Function to convert hours to minutes and seconds
def convert_time(hours):
    minutes = hours * 60
    seconds = hours * 3600
    return minutes, seconds 

#processing to convert hours to minutes and seconds
def main():
    while True:
        try:
            # Input: Prompt the user to enter a time duration in hours
            hours = float(input("Enter a time duration in hours (non-negative): "))
            
            # Error handling to ensure the user enters a non-negative number
            if hours < 0:
                raise ValueError("Please enter a non-negative number.")
            
            # Convert the time duration to minutes and seconds
            minutes, seconds = convert_time(hours)
            
            # Output: Display the converted time duration in minutes and seconds
            print(f"{hours} hours is equal to {minutes} minutes and {seconds} seconds.")
            break  # Exit the loop after successful conversion
            
        except ValueError as e:
            print(e)  # Print the error message and prompt again    
            

#output: Display the converted time duration in minutes and seconds
if __name__ == "__main__":    main()    

