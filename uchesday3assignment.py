# IF ELSE STATEMENT
# If else statement is a programming construct used to make decisions based on certain conditions.
# it allows the program to execute different blocks of code based on whether a condition is true or false.

# age= 18
# age= input(" please, Enter your age:")
# age= int(age)
# if age>=18:
#     print("you are eligible to vote:")
# else:
#     print("you are not eligible to vote:")
# In this example, the program checks whether the 'age' variable is greater than or equal to 18. If it is,
# it will print "You are eligible to vote." Otherwise, it will print "You are not eligible to vote."

# NESTED DICTIONARY
# A nested is a dictionary that has another dictionary as its value. This means that values of the outer
# dictionary can be accessed using two keys.

# my_dict={
#     "pilot1":{
#         "name":"Arnold",
#         "age":30,
#         "city":"Kaduna"
#     },
#     "pilot2":{
#         "name":"Oge",
#         "age":25,
#         "city":"Anambra"
#     }
# }
# Accessing values in the nested dictionary
# print(my_dict["pilot1"]["name"])
# print(my_dict["pilot2"]["name"])

# WHILE LOOP
# While loop allow you to repeatedly execute a block of code as long as a given condition is true.

# count=1
# while count<=5:
#     print(count)
#     count+=1

# FOR LOOP IN BOTH LIST AND TUPLE
# For loop can be used to iterate over both lists and tuples
# For loop with a List
# my_list=[1,2,3,4,5]
# for item in my_list:
#     print(item)
# For loop with a Tuple
# my_tuple=(6,7,8,9,10)
# for item in my_tuple:
#     print(item)

# WHILE COUNT
# This counts the occurence of a specific element in a list
# my_list=[1,2,3,4,1,1,2,3,4,5]
# count the occurence of a specific element
# count=my_list.count(1)
# print(f"The count of 1 in the list is:{count}")

# WHILE TRUE
# While True is a looping construct in the Python programming language that allows a block of code to be repeated 
# indefinitely. It is often used in conjunction with a break statement, which allows the loop to be exited 
# under certain conditions

# counter = 0
# while True:
#     print("This loop will run forever!")
#     counter += 1
#     if counter == 10:
#         break