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
    '0': ['1'],
    '1': ['3'],
    '2': ['1'],
    '3': ['2', '4'],
    '4': ['5'],
    '5': ['7'],
    '6': ['4'],
    '7': ['6']
}

print("DFS Traversal starting from node 0:")
dfs(graph, '0')
