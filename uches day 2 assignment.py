# Create a grocery list containing at least 6 items.

groceries= ["Bread", "Eggs", "Honey", "Wheat", "Millet", "Milk"]
print(groceries)

# Write a python program to print the indexes of the previously created list using 
# the following index (index 2, 2 till end, 4 and 5)

print(groceries [2])
print(groceries [2:])
print(groceries [4:6])

# Write a program to append, insert, extend, remove to the list

groceries.append("Butter")
print(groceries)
groceries.insert(0, "garri")
print(groceries)
added_groceries = ["cereals", "oats", "sugar"]
groceries.extend(added_groceries)
print(groceries)
groceries.remove("Milk")
print(groceries)

# Create a nested dictionary using different 3 kinds of phones and their keys should be name, model, storage and ram. 
# Use the update method to change the ram size of thw second phone.

Phone_Brands= {
    "iphone":{
    "model":"12pro",
    "storage":"256gb",
    "ram":"4"
    },

    "Tecno":{
    "model":"camon 19",
    "storage":"128gb",
    "ram":"4"
    },

    "itel":{
    "model":"T22",
    "storage":"64gb",
    "ram":"4"
    }
}
Phone_Brands["Tecno"].update({"ram":"8"})
print(Phone_Brands["Tecno"])

