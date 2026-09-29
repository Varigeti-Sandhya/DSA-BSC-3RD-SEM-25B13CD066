def sift_down(a, root, size):  # Restore max-heap order below root.
    while 2 * root + 1 < size:  # While a left child exists.
        child = 2 * root + 1  # Left child's index.
        if child + 1 < size and a[child + 1] > a[child]:  # Right is bigger.
            child += 1  # Choose the right child.
        if a[root] >= a[child]:  # Parent already dominates.
            break  # Heap is repaired.
        a[root], a[child] = a[child], a[root]  # Move larger child up.
        root = child  # Continue down that branch.
def heap_sort(a):  # Sort in place with a max heap.
    for root in range(len(a) // 2 - 1, -1, -1):  # Visit internal nodes backward.
        sift_down(a, root, len(a))  # Build the heap.
    for end in range(len(a) - 1, 0, -1):  # Shrink heap one item at a time.
        a[0], a[end] = a[end], a[0]  # Put maximum at the end.
        sift_down(a, 0, end)  # Repair the reduced heap.
    return a  # Give back ascending values.
print(heap_sort([4, 1, 3, 2]))  # Run the example.