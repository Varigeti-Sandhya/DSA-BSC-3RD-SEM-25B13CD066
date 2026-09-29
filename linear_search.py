def linear_search(items, key):  # Define a reusable search function.
    for i, value in enumerate(items):  # Visit each position and value.
        if value == key:  # Check whether this is the sought item.
            return i  # Give back the first matching index.
    return -1  # Signal that no item matched.
numbers = [8, 3, 11, 5]  # An unsorted input list.
print(linear_search(numbers, 11))  # Search for a present value.
print(linear_search(numbers, 7))  # Search for an absent value.
