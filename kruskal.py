def kruskal(vertices, edges):  # MST of an undirected graph.
    parent = {v: v for v in vertices}  # Each vertex begins alone.
    def find(x):  # Find component representative.
        if parent[x] != x:  # Not yet at a root.
            parent[x] = find(parent[x])  # Compress the path.
        return parent[x]  # Return the root.
    chosen = []  # Accepted edges.
    for weight, u, v in sorted(edges):  # Cheapest edges first.
        a, b = find(u), find(v)  # Find their components.
        if a != b:  # Different components: no cycle.
            parent[a] = b  # Merge the components.
            chosen.append((u, v, weight))  # Accept edge.
    if len(chosen) != len(vertices) - 1:  # Connected MST needs V-1 edges.
        raise ValueError("Graph is disconnected")  # Only a forest exists.
    return chosen, sum(w for _, _, w in chosen)  # Edges and total.
vertices = ["A", "B", "C", "D"]  # Four campuses.
edges = [(1, "A", "B"), (2, "B", "C"), (3, "A", "C"),  # Triangle.
         (4, "C", "D"), (5, "B", "D")]  # Links to D.
print(kruskal(vertices, edges))  # Display MST.