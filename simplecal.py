# Simple Calculator in Python

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main program
def main():
    # Display menu to the user
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Take user's choice
    choice = input("Enter choice (1/2/3/4): ")

    # Take input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the chosen operation
    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input")

# Execute the main program
if __name__ == "__main__":
    main()






# NOTE THIS CODE IS ENHACE VERSION AND PERFECT FOR SIMPLE CALCULATOR 


"""
summarized version of the simple calculator in Python:

This Python script implements a basic calculator with functions for addition, subtraction, multiplication, and division. 
It presents a menu for the user to choose an operation, prompts for two numbers as input, and performs the selected operation. 
The program handles division by zero by displaying an error message when attempting such an operation. 
It provides straightforward arithmetic calculations based on the user's input, ensuring clear functionality for basic mathematical operations.

"""