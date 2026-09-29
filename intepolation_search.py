def interpolation_search(a, key):  # Search sorted numeric values.
    low, high = 0, len(a) - 1  # Set the candidate interval.
    while low <= high and a[low] <= key <= a[high]:  # Stay in range.
        if a[low] == a[high]:  # Avoid dividing by zero.
            return low if a[low] == key else -1  # Check equal values.
        pos = low + (key - a[low]) * (high - low) // (a[high] - a[low])  # Estimate.
        if a[pos] == key:  # Check the estimate.
            return pos  # Found it.
        if a[pos] < key:  # Estimate was too low.
            low = pos + 1  # Raise the lower boundary.
        else:  # Estimate was too high.
            high = pos - 1  # Lower the upper boundary.
    return -1  # Key is absent.
print(interpolation_search([10, 20, 30, 40, 50], 40))  # Present.
print(interpolation_search([10, 20, 30, 40, 50], 35))  # Absent.