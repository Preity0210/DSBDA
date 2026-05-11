graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input(f"Enter neighbors of {vertex}: ").split()
    graph[vertex] = neighbors

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

start = input("Enter starting vertex: ")

print("\nDFS Traversal:")
dfs(start)