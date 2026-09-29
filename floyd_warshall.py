def floyd_warshall(vertices, edges):  # Compute all-pairs distances.
    inf = float("inf")  # Represent unreachable pairs.
    dist = {u: {v: (0 if u == v else inf) for v in vertices} for u in vertices}  # Matrix.
    for u, v, weight in edges:  # Load directed edges.
        dist[u][v] = min(dist[u][v], weight)  # Keep cheapest parallel edge.
    for k in vertices:  # Permit k as an intermediate.
        for i in vertices:  # Choose start vertex.
            for j in vertices:  # Choose end vertex.
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  # Relax.
    if any(dist[v][v] < 0 for v in vertices):  # Check for negative cycle.
        raise ValueError("Negative cycle")  # Distances not defined.
    return dist  # Return distance matrix.
names = ["A", "B", "C"]  # Vertex order for display.
result = floyd_warshall(names, [("A", "B", 3), ("B", "C", 2), ("A", "C", 10)])  # Input.
for name in names:  # Print each source row.
    print(name, [result[name][v] for v in names])  # Display distances.