person = {
    "brand": "Ford",
    "electric": False,
    "birth_year": 1964,
    "colors": ["red", "white", "blue"],
}
print(person)


person["birth_year"] = 2024  # replace previous automatically
print(person)

person["occupation"] = "Engineer"
print(person)

del person["colors"]
print(person)


# Looping through the dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "name" in person:
    print("Name exists in the dictionary.")
else:
    print("exist")

    # Getting the length of the dictionary
length = len(person)

print(
    "The length of the dictionary is:", length
)  # Output: The length of the dictionary is: 3


# Getting all values as a list
values_list = list(person.values())

print("Values in the dictionary:", values_list)

# Getting all keys as a list
keys_list = list(person.keys())

print("Keys in the dictionary:", keys_list)

# dict can be nested
address = {"address": {"city": "New York", "state": "NY", "zipcode": "10001"}}

person["address"] = address;

print(person)
