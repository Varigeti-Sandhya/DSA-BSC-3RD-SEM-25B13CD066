def quick_sort(a):  # Return a sorted copy.
    if len(a) < 2:  # Empty/singleton list is sorted.
        return a  # Base case.
    pivot = a[len(a) // 2]  # Choose the middle value.
    less = [x for x in a if x < pivot]  # Values below pivot.
    equal = [x for x in a if x == pivot]  # Keep duplicates.
    more = [x for x in a if x > pivot]  # Values above pivot.
    return quick_sort(less) + equal + quick_sort(more)  # Combine.
print(quick_sort([4, 1, 3, 2]))  # Run the example.