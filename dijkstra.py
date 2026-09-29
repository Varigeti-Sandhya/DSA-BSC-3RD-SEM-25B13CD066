import heapq  # Min-priority queue.
def dijkstra(graph, start):  # Shortest costs from one source.
    distance = {v: float("inf") for v in graph}  # Unknown initially.
    distance[start] = 0  # Source costs zero to reach.
    heap = [(0, start)]  # Candidate (cost, vertex).
    while heap:  # While candidate routes remain.
        cost, u = heapq.heappop(heap)  # Cheapest candidate.
        if cost != distance[u]:  # A newer shorter route exists.
            continue  # Ignore this stale heap entry.
        for v, weight in graph[u]:  # Inspect outgoing edges.
            if weight < 0:  # Dijkstra requires non-negative edges.
                raise ValueError("Negative edge")  # Refuse invalid input.
            candidate = cost + weight  # Cost via u.
            if candidate < distance[v]:  # Found a shorter route.
                distance[v] = candidate  # Save new best.
                heapq.heappush(heap, (candidate, v))  # Revisit v later.
    return distance  # Unreachable vertices remain infinity.
g = {"A": [("B", 4), ("C", 1)], "B": [("D", 1)],  # Directed demo.
     "C": [("B", 2), ("D", 5)], "D": []}  # Remaining edges.
print(dijkstra(g, "A"))  # Distances from A.
