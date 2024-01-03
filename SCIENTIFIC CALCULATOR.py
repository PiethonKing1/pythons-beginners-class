import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract y from x
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide x by y, with error handling for division by zero
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Function to calculate the square root of a number, with error handling for negative input
def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of a negative number"

# Function to exponentiate x to the power of y
def exponentiate(x, y):
    return x ** y

# Main calculator function
def calculator():
    print("Simple Scientific Calculator")

    # Main loop to repeatedly prompt the user for input
    while True:
        print("\nChoose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exponentiation")
        print("7. Exit")

        # Get user's choice of operation
        choice = input("Enter choice (1-7): ")

        # Check if the choice is a valid operation
        if choice in ('1', '2', '3', '4', '6'):
            try:     
        # This is the block of code where you anticipate that an exception might occur. 
        # It is the part of the code that you want to monitor for potential errors
                # Get user input for numbers, with error handling for invalid input
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input. Please enter valid numbers.")
                continue

            # Perform the selected operation based on the user's choice
            if choice == '1':
                print("Result: ", add(num1, num2))
            elif choice == '2':
                print("Result: ", subtract(num1, num2))
            elif choice == '3':
                print("Result: ", multiply(num1, num2))
            elif choice == '4':
                print("Result: ", divide(num1, num2))
            elif choice == '6':
                print("Result: ", exponentiate(num1, num2))

        # Check if the choice is for square root
        elif choice == '5':
            try:
                # Get user input for a number, with error handling for invalid input
                num = float(input("Enter a number: "))
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            # Calculate and display the square root
            print("Result: ", square_root(num))

        # Check if the user chose to exit
        elif choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        # If the choice is not valid, prompt the user to enter a valid option
        else:
            print("Invalid choice. Please enter a valid option (1-7).")

# Entry point to the script
if __name__ == "__main__":
    # Call the calculator function when the script is executed
    calculator()