from collections import deque  # Efficient FIFO queue.
def bfs(graph, start):  # Visit reachable nodes in layers.
    queue = deque([start])  # Queue begins with source.
    seen = {start}  # Mark at enqueue time to prevent duplicates.
    order = []  # Save visitation sequence.
    while queue:  # Continue until no frontier remains.
        node = queue.popleft()  # Remove oldest discovered vertex.
        order.append(node)  # Record the visit.
        for neighbor in graph.get(node, []): # Examine its neighbours.
            if neighbor not in seen: # Skip already discovered nodes.
                seen.add(neighbor) # Mark immediately
                queue.append(neighbor)  # Explore later.
    return order  # Return BFS order.
graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}  # Input.
print(bfs(graph, "A"))  # Traverse from A.
