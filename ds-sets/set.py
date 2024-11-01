# Creating a set
colors = {"red", "white", "blue"}
print("Initial set:", colors)

# Adding a value to the set
colors.add("green")
print("After adding 'green':", colors)

# Attempting to add a duplicate value (will have no effect)
colors.add("blue")  # "blue" is already in the set
print("After trying to add 'blue' again:", colors)

# Removing a value from the set
colors.remove("white")  # Will raise KeyError if 'white' is not present
print("After removing 'white':", colors)

# Using discard (won't raise an error if the item is not present)
colors.discard("yellow")  # 'yellow' is not in the set, so no error
print("After trying to discard 'yellow':", colors)

# Checking if a value exists in the set
if "red" in colors:
    print("Red exists in the set.")
else:
    print("Red does not exist in the set.")

# Getting the length of the set
length = len(colors)
print("The length of the set is:", length)

# Looping through the set
print("Colors in the set:")
for color in colors:
    print(color)

# Nesting a set in a dictionary
person = {"name": "Alice", "favorite_colors": colors}

print("Person dictionary with a set:", person)
