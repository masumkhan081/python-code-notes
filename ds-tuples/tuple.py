# Creating a tuple
colors = ("red", "white", "blue")
print("Initial tuple:", colors)

# Accessing a value by index
first_color = colors[0]  # Accessing the first item
print("First color:", first_color)

# Tuples are immutable, so you cannot change an element directly
# colors[0] = "green"  # This would raise a TypeError

# To create a modified version, you can convert to a list, modify, and convert back
modified_colors = list(colors)
modified_colors[0] = "green"  # Change the first element
colors = tuple(modified_colors)  # Convert back to tuple
print("After modification (new tuple):", colors)

# Adding a value to a tuple (create a new tuple)
new_colors = colors + ("yellow",)  # Adding "yellow"
print("After adding 'yellow':", new_colors)

# Deleting a value from a tuple is not possible (immutable)
# However, you can create a new tuple without a specific element
new_colors = new_colors[:1] + new_colors[2:]  # Remove the second element
print("After removing 'white':", new_colors)

# Looping through the tuple
print("Colors in the tuple:")
for index, color in enumerate(new_colors):
    print(f"Index {index}: {color}")

# Checking if a value exists in the tuple
if "red" in new_colors:
    print("Red exists in the tuple.")
else:
    print("Red does not exist in the tuple.")

# Getting the length of the tuple
length = len(new_colors)
print("The length of the tuple is:", length)

# Nesting a tuple in a dictionary
person = {"name": "Alice", "favorite_colors": new_colors}

print("Person dictionary with a tuple:", person)
