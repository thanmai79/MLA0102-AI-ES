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
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (cost + edge_cost, neighbor, path + [neighbor])
                )

    return None, float("inf")

# Given graph input
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 1)],
    'D': [('G', 3)],
    'G': []
}

start = 'S'
goal = 'G'

path, cost = uniform_cost_search(graph, start, goal)

print("Optimal Path:", " -> ".join(path))
print("Total Cost:", cost)
