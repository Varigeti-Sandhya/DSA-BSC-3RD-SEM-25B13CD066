def merge_sort(a):  # Return a new sorted list.
    if len(a) <= 1:  # A singleton is sorted.
        return a  # Stop recursion.
    mid = len(a) // 2  # Split near the middle.
    left = merge_sort(a[:mid])  # Sort the left half.
    right = merge_sort(a[mid:])  # Sort the right half.
    out = []  # Build the merged result.
    i = j = 0  # Pointers into both halves.
    while i < len(left) and j < len(right):  # While both have items.
        if left[i] <= right[j]:  # Left head is smaller or tied.
            out.append(left[i])  # Copy the left item.
            i += 1  # Advance left pointer.
        else:  # Right head is smaller.
            out.append(right[j])  # Copy the right item.
            j += 1  # Advance right pointer.
    return out + left[i:] + right[j:]  # Append the leftover tail.
print(merge_sort([4, 1, 3, 2]))  # Run the example.