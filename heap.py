import heapq  # Standard-library min-heap implementation.
priority = []  # Start with an empty heap.
for value in [5, 2, 7, 1]:  # Add tasks one by one.
    heapq.heappush(priority, value)  # Push each new value.
print(heapq.heappop(priority))  # Remove the smallest task.
print(heapq.heappop(priority))  # Remove the next smallest.
print(sorted(priority))  # Display remaining VALUES in order.
