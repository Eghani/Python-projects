# Unit Converter in Python

# Function to convert kilometers to miles
def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Main program
def main():
    # Display choices to the user
    print("Choose the conversion you want to perform:")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    
    # Take user's choice
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        # Kilometers to Miles conversion
        kilometers = float(input("Enter the distance in kilometers: "))
        miles = km_to_miles(kilometers)
        print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
    elif choice == '2':
        # Celsius to Fahrenheit conversion
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Execute the main program
if __name__ == "__main__":
    main()


"""
The Python script allows the user to convert units by choosing between two options: converting kilometers to 
miles or Celsius to Fahrenheit. It defines two functions: `km_to_miles`, which multiplies the input kilometers by 0.621371 
to get miles, and `celsius_to_fahrenheit`, which converts Celsius to Fahrenheit using the formula \((\text{celsius} \times 9/5) + 32\). 
The main program prompts the user to select a conversion type, takes the necessary input, performs the conversion using the
appropriate function, and prints the result. If an invalid choice is made, it displays an error message.

"""