import heapq

def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [start])]   # (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for neighbor, edge_cost in graph[node]:
            heapq.heappush(
                pq,
                (cost + edge_cost, neighbor, path + [neighbor])
            )

    return None, float("inf")

# Given graph input
graph = {
    'V1': [('V2', 4), ('V3', 2)],
    'V2': [('V4', 5)],
    'V3': [('V5', 3)],
    'V4': [('V6', 6)],
    'V5': [('V6', 7)],
    'V6': []
}

start = 'V1'
goal = 'V6'

path, cost = uniform_cost_search(graph, start, goal)

print("Optimal Path:", " -> ".join(path))
print("Total Cost:", cost)
