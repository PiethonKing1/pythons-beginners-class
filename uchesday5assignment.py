# I created a display menu for the user to select the desired operation. This can be done using 
# the print()function to output the menu options.
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    
# The user was prompted to enter their choice by using the input() function to capture their input as string.
    operation = int(input("Enter your option: "))
    if operation >=5:
        print("Invalid operation. Please choose a valid operation")
    elif operation <=0:
        print("Invalid operation. Please choose a valid operation")
       

# Then, prompt the user to enter the two numbers or inputs required for the operation
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))



    if operation == 1:
        print("Result:", num1 + num2)
    elif operation == 2:
        print("Result:", num1 - num2)
    elif operation == 3:
        print("Result:", num1 * num2)
    elif operation == 4:
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operation. Please choose a valid operation.")

    calculator()

calculator()