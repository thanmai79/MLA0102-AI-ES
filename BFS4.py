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
    '0': ['1'],
    '1': ['3'],
    '2': ['1'],
    '3': ['2', '4'],
    '4': ['5'],
    '5': ['7'],
    '6': ['4'],
    '7': ['6']
}

print("BFS Traversal:")
bfs(graph, '1')
