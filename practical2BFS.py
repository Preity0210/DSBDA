# BFS Program using Queue

from collections import deque

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input(f"Enter neighbors of {vertex}: ").split()
    graph[vertex] = neighbors

visited = set()

def bfs(start):
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

start = input("Enter starting vertex: ")

print("\nBFS Traversal:")
bfs(start)