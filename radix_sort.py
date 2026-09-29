def radix_sort(a):  # Sort non-negative integers by digits.
    if any(x < 0 for x in a):  # This version excludes negatives.
        raise ValueError("Use non-negative integers")  # Explain the restriction.
    place = 1  # Start with the units digit.
    maximum = max(a, default=0)  # Highest number controls passes.
    while maximum // place > 0:  # While a digit remains.
        buckets = [[] for _ in range(10)]  # One bucket per digit.
        for value in a:  # Read in the current order.
            digit = (value // place) % 10  # Extract this digit.
            buckets[digit].append(value)  # Stable insertion into bucket.
        a = [value for bucket in buckets for value in bucket]  # Flatten.
        place *= 10  # Move to the next digit.
    return a  # Return ascending values.
print(radix_sort([21, 13, 12]))  # Run the example.