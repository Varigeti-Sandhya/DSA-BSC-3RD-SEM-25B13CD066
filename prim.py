import heapq  # Min-priority queue for frontier edges.
def prim(graph, start):  # MST of a connected undirected graph.
    visited = {start}  # Begin with one vertex.
    heap = [(w, start, v) for v, w in graph[start]]  # Frontier edges.
    heapq.heapify(heap)  # Arrange frontier by weight.
    chosen = []  # MST edges.
    while heap and len(visited) < len(graph):  # Until all are reached.
        weight, u, v = heapq.heappop(heap)  # Cheapest frontier edge.
        if v in visited:  # Edge would create a cycle.
            continue  # Skip it.
        visited.add(v)  # Bring new vertex into the tree.
        chosen.append((u, v, weight))  # Keep this edge.
        for neighbor, cost in graph[v]:  # Expand the frontier.
            if neighbor not in visited:  # Only candidates outside tree.
                heapq.heappush(heap, (cost, v, neighbor))  # Offer edge.
    if len(visited) != len(graph):  # A disconnected vertex remained.
        raise ValueError("Graph is disconnected")  # No full MST.
    return chosen, sum(w for _, _, w in chosen)  # Edges and total.
graph = {"A": [("B", 1), ("C", 3)],  # Undirected adjacency list.
         "B": [("A", 1), ("C", 2), ("D", 5)],  # B neighbours.
         "C": [("A", 3), ("B", 2), ("D", 4)],  # C neighbours.
         "D": [("B", 5), ("C", 4)]}  # D neighbours.
print(prim(graph, "A"))  # Display MST from A