from collections import defaultdict

def topological_sort(graph):
    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)

    visited = set()
    stack = []

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack

# Contoh penggunaan
tasks = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': [],
    'D': ['E'],
    'E': [],
    'F': ['D']
}

sorted_tasks = topological_sort(tasks)
print("Urutan pengerjaan tugas:")
for task in sorted_tasks:
    print(task, end=" ")