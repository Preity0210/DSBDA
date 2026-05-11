edges = [
    (1,'A','B'),
    (2,'B','C'),
    (4,'A','C')
]

edges.sort()

print("Kruskal MST:")

for edge in edges:
    print(edge[1], "-", edge[2], "=", edge[0])