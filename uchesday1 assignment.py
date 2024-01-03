# +Using personal examples differentiate btw tuple and a list
#  List Example
# wears_list=["versace","givenchy","gucci","balenciaga"]
# print(wears_list)

# In a list, you can modify, add, or remove items. for instance, if you decide to add "nike" to your
# wear list, you can do so with wear_list.append("nike"). List are written in square brackets

# Tuple Example
# grocery_tuple=("milk","sugar","oats","bread")
# print(grocery_tuple)

# Tuple are immutable, meaning you can't change their contents. Once you've created a tuple, 
# you can't add, remove, or modify elements. Tuples are written in round brackets

# Q2.Using examples explain string formatting
# String formatting is a way to insert values into a string.
# Using % operator
# name='Uchenna'
# age=32
# string='Hi, %s' % name
# print(string)
# print("%s is %d years old." %(name, age))
# print("I like to %s pinneapple." %'eat')
# x="dance"
# print("Uche loves to %s and %s too!" %(x, "sing"))
# Using Format()method
# print("Let's {} the {} with {} intelligence.".format('impact', 'world', 'artificial'))
# Apc="president {} won the {} in the year {}.".format('Tinubu', 'Election', '2023')
# print(Apc)

# Q3.Using X and y as variable use the following operators +*/
# x=12
# y=23
# sum=(x+y)
# print(sum)
# x=40
# y=10
# div=(x/y)
# print(div)
# x=4
# y=6
# print(x*y)

# # Write a variable assign to a value, use the format method to print an output.
# value = 42
# print(f"The assigned value is: {value}")

# Get a variable name and use the arithmetic operators to add, minus, divide and multiply.
variable1 = float(input("Enter the first number: "))
variable2 = float(input("Enter the second number: "))

addition_result = variable1 + variable2
subtraction_result = variable1 - variable2
division_result = variable1 / variable2
multiplication_result = variable1 * variable2

print("Addition Result: ", addition_result)
print("Subtraction Result: ", subtraction_result)
print("Division Result: ", division_result)
print("Multiplication Result: ", multiplication_result)

# write a code to calculate the division of two numbers and round it up to the nearest whole number.
# import math

# def divide_and_round_up(num1, num2):
#     result = num1 / num2
#     rounded_up = math.ceil(result)
#     return rounded_up
# num1 = 12
# num2 = 3
# result = divide_and_round_up(num1, num2)

# print(f"The result of {num1} divided by {num2} rounded up is: {result}")
