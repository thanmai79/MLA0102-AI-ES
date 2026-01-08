def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Given graph input
graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': [],
    '4': ['2', '5'],
    '5': ['2', '4']
}

print("DFS Traversal starting from node 1:")
dfs(graph, '1')
