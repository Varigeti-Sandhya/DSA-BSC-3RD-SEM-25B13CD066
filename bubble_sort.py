def bubble_sort(a):  # Sort a list in place.
    for end in range(len(a) - 1, 0, -1):  # Shrink the unsorted end.
        for j in range(end):  # Scan neighbouring pairs.
            if a[j] > a[j + 1]:  # Detect a wrong order.
                a[j], a[j + 1] = a[j + 1], a[j]  # Swap neighbours.
    return a  # Return the sorted list.
print(bubble_sort([4, 1, 3, 2]))  # Run the example.