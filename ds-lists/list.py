# Creating a list
colors = ["red", "white", "blue"]
print("Initial list:", colors)

# Accessing a value by index
first_color = colors[0]  # Accessing the first item
print("First color:", first_color)

# Inserting a value at a specific index
colors.insert(1, "green")  # Insert "green" at index 1
print("After insertion:", colors)

# Replacing a value at a specific index
colors[2] = "yellow"  # Replace the color at index 2
print("After replacement:", colors)

# Deleting a value by index
del colors[3]  # Delete the color at index 3
print("After deletion:", colors)

# Looping through the list
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Checking if a value exists in the list
if "blue" in colors:
    print("Blue exists in the list.")
else:
    print("Blue does not exist in the list.")

# Getting the length of the list
length = len(colors)
print("The length of the list is:", length)

# Getting all values as a list (since this is already a list)
print("Values in the list:", colors)

# Nesting a list
person = {
    "name": "Alice",
    "favorite_colors": colors
}

print("Person dictionary with a list:", person)
