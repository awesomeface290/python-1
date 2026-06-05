'''
Challenge: Handle negative exponents efficiently.

====================================
Description: Develop a function named power that takes two integers, base and exponent, as input and returns base raised to the power of exponent.
'''

# Function calcuulation using exponentiation by squaring
def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        if base == 0:
            raise ValueError("0 cannot be raised to a negative power")
        return 1 / power(base, -exponent)
    
    if exponent % 2 == 0:
        half = power(base, exponent // 2)
        return half * half
    else:
        return base * power(base, exponent - 1)


# Test cases
if __name__ == "__main__":
    try:
        base_in = input("Enter base (number): ")
        exp_in = input("Enter exponent (integer, can be negative): ")

        base = float(base_in)
        exponent = int(exp_in)

        result = power(base, exponent)
        print(f"{base}^{exponent} = {result}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    