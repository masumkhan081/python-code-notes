# Creating a list
my_list = [1, 2, 3, 2, 1, 4]
print("Original List:", my_list)

# Converting the list to a set
my_set = set(my_list)
print("Converted Set:", my_set)  # Output: {1, 2, 3, 4}


# Creating a set
my_set = {1, 2, 3, 2, 1, 4}
print("Original Set:", my_set)

# Converting the set to a list
my_list = list(my_set)
print("Converted List:", my_list)  # Output: [1, 2, 3, 4] (order may vary)


my_list = [1, 2, 3]
my_tuple = tuple(my_list)

my_tuple = (1, 2, 3)
my_list = list(my_tuple)

my_dict = {"a": 1, "b": 2}
my_list_of_tuples = list(my_dict.items())


my_list_of_tuples = [("a", 1), ("b", 2)]
my_dict = dict(my_list_of_tuples)

my_dict = {"a": 1, "b": 2}
my_set_from_keys = set(my_dict.keys())

my_set_from_values = set(my_dict.values())

my_tuple = (1, 2, 3)
my_set = set(my_tuple)

my_set = {1, 2, 3}
my_tuple = tuple(my_set) 
