from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Graph input
graph = {
    '1': ['2', '3'],
    '2': ['5', '6'],
    '3': ['4', '7'],
    '4': ['3', '8'],
    '5': [],
    '6': [],
    '7': ['3', '8'],
    '8': ['7', '4']
}

print("BFS Traversal:")
bfs(graph, '1')
