graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(node, visited=set()):
    if node not in visited:
        print(node)  # Visit the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

dfs('F')
