def selection_sort(a):  # Sort by repeated minimum selection.
    for i in range(len(a)):  # Position to fill next.
        smallest = i  # Assume its current value is smallest.
        for j in range(i + 1, len(a)):  # Inspect the remaining values.
            if a[j] < a[smallest]:  # Found a smaller item.
                smallest = j  # Remember its position.
        a[i], a[smallest] = a[smallest], a[i]  # Place it first.
    return a  # Provide the result.
print(selection_sort([4, 1, 3, 2]))  # Run the example.