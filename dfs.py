def dfs(graph, start):  # Visit deep branches first.
    seen = set()  # Track visited vertices.
    order = []  # Save visit order.
    def visit(node):  # Recursive helper for one vertex.
        if node in seen:  # A cycle may revisit a vertex.
            return  # Do not repeat its work.
        seen.add(node)  # Mark this vertex as visited.
        order.append(node)  # Record its first visit.
        for neighbor in graph[node]:  # Try neighbours in listed order.
            visit(neighbor)  # Explore each branch fully.
    visit(start)  # Begin at source.
    return order  # Return traversal order.
graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}  # Input.
print(dfs(graph, "A"))  # Traverse from A.

