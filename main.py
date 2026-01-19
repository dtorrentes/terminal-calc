# main.py
def main():
    """
    A simple terminal app that interacts with the user
    and performs a basic calculation.
    """
    
    # Ask the user for their name
    print("=" * 30)
    print(" Welcome to the Number Squarer ")
    print("=" * 30)
    name = input("What is your name? ")
    # Ask for a number
    # We use a loop to ensure we get a valid number
    while True:
        try:
            number_input = input(f"Hi {name}, please enter a number to square: ")
            number = float(number_input)
            break # Exit loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    # Perform a basic calculation (squaring the number)
    squared_result = number ** 2
    # Print a clean, formatted result
    print("\n" + "="*30)
    print(f"RESULTS FOR {name.upper()}")
    print("="*30)
    print(f"Input Number : {number}")
    print(f"Squared Value: {squared_result:,.2f}") # Formatted with commas and 2 decimal places
    print("="*30)
if __name__ == "__main__":
    main()
