'''
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.

==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency
'''

# challenge 1: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs. 

# Define a dictionary of exchange rates
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'JPY': 110.0
}
# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates:
        raise ValueError(f"Invalid currency: {from_currency}")
    if to_currency not in exchange_rates:
        raise ValueError(f"Invalid currency: {to_currency}")
    
    # Convert the amount to USD first
    amount_in_usd = amount / exchange_rates[from_currency]
    # Then convert from USD to the target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount

# Main function to run the currency converter
def main():
    print("Welcome to the Currency Converter!")
    print("Available currencies: USD, EUR, GBP, JPY")
    
    try:
        amount = float(input("Enter the amount you want to convert: "))
        from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
        to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
        
        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    
    except ValueError as e:
        print(e)    
if __name__ == "__main__":    main()    

