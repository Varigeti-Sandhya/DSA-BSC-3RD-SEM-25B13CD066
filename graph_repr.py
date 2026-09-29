vertices = ["A", "B", "C"]  # Fix vertex order for matrix rows.
edges = [("A", "B"), ("A", "C"), ("B", "C")]  # Undirected edges.
graph = {v: [] for v in vertices}  # Empty neighbour lists.
for u, v in edges:  # Process each edge.
     graph[u].append(v)  # Record u-to-v.
     graph[v].append(u)  # Record v-to-u too.
index = {v: i for i, v in enumerate(vertices)}  # Map labels to indices.
matrix = [[0] * len(vertices) for _ in vertices]  # Zero means no edge.
for u, v in edges:  # Mark each undirected edge.
    matrix[index[u]][index[v]] = 1  # Mark u-to-v.
    matrix[index[v]][index[u]] = 1  # Mark v-to-u.
print(graph)  # Adjacency list.
for row in matrix:  # Print one matrix row at a time.
    print(row)  # Check its zeros and ones.
