edges = int(input("Enter number of edges: "))

graph = []

for i in range(edges):
    u, v, w = input("Enter edge and weight: ").split()
    graph.append((int(w), u, v))

graph.sort()

print("Minimum Spanning Tree:")
for edge in graph:
    print(edge[1], "-", edge[2], "=", edge[0])

