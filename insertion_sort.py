def insertion_sort(a):  # Build a sorted prefix.
    for i in range(1, len(a)):  # Take the next unsorted item.
        key = a[i]  # Save it before shifting.
        j = i - 1  # Begin at the end of the sorted prefix.
        while j >= 0 and a[j] > key:  # Shift larger items.
            a[j + 1] = a[j]  # Make space for key.
            j -= 1  # Move one place left.
        a[j + 1] = key  # Put key into the gap.
    return a  # Provide the result.
print(insertion_sort([4, 1, 3, 2]))  # Run the example.